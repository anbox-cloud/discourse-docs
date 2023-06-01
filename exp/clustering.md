While it is possible to install Anbox Cloud on a single machine, you usually want to distribute the load over several machines in a cluster.

The Anbox Cloud Appliance provides basic and experimental support for multi-node setups. See [Multi-node support for the Anbox Cloud Appliance](#multi-node-appliance).

If you're running Anbox Cloud, full clustering support is available. See [Clustering for full Anbox Cloud deployments](#clustering-anbox-cloud).

<a name="multi-node-appliance"></a>
## Multi-node support for the Anbox Cloud Appliance

If you're running the Anbox Cloud Appliance and you want to extend the available container capacity, you can join additional machines to the appliance.

The appliance uses [FAN networking](https://wiki.ubuntu.com/FanNetworking) to spawn an overlay network that allows containers on different machines to communicate with each other. FAN networking requires a `/16` or `/24` subnet on the network interface. If the appliance is installed on a machine that is not on such a subnet, the appliance disables FAN networking. In this case, extending the appliance with additional nodes will not be possible.

This setup extends the capacity, but currently, it does not provide support for high availability (HA).

See [How to join a machine to the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-join-a-machine-to-the-anbox-cloud-appliance/29054) for instructions on how to add machines to the appliance.

<a name="clustering-anbox-cloud"></a>
## Clustering for full Anbox Cloud deployments

In a clustering setup for a full Anbox Cloud deployment, one node is dedicated to host the AMS service (the management node). If you use the streaming stack, two additional nodes are dedicated to host the extra services required for streaming. All other nodes are used as worker nodes.

Each worker node runs [LXD](https://linuxcontainers.org/) in [clustering mode](https://linuxcontainers.org/lxd/docs/latest/clustering/), and this LXD cluster is used to host the Android containers.

### Cluster capacity

Anbox Cloud is optimised to provide containers at high density per host. To determine how many cluster nodes you need and what resources they should have, you must estimate the capacity that you require for your use case. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for more information.

### LXD auto scaling

Different use cases for Anbox Cloud require elasticity of the LXD cluster to deal with dynamic user demand throughout a certain time period. This involves increasing the number of nodes of the LXD cluster when demand increases and reducing the number of nodes when demand decreases. As Anbox Cloud provides fine-grained capacity management to have tight control over how many users / containers are running on a single node, the driving factor for an auto scaling implementation cannot be deduced from CPU, memory or GPU load but from the planned capacity of the currently available nodes in the cluster.

The current release of Anbox Cloud has no builtin auto scaling implementation but comes with all needed primitives to build one. In a future version, Anbox Cloud will provide an auto scaling framework that will simplify various aspects of an implementation.

#### Guidelines for auto scaling

The following guidelines are both recommended and must-have aspects of an auto scaling implementation. Make sure that your auto scaling implementation follows these to stay within a supported and tested scope.

1. Don't scale the LXD cluster below three nodes. You should keep three active nodes at all times to ensure the database LXD uses can achieve a quorum and is highly available. If you run below three nodes, your cluster is very likely to get into a non-functional state or be lost completely (see [LXD documentation](https://linuxcontainers.org/lxd/docs/latest/clustering#recover-from-quorum-loss) for more information).
1. A single LXD cluster should take no more than 40 nodes.
1. If you need more than 40 nodes, you should create a separate cluster in a separate Juju model with its own AMS.
1. Scaling a cluster up with multiple new nodes in parallel is fine and recommended if you need to quickly increase your cluster capacity.
1. Scaling down **MUST** strictly happen in a sequential order with no other scaling operations (for example, scale up) running in parallel.
1. Before removing a LXD node from the cluster you **MUST** delete all containers on it first.

#### Scaling up or down

See [How to scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322) and [How to scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323) for instructions on how to add or remove nodes from the cluster.

### When to scale up or down the cluster?

Answering the question when to scale a cluster up and down is not simple and is different for each use case. The traditional approach to measure CPU, memory or GPU load does not apply for Anbox Cloud as capacity is well planned and the number of containers per node is configured ahead of time. Furthermore, user patterns are hard to predict and will be different in each case. For that reason, custom logic is required to take a decision when a cluster should be scaled up or down.

Anbox Cloud provides various metrics to help decide when to scale up or down. See the [relevant documentation](https://discourse.ubuntu.com/t/prometheus-metrics/19521) for a list of available metrics that can be used to take a decision. Based on this together with data from a production system, you can build a model trying to predict when auto scaling should trigger or not.

Future versions of Anbox Cloud will provide a framework which will help to implement such a model.
