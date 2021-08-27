Anbox Cloud is optimized to provide containers at high density per host. However in order to provide enough underlying resources for a specific number of containers  we need to do some calculations to find out how many LXD machines with how many resources we need.

Each container will take a specific amount of resources defined by the instance type used by the application it is launched for. If an application uses the `a2.3` instance type it requires 2 CPU cores and 3GB of memory and 3GB of disk space (see [Instance Types](https://discourse.ubuntu.com/t/instance-types/17764) for details on how much resources each instance type requires). AMS internally summarizes the amount of resources used by containers on a single machine and disallows launching additional containers when all resources are used.

For a machine with 8 CPU cores and 16GB of memory we could only launch 4 containers before we run out of resources. As a single container will not use the dedicated CPU cores all time at 100% AMS allows overcommiting available resources.

Each node has two configuration items called `cpu-allocation-rate` and `memory-allocation-rate` of type float which define the multiplicator used for overcomitting resources. By default AMS sets `cpu-allocation-rate` to `4` and `memory-allocation-rate` to 2. This sums up the available resources to `4 * 8 CPU cores = 36 CPU Cores` and `2 * 16GB memory = 32GB memory` which will allow 10 containers to take place on the node.

The currently configured allocation rates for a specific node can be shown via the following command:

```bash
$ amc node show lxd0
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

Based on this we can calculate now the amount of resources we need to run a specific number of containers. For example if we have a Qualcomm Centriq 2400 which has 48 CPU cores and want to run 100 containers of instance type `a2.3`:

```bash
CPU allocation rate = 100 * 2 CPU cores / 48 CPU cores ~= 5
Memory needed = 100 * 3GB / 2 = 150 GB
Disk space needed = 100 * 3GB = 300 GB
```

In this example we used a memory allocation rate of `2`.

Which CPU allocation rate makes sense always depends on which type of application will be running inside the containers and which amount of CPU it needs. For low CPU intensive applications a higher and for high CPU intensive applications a lower allocation rate makes sense.
