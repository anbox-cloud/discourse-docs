Anbox Cloud gathers various performance metrics and makes them accessible through API endpoints. While Anbox Cloud does not provide its own observability solution, it supports implementing and integrating custom solutions for monitoring performance.

See [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521) for a list of available metrics and how to access them. [LXD provided metrics](https://documentation.ubuntu.com/lxd/en/latest/reference/provided_metrics/) has a list of metrics available through LXD.

The implementation of a monitoring or observability solution depends on your specific use case and the tools that you want to use. See [Open source observability for enterprises](https://ubuntu.com/observability) for an overview of observability tools and stacks that are recommended and supported by Canonical. In particular, see the [Canonical Observability Stack (LMA2)](https://juju.is/docs/lma2).

Anbox Cloud includes the following reference implementations that you can use as a starting point for planning and integrating your custom observability solution:

- [Example: Collect metrics](https://discourse.ubuntu.com/t/monitoring-grafana/17787)
- [Example: Monitor status](https://discourse.ubuntu.com/t/monitoring-nagios/17788)

These examples show how to set up an observability solution in a full Anbox Cloud deployment. They can also be used for a first test. Be aware though that these examples are provided for reference only. They are not fully supported and should not be used in a production environment. They cannot be used with the Anbox Cloud Appliance.

<a name="monitoring-dashboard"></a>
## Monitoring dashboard in the Anbox Cloud Appliance

The Anbox Cloud Appliance comes with a basic monitoring dashboard that displays the metrics collected through Telegraf and Prometheus.

To access the dashboard, complete the following steps:

1. Log on to the machine that runs the Anbox Cloud Appliance and create a user account for the monitoring dashboard:

        anbox-cloud-appliance monitor account create <user_name> --email=<email_address> --password=<password> --role=<role>

    The available roles are `viewer`, `editor` and `admin`.

2. Make sure that the monitoring dashboard is exposed. This is the default. If you unexposed it earlier, expose it again by running the following command:

        anbox-cloud-appliance monitor expose
3. Access the monitoring dashboard at `https://<your-machine-address>/monitor/` and log on with the user account that you created.
4. Click the search symbol on the left-hand side and go to the **Search dashboards** page.
5. Select the dashboard that contains the information you're interested in to display it.

If you want to monitor additional metrics and events, you can do so by adding plugins to Telegraf. See [How to configure Telegraf](https://discourse.ubuntu.com/t/how-to-configure-telegraf/30365) for more information.
