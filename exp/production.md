When you are planning a production deployment, you should consider the aspects that you want to customise for best results. This topic covers the most common and important requirements when you are planning to move your Anbox Cloud deployment to production. While there could be other specifically tailored needs, this topic helps you identify your basic requirements and deployment strategy.

## Hardware requirements 

Depending on your workload and the type of deployment you choose, hardware requirements can differ. See [requirements](https://discourse.ubuntu.com/t/requirements/17734) to get an idea about the kind of hardware that is required to run a full Anbox Cloud deployment with the streaming stack or a minimal core version of the deployment without the streaming stack. 

You should pay special attention to the hardware requirements of applications that are used but not maintained by Anbox Cloud. 

## Software requirements 

Anbox Cloud deployments require the Ubuntu operating system. You should consider the Ubuntu OS, LXD, and Juju versions supported by Anbox Cloud for a production deployment. See [requirements](https://discourse.ubuntu.com/t/requirements/17734) to see compatible software versions.

## Networking requirements 

Consider the following questions to decide your networking requirements:

* In your deployment, how many virtual private clouds(VPC) do you need per cluster?
* Do you need subnets? If yes, what is the range of the subnets that you want to define?
* Have you defined your AWS regions?
* For each cluster, how do you want to map the subnets within the virtual private clouds into Juju spaces?
* Where is your Anbox Application Registry (AAR) deployed? How will the AMS in other clusters connect to AAR? Define your virtual private cloud peering requirements based on the number of clusters you have and where AAR is deployed. To know more about AAR, see the following links:
    * [Anbox Application Registry](https://discourse.ubuntu.com/t/anbox-application-registry-aar/17761)
    * [How to deploy an AAR](https://discourse.ubuntu.com/t/how-to-deploy-an-aar/17749) 
    * [How to configure an AAR](https://discourse.ubuntu.com/t/how-to-configure-an-aar/24319)

## Storage requirements
Based on your safety protocols, think about where you would want to host your storage. Also, refer to the following links that will help you plan and calculate your storage needs:

* [Requirements](https://discourse.ubuntu.com/t/requirements/17734)
* [etcd recommendations](https://etcd.io/docs/v3.5/op-guide/hardware/)
* [Capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717)

## Scalability, High availability, and redundancy

With Anbox Cloud, you can scale your deployment to as many clusters and subclusters as you require. It is a good idea to define how many Anbox clusters you want to deploy and how many subclusters per cluster. 

You should also define the number of instances that you require for each model/service. For example, think about the number of Juju controller instances that you need.

Anbox Cloud comes with support for High Availability (HA) for both Core and the Streaming Stack.You can define HA by adding new Juju units. See [How to enable High availability?](https://discourse.ubuntu.com/t/how-to-enable-high-availability/17754) to plan your HA requirements.

## Security

### Control Plane TLS Termination

The components of Anbox Cloud need to be able to communicate securely over the network. This is accomplished using TLS and public-key encryption with a chain of trust up to a shared root Certificate Authority (CA). However, when the cluster is being brought up or a new unit is being added, the chain of trust and certificates required must be bootstrapped into the machines.

All communication between Juju units and the Juju controller happens over TLS-encrypted websockets. The certificate for the TLS connection to the controller is added as explicitly trusted to each machine as part of the bootstrap process using a combination of cloud-init and SSH.

With this secure channel, Juju charms can communicate with each other using relation data. The data published by one unit is sent to the controller, which then makes it available for all other units on the same relation. The data for each relation is scoped by ID and is only visible to units participating in the specific relation on which it is set.

### Patching

You should keep your Anbox deployment updated to the latest available stable version. You should also update the other applications which make up Anbox. Keeping up to date ensures you have the latest fixes and security patches for smooth operation of your cluster.
For details about the Anbox Cloud release roadmap, see 
[Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359).

## Data backup

Consider how frequently you want your data backed up and where you want to host your backed up data.

## Load balancing 

Load balancing is done using the Elastic Load Balancing from AWS. Assess how many load balancers you require and whether you want to place them on public or private subnets. You should also think about whether you want to associate these load balancers with Elastic IPs.

## Monitoring and metrics

Although Anbox Cloud does not offer its own observability solution, Anbox Cloud gathers various performance metrics that you can access through API endpoints to create a monitoring solution.

The following table lists and describes the various components that make up the Canonical Monitoring & Management Stack: 

| Category | Component | Description |  
|------|------|---------|
| Logging Stack | Graylog | Graylog is a centralised log aggregator and analyser.  |
|   | Filebeat | The next-generation Log Forwarder, Filebeat tails logs and quickly sends this information to Graylog for further parsing |
|   | Elasticsearch | Elasticsearch, storage backend for Graylog, is a flexible and powerful open source, distributed, real-time search and analytics engine. |
| Metric Collector | Prometheus | Prometheus is a systems and service monitoring system. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.|
|   | Telegraf | Telegraf is an agent which collects metrics from the core services and writes them into Prometheus. |
| Metric Visualiser | Grafana | The leading graph and dashboard builder for visualising time series metrics. |
|  Alerting System | Nagios | Nagios is a monitoring and management system for hosts, services, and networks. |
|    | NRPE | This service runs as a background process on the hosts and processes command execution requests from the check_nrpe plugin on the Nagios service. |


In addition to understanding these components, you can decide if you want to use Canonical's monitoring system or a customised version. See [How to monitor Anbox Cloud?](https://discourse.ubuntu.com/t/how-to-monitor-anbox-cloud/24338) and [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521) for a detailed understanding of monitoring and metrics to assess your own monitoring needs for the production deployment. To help you in your assessment, you can refer to these example implementations: [Example: Collect metrics](https://discourse.ubuntu.com/t/example-collect-metrics/17787) and [Example: Monitor status](https://discourse.ubuntu.com/t/example-monitor-status/17788).

## Licensing and Support

You need the Ubuntu Pro subscription to use Anbox Cloud. Depending on the type of subscription you choose, your support model differs. You can refer to the [Ubuntu Pro website](https://ubuntu.com/pro) to learn and compare the different types of subscriptions. 

## Upgrade

When you consider a production deployment, it is important to assess your upgrade roadmap. For more information about upgrading Anbox Cloud and the prerequisites required for the upgrade process, see [How to upgrade Anbox Cloud](https://discourse.ubuntu.com/t/how-to-upgrade-anbox-cloud/17750). 

You can also choose to subscribe to the [announcements about Anbox Cloud releases](https://discourse.ubuntu.com/c/anbox-cloud/announcements/55) on discourse. For insights into the Anbox Cloud release roadmap, see [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359).