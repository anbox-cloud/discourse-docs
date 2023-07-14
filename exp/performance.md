The performance of your Anbox Cloud deployment depends on a lot of different factors. To ensure optimal performance, check and monitor all areas and tune your deployment based on your findings.

To measure the performance based on different parameters, you should [run performance benchmarks](https://discourse.ubuntu.com/t/how-to-run-benchmarks/17770). See the provided [Performance benchmarks](https://discourse.ubuntu.com/t/performance-benchmarks/24709) as a reference for what performance you can expect with different hardware configurations.

The main areas for performance tuning are:

- [Container density](#container-density)
- [Container CPU access](#container-cpu-access)
- [Hardware and network setup](#hardware-setup)
- [Container startup time](#startup-time)
- [Client devices](#client-devices)

<a name="container-density"></a>
## Container density

The most apparent performance aspect is how many containers you can run on each of your machines.

Of course, the container density depends a lot on the available hardware. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for detailed information about estimating the necessary capacity and the hardware requirements for your Anbox Cloud deployment.

In addition, check your applications and make sure they use the resources in a fair way. Applications should avoid spikes in GPU utilisation, because such spikes require the application to reserve more resources and therefore reduce the container density.

Generally, applications should use the smallest suitable instance type. However, if you see an overall bad performance when running the application, using a more powerful instance type usually helps (even though it reduces the container density). As an example, consider an application that runs on an Anbox Cloud deployment that does not have any GPUs installed. In this case, the rendering workload is put on the CPU instead of the GPU, and if the instance type of the application does not have a sufficient number of vCPU cores, the performance of the application is impacted. This can show, for example, in the virtual keyboard being really slow. By switching to a more powerful instance type, the container density is reduced, but the performance of each application container is increased.

<a name="container-cpu-access"></a>
## Container CPU access

AMS has different modes to grant CPU access to a container. The `cpu.limit_mode` configuration option can be used to change the mode. The possible modes are:

* `scheduler` :

    This mode uses the LXD [`limits.cpu.allowance`](https://documentation.ubuntu.com/lxd/en/latest/reference/instance_options/#cpu-limits) configuration option to grant a container a CPU time budget via the Linux CFS scheduler. See [CFS Bandwidth Control](https://www.kernel.org/doc/html/latest/scheduler/sched-bwc.html) for more details.
* `pinning` :

   This mode uses the LXD [`limits.cpu`](https://documentation.ubuntu.com/lxd/en/latest/reference/instance_options/#cpu-limits) configuration option to pin a set of CPU cores to a container. LXD is responsible for allocating a specific number of cores to a container and load-balance all running containers on all available cores.

   Using `pinning` requires a system with [cgroup-v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) enabled. Otherwise, limitations of [cgroup-v1](https://docs.kernel.org/admin-guide/cgroup-v1/index.html) might cause the load distribution over available CPU cores to not be optimal. [cgroup-v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) is enabled by default starting with Ubuntu 22.04 and can be enabled on Ubuntu 20.04 by booting with `systemd.unified_cgroup_hierarchy=1` added to [the kernel boot parameters](https://wiki.ubuntu.com/Kernel/KernelBootParameters).

By default, AMS uses the `scheduler` option, because it provides the most generic solution to a large set of use cases that Anbox Cloud supports. However, in some cases CPU pinning might be the better option to distribute load across all available CPU cores on a system.

<a name="hardware-setup"></a>
## Hardware and network setup

See [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) for the minimum hardware requirements for Anbox Cloud. Note that these list the minimum requirements, and using more powerful hardware will increase performance.

For optimal performance, you should use a dedicated block device for LXD storage. Using a loop file is considerably slower. See [LXD storage](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802#lxd-storage) for more information.

The overall performance depends not only on the hardware used for the actual Anbox Cloud deployment, but also on the setup used for other components that Anbox Cloud relies on. For example, the etcd database must use a hard disk that is fast enough; see [Hardware recommendations](https://etcd.io/docs/v3.5/op-guide/hardware/) for detailed information.

Also make sure that there is a stable network connection between the nodes of your cluster, to decrease the latency between nodes.

<a name="startup-time"></a>
## Container startup time

A very noticeable performance issue is a long wait time when starting an application.

When a user starts an application, Anbox Cloud retrieves the application image and launches a new container for it. By default, Anbox Cloud turns off image compression in LXD when launching a container from an image. This method speeds up the launch of the container (because the image does not need to be uncompressed), but it causes more traffic over the network (because the image is transferred uncompressed). If the network connection between your cluster nodes is rather slow, the overall container startup time might improve by enabling image compression. You can change the default configuration by setting the [images_compression_algorithm](https://charmhub.io/ams-lxd/configure#images_compression_algorithm) configuration on the `ams-lxd` charm. Of course, in addition to compression, the size of the image is also relevant. The smaller the image, the faster it can be synchronised across the LXD nodes in a cluster.

Another configuration that affects the container startup time is [shiftfs_enabled](https://charmhub.io/ams-lxd/configure#shiftfs_enabled). This configuration is currently disabled by default, because it can cause issues with some Android applications. However, if your applications run fine with `shiftfs_enabled` set, it can considerably improve the container startup time. You should be aware though that support for shiftfs might be dropped in future releases.

You should also check the hooks that you use in your application. If you use any startup hooks (`pre-start` or `post-start`) that take a long time or wait for resources to become available, the container startup is delayed. If you use a `post-stop` hook that prolongs the container shutdown, this might also affect the startup time of new containers (because it might not be possible to start more containers until the existing containers terminate).

<a name="client-devices"></a>
## Client devices

In addition to optimising the performance of your Anbox Cloud deployment, you must also make sure that the client devices that access it can fully utilise its capabilities.

All client devices that access an Anbox Cloud deployment must be capable of low-latency video decoding. They must also use a compatible version of Android WebView (version 90 at the minimum, and ideally the latest stable release).

Furthermore, the network connection is crucial. When implementing your applications, you must take into account what kind of connection the client devices will usually have (for example, 4G, 5G or WiFi), so that you can optimise the network traffic that your applications require.

Also make sure to optimise the network path from the Anbox Cloud server to the client devices. What exactly that entails depends on your specific use case; for public clouds, it often means choosing the region that is located closest to the end users. When using a bare metal installation, you should deploy servers that are geographically close to the end users. There might also be other solutions depending on the network service route.
