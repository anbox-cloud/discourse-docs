.. _howto_monitor_install:

============================
Install the monitoring stack
============================

Anbox Cloud provides a reference for a monitoring stack based on
Prometheus, Grafana and Telegraf. In order to simplify and speed up the
deployment of Anbox Cloud itself, the reference monitoring stack is
provided as a separate
`overlay <https://juju.is/docs/charm-bundles#heading--overlay-bundles>`_
file.

Core Deployment
===============

To integrate the monitoring stack into either a fresh or an existing
Anbox Cloud Core deployment, copy the following code snippet into a
``monitoring.yaml`` file.

.. code:: yaml

   applications:
     grafana-proxy:
       charm: 'cs:haproxy'
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
       charm: 'cs:prometheus2-18'
       num_units: 1
       to:
         - '2'

     ams-monitor:
       charm: 'cs:telegraf-39'
       options:
         tags: region=cloud-0
         prometheus_output_port: "20003"

     lxd-monitor:
       charm: 'cs:telegraf-39'
       options:
         tags: region=cloud-0
         prometheus_output_port: "20004"

     grafana:
       charm: 'cs:grafana-36'
       num_units: 1
       options:
         root_url: '%(protocol)s://%(domain)s:%(http_port)s/grafana'
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

The ideal requirements for the machine for monitoring stack deployment
are the following:


.. list-table::
   :header-rows: 1

   * - ID
     - Architecture
     - CPU cores
     - RAM
     - Disk
     - GPUs
     - COMPONENTs
   * - 2
     - amd64
     - 4
     - 4GB
     - 100GB SSD
     - no
     - Grafana, Prometheus


Then deploy the Anbox Cloud Core bundle with the overlay file:

.. code:: bash

   $ juju deploy cs:~anbox-charmers/anbox-cloud-core --overlay monitoring.yaml

The monitoring stack will be available after all added units end up with
the active status.

Streaming Stack Deployment
==========================

For the monitoring stack integration either for a fresh or an existing
Anbox Cloud Streaming Stack deployment, the overlay file is quite
similar to what you use for monitoring stack integration for core
deployment but with minor further modifications. Just copy the following
code snippet into a ``monitoring.yaml`` file.

.. code:: yaml

   applications:
     grafana-proxy:
       charm: 'cs:haproxy'
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
       charm: 'cs:prometheus2-18'
       num_units: 1
       to:
         - '3'

     ams-monitor:
       charm: 'cs:telegraf-39'
       options:
         tags: region=cloud-0
         prometheus_output_port: "20003"

     lxd-monitor:
       charm: 'cs:telegraf-39'
       options:
         tags: region=cloud-0
         prometheus_output_port: "20004"

     grafana:
       charm: 'cs:grafana-36'
       num_units: 1
       options:
         root_url: '%(protocol)s://%(domain)s:%(http_port)s/grafana'
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

The ideal requirements for the machine for monitoring stack deployment
are the following:


.. list-table::
   :header-rows: 1

   * - ID
     - Architecture
     - CPU cores
     - RAM
     - Disk
     - GPUs
     - COMPONENTs
   * - 3
     - amd64
     - 4
     - 4GB
     - 100GB SSD
     - no
     - Grafana, Prometheus


Then deploy the Anbox Cloud Streaming Stack bundle with the overlay
file:

.. code:: bash

   $ juju deploy cs:~anbox-charmers/anbox-cloud --overlay monitoring.yaml

The monitoring stack will be available after all added units end up with
the active status.
