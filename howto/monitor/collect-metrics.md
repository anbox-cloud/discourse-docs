This example implementation provides a starting point for a monitoring stack that can be used to gather metrics with [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) and [Prometheus](https://prometheus.io/) and access them through [Grafana](https://grafana.com/).

[note type="information" status="Important"]This reference implementation is provided for demonstration purposes only. It does not cover all aspects that you should consider for a production-level solution (for example, high availability). It cannot be used with the Anbox Cloud Appliance.[/note]

In this setup, every LXD cluster node runs a Telegraf instance that gathers the machine metrics. All Anbox containers that exist on the node also report their metrics to the Telegraf instance.

Prometheus gathers the metrics provided by the different sources (the Telegraf instances, AMS, Anbox Stream Gateway and NATS) and stores them in its time series database. You can then access, query and visualise the full metrics data through Grafana.

![Architecture for collecting metrics|462x312](https://assets.ubuntu.com/v1/17a66908-collect-metrics.png)

## Deploy the solution

The monitoring stack is provided as an [overlay file](https://discourse.ubuntu.com/t/installation-customizing/17747#overlay-files) that you use when deploying Anbox Cloud.

The overlay file adds a machine to the deployment (with ID `2` for the `anbox-cloud-core` bundle or ID `3` for the `anbox-cloud` bundle), which is used to run Grafana, Prometheus and HAProxy (as a reverse proxy that secures access to the internal endpoints of the other services). In addition, the overlay installs and configures Telegraf for both AMS and the LXD nodes, and it creates the required relations.

The minimum requirements for the additional machine are as follows:

Architecture   | CPU cores | RAM  | Disk       | GPUs | Components  |
---------------|-----------|------|------------|------|-------------|
amd64          | 4         | 4 GB | 100 GB SSD | no   | Grafana, Prometheus |

Complete the following steps to deploy Anbox Cloud with the reference monitoring stack:

1. Create a `monitoring.yaml` file with the following content, depending on which [Juju bundle](https://discourse.ubuntu.com/t/about-anbox-cloud/17802#juju-bundles) you want to deploy:

   [Details="For the `anbox-cloud-core` bundle"]
   ```yaml
   applications:
     grafana-proxy:
       charm: 'haproxy'
       num_units: 1
       expose: true
       options:
         default_mode: tcp
         peering_mode: active-active
         ssl_cert: SELFSIGNED
         ssl_key: SELFSIGNED
         services: |
           - service_name: app-grafana
             service_host: "0.0.0.0"
             service_port: 443
             service_options:
               - mode http
               - http-request set-path %[path,regsub(^/grafana/?,/)]
               - balance leastconn
             server_options: check verify none inter 2000 rise 2 fall 5 maxconn 4096
             crts: [DEFAULT]
           - service_name: http_service
             service_host: "0.0.0.0"
             service_port: 80
             service_options:
               - mode http
               - http-request redirect scheme https
       to:
         - '2'
     prometheus:
       charm: 'prometheus2'
       num_units: 1
       to:
         - '2'
     ams-monitor:
       charm: 'telegraf'
       options:
         tags: region=cloud-0
         prometheus_output_port: "20003"
     lxd-monitor:
       charm: 'telegraf'
       options:
         tags: region=cloud-0
         prometheus_output_port: "20004"
     grafana:
       charm: 'grafana'
       num_units: 1
       options:
         root_url: '%(protocol)s://%(domain)s:%(http_port)s/grafana'
         # See https://grafana.com/blog/2023/08/24/grafana-security-update-gpg-signing-key-rotation/
         install_keys: |
            - |
            -----BEGIN PGP PUBLIC KEY BLOCK-----
            mQGNBGO4aiUBDAC82zo3vUyQH3yTCabQ7ZpospBg/xXBbJWbQNksIbEP/+I12CjB
            zac1QcMFd27MJlyXpsTqqSo1ZHOisNy0Tmyl/WlqMyoMeChg+LmIHLNbvAK0jPOX
            1Pt2OykXJWN9Ru+ZZ4uQNgdKO5nXS6CZtK+McfhRwwghp+vlZFJgqP6aGR2A4cZ7
            IJpUQIoT/8GY6Fdx5TStTJucVUXjSJ3VqafZe4c0WHrk5Yb0UptYPBj9brZkmC9F
            Uz6BLX6eO0HGLdwvYzoenlN1sD/2dclUtxoKYmfKDgpcG1V4vOClYPgOZ7g6jvwU
            +nW39VGwR7yzbEAmGxVcd93QNUjTaZMfO3xJFm1UG5JwC6VJcd7Wp3hNHJle/y62
            lw0N2AATqJ7AV6PXKBPNebXvCB0LqkAiC/W//imeMCk9hfREmb5rhf1s83owpJaQ
            gScEtJYIVgOqgGoFE8wkCkHFG1slneLykmGK2xAJ2Rk63MIAE4hL9WKLV624LMid
            JqH3YIEA6pR+GlEAEQEAAbQmR3JhZmFuYSBMYWJzIDxlbmdpbmVlcmluZ0BncmFm
            YW5hLmNvbT6JAdQEEwEIAD4WIQQOIuuI454SJ3p3YK6eQ5sQLPPAxgUCY7hqJQIb
            AwUJA8JnAAULCQgHAgYVCgkICwIEFgIDAQIeAQIXgAAKCRCeQ5sQLPPAxhXnDACu
            6rtTbZsbHYaotiQ757UX+Yu+hXTDBQe74ahEqKAYLg2JKzYNx2Q7UovvVLJ3JZQ4
            e2lezdj7NkeyuSuiq1C/A58fqRICqNh8vRCqOQ9+zfUy9DHwkCrLUVY+31MGLh3G
            nXuNrb4AzC2PPNL+VoJhhYnXoFO6Ko6ftzmKeIVeuNp6YfM95gyfIupXGvmwefgx
            fHIaq0MaeFhIf1RgcvPyMVIMCUoaHMeA5+Z2REjc9iopT4YVzn7ZmoG5vlXIo2gX
            HGWFUQDTD3PW9cURVdaHAYcN0owl4o90jef14Md9xgTUIDx6soFhD3wXpiV5z/HC
            7BZqe5mdpp0vDuQNRkqX/uALOBDdoh/r5mBjFxOzNeBHAtf8Fer9/w6g222sGUz/
            I3BCBFBRUKEBaExvonIEFToVDM4nHTCW9vTgnPOLkgX8GBfF3cobmnJlKrX5gLKQ
            MKs+9JtaRi8+RBb8hOCm3tGxW+o6GKwZ6BGYrsTzFHNfWV42EwXJUhbfQnK5K0S5
            AY0EY7hqJQEMAO/jPuCVTthJR5JHFtzd/Sew59YJVIb8FgCPaZRKZwZ0rznMuZDf
            HB6pDdHe5yy84Ig2pGundrxURkax5oRqQsTc6KWU27DPpyHx5yva1A7Sf55A0/i6
            XLBd2IFabijChiYhVxD/CFOwMtkhjU5CLY67fZ6FRB20ByrlDSNrhVMJ5F8lxRNb
            Kh14Jc4Hk4F2Mm1+VlNdrmFqSzPF9JcEvUYHSuzOHi14L1jS2ECdyakbYLHGiHhj
            dxuTVlUTEZ9fZ73qRLRViUsy1fwMWTUBWwyO5Qpgbtps3+WefusuJycWnQDOZxxr
            0/SGxTE3qNn5kWXCg56t0YFISlhGM2ImU+BdTY+p8AthibdhZCTYswoghkPGVXbu
            DGR98tVaeG1hLHsL3yh17VbukSCliyurOleQt2AuG9kKieU8zcxsXvFASz2fJOiQ
            T7ehyDMCK0rLSigA66pZ63PVy05NnH4P4MNRvCE03KthblDrMiF0BckB0fDxBbd8
            17FEDGkunWKWmwARAQABiQG8BBgBCAAmFiEEDiLriOOeEid6d2CunkObECzzwMYF
            AmO4aiUCGwwFCQPCZwAACgkQnkObECzzwMbAYAv+PWbRuO7McuaD8itXAtqW9o4F
            o9PBMGXXJuWfN2UathyGuS6iZNCdIZMZgpOfuuk2ctFKeQHizM/hfUrguNGhvZX+
            xSbuq8M+/dx+c2Lse7NDP0Q8Pw9UaDHcW6gTTLizq/CWhFpOD2IH2ywxY3IrAvzG
            R4pDs+NodJgLCQPd1ez/lGk90mk/j17Yue2sD2fwJyqWqbHZJe8qgfvEtn+WPK33
            84JN9DgDkcq7ThoLxU0Q7U3SempJGT98Yg2RWMAPj51DqtZOIVdeKoR8lr1rk3Kv
            X7sojTBU4eWUrc0A3GwoqyCXz9xlXb8OLhTsFAlsQCLkgK7Rdt3sXyg3QkFQmGuk
            MnYQV0TkaAcXE2p03nk45vVrWoGJPzDfx68LBT6Ck/Ytw8/QHm4zqjZBLH5cMdax
            Fj8eP2CocfRC+Lqv0azQwyEVMkYSMKoFbhXmjiBZn9JxblndKnVbByA1/nMAa0Q7
            HTJC50jDJfpM9d1xQW/W5LBSQjd3czM6zlRXsliX
            =lSMJ
            -----END PGP PUBLIC KEY BLOCK-----
       to:
         - '2'
   relations:
     - ['ams:prometheus', 'prometheus:scrape']
     - ['grafana:grafana-source', 'prometheus:grafana-source']
     - ['grafana-proxy:reverseproxy', 'grafana:website']
     - ['lxd-monitor:prometheus-client', 'prometheus:target']
     - ['lxd-monitor:juju-info', 'lxd:juju-info']
     - ['ams-monitor:prometheus-client', 'prometheus:target']
     - ['ams-monitor:juju-info', 'ams:juju-info']
     - ['ams:grafana', 'grafana:dashboards']
   machines:
     '0':
       series: focal
       constraints: "cpu-cores=4 mem=8G root-disk=100G"
     '1':
       series: focal
       constraints: "cpu-cores=8 mem=16G root-disk=200G"
     '2':
       series: focal
       constraints: "cpu-cores=4 mem=4G root-disk=100G"
   ```
   [/Details]

   [Details="For the `anbox-cloud` bundle"]
   ```yaml
   applications:
     grafana-proxy:
       charm: 'haproxy'
       num_units: 1
       expose: true
       options:
         default_mode: tcp
         peering_mode: active-active
         ssl_cert: SELFSIGNED
         ssl_key: SELFSIGNED
         services: |
           - service_name: app-grafana
             service_host: "0.0.0.0"
             service_port: 443
             service_options:
               - mode http
               - http-request set-path %[path,regsub(^/grafana/?,/)]
               - balance leastconn
             server_options: check verify none inter 2000 rise 2 fall 5 maxconn 4096
             crts: [DEFAULT]
           - service_name: http_service
             service_host: "0.0.0.0"
             service_port: 80
             service_options:
               - mode http
               - http-request redirect scheme https
       to:
         - '3'
     prometheus:
       charm: 'prometheus2'
       num_units: 1
       to:
         - '3'
     ams-monitor:
       charm: 'telegraf'
       options:
         tags: region=cloud-0
         prometheus_output_port: "20003"
     lxd-monitor:
       charm: 'telegraf'
       options:
         tags: region=cloud-0
         prometheus_output_port: "20004"
     grafana:
       charm: 'grafana'
       num_units: 1
       options:
         root_url: '%(protocol)s://%(domain)s:%(http_port)s/grafana'
         # See https://grafana.com/blog/2023/08/24/grafana-security-update-gpg-signing-key-rotation/
         install_keys: |
            - |
            -----BEGIN PGP PUBLIC KEY BLOCK-----
            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
            =lSMJ
            -----END PGP PUBLIC KEY BLOCK-----
       to:
         - '3'
   relations:
     - ['ams:prometheus', 'prometheus:scrape']
     - ['grafana:grafana-source', 'prometheus:grafana-source']
     - ['grafana-proxy:reverseproxy', 'grafana:website']
     - ['lxd-monitor:prometheus-client', 'prometheus:target']
     - ['lxd-monitor:juju-info', 'lxd:juju-info']
     - ['ams-monitor:prometheus-client', 'prometheus:target']
     - ['ams-monitor:juju-info', 'ams:juju-info']
     - ['ams:grafana', 'grafana:dashboards']
     - ['anbox-stream-gateway:prometheus', 'prometheus:scrape']
     - ['anbox-stream-gateway:grafana', 'grafana:dashboards']
   machines:
     '0':
       series: focal
       constraints: "cpu-cores=4 mem=4G root-disk=100G"
     '1':
       series: focal
       constraints: "cpu-cores=4 mem=8G root-disk=100G"
     '2':
       series: focal
       constraints: "cpu-cores=8 mem=16G root-disk=200G"
     '3':
       series: focal
       constraints: "cpu-cores=4 mem=4G root-disk=100G"
   ```
   [/Details]

   [note type="information" status="Note"]For a production-level solution, replace the automatically generated self-signed SSL credentials with proper ones.[/note]
1. Deploy Anbox Cloud with the overlay file.

   - For the `anbox-cloud-core` bundle:

         juju deploy anbox-cloud-core --overlay monitoring.yaml

   - For the `anbox-cloud` bundle:

         juju deploy anbox-cloud --overlay monitoring.yaml

   [note type="information" status="Note"]You can use the same command if you already deployed Anbox Cloud. In this case, Juju checks the existing deployment and only deploys new components.[/note]
1. Wait until all added units are in `active` state.

## Access Grafana

To access the metrics in Grafana, go to `https://<IP_address>/grafana` in your browser.

Replace `<IP_address>` with the IP address of the machine on which you deployed the `grafana-proxy` application. If you don't know the address, run `juju status` to display the information for all machines.

You must enter your user name and password to log in. The user name is `admin`. You can determine the password by running the following command:

    juju run-action --wait grafana/0 get-admin-password

If you have deployed more than one Grafana unit, you might need to replace the `0` in `grafana/0` with the suitable unit ID. Check `juju status` if you are in doubt.

The response should look similar to this:

```yaml
unit-grafana-0:
  id: 29f07367-556b-41d0-8318-b9fa13a78b63
  results:
    password: jd673zyYWkR7kyPW
  status: completed
  timing:
    completed: 2018-06-29 13:29:38 +0000 UTC
    enqueued: 2018-06-29 13:29:36 +0000 UTC
    started: 2018-06-29 13:29:38 +0000 UTC
  unit: grafana/0
```

In this example output, the password is `jd673zyYWkR7kyPW`.
