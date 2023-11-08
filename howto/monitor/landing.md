Anbox Cloud gathers various performance metrics and makes them accessible through API endpoints. While Anbox Cloud does not provide its own observability solution, it supports implementing and integrating custom solutions for monitoring performance.

See [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521) for a list of available metrics and how to access them. [LXD Metric exporter for instances](https://discuss.linuxcontainers.org/t/lxd-metric-exporter-for-instances/11735) has a list of metrics available through LXD.

The implementation of a monitoring or observability solution depends on your specific use case and the tools that you want to use. See [Open source observability for enterprises](https://ubuntu.com/observability) for an overview of observability tools and stacks that are recommended and supported by Canonical. In particular, see the [Canonical Observability Stack (LMA2)](https://juju.is/docs/lma2).

Anbox Cloud includes the following reference implementations that you can use as a starting point for planning and integrating your custom observability solution:

- [Example: Collect metrics](https://discourse.ubuntu.com/t/monitoring-grafana/17787)
- [Example: Monitor status](https://discourse.ubuntu.com/t/monitoring-nagios/17788)

These examples show how to set up an observability solution in a full Anbox Cloud deployment. They can also be used for a first test. Be aware though that these examples are provided for reference only. They are not fully supported and should not be used in a production environment. They cannot be used with the Anbox Cloud Appliance.
