The Anbox Cloud Appliance is not yet available from the Azure Marketplace. However, you can install the Anbox Cloud Appliance snap on an Azure machine.

The following instructions guide you through all relevant steps to deploy the Anbox Cloud Appliance on Azure. For additional information, see the [Microsoft documentation](https://docs.microsoft.com/en-gb/azure/virtual-machines/) about creating virtual machines in Azure.

The entire deployment process will take 20-30 minutes, depending on the selected hardware and the network conditions.

## Check the prerequisites

Check the hardware requirements for the Anbox Cloud Appliance [here](https://discourse.ubuntu.com/t/requirements/17734#appliance).

In addition, make sure you have the following prerequisites:

* An Ubuntu SSO account. If you don't have one yet, create it [here](https://login.ubuntu.com).
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to https://ubuntu.com/pro to retrieve it.
  [note type="caution" status="Warning"]The *Ubuntu Pro (Infra-only)* token does **NOT** work and will result in a failed deployment. You need an *Ubuntu Pro* subscription.[/note]
* An Azure account that you use to create the virtual machine.

## Create a virtual machine

Complete the following steps to create a virtual machine on which you can install the Anbox Cloud Appliance.

### 1. Deploy a Linux virtual machine

Log on to the [Microsoft Azure Portal](https://portal.azure.com/) and select the **Quickstart Center** service.

![Quickstart Center](https://assets.ubuntu.com/v1/0ca30941-azure_quickstart-co.png)

In the Quickstart Center, select **Deploy a virtual machine**. On the resulting screen, select **Create a Linux virtual machine**.

![Deploy a virtual machine](https://assets.ubuntu.com/v1/d0ac4cf5-azure_deploy-vm-co.png)

### 2. Configure basic settings

On the **Basics** tab of the virtual machine configuration, specify the required information. Several of the options are specific to how and where you want to deploy your virtual machine. In most cases you can keep the default values, but make sure to set the following configurations:

* Select the latest Ubuntu image (Ubuntu Server 22.04 LTS) for the architecture that you want to use. The following instructions and screenshots use the Arm64 architecture.
* Select a size that matches the [hardware requirements](https://discourse.ubuntu.com/t/requirements/17734#appliance). For example, select `Standard_D16ps_v5`, which has 16 vCPUs and 64 GB of RAM.
* Change the user name of the administrator account to `ubuntu`.
* Accept the defaults for the inbound port rules for now; these rules will be configured later in the setup process.

![Basics tab](https://assets.ubuntu.com/v1/9c8844a2-azure_config-basics-co.png)

Click **Next: Disks** to continue to the next tab.

### 3. Configure disks

Azure separates the main disk for the operating system and any data disks. On the **Disks** tab of the virtual machine configuration, you can configure the OS disk and attach data disks.

For the Anbox Cloud Appliance, you should attach a separate data disk of at least 50 GB. To do so, click **Create and attach a new disk**. You can accept the default settings and change the disk size according to your requirements. For performance reasons, we recommend using 100 GB or more.

![Create and attach a new disk](https://assets.ubuntu.com/v1/8fea8b11-azure_config-disk.png)

Click **Next: Networking** to continue to the next tab.

### 4. Configure networking

For networking, the Anbox Cloud Appliance requires the following change to the default settings:

1. For the **NIC network security group**, select **Advanced** and create a network security group.
1. Add an inbound security rule that allows access to the following destination port ranges: `80,443,8444,5349,10000-11000,60000-60100`
1. Change the name of the rule and, if relevant for your setup, adapt the priority of the rule.

![Network security group configuration](https://assets.ubuntu.com/v1/a7be81a2-azure_config-secgroup-co.png)

### 5. Finalise the configuration

Check the configuration settings on the remaining tabs and make sure they are suitable for your deployment. The Anbox Cloud Appliance does not require any changes to the default configuration for these areas.

### 6. Review and create

On the **Review + create** tab, check the final configuration. If everything looks good, click **Create** to launch the virtual machine.

![Review + create](https://assets.ubuntu.com/v1/c6ff12de-azure_config-review.png)

Azure will prompt you to download your private key before it starts creating the virtual machine. Make sure to save the private key in a secure location and with secure permissions (0600).

![Deployment](https://assets.ubuntu.com/v1/fafd883f-azure_progress.png)

When deployment is complete, you can log on to the machine and install the Anbox Cloud Appliance.

## Log on to the machine

To install the Anbox Cloud Appliance, you must log on to the virtual machine that you just created.

To do so, go to the resource page of your virtual machine and find its public IP address. Then use SSH to log on to the machine, using the user name `ubuntu` and the private key file that you downloaded during the creation of the virtual machine. For example:

    ssh -i Downloads/anbox-cloud-appliance_key.pem ubuntu@192.0.2.15

## Install the appliance

After logging on to the virtual machine, follow the [Install the Anbox Cloud Appliance on your local machine](https://discourse.ubuntu.com/t/install-appliance/22681) tutorial to install and initialise the Anbox Cloud Appliance and to register with the dashboard.
