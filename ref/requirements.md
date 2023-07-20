To run Anbox Cloud, you must fulfil a few minimum requirements, which differ depending on the kind of deployment you choose.

The [General requirements](#general) apply to all kinds of deployments. In addition, check the [requirements for the Anbox Cloud Appliance](#appliance) if you run the appliance or the [requirements for Juju-based deployments](#juju-based) if you run Anbox Cloud. See [Variants](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802#variants) for an explanation of the differences between both variants.

<a name="general"></a>
## General requirements

The following requirements apply to all variants of Anbox Cloud.

### Ubuntu Pro token

After registering to Anbox Cloud, you should have received an [Ubuntu Pro](https://ubuntu.com/pro) token. If you haven't received one, please contact [support](https://support.canonical.com/) or your Canonical account representative as you'll need it to deploy Anbox Cloud.

### Ubuntu OS

Anbox Cloud is supported only on the [Ubuntu](https://ubuntu.com/) operating system. Other Linux-based operating systems are not supported. You must run either the [server](https://ubuntu.com/download/server) or the [cloud](https://ubuntu.com/download/cloud) variant of Ubuntu. Running Anbox Cloud on an Ubuntu Desktop installation is not supported.

See [Ubuntu version for the Anbox Cloud Appliance](#appliance-ubuntu-version) or [Ubuntu version for Juju-based deployments](#ac-ubuntu-version) for information about the supported Ubuntu versions.

<a name="appliance"></a>
## Anbox Cloud Appliance

The Anbox Cloud Appliance has the following minimum hardware requirements:

* 64 bit x86 or Arm CPU with >= 4 CPU cores
* 8 GB of memory
* 40 GB of disk space for the OS
* optional, but strongly recommended: >= 50GB block volume to host container storage

The above defines a minimum of what is necessary to run the Anbox Cloud Appliance. As Anbox Cloud is dependent on available resources to launch its Android containers, the available resources dictate the maximum number of possible containers. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for an explanation on how to plan for a specific capacity on your appliance.

On public clouds it's recommended to always allocate an additional storage volume for the container storage. If no additional storage volume is available, the appliance will create an on-disk image it will use for the container storage. This is sufficient for very simple cases but does not provide optimal performance and will slow down operations and container startup time.

For external access to the Anbox Cloud Appliance, you must expose a couple of network ports on the machine where the appliance is running. See [Network ports](https://discourse.ubuntu.com/t/network-ports/33650#appliance) for the list of ports that must be exposed. How to allow incoming traffic on the listed ports differs depending on the cloud used. See the documentation of the cloud for further information on how to change the firewall.

<a name="appliance-ubuntu-version"></a>
### Ubuntu version

The Anbox Cloud Appliance supports the following Ubuntu versions:

* 20.04 (focal)
* 22.04 (jammy)

<a name="appliance-lxd-version"></a>
### LXD version

The Anbox Cloud Appliance currently supports the following LXD versions:

* &gt;= 5.0

<a name="juju-based"></a>
## Juju-based deployments

Anbox Cloud deployments are managed by Juju. They can be created on all the [supported clouds](https://juju.is/docs/clouds) as well as manually provided machines as long as they follow the required minimums.

<a name="ac-ubuntu-version"></a>
### Ubuntu version

Anbox Cloud supports the following Ubuntu versions:

* 20.04 (focal)
* 22.04 (jammy)

For new deployments, Ubuntu 22.04 (jammy) is preferred.

[note type="information" status="Note"]
The HAProxy load balancer currently has no support for Ubuntu 22.04. Therefore, the Juju bundle uses Ubuntu 20.04 for the machine that runs the load balancer.
[/note]

<a name="juju-lxd-version"></a>
### LXD version

Anbox Cloud currently supports the following LXD versions:

* &gt;= 4.0

<a name="juju-version"></a>
### Juju version

Anbox Cloud requires [Juju](https://juju.is/) to be installed to manage the different components and their dependencies. Starting with Anbox Cloud 1.13, the required Juju version is **2.9**. Earlier versions require Juju **2.8**.

You can install Juju 2.9 with the following command:

    snap install --classic --channel=2.9/stable juju

To switch to the 2.9 series, use the following command:

    snap refresh --channel=2.9/stable juju

See the [Juju documentation](https://juju.is/docs/installing) for more information.

<a name="minimum-hardware"></a>
### Minimum hardware

While you can run Anbox Cloud on a single machine, we strongly recommend using several machines for a production environment.

To run a full Anbox Cloud deployment including the streaming stack, we recommend the following setup:

ID | Architecture   | CPU cores | RAM  | Disk       | GPUs |  FUNCTION |
---|----------------|-----------|------|------------|------|------------|
-  | amd64 or arm64 | 4         | 4GB  | 50GB SSD   | no   |  Hosts the  [Juju controller](https://discourse.juju.is/t/controllers/1111)  |
0  | amd64 or arm64 | 2         | 2GB  | 100GB SSD  | no   |  Hosts the load balancer |
1  | amd64 or arm64 | 4         | 8GB  | 100GB SSD  | no   |  Hosts the streaming stack control plane |
2  | amd64 or arm64 | 4         | 8GB  | 100GB SSD  | no   |  Hosts the management layer of Anbox Cloud (for example, AMS) |
3  | amd64 or arm64 | 8         | 16GB | 200GB NVMe | optional   |  LXD worker node that hosts the actual Anbox containers  |

To run the core version of Anbox Cloud without the streaming stack, we recommend the following setup:

ID | Architecture   | CPU cores | RAM  | Disk       | GPUs |  FUNCTION |
---|----------------|-----------|------|------------|------|------------|
-  | amd64 or arm64 | 4         | 4GB  | 50GB SSD   | no   |  Hosts the  [Juju controller](https://discourse.juju.is/t/controllers/1111)  |
0  | amd64 or arm64 | 4         | 8GB  | 100GB SSD  | no   |  Hosts the management layer of Anbox Cloud (for example, AMS)  |
1  | amd64 or arm64 | 8         | 16GB | 200GB NVMe | optional   |  LXD worker node that hosts the actual Anbox containers  |

Some additional information:

- The ID in the table corresponds to the ID that the Juju bundle uses.
- You can mix architectures for the different machines. However, if you have several LXD nodes, all of them must have the same architecture.
- The specified number of cores and RAM is only the minimum required to run Anbox Cloud at a sensible performance.

  More CPU cores and more RAM on the machine hosting LXD will allow to run a higher number of containers. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for an introduction of how many resources are necessary to host a specific number of containers.
- If you require GPU support, see [Supported rendering resources](tbd) for a list of supported GPUs.

Applications not maintained by Anbox Cloud may have different hardware recommendations:
 - **etcd**: [Hardware recommendations](https://etcd.io/docs/v3.5/op-guide/hardware/)
 - **HAProxy** (load balancer for the Stream Gateway and the dashboard): [Installation](https://www.haproxy.com/documentation/hapee/latest/getting-started/hardware/)

Please note that these are just baselines and should be adapted to your workload. No matter the application, [monitoring and tuning the performance](https://discourse.ubuntu.com/t/about-performance/29416) is always important.
