[Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) is a server-based agent that collects and sends metrics and events about the system it monitors.

Anbox Cloud automatically deploys Telegraf on every machine and configures it to collect basic metrics. You can then access these metrics through the [monitoring dashboard](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338#monitoring-dashboard) in the Anbox Cloud Appliance, or through the observability solution that you implement for your full Anbox Cloud deployment (see [Example: Collect metrics](https://discourse.ubuntu.com/t/monitoring-grafana/17787)).

You can customise the Telegraf configuration and add and configure plugins that you want to use. For example, you might want to add an input plugin that collects GPU statistics (like the [Nvidia System Management Interface (SMI) Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/nvidia_smi)), or the `file` output plugin to write the metrics to an output file. See the [Telegraf documentation](https://docs.influxdata.com/telegraf/) for available plugins and configurations.

## Configure Telegraf in the Anbox Cloud Appliance

If you use the Anbox Cloud Appliance, add your custom configuration files to the `$SNAP_COMMON/telegraf/conf.d/` folder. Any files in that folder are added to the default configuration.

Do not modify the `$SNAP_COMMON/telegraf/main.conf` file. This file is managed by the Anbox Cloud Appliance and might be overwritten during an update.

## Configure Telegraf in a full Anbox Cloud deployment

When [deploying Anbox Cloud with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744), Telegraf is deployed as a charm.

To configure it, follow the instructions in the [Telegraf documentation](https://docs.influxdata.com/telegraf/).
