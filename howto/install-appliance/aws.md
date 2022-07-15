You can install the Anbox Cloud Appliance on AWS in one of two ways:

- Install through the AWS Marketplace. This is the recommended way, because this method simplifies the installation and deployment process and allows billing to be handled directly through AWS.
- Install the Anbox Cloud Appliance snap on an AWS machine. This method is not recommended, but if you want to do it anyway, see the [Install the Anbox Cloud Appliance on your local machine](https://discourse.ubuntu.com/t/install-appliance/22681) tutorial for instructions on how to install the snap.

The following instructions guide you through all relevant steps to deploy the Anbox Cloud Appliance from the AWS Marketplace. For additional information, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html) about launching an instance.

The entire deployment process will take 10-15 minutes, depending on the selected hardware and the network conditions.

## Before you start

Deploying the Anbox Cloud Appliance requires some familiarity with AWS. In particular, you should be familiar with:

- Amazon Elastic Compute Cloud (Amazon EC2), for basic EC2 configuration
- Amazon Elastic Block Storage (Amazon EBS), for configuring the EC2 instance storage
- Amazon Virtual Private Cloud (Amazon VPC), for configuring an internet facing subnet and a security group

The appliance uses the following billable services by AWS:

- EC2 and Marketplace appliance (see the AWS Marketplace product page for costs)
- Network egress (for example, see the [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/) page for costs)

### Choose an architecture

AWS supports running the Anbox Cloud Appliance both on [AWS Graviton](https://aws.amazon.com/ec2/graviton/) Arm-based instances and on x86 instances. Before installing the appliance, decide which architecture you want to use. The appliance supports the same set of features on both architectures, but you should factor in the following aspects:

* AWS Graviton (Arm) and x86 offer equal performance for Android applications.
* GPUs are available for both x86 and AWS Graviton (Arm).
  [note type="information" status="Note"]To use GPUs with AWS Graviton (Arm), you must select a [G5g instance](https://aws.amazon.com/de/ec2/instance-types/g5g/). This instance type might not be available in all regions.[/note]
* Not all Android applications support the x86 ABI. Therefore, some applications can run only on Arm.

For detailed information about the offering, see the following pages on the AWS Marketplace:

* [Anbox Cloud Appliance for AWS Graviton (Arm)](https://aws.amazon.com/marketplace/pp/prodview-aqmdt52vqs5qk)
* [Anbox Cloud Appliance for x86](https://aws.amazon.com/marketplace/pp/prodview-3lx6xyaapstz4)

### Check the prerequisites

Check the hardware requirements for the Anbox Cloud Appliance [here](https://discourse.ubuntu.com/t/requirements/17734#appliance).

In addition, make sure you have the following accounts:

* An Ubuntu SSO account. If you don't have one yet, create it [here](https://login.ubuntu.com).
* An AWS account that you use to buy a subscription to the Anbox Cloud Appliance.
  [note type="information" status="Note"]The quota for your AWS account must be sufficient for the instance types that you plan to use.[/note]

## Install the appliance

Complete the following steps to subscribe to the Anbox Cloud Appliance offering, get access to the required instances and configure them correctly.

### 1. Start the launch wizard

Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/) and log in.

On the EC2 dashboard, click **Launch Instance** to start the Launch Instance Wizard.

![Start the Launch Instance Wizard|690x451](https://assets.ubuntu.com/v1/17073a3d-install_appliance_launch-wizard.png)

[note type="information" status="Note"]You should go through all steps in the wizard before launching the instance. In most steps, you can accept the default configuration, but you must configure the required storage for the instance. Therefore, do not click **Review and Launch** until you reach the final page of the wizard.[/note]

### 2. Select the AMI

To select the Amazon Machine Image (AMI), type "Anbox Cloud" in the search field.

Choose either the Arm variant or the x86 variant and click **Select**.

![Select the Amazon Machine Image (AMI)|690x451](https://assets.ubuntu.com/v1/ce51218c-install_appliance_select-ami.png)

You will be presented with the pricing information. Click **Continue** to confirm.

### 3. Choose an instance type

AWS offers various instance types. The Anbox Cloud Appliance images are listed for a subset of the available instance types only.

Select the instance type that is most suitable for what you're planning to do. For example, if you just want to try out the Anbox Cloud Appliance, an instance type with GPU support and limited CPU and memory is sufficient. See the [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734#appliance) for the minimum hardware requirements.

![Choose an instance type|690x451](https://assets.ubuntu.com/v1/f61efdc4-install_appliance_instance-type.png)

In this example, we picked `g4dn.2xlarge`, which provides 8 vCPUs, 32 GB of memory and a single NVIDIA Tesla T4 GPU.

Click **Next: Configure Instance Details** to continue.

### 4. Configure the instance details

You do not need to customise any of the settings in the instance details, but you can fine-tune things. For example, you might want to put the instance onto a different VPC or subnet.

![Configure the instance details|690x451](https://assets.ubuntu.com/v1/3aed5594-install_appliance_configure-instance.png)

Click **Next: Add Storage** to continue.

### 5. Add storage

The Anbox Cloud instance requires sufficient storage to work correctly. The root disk should have at minimum 50 GB and for best performance, you should create an additional EBS volume of at least 50 GB. Anbox Cloud uses the additional volume exclusively to store all of its data, including containers. Using a separate volume isolates it from the operating system, which increases performance. If no additional EBS volume is added, the Anbox Cloud Appliance automatically creates an image on the root disk, which is used to store any data. However, this is not recommended.

![Add storage|690x451](https://assets.ubuntu.com/v1/1ee4160c-install_appliance_add-storage.png)

In this example, we use three storage volumes:

* `/dev/sda1` as root disk with a size of 50 GB.
* An ephemeral `/dev/nvme0n1` disk (part of the `g4dn` instance), which is ignored by the Anbox Cloud Appliance.
* `/dev/sdb` as EBS volume with a size of 100 GB.

If you don't have any specific requirements, we recommend choosing the same configuration.

Click **Next: Add Tags** and then **Next: Configure Security Group** to continue.

### 6. Configure the security group

To allow external access, you must open several ports in the security group attached to the AWS instance. The AMI already comes with the required configuration, so you don't need to do any changes. For reference, all required ports are documented [here](https://discourse.ubuntu.com/t/requirements/17734).

![Configure the security group|690x451](https://assets.ubuntu.com/v1/2910cbd3-install_appliance_security-group.png)

Click **Review and Launch** to continue.

### 7. Review and launch

You should now review the instance configuration. If everything is correct, click **Launch**.

You are prompted to select a key pair. You can choose an existing key pair or create one if you don't have one yet. Make sure to save the private key in a secure location.

![Confirm to launch instances|690x451](https://assets.ubuntu.com/v1/c13f7244-install_appliance_launch-instances.png)

Click **Launch Instances** to continue. AWS will verify your configuration, subscribe you to the product and launch the instance.

![Launch status|690x451](https://assets.ubuntu.com/v1/5115a09d-install_appliance_launch-status.png)

## Access the appliance

When the instance is successfully launched, you can find its public IP address in the instance details page. Use this IP address or the corresponding DNS name to access the status web page.

[note type="information" status="Note"]By default, the Anbox Cloud Appliance uses self-signed certificates, which might cause a security warning in your browser. Use the mechanism provided by your browser to proceed to the web page.[/note]

![Appliance welcome screen|690x343, 100%](https://assets.ubuntu.com/v1/f35744dc-install_appliance_initialise.png)


## Log on to the machine

To finalise the installation, you must log on to the machine that hosts the appliance. To do so, use the user name `ubuntu` and provide the path to your private key file when connecting. See [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) for instructions on how to connect.

## Finalise the installation

After the installation is complete, you must initialise the appliance and register your Ubuntu SSO account with the dashboard of the appliance. See [How to finalise the installation](tbd) for instructions.
