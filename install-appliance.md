The Anbox Cloud Appliance provides a deployment of Anbox Cloud to a single machine.
This offering is well suited for initial prototype and small scale deployments.

## What you need

* An Ubuntu SSO account. If you don't have one yet, create it [here](https://login.ubuntu.com).
* When installing from [AWS Marketplace](https://aws.amazon.com/marketplace/):

  * An AWS account that you use to buy a subscription to the Anbox Cloud Appliance.
  
* When installing the [snap](https://snapcraft.io/):

  * A virtual or bare metal machine running Ubuntu 20.04. See the detailed requirements [here](https://discourse.ubuntu.com/t/requirements/17734).
  
    > **NOTE:** The Anbox Cloud Appliance is currently supported on [AWS](https://aws.amazon.com/) and [Oracle Cloud (OCI)](https://www.oracle.com/cloud/). Official support for other clouds, namely Azure and Google Cloud, will be added soon.
  
  * Your *Ubuntu Advantage for **Applications*** token. If you don't have yours yet, get it from https://ubuntu.com/advantage or [speak to your Canonical representative](https://anbox-cloud.io/contact-us).

    > **WARNING:** The *Ubuntu Advantage for **Infrastructure*** token that every user gets for free for personal use does **NOT** work and will result in a failed deployment.

## Install the appliance

The Anbox Cloud Appliance is available through the AWS Marketplace and as a snap.

* When installing on AWS, follow the steps in [Install from AWS Marketplace](#install-aws).
* When installing on a local machine or in another cloud, follow the steps in [Install the snap](#install-snap)

<a name="install-aws"></a>
### Install from AWS Marketplace

Installing the Anbox Cloud Appliance through the AWS Marketplace simplifies the installation and deployment process and allows billing to be handled directly through AWS. The following steps guide you through all relevant steps to deploy the Anbox Cloud Appliance in your AWS account.

#### Choose an instance architecture

First, decide if you want to deploy the Anbox Cloud Appliance on an x86 or Arm instance architecture. AWS supports both.

The decision should factor in the following aspects:

* GPUs are currently available for x86. NVIDIA GPUs will only become available for Arm instances [later in 2021](https://aws.amazon.com/blogs/machine-learning/aws-and-nvidia-to-bring-arm-based-instances-with-gpus-to-the-cloud/).
* Not all Android applications support the x86 ABI. Therefore, some applications can run only on Arm.

Once you have decided for an instance architecture, go to the corresponding marketplace page:

* [Anbox Cloud Appliance for x86](https://aws.amazon.com/marketplace/pp/prodview-3lx6xyaapstz4)
* [Anbox Cloud Appliance for Arm](https://aws.amazon.com/marketplace/pp/prodview-aqmdt52vqs5qk)

After subscribing to the marketplace product, create an instance using the AMI and the [AWS EC2 wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html).

#### Choose an instance type

AWS offers various instance types. The Anbox Cloud Appliance images are only listed for a subset of the available instance types.

Select the instance type that is most suitable for what you're planning to do. For example, if you just want to try out the Anbox Cloud Appliance, an instance type with GPU support and limited CPU and memory is sufficient.

![00_appiance-aws-instance-type|690x532](upload://AskBufPuBZg586bSaI6Eg39XGqy.png) 

In this example, we picked *g4dn.xlarge*, which provides 4 vCPUs, 16 GB of memory and a single NVIDIA Tesla T4 GPU.

#### Configure the instance details

You do not need to customise any of the settings in the instance details, but you can fine-tune things. For example, you might want to put the instance onto a different VPC or subnet.

![01_appliance_configure_instance|690x533](upload://pnZxItbD6stRmcpunjQxCOjqwfn.png) 

#### Add storage

The Anbox Cloud instance requires sufficient storage to work correctly. The root disk should have at minimum 50 GB and for best performance, you should create an additional EBS volume of at least 50 GB. Anbox Cloud uses the additional volume exclusively to store all of its containers. Using a separate volume isolates them from the operating system, which increases performance. If no additional EBS volume is added, the Anbox Cloud Appliance automatically creates an image on the root disk, which is used to store the containers. However, this is not recommended.

![02_appliance_disk|690x533](upload://ztC8wxUxM4FFJXmXxz2ZKApNq5j.png) 

In this example, we use three storage volumes:

* `/dev/sda1` as root disk with a size of 50 GB.
* An ephemeral `/dev/nvme0n1` disk (part of the g4dn instance), which is ignored by the Anbox Cloud Appliance.
* `/dev/sdb` as EBS volume with a size of 100 GB.

If you don't have any specific requirements, we recommend choosing the same configuration.

#### Configure the security group

To allow external access, you must open several ports in the security group attached to the AWS instance. The AMI already comes with the required configuration, so you don't need to do any changes. For reference, all required ports are documented [here](https://discourse.ubuntu.com/t/requirements/17734).

![03_appliance_security_types|690x534](upload://9KG97kpHpVdvvMDIp7qdQFnO6zT.png) 

#### Review and launch

You should now review the instance configuration. If everything is correct, launch the instance.

When the instance is successfully launched, you can find its public IP address in the instance details page. Use this IP address or the corresponding DNS name to access the status web page (in the following steps referred to as `https://your-machine-address`).

Next, continue with the instructions in [Initialise the appliance](#initialise).

<a name="install-snap"></a>
### Install the snap

The Anbox Cloud Appliance requires a valid Ubuntu Advantage for Applications subscription. 

Before installing the appliance, you must attach the machine on which you're running the Anbox Cloud Appliance to your Ubuntu Advantage for Applications subscription. To do so, run the following command, replacing *<UA_token>* with your Ubuntu Advantage for Applications token:

    sudo ua attach <UA_token>

Then install the `anbox-cloud-appliance` snap, which handles the installation and deployment of Anbox Cloud:

    sudo snap install --classic anbox-cloud-appliance

#### Install additional tools

The appliance requires a few additional tools.

- Enter the following command to install Juju:

      sudo snap install --channel=2.8/stable juju
    
  Anbox Cloud currently requires Juju 2.8 (see [Juju version](https://anbox-cloud.io/docs/installation/upgrading-from-previous-versions#juju-version) for more information).
  
- Enter the following command to install amc:

      sudo snap install amc

<a name="initialise"></a>
## Initialise the appliance

After the installation, access `https://your-machine-address`. This web page provides status information for the following initialisation process.

![appliance-welcome|690x343, 100%](upload://yIGZThPljsjPyRAVQVFkZOiVVNF.png)

Invoke the initialisation process of the Anbox Cloud Appliance via SSH on the machine that hosts the appliance:

    sudo anbox-cloud-appliance init

You will be asked a few questions. If you don't want to make any specific changes, you can safely stay with the offered default answers.

```bash
Welcome to the Anbox Cloud Appliance!

The following questions will guide you through the initial setup of the
appliance. If you don't care about answering any of them you can just
accept the defaults.

For any further questions please have a look a the official Anbox Cloud
documentation at https://anbox-cloud.io/docs

Both the containers used to deploy the control plane services of the
Anbox Cloud Appliance and the ones used for the actual Android instances
require storage. Choosing an appropriate storage device and size will
affect both performance and density. By default each Android instance
will occupy 3GB of disk storage. Depending on the number of containers
you intend to run you should calculate:

storage size = 15 GB (for the OS) + 3GB * number of Android instances

Anbox Cloud uses ZFS under the hood for the LXD storage pool which
implements deduplication, so the actual space occupied later will be
less but may grow up to the maximum in some cases.

If you don't choose to use a dedicated block storage device the
appliance will allocate an on-disk image on the root disk of the
instance it's running on. You can influence the size of the image
by specifying a custom size.

If you don't specify a block device or a custom size, the appliance
will decide automatically on the location and best size for the LXD
storage pool.

Do you want to use a dedicated block storage device? [default=yes]
What is the path to the block storage device?  [default=/dev/nvme1n1]

Is the appliance deployed behind a NAT and should be available on a public address? [default=yes]
Do you have a DNS name you want to use instead of the IP address? [default=yes]
Which DNS name you want to use (e.g. anbox-cloud.io)?  [default=ec2-18-185-179-72.eu-central-1.compute.amazonaws.com]

Configuration completed. Do you want to initiate the bootstrap process now? [default=yes]

Everything configured, starting the bootstrap process now. You can
watch https://ec2-18-185-179-72.eu-central-1.compute.amazonaws.com for progress updates
```

After the command has returned, the initialisation process will run fully automatically in the background. You can watch the status web page at `https://your-machine-address` for progress information.

![appliance-deployment|690x442](upload://5Eti9Lj0Q4VpYmpEvVMzK4fjkxH.png)

Alternatively, use the `anbox-cloud-appliance status` command to monitor the progress information on the command line.

```bash
status: initializing
progress: 60
update-available: false
reboot-needed: false
```

## Register your user account

Once the initialisation process has finished, you are presented with a welcome page on `https://your-machine-address` with instructions on how to register a user account with your installation. 

![appliance-dashboard|690x442](upload://l4EPbQr1NcsD78r3K03F3ISjiL2.png)

Register your Ubuntu SSO account by running the following command via SSH on the machine that hosts the appliance:

    anbox-cloud-appliance dashboard register <your Ubuntu SSO email address>

The output provides a link that you must open in your web browser to finish the account creation. By default, the registration link expires after one hour. After registering, you can log into the appliance dashboard with your Ubuntu SSO account.

## Done!

Your Anbox Cloud Appliance is now fully set up and ready to be used! You can read more about your next steps [here](https://discourse.ubuntu.com/t/getting-started/17756).

You can find more information about how to use the appliance in the documentation. The appliance installation is nearly identical to installing via Juju, so all the commands and examples not relating directly to Juju will apply.
