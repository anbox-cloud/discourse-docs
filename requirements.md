To run Anbox Cloud, you must fulfil a few minimum requirements, which differ depending on the kind of deployment you choose.

The [General requirements](#general) apply to all kinds of deployments. In addition, check the [requirements for the Anbox Cloud Appliance](#appliance) if you run the appliance or the [requirements for Juju-based deployments](#juju-based) if you run Anbox Cloud. See [Variants](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802#variants) for an explanation of the differences between both variants.

<a name="general"></a>
## General requirements

The following requirements apply to all variants of Anbox Cloud.

### Ubuntu Advantage token

After registering to Anbox Cloud, you should have received an [Ubuntu Advantage for Applications](https://ubuntu.com/advantage) token. If you haven't received one, please contact [support](https://support.canonical.com/) or your Canonical account representative as you'll need it to deploy Anbox Cloud.

[note type="information" status="Note"]When [installing the Anbox Cloud Appliance from the AWS Marketplace](https://discourse.ubuntu.com/t/how-to-install-the-appliance-on-aws/29703), the Ubuntu Advantage token is included in the Anbox Cloud Appliance subscription and is used under the hood during the deployment. Therefore, you will not receive it separately.[/note]

### Ubuntu OS

Anbox Cloud is supported only on the [Ubuntu](https://ubuntu.com/) operating system. Other Linux-based operating systems are not supported.

You must run either the [server](https://ubuntu.com/download/server) or the [cloud](https://ubuntu.com/download/cloud) variant of Ubuntu. Running Anbox Cloud on a Ubuntu Desktop installation is not supported.

Supported Ubuntu versions:

* 18.04 (bionic) - see [Linux kernel](#linux-kernel) below for limitations
* 20.04 (focal)

For new deployments, Ubuntu 20.04 (focal) is preferred.

<a name="linux-kernel"></a>
### Linux kernel

Anbox Cloud is only supported on the Ubuntu variant of the Linux kernel starting with version 5.4. The GA kernel for Ubuntu 18.04 (based on 4.15) is not supported.

AppArmor support must be enabled in the kernel as it's mandatory for the Anbox containers to run.

The following table gives an overview of the available kernel versions for the different supported clouds:

|CLOUD|KERNEL VERSION|UBUNTU PACKAGES||
| --- | --- | --- | --- |
|AWS|>= 5.4|`linux-aws`, `linux-modules-extra-aws`||
|GCE|>= 5.4|`linux-gcp`, `linux-modules-extra-gcp`||
|Azure|>= 5.4|`linux-azure`, `linux-modules-extra-azure`||
|OCI|>= 5.4|`linux-oracle`, `linux-modules-extra-oracle`||
|Private|>= 5.4|`linux-generic`||

<a name="appliance"></a>
## Anbox Cloud Appliance

The Anbox Cloud Appliance has the following minimum hardware requirements:

* 64 bit x86 or Arm CPU with >= 4 CPU cores
* 8 GB of memory
* 40 GB of disk space for the OS
* optional, but strongly recommended: >= 50GB block volume to host container storage

The above defines a minimum of what is necessary to run the Anbox Cloud Appliance. As Anbox Cloud is dependent on available resources to launch its Android containers, the available resources dictate the maximum number of possible containers. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for an explanation on how to plan for a specific capacity on your appliance.

On public clouds it's recommended to always allocate an additional storage volume for the container storage. If no additional storage volume is available, the appliance will create an on-disk image it will use for the container storage. This is sufficient for very simple cases but does not provide optimal performance and will slow down operations and container startup time.

For external access to the Anbox Cloud Appliance, a couple of network ports must be exposed on the machine it's running on. The following table lists all ports.

| Port(s) | Protocol | Necessity | Description |
|------------|--------------|----------------|-------------------|
| 80 | TCP | mandatory  | HTTP (redirects to HTTPS on port 443)|
| 443 | TCP | mandatory | HTTPS |
| 5349 | UDP | mandatory | STUN/TURN
| 60000-60100 | UDP | mandatory | TURN relay ports |
| 10000-11000 | UDP | optional | Service endpoints exposed by AMS |
| 10000-11000 | TCP | optional | Service endpoints exposed by AMS |

How to allow incoming traffic on the listed ports is different depending on the cloud used. Please consult the documentation of the cloud for further information on how to change the firewall.

<a name="juju-based"></a>
## Juju-based deployments

Anbox Cloud deployments are managed by Juju. They can be created on all the [supported clouds](https://juju.is/docs/clouds) as well as manually provided machines as long as they follow the required minimums.

<a name="juju-version"></a>
### Juju version

Anbox Cloud requires [Juju](https://juju.is/) to be installed to manage the different components and their dependencies. Starting with Anbox Cloud 1.13, the required Juju version is **2.9**.

[note type="information" status="Note"]If you are using Anbox Cloud 1.11 or earlier, the required Juju version is **2.8**.[/note]

You can install Juju 2.9 with the following command:

    snap install --classic --channel=2.9/stable juju

To switch to the 2.9 series, use the following command:

    snap refresh --channel=2.9/stable juju

See the [Juju documentation](https://juju.is/docs/installing) for more information.

<a name="minimum-hardware"></a>
### Minimum hardware

While you can run Anbox Cloud on a single machine, we strongly recommend the following setup for a production environment:

ID | Architecture   | CPU cores | RAM  | Disk       | GPUs |  FUNCTION |
---|----------------|-----------|------|------------|------|------------|
0  | amd64          | 4         | 4GB  | 50GB SSD   | no   |  Hosts the  [Juju controller](https://discourse.juju.is/t/controllers/1111)  |
1  | amd64          | 4         | 8GB  | 100GB SSD  | no   |  Host the management layer of Anbox Cloud  |
2  | amd64 or arm64 | 8         | 16GB | 200GB NVMe | optional   |  LXD worker node. Hosts the actual Anbox containers  |

The specified number of cores and RAM is only the minimum required to run Anbox Cloud at a sensible performance.

More CPU cores and more RAM on the machine hosting LXD will allow to run a higher number of containers. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for an introduction of how many resources are necessary to host a specific number of containers.

If you require GPU support, see [About GPU support](https://discourse.ubuntu.com/t/gpu-support/17768) for a list of supported GPUs.

Applications not maintained by Anbox Cloud may have different hardware recommendations:
 - **etcd**: [Hardware recommendations](https://etcd.io/docs/v3.5/op-guide/hardware/)
 - **HAProxy** (load balancer for the Stream Gateway and the dashboard): [Installation](https://www.haproxy.com/documentation/hapee/latest/installation/getting-started/os-hardware/#hardware-requirements)

Please note that these are just baselines and should be adapted to your workload. No matter the application, [monitoring and tuning the performance](https://discourse.ubuntu.com/t/about-performance/29416) is always important.
