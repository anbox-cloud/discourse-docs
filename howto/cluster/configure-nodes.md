Your cluster or multi-node appliance might contain nodes with different resources and different capacity. Therefore, each node can be configured separately.

## Show node configuration

To display the current node configuration for a node (for example, `lxd0`), enter the following command:

    amc node show <node>

This command will return output similar to the following:

```bash
name: lxd0
status: online
disk:
    size: 100GB
network:
    address: 10.119.216.34
    bridge-mtu: 1500
config:
    public-address: 10.119.216.34
    use-port-forwarding: true
    cpu-cores: 8
    cpu-allocation-rate: 4
    memory: 16GB
    memory-allocation-rate: 2
    gpu-slots: 10
    gpu-encoder-slots: 0
    tags: []
```

<a name="configure-allocation-rates"></a>
## Configure allocation rates

AMS allows over-committing available resources on a node. This mechanism improves resource usage, because usually, containers don't use 100% of their dedicated resources all of the time.

By default, AMS uses a CPU allocation rate of `4` and a memory allocation rate of `2`. See [Over-committing](https://discourse.ubuntu.com/t/about-capacity-planning/28717#overcommitting) for more information.

You can configure the allocation rates with the `cpu-allocation-rate` and `memory-allocation-rate` configuration items.

Use the following commands to set the allocation rates on a node (for example, `lxd0`):

    amc node set <node> cpu-allocation-rate <value>
    amc node set <node> memory-allocation-rate <value>

<a name="configure-node-accept-new-containers"></a>
## Configure if a node can accept new containers

You can configure a node to stop accepting new containers. This is especially important in certain scenarios such as [scaling down a LXD cluster](https://discourse.ubuntu.com/t/how-to-scale-down-a-lxd-cluster/24323). When you want to remove a node from the LXD cluster, the node must not have any containers. Hence, all running containers must be removed or disconnected and AMS must stop considering the node for new containers.

Use the following command to prevent the node from accepting new containers:

    amc node set <node> unscheduable true  

<a name="configure-gpu-slots"></a>
## Configure GPU slots

GPU slots are used to share GPUs amongst containers. See [About GPU support](https://discourse.ubuntu.com/t/gpu-support/17768) and [GPU slots](https://discourse.ubuntu.com/t/about-capacity-planning/28717#gpu-slots) for more information.

Each GPU-equipped cluster node is configured with a number of GPU slots and a number of GPU encoder slots. See [Node-specific configuration](https://discourse.ubuntu.com/t/ams-configuration/20872#node-specific) for the default values that are used. Nodes without GPU are configured with 0 GPU slots and 0 GPU encoder slots.

Use the following command to change the number of GPU slots for a node  (for example, `lxd0`):

    amc node set <node> gpu-slots <number>
