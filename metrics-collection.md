Anbox Cloud allows you to collect various metrics from a deployment. This includes various metrics about the hardware and how it's being used but also about Anbox Cloud itself, like how many containers are currently running etc.

The following table shows an overview of the metrics available through [Prometheus](https://prometheus.io/):

| Name                        | Description                                                 |
| --------------------------- |:------------------------------------------------------------|
| `nodes`                     | The number of nodes in the cluster                          |
| `applications`              | The number of applications in the cluster                   |
| `containers`                | The number of containers in the cluster                     |
| `container_boot_time`       | The number of seconds it takes to boot a container          |
| `container_per_application` | The number of containers per application                    |
| `containers_per_status`     | The number of containers per container status               |
| `available_cpu`             | The total number of CPUs available in a node of the cluster |
| `used_cpu`                  | The number of CPUs used in a node of the cluster            |
| `available_memory`          | The total memory available in a node of the cluster         |
| `used_memory`               | The memory used in a node of the cluster                    |


## Requirements

In order to collect various metrics from the LXD machines Anbox Cloud uses [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/). For visualization purposes [Grafana](https://grafana.com/) is being used.

To make the deployment of all necessary components easy and straight forward a Juju bundle called `cs:~anbox-charmers/anbox-cloud-metrics` is available in the [Juju charm store](https://jujucharms.com).

By default the bundle deploys [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/) into a new machine and will make access to [Grafana](https://grafana.com/) available through a HTTPS secured proxy powered by [Apache](https://httpd.apache.org/).

> Tip: When you're structuring your production deployment you may want to follow our instructions for a [customized deployment](https://discourse.ubuntu.com/t/installation-customizing/17747) and directly include any relevant components in your own deployment bundle.

More details about using the deployed metrics collection stack can be found [here](https://discourse.ubuntu.com/t/monitoring/17785).

## Deployment

You can add the metrics services to an existing Anbox Cloud deployment by executing:

```bash
$ juju deploy cs:~anbox-charmers/anbox-cloud-metrics
```

If you're using the manual Juju provider as described in the [custom install guide](https://discourse.ubuntu.com/t/installation-customizing/17747) you can map the machine defined in the bundle to an existing one on your bundle:

```bash
$ juju deploy cs:~anbox-charmers/anbox-cloud-metrics --map-machines 0=2
```

As in previous deployment steps, you can check the status of the deployment with:

```bash
$ watch -c juju status --color --relations=true
```

When the deployment finished, the status should look like this.

```
Model    Controller   Cloud/Region   Version  SLA          Timestamp
default  anbox-cloud  aws/us-east-2  2.5.0    unsupported  16:03:32+08:00

App                  Version  Status  Scale  Charm                Store       Rev  OS      Notes
ams                           active      1  ams                  local         0  ubuntu
ams-node-controller           active      1  ams-node-controller  local         0  ubuntu  exposed
easyrsa              3.0.1    active      1  easyrsa              jujucharms  195  ubuntu
etcd                 3.2.10   active      1  etcd                 jujucharms  338  ubuntu
grafana                       active      1  grafana              jujucharms   22  ubuntu
grafana-proxy                 unknown     1  apache2              jujucharms   26  ubuntu  exposed
lxd                           active      1  lxd                  local         0  ubuntu
prometheus                    active      1  prometheus2          jujucharms    8  ubuntu
telegraf                      active      1  telegraf             jujucharms   27  ubuntu

Unit                      Workload  Agent      Machine  Public address  Ports               Message
ams/0*                    active    idle       0        18.224.58.129   8443/tcp,9103/tcp
easyrsa/0*                active    idle       0        18.224.58.129                       Certificate Authority connected.
etcd/0*                   active    idle       0        18.224.58.129   2379/tcp            Healthy with 1 known peer
grafana-proxy/0*          unknown   idle       2        18.216.182.177  80/tcp,443/tcp
grafana/0*                active    executing  2        18.216.182.177  3000/tcp            Started grafana-server
lxd/0*                    active    idle       1        52.14.125.184   8095/tcp,8443/tcp
  ams-node-controller/0*  active    idle                52.14.125.184   10000-11000/tcp
  telegraf/0*             active    idle                52.14.125.184   9103/tcp            Monitoring lxd/0
prometheus/0*             active    executing  2        18.216.182.177  9090/tcp,12321/tcp  Ready

Machine  State    DNS             Inst id              Series  AZ          Message
0        started  18.224.58.129   i-0368b9501551aed87  bionic  us-east-2a  running
1        started  52.14.125.184   i-019d854aed4ad262e  bionic  us-east-2b  running
2        started  18.216.182.177  i-01f7943b88b44e212  bionic  us-east-2c  running

Relation provider           Requirer                    Interface         Type         Message
ams:prometheus              prometheus:scrape           prometheus        regular
easyrsa:client              etcd:certificates           tls-certificates  regular
etcd:cluster                etcd:cluster                etcd              peer
etcd:db                     ams:etcd                    etcd              regular
grafana:website             grafana-proxy:reverseproxy  http              regular
lxd:api                     ams-node-controller:lxd     rest              subordinate
lxd:api                     ams:lxd                     rest              regular
lxd:juju-info               telegraf:juju-info          juju-info         subordinate
prometheus:grafana-source   grafana:grafana-source      grafana-source    regular
telegraf:prometheus-client  prometheus:target           http              regular
```
