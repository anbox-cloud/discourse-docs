The Anbox Cloud Appliance provides a deployment of Anbox Cloud to a single machine. This offering is well suited for initial prototype and small scale deployments.

[note type="information" status="Note"]
There are differences between the Anbox Cloud Appliance and the full Anbox Cloud installation (see [Variants](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802#variants)). This tutorial focuses on installing the **Anbox Cloud Appliance** on a local machine. To install the appliance on a cloud platform, see [How to install the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702).

For instructions on how to install **Anbox Cloud**, see [How to install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336).
[/note]

This tutorial guides you through the steps that are required to install and initialise the Anbox Cloud Appliance on your local machine from the [snap](https://snapcraft.io/anbox-cloud-appliance):

1. [Check the prerequisites](#prerequisites)
2. [Install the appliance](#install)
3. [Initialise the appliance](#initialise)
4. [Register with the dashboard](#register)

<a name="prerequisites"></a>
## Check the prerequisites

Make sure you have the following prerequisites:

* An Ubuntu SSO account. If you don't have one yet, create it [here](https://login.ubuntu.com).
* A virtual or bare metal machine running Ubuntu 20.04 or 22.04. See the detailed requirements [here](https://discourse.ubuntu.com/t/requirements/17734).
* [note type="caution" status="Warning"]It is not recommended to run Anbox Cloud on an Ubuntu desktop appliance. Always use the [server](https://ubuntu.com/download/server) or the [cloud](https://ubuntu.com/download/cloud) variant.[/note]
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to https://ubuntu.com/pro to retrieve it.
  [note type="caution" status="Warning"]The *Ubuntu Pro (Infra-only)* token does **NOT** work and will result in a failed deployment. You need an *Ubuntu Pro* subscription.[/note]

<a name="install"></a>
## Install the appliance

The following instructions guide you through all relevant steps to install the Anbox Cloud Appliance from the [snap](https://snapcraft.io/anbox-cloud-appliance).

### 1. Update your system

Run the following commands to ensure that all installed packages on your system are up-to-date:

    sudo apt update
    sudo apt upgrade

### 2. Install dependencies

The Anbox Cloud Appliance requires LXD >= 5.0. Check which version you have currently installed:

    lxd --version

If LXD is not installed, run:

    snap install --channel=5.0/stable lxd

If LXD is already installed but the version is older than 5.0, run:

    snap refresh --channel=5.0/stable lxd

<a name="attach-ubuntu-pro"></a>
### 3. Attach your machine to the Ubuntu Pro subscription

The Anbox Cloud Appliance requires a valid Ubuntu Pro subscription.

Before installing the appliance, you must attach the machine on which you want to run the Anbox Cloud Appliance to your Ubuntu Pro subscription. To do so, run the following command, replacing *<UA_token>* with your Ubuntu Pro token:

    sudo ua attach <UA_token>

### 4. Install the snap

Run the following command to install the `anbox-cloud-appliance` snap, which handles the installation and deployment of the Anbox Cloud Appliance:

    sudo snap install --classic anbox-cloud-appliance

<a name="additional-tools"></a>
### 5. Install additional tools

The appliance requires a few additional tools. Run the following commands to install them:

    sudo snap install amc
    sudo snap install --classic --channel=2.9/stable juju

[note type="information" status="Note"]
See [Juju version](https://discourse.ubuntu.com/t/installation-requirements/17734#juju-version) for information about which Juju version is required for your version of Anbox Cloud.
[/note]

<a name="initialise"></a>
## Initialise the appliance

After the installation, access the appliance in your web browser by entering the IP of your machine (in the following steps referred to as `https://your-machine-address`). This web page provides status information for the following initialisation process.

[note type="information" status="Note"]By default, the Anbox Cloud Appliance uses self-signed certificates, which might cause a security warning in your browser. Use the mechanism provided by your browser to proceed to the web page.[/note]

![Appliance welcome screen|690x343, 100%](https://assets.ubuntu.com/v1/f35744dc-install_appliance_initialise.png)

See [How to finalise the installation](https://discourse.ubuntu.com/t/how-to-finalise-the-installation/29704) for detailed information about the initialisation process.

### 1. Start the initialisation process

On your machine, enter the following command to invoke the initialisation process of the Anbox Cloud Appliance:

    sudo anbox-cloud-appliance init

You will be asked a few questions. Accept the default answers for all of them.

### 2. Monitor the progress

When the command returns, the initialisation process will run fully automatically in the background. You can watch the status web page at `https://your-machine-address` for progress information.

![Anbox Cloud deployment|690x442](https://assets.ubuntu.com/v1/279e12e3-install_appliance_status.png)


<a name="register"></a>
## Register with the dashboard

Once the initialisation process has finished, you are presented with a welcome page on `https://your-machine-address` with instructions on how to register a user account with your installation. This registration is needed to access the [web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871).

![Instructions for registering Ubuntu SSO account|690x442](https://assets.ubuntu.com/v1/93b47634-install_appliance_register.png)

### 1. Register your Ubuntu SSO account

Enter the following command to register your Ubuntu SSO account:

    anbox-cloud-appliance dashboard register <your Ubuntu SSO email address>

To finish the account creation, open the link provided in the output in your web browser.

### 2. Log into the appliance dashboard

After registering, you can log into the appliance dashboard at `https://your-machine-address` with your Ubuntu SSO account.

## Done!

Your Anbox Cloud Appliance is now fully set up and ready to be used! Next, you should check out the [Get started with Anbox Cloud (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958) or the [Get started with Anbox Cloud (CLI)](https://discourse.ubuntu.com/t/getting-started/17756) tutorial to familiarise yourself with how to use Anbox Cloud.

You can find more information about how to use the appliance in the documentation. The appliance installation is nearly identical to installing via Juju, so all the commands and examples not relating directly to Juju will apply.

If you want to increase the capacity of your Anbox Cloud Appliance deployment, you can add more machines to it. See [How to join a machine to the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-join-a-machine-to-the-anbox-cloud-appliance/29054) for instructions.
