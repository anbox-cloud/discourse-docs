Anbox Cloud provides a rich software stack that enables you to run Android applications in the cloud for all kinds of different use cases, including high-performance streaming of graphics to desktop and mobile client devices.

At its heart, it uses lightweight container technology instead of full virtual machines and maintains a single Android system per container. This approach allows for higher density and better performance per host while ensuring security and isolation of each container. Depending on the target platform, payload and desired application performance (for example, frame rate), Anbox Cloud can run more than 100 containers on a single machine.

For containerisation of Android, Anbox Cloud uses the well established and secure container hypervisor [LXD](https://linuxcontainers.org/). LXD is secure by design, scales to a large number of containers and provides advanced resource management for hosted containers.

<a name="variants"></a>
## Variants

Anbox Cloud comes in two different variants that serve different purposes:

**Anbox Cloud Appliance**

The Anbox Cloud Appliance is a self-contained deployment variant of Anbox Cloud. It uses a sensible standard configuration to hide the complexity and flexibility of [Juju](https://juju.is/). In this way, the Anbox Cloud Appliance allows simple and fast development and prototyping.

**Anbox Cloud**

The regular Anbox Cloud uses [Juju](https://juju.is/) for deployment and operations. It provides rich features and is ready made for a large scale deployment.

See the following table for a comparison of features for the different variants:

| Feature | Anbox Cloud Appliance | Anbox Cloud |
|---------|-----------------------|-------------|
| [Streaming capabilities](https://discourse.ubuntu.com/t/streaming-android-applications/17769) | ✓ | ✓ |
| [Web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871) | ✓ | ✓ |
| [Android API version](https://discourse.ubuntu.com/t/provided-images/24185) | 10, 11, 12 | 10, 11, 12 |
| [Security updates](https://ubuntu.com/support) | ✓ | ✓ |
| [Community support](https://discourse.ubuntu.com/c/anbox-cloud/) | ✓ | ✓ |
| [Vendor support available](https://ubuntu.com/support) | ✓* | ✓ |
| [Monitoring](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338) | - | ✓ |

*\* When purchasing the Anbox Cloud Appliance through the AWS Marketplace, the Ubuntu Pro subscription does not include vendor support.*

Which of both variants you choose depends on your needs. The appliance is well suited for quick prototyping and development or small scale deployments, whereas the regular Anbox Cloud is best to scale big.

[note type="information" status="Tip"]
We recommend to always start with the Anbox Cloud Appliance for first tests. You can then expand to a full Anbox Cloud installation later.
[/note]

## Components

Anbox Cloud is composed of different components that interact with one another.

The core stack includes all components that are required for a basic deployment of Anbox Cloud to work. The streaming stack is a set of components needed to provide streaming functionality.
For containerisation, Anbox Cloud includes LXD.

### Core stack

Anbox Cloud takes care of all management aspects and provides both a fully functional implementation and an integration model to support existing infrastructure and service implementations.

The following figure gives an overview of the different components and their responsibility within the core stack of Anbox Cloud.

![Anbox Cloud core stack|690x398](https://assets.ubuntu.com/v1/e74d1a49-anbox_cloud_core-stack.png)

At the heart of Anbox Cloud sits the [**Anbox Management Service (AMS)**](https://discourse.ubuntu.com/t/about-ams/24321). **AMS** has the job to handle all aspects of the application and container life cycle (including application and image updates) while ensuring high density, performance and fast container startup times.

A developer or system administrator will manage **AMS** through the **command line interface (AMC)** or through custom-built tools interacting with the [**AMS HTTP API**](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801).

For example, a simple Android application testing service would provide a user-facing interface dealing with things like authentication and user management, and would communicate with the REST API to add applications or start and stop containers when a user asks to.

Anbox Cloud can be heavily customised and extended via [**platform plugins**](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#anbox-platform-sdk) and [**addons**](https://discourse.ubuntu.com/t/managing-addons/17759). Platform plugins and addons can be built to add specific streaming capabilities, perform operations within Android containers and much more. One example of a platform plugin is the [**Anbox WebRTC Platform**](https://discourse.ubuntu.com/t/anbox-platforms/18733) used in the Anbox Streaming Stack. Addons are ways to customise the base image by installing additional software and running scripts on different life cycle hooks.

### Streaming stack

Starting from 1.4, Anbox Cloud comes with an easy to use streaming solution. The [**Anbox Streaming Stack**](https://discourse.ubuntu.com/t/streaming-android-applications/17769) is a collection of components designed to run containers on GPU-equipped machines and stream their visual output to clients via [WebRTC](https://webrtc.org/).

The following figure shows an overview of how the different components work together to enable this.

![Anbox Cloud streaming stack|690x440](https://assets.ubuntu.com/v1/bcf90bb6-anbox_cloud_streaming-stack.png)

The main components powering the streaming stack in Anbox Cloud are:

**Agent**: Software running on a server equipped with a GPU connected to Anbox Cloud. It serves as an entry point that the gateway can connect to.

**Anbox Stream Gateway**: The central component that connects clients with agents. Its role is to choose the best possible region depending on the user location and server capacities.

**Client**: The end user application that will display the stream. It can be a desktop application, a website, a mobile application, a TV, a car system or anything capable of handling a WebRTC stream. Anbox Cloud provides an SDK along with the streaming stack to simplify integration with web-based applications.

**TURN/STUN servers**: Servers that find the most optimal network path between a client and the container running its application. The streaming stack provides secure STUN and TURN servers, but you can use public ones as well.

**NATS**: A messaging system that the different components use to communicate (see the [project page](https://github.com/nats-io)).

### LXD

Anbox Cloud includes LXD for hosting and managing the Ubuntu containers that run the nested Android containers.

LXD is installed through the [`ams-lxd` charm](https://charmhub.io/ams-lxd), which adds some Anbox-specific configuration to LXD. AMS configures LXD automatically and fully manages it, which means that in most scenarios, you do not need to worry about LXD at all.

If you want to check what LXD is doing, you can always run `lxc list` to display the existing containers. For the full deployment, LXD is used to host the AMS containers. If you run the Anbox Cloud Appliance, LXD is in addition used to containerise the Anbox Cloud deployment, which means that it hosts containers for the different Juju machines that Anbox Cloud requires:

```
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
|           NAME           |  STATE  |          IPV4          | IPV6 |   TYPE    | SNAPSHOTS | LOCATION |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| ams-cdr3292j841mb72gksog | RUNNING | 192.168.96.1 (eth0)    |      | CONTAINER | 0         | lxd0     |
|                          |         | 192.168.250.1 (anbox0) |      |           |           |          |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| juju-73e292-0            | RUNNING | 240.0.233.254 (eth0)   |      | CONTAINER | 0         | lxd0     |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| juju-73e292-1            | RUNNING | 240.0.98.38 (eth0)     |      | CONTAINER | 0         | lxd0     |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| juju-73e292-2            | RUNNING | 240.0.61.208 (eth0)    |      | CONTAINER | 0         | lxd0     |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| juju-34631c-0            | RUNNING | 240.0.180.30 (eth0)    |      | CONTAINER | 0         | lxd0     |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
```

<a name="lxd-storage"></a>
#### LXD storage

For LXD storage, Anbox Cloud uses a ZFS storage pool, which it creates automatically. This storage pool can be located on either a dedicated block storage device or a loop file. See [Data storage location](https://linuxcontainers.org/lxd/docs/latest/explanation/storage/#data-storage-location) in the LXD documentation for more information.

While a loop file is easy to set up, it is much slower than a block device. Therefore, we recommend using a block device that is dedicated to LXD storage only.

If you are doing a full deployment, configure the storage before starting the deployment. See the *Customise storage* section in [How to deploy Anbox Cloud with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744#customise-storage) or [How to deploy Anbox Cloud on bare metal](https://discourse.ubuntu.com/t/deploy-anbox-cloud-on-bare-metal/26378#customise-storage) for instructions. If you skip the configuration, Anbox Cloud sets up a loop-file with an automatically calculated size, which is not recommended.

If you are using the Anbox Cloud Appliance, you are prompted during the initialisation process to specify the storage location, and, if you choose a loop file, its size. When choosing a size, keep in mind that the loop file cannot be larger than the root disk, and that it will cause the disk to fill up as the loop file grows to its maximum size over time. The created storage pool is used to store all Anbox Cloud content, thus both the Juju containers and the AMS containers.

<a name="juju-bundles"></a>
## Juju bundles

The regular Anbox Cloud variant provides two different Juju bundles:

* The `anbox-cloud-core` bundle provides a minimised version of Anbox Cloud. This version is sufficient if you don't want to use the Anbox Cloud streaming stack.

  For more information, see the [charm page](https://charmhub.io/anbox-cloud-core).

* The `anbox-cloud` bundle provides the full version of Anbox Cloud, including its streaming stack.

  For more information, see the [charm page](https://charmhub.io/anbox-cloud).

[note type="information" status="Tip"]
For detailed information about the charm, check the `bundle.yaml` file in the bundle.

You can download the bundle with `juju download <charm_name>`, thus `juju download anbox-cloud-core` or `juju download anbox-cloud`. Unzip the bundle to access the `bundle.yaml` file.
[/note]

If you don't need to stream the visual output of the Android containers, you can use the `anbox-cloud-core` bundle. Otherwise, you should use the `anbox-cloud` bundle. However, even without the streaming stack, there are still ways to get visual access for inspection purposes. See [How to access a container](https://discourse.ubuntu.com/t/container-access/17772) for details.
