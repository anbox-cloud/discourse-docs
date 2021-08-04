The Anbox Cloud Appliance offers a single machine based deployment of Anbox Cloud
which is well suited for initial prototype and small scale deployments.

## What you will need

* A virtual or bare metal machine on [AWS](https://aws.amazon.com/) or [Oracle Cloud (OCI)](https://www.oracle.com/cloud/) running Ubuntu 20.04. Please have a look at the detailed requirements  [here](https://discourse.ubuntu.com/t/requirements/17734)
* Your *Ubuntu Advantage for **Applications*** token. If you don't have yours yet, get it from https://ubuntu.com/advantage or speak to your Canonical representative

> **WARNING:** The *Ubuntu Advantage for **Infrastructure*** token every user gets for free for personal use does **NOT** work and will result in a failed deployment!

> **NOTE:** The Anbox Cloud Appliance will receive official support for other clouds, namely Azure and Google Cloud soon.

### Install Appliance

As the first step we have to install the `anbox-cloud-appliance` snap which will handle the installation and deployment of Anbox Cloud:

    $ sudo snap install --classic anbox-cloud-appliance

After the installation you will find a status web page at https://your-machine-address which provides status information for the following initialization process.

![appliance-welcome|690x343, 100%](upload://yIGZThPljsjPyRAVQVFkZOiVVNF.png)

Now that the snap is installed we can invoke the initialization process of the Anbox Cloud Appliance. You will be asked a few questions but if you don't want to make any specific changes it's safe to stay with the offered default answers.

```bash
$ sudo anbox-cloud-appliance init
Welcome to the Anbox Cloud Appliance!

The following questions will guide you through the initial setup of the
appliance. If you don't care about answering any of them you can just
accept the defaults.

For any further questions please have a look a the official Anbox Cloud
documentation at https://anbox-cloud.io/docs

Both the containers used to deploy the control plane services of the
Anbox Cloud Appliance and the ones used for the actual Android instances
require storage. Choosing an appropiate storage device and size will
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

If you don't specifiy a block device or a custom size, the appliance
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

After the command has returned the initialization process will run fully automatic in the background and you can watch the status web page at https://your-machine-address for progress information.

![appliance-deployment|690x442](upload://5Eti9Lj0Q4VpYmpEvVMzK4fjkxH.png)

Alternatively the following command provides progress information on the command line:

```bash
$ anbox-cloud-appliance status
status: initializing
progress: 60
update-available: false
reboot-needed: false
```

Once the initialization process has finished you will be presented with a welcome page on https://your-machine-address with instructions on how to register a user account with your installation. You will need an Ubuntu SSO account in order to log into the dashboard, so if you haven't created one yet, you can do so [here](https://login.ubuntu.com)

![appliance-dashboard|690x442](upload://l4EPbQr1NcsD78r3K03F3ISjiL2.png)

Your Ubuntu SSO account can now be registered by running the following command via SSH on the machine hosting the appliance:

```bash
$ anbox-cloud-appliance dashboard register <your Ubuntu SSO email address>
Visit https://ec2-18-185-179-72.eu-central-1.compute.amazonaws.com/register?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNpbW9uLmZlbHNAY2Fub25pY2FsLmNvbSIsImV4cCI6MTYyMzMxNzU0N30.0YVd8paPyU6b_5evf76t0Kf_1w20mHecNiI26jTWg1s to finish your registration
```

The output provides  a link you need to open in your web browser to finish the account creation. By default the registration link expires after one hour.  You can now log into the appliance dashboard with your Ubuntu SSO account.

## Done!

Your Anbox Cloud Appliance is now fully setup and ready to be used! You can read more about your next steps [here](https://discourse.ubuntu.com/t/getting-started/17756)

You will find more information about how to use the appliance in the documentation. In general the Anbox Cloud Appliance is deploying the same Anbox Cloud as you can deploy manually via Juju but takes away all the burden to deal with the deployment itself. With that all not Juju related commands and examples given in the documentation apply to the appliance the same way as for a regular deployment.
