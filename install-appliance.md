The Anbox Cloud Appliance provides a deployment of Anbox Cloud to a single machine.
This offering is well suited for initial prototype and small scale deployments.

## What you need

* A virtual or bare metal machine on [AWS](https://aws.amazon.com/) or [Oracle Cloud (OCI)](https://www.oracle.com/cloud/) running Ubuntu 20.04. See the detailed requirements [here](https://discourse.ubuntu.com/t/requirements/17734).
* An Ubuntu SSO account. If you don't have one yet, create it [here](https://login.ubuntu.com).
* Your *Ubuntu Advantage for **Applications*** token. If you don't have yours yet, get it from https://ubuntu.com/advantage or speak to your Canonical representative.

> **WARNING:** The *Ubuntu Advantage for **Infrastructure*** token that every user gets for free for personal use does **NOT** work and will result in a failed deployment.

> **NOTE:** The Anbox Cloud Appliance will receive official support for other clouds, namely Azure and Google Cloud, soon.

### Install appliance

First, we must install the `anbox-cloud-appliance` snap, which handles the installation and deployment of Anbox Cloud:

    sudo snap install --classic anbox-cloud-appliance

After the installation, access `https://your-machine-address`. This web page provides status information for the following initialisation process.

![appliance-welcome|690x343, 100%](upload://yIGZThPljsjPyRAVQVFkZOiVVNF.png)

### Install additional tools

The appliance requires a few additional tools.

- Enter the following command to install Juju:

      sudo snap install --channel=2.8/stable juju
    
  Anbox Cloud currently requires Juju 2.8 (see [Juju version](https://anbox-cloud.io/docs/installation/upgrading-from-previous-versions#juju-version) for more information).
  
- Enter the following command to install amc:

      sudo snap install amc

### Initialise the appliance

Now that the snap is installed, we can invoke the initialisation process of the Anbox Cloud Appliance:

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

Once the initialisation process has finished, you are presented with a welcome page on `https://your-machine-address` with instructions on how to register a user account with your installation. 

![appliance-dashboard|690x442](upload://l4EPbQr1NcsD78r3K03F3ISjiL2.png)

Register your Ubuntu SSO account by running the following command via SSH on the machine that hosts the appliance:

    anbox-cloud-appliance dashboard register <your Ubuntu SSO email address>

The output provides a link that you must open in your web browser to finish the account creation. By default, the registration link expires after one hour. After registering, you can log into the appliance dashboard with your Ubuntu SSO account.

## Done!

Your Anbox Cloud Appliance is now fully set up and ready to be used! You can read more about your next steps [here](https://discourse.ubuntu.com/t/getting-started/17756).

You can find more information about how to use the appliance in the documentation. The appliance installation is nearly identical to installing via Juju, so all the commands and examples not relating directly to Juju will apply.
