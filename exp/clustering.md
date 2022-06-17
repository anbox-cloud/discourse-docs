While it is possible to install Anbox Cloud on a single machine, you usually want to distribute the load over several machines in a cluster. In such a clustering setup, one node is dedicated to host the AMS service (the management node). If you use the streaming stack, two additional nodes are dedicated to host the extra services required for streaming. All other nodes are used as worker nodes.

Each worker node runs [LXD](https://linuxcontainers.org/) in clustering mode, and this LXD cluster is used to host the Android containers.

[note type="information" status="Note"]Clustering is currently not available for the Anbox Cloud Appliance.[/note]

## Cluster capacity

Anbox Cloud is optimised to provide containers at high density per host. To determine how many cluster nodes you need and what resources they should have, you must estimate the capacity that you require for your use case. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for more information.

## LXD auto scaling

Different use cases for Anbox Cloud require elasticity of the LXD cluster to deal with dynamic user demand throughout a certain time period. This involves increasing the number of nodes of the LXD cluster when demand increases and reducing the number of nodes when demand decreases. As Anbox Cloud provides fine-grained capacity management to have tight control over how many users / containers are running on a single node, the driving factor for an auto scaling implementation cannot be deduced from CPU, memory or GPU load but from the planned capacity of the currently available nodes in the cluster.

The current release of Anbox Cloud has no builtin auto scaling implementation but comes with all needed primitives to build one. In a future version, Anbox Cloud will provide an auto scaling framework that will simplify various aspects of an implementation.

### Guidelines for auto scaling

The following guidelines are both recommended and must-have aspects of an auto scaling implementation. Make sure that your auto scaling implementation follows these to stay within a supported and tested scope.

1. Don't scale the LXD cluster below three nodes. You should keep three active nodes at all times to ensure the database LXD uses can achieve a quorum and is highly available. If you run below three nodes, your cluster is very likely to get into a non-functional state or be lost completely (see [LXD documentation](https://linuxcontainers.org/lxd/docs/latest/clustering#recover-from-quorum-loss) for more information).
2. A single LXD cluster should take no more than 40 nodes.
3. If you need more than 40 nodes, you should create a separate cluster in a separate Juju model with its own AMS.
4. Scaling a cluster up with multiple new nodes in parallel is fine and recommended if you need to quickly increase your cluster capacity.
5. Scaling down **MUST** strictly happen in a sequential order with no other scaling operations (for example, scale up) running in parallel.
6. You **MUST NOT** remove a LXD database node (check `lxc cluster ls` on any LXD node) when scaling down. Due to issues in [LXD](https://linuxcontainers.org/lxd/introduction/) and its [raft implementation](https://github.com/canonical/raft), this might lead to an unhealthy cluster in some cases. These issues are currently (March 2021) being worked on by the LXD engineering team.
7. Before removing a LXD node from the cluster you **MUST** delete all containers on it first.

### Scaling up or down

See [How to scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322) and [How to scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323) for instructions on how to add or remove nodes from the cluster.

## When to scale up or down the cluster?

Answering the question when to scale a cluster up and down is not simple and is different for each use case. The traditional approach to measure CPU, memory or GPU load does not apply for Anbox Cloud as capacity is well planned and the number of containers per node is configured ahead of time. Furthermore, user patterns are hard to predict and will be different in each case. For that reason, custom logic is required to take a decision when a cluster should be scaled up or down.

Anbox Cloud provides various metrics to help decide when to scale up or down. See the [relevant documentation](https://discourse.ubuntu.com/t/prometheus-metrics/19521) for a list of available metrics that can be used to take a decision. Based on this together with data from a production system, you can build a model trying to predict when auto scaling should trigger or not.

Future versions of Anbox Cloud will provide a framework which will help to implement such a model.
