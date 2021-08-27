Different use cases for Anbox Cloud require elasticity of the LXD cluster to deal with dynamic user demand throughout a certain time period. This involves increasing the number of nodes of the LXD cluster when demand increases and reducing the number of nodes when demand decreases. As Anbox Cloud provides fine grained capacity planning to have tight control over how many users / containers are running on a single node the driving factor for an auto scaling implementation cannot be deduced from CPU, memory or GPU load but from the planned capacity of the currently available nodes in the cluster.

The current release of Anbox Cloud has no builtin auto scaling implementation but comes with all needed primitives to build one. In a future version, Anbox Cloud will  provide an auto scaling framework which will simplify various aspects of an implementation.

## Guidelines for Auto Scaling

The following are both recommended and must-have aspects of an auto scaling implementation. Please make sure your auto scaling implementation follows these to stay within a supported and tested scope.

1. Don't scale the LXD cluster below 3 nodes. You should keep three active nodes at all times to ensure the database LXD uses can achieve a quorum and is highly available. If you run below three nodes your cluster is very likely to get into a non-functional state or be lost completely (see [LXD documentation](https://lxd.readthedocs.io/en/latest/clustering/#recover-from-quorum-loss) for more information).
2. A single LXD cluster should take no more than 40 nodes
3. If you need more than 40 nodes you should create a separate cluster in a separate Juju model with its own AMS.
4. Scaling a cluster up with multiple new nodes in parallel is fine and recommended if you need to quickly increase your cluster capacity.
5. Scaling down **MUST** strictly happen in a sequential order with now other scaling operations running in parallel (e.g. scale up)
6. You **MUST NOT** remove a LXD database node (Check `lxc cluster ls` on any LXD node) when scaling down. Due to issues in [LXD](https://linuxcontainers.org/lxd/introduction/) and it's [raft implementation](https://github.com/canonical/raft)  this may lead to an unhealthy cluster in some cases. These issues are currently (March 2021) actively being worked by the LXD engineering team.
7. Before removing a LXD node from the cluster you **MUST** delete all containers on it first.

## Scale Up an LXD Cluster

Scaling an LXD cluster  can be achieved via Juju in case of Anbox Cloud. Juju automates the deployment of the individual units and links them together.

Adding additional LXD units or removing existing ones is not an instant operation. Adding a new node for example can take 5-10 minutes and need to be planned in advance. The deployment of a single node will include the following steps:

1. Allocate a new machine from the underlying cloud provider
2. Machine startup and first time initialization
3. LXD installation process
4. Registration of the LXD node with the existing cluster and AMS
5. Synchronization of necessary artifacts from other nodes in the LXD cluster (images, ..)

To add additional LXD nodes run

    $ number_of_units=3
    $ juju add-unit -n “$number_of_units” lxd

This will trigger the deployment of the nodes and you can for example use

    $ snap install --classic juju-wait
    $ juju wait -w

to wait until the deployment has settled. Due to internal implementation details waiting for just the units to settle and report status “active” is not enough and you also have to check that the unit is correctly added to AMS and is itself part of the LXD cluster. You can do that with code similar to the following script:

    $ cat << EOF > wait-or-unit.sh
    #!/bin/sh -ex
    unit=$1
    # Drop slash from the unit name
    node_name=${unit/\//}
    while true; do
      if juju ssh ams/0 -- /snap/bin/amc node ls | grep -q "${node_name}.*online"
        break
      fi
      sleep 5
    done
    while true ; do
      if juju ssh "$unit" -- lxc cluster ls ; then
        break
      fi
      sleep 5
    done
    EOF
    $ chmod +x wait-for-unit.sh
    $ ./wait-for-unit.sh "lxd/1"

The script just serves as an example and you should implement a similar check in your auto scaling implementation. If you scale up with multiple nodes at a time your implementation should check for all new nodes to be fully added to both AMS and the LXD cluster.

## Scale Down a LXD Cluster

Scaling down an LXD cluster involves more checks than scaling up. First a suitable candidate node needs to be picked. When a node is removed all still running containers on it are stopped and potentially connected users are disconnected. To avoid this AMS provides a feature to mark a node as unschedulable so that it will not be considered for any further container launches. You can mark a node as unschedulable with

    # NOTE: The typo is correct and will be fixed in a future Anbox Cloud release
    $ amc node set lxd0 unscheduable true

Now the node won't be considered for any further container launches. As it may still host containers you can now either decide to kill all containers or wait for your users to disconnect. You can check with the following command if the node still hosts containers:

    $ amc ls --filter node=lxd0 --format=csv | wc -l

If you want to kill all containers immediately you can run

    $ for id in $(amc ls --filter node=lxd0 --format=csv | cut -d, -f1) ; do amc delete -y "$id" ; done

When the node is ready to be removed you can simply remove it by using Juju

    $ juju remove-unit lxd/0

Once you invoke the removal of the node you **MUST** wait for the node to be fully removed before you attempt to remove the next node or add a new one. You can do that with a combination of `juju wait` and the following script (which is the inverse of the one we used above when scaling up):

    $ cat << EOF > wait-or-unit.sh
    #!/bin/sh -ex
    unit=$1
    # Drop slash from the unit name
    node_name=${unit/\//}
    while true; do
      if ! juju ssh ams/0 -- /snap/bin/amc node ls | grep -q “$node_name”
        break
      fi
      sleep 5
    done
    while true ; do
      if ! juju ssh "$unit" -- lxc cluster ls ; then
        break
      fi
      sleep 5
    done
    EOF
    $ chmod +x wait-for-unit.sh
    $ ./wait-for-unit.sh "lxd/1"

Once the unit is fully removed you can continue to remove the next one.

## When to should the cluster scale up or down?

Answering the question when to scale a cluster up and down is not simple and is different for each use case. The traditional approach to measure CPU, memory or GPU load does not apply for Anbox Cloud as capacity is well planned and the number of containers per node is configured ahead of time. Furthermore user patterns are hard to predict and will be different in each case. For that reason custom logic is required to take a decision when a cluster should be scaled up or down.

Anbox Cloud provides various metrics to help to decide when to scale up or down. See the [relevant documentation](https://discourse.ubuntu.com/t/prometheus-metrics/19521) for a list of available metrics which can be used to take a decision. Based on this a model can be built together with data from a production system trying to predict when auto scaling should trigger or not.

Future versions of Anbox Cloud will provide a framework which will help to implement such a model.
