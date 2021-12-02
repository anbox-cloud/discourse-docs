.. _tut_installing-appliance:

=================
Install the |ACA|
=================

The Anbox Cloud Appliance provides a deployment of Anbox Cloud to a
single machine. This offering is well suited for initial prototype and
small scale deployments.

.. note::
   There are differences between
   the Anbox Cloud Appliance and the full Anbox Cloud installation (see
   :ref:`exp_anbox-cloud-variants`).
   This section focuses on the **Anbox Cloud Appliance**. For instructions
   on how to install **Anbox Cloud**, see :ref:`howto_install_landing`.


This tutorial guides you through the steps that are required to install
and initialise the Anbox Cloud Appliance, either from the `AWS Marketplace <https://aws.amazon.com/marketplace/>`_ or from the
`snap <https://snapcraft.io/anbox-cloud-appliance>`_:

1. :ref:`tut_installing-appliance-prerequisites`
2. :ref:`tut_installing-appliance-install`
3. :ref:`tut_installing-appliance-initialise`
4. :ref:`tut_installing-appliance-register`

.. _tut_installing-appliance-prerequisites:

Check the prerequisites
=======================

Before you start the installation, ensure that you have the required
accounts and prerequisites:

-  An Ubuntu SSO account. If you don’t have one yet, create it
   `here <https://login.ubuntu.com>`__.
-  When installing from the `AWS Marketplace <https://aws.amazon.com/marketplace/>`_:

   -  An AWS account that you use to buy a subscription to the Anbox
      Cloud Appliance.

-  When installing the
   `snap <https://snapcraft.io/anbox-cloud-appliance>`_:

   -  A virtual or bare metal machine running Ubuntu 20.04. See the
      detailed requirements
      :ref:`here <requirements>`.

      .. note::
         The Anbox Cloud Appliance
         is currently supported on `AWS <https://aws.amazon.com/>`_ and
         `Oracle Cloud (OCI) <https://www.oracle.com/cloud/>`_. Official
         support for other clouds, namely Azure and Google Cloud, will be
         added soon.
   -  Your *Ubuntu Advantage for Applications* token. If you don’t
      have one yet, `speak to your Canonical representative <https://anbox-cloud.io/contact-us>`_. If you
      already have a UA Applications token, sign in on
      https://ubuntu.com/advantage to retrieve it.

      .. warning::
         The *Ubuntu Advantage
         for Infrastructure* token that every user gets for free for
         personal use does **NOT** work and will result in a failed
         deployment. You must purchase a *Ubuntu Advantage
         for Applications* subscription by `contacting Canonical <https://anbox-cloud.io/contact-us>`_.

.. _tut_installing-appliance-install:

Install the appliance
=====================

The Anbox Cloud Appliance is available through the AWS Marketplace and
as a snap.

-  When installing on AWS, follow the steps in :ref:`tut_installing-appliance-install-aws`.
-  When installing on a local machine or in another cloud, follow the
   steps in :ref:`tut_installing-appliance-install-snap`.

.. _tut_installing-appliance-install-aws:

Install from the AWS Marketplace
--------------------------------

.. note::
   Skip this section when installing
   the snap.

Installing the Anbox Cloud Appliance through the AWS Marketplace
simplifies the installation and deployment process and allows billing to
be handled directly through AWS.

AWS supports running the Anbox Cloud Appliance on the `AWS Graviton <https://aws.amazon.com/ec2/graviton/>`_ Arm-based instances
or on x86 instances. Before installing the appliance, decide which
architecture you want to use. The appliance supports the same set of
features on both architectures, but you should factor in the following
aspects:

-  AWS Graviton (Arm) and x86 offer equal performance for Android
   applications.
-  GPUs are currently available for x86. NVIDIA GPUs will only become
   available for Arm instances `later in 2021 <https://aws.amazon.com/blogs/machine-learning/aws-and-nvidia-to-bring-arm-based-instances-with-gpus-to-the-cloud/>`_.
-  Not all Android applications support the x86 ABI. Therefore, some
   applications can run only on Arm.

For detailed information about the offering, see the following pages on
the AWS Marketplace:

-  `Anbox Cloud Appliance for AWS Graviton (Arm) <https://aws.amazon.com/marketplace/pp/prodview-aqmdt52vqs5qk>`_
-  `Anbox Cloud Appliance for x86 <https://aws.amazon.com/marketplace/pp/prodview-3lx6xyaapstz4>`_

The following instructions guide you through all relevant steps to
deploy the Anbox Cloud Appliance in your AWS account. For additional
information, see the `AWS documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html>`_
about launching an instance.

The entire deployment process will take 10-15 minutes, depending on the
selected hardware and the network conditions.

Before you start
~~~~~~~~~~~~~~~~

Deploying the Anbox Cloud Appliance requires some familiarity with AWS.
In particular, you should be familiar with:

-  Amazon Elastic Compute Cloud (Amazon EC2), for basic EC2
   configuration
-  Amazon Elastic Block Storage (Amazon EBS), for configuring the EC2
   instance storage and managing encryption
-  Amazon Virtual Private Cloud (Amazon VPC), for configuring an
   internet facing subnet and a security group

The appliance uses the following billable services by AWS:

-  EC2 and Marketplace appliance (see the AWS Marketplace product page
   for costs)
-  Network egress

You do not need to request an increase in limits for your AWS account
for this deployment.

1. Start the launch wizard
~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the `Amazon EC2 console <https://console.aws.amazon.com/ec2/>`_
and log in.

On the EC2 dashboard, click **Launch Instance** to start the Launch
Instance Wizard.

.. figure:: /images/install_appliance_launch-wizard.png
   :alt: Start the Launch Instance Wizard

   Start the Launch Instance Wizard

.. note::
   You should go through all steps
   in the wizard before launching the instance. In most steps, you can
   accept the default configuration, but you must configure the required
   storage for the instance. Therefore, do not click **Review and Launch**
   until you reach the final page of the wizard.

2. Select the AMI
~~~~~~~~~~~~~~~~~

To select the Amazon Machine Image (AMI), type “Anbox Cloud” in the
search field.

Choose either the Arm variant or the x86 variant and click **Select**.

.. figure:: /images/install_appliance_select-ami.png
   :alt: Select the Amazon Machine Image (AMI)

   Select the Amazon Machine Image (AMI)

You will be presented with the pricing information. Click **Continue**
to confirm.

3. Choose an instance type
~~~~~~~~~~~~~~~~~~~~~~~~~~

AWS offers various instance types. The Anbox Cloud Appliance images are
listed for a subset of the available instance types only.

Select the instance type that is most suitable for what you’re planning
to do. For example, if you just want to try out the Anbox Cloud
Appliance, an instance type with GPU support and limited CPU and memory
is sufficient. See the
:ref:`Requirements <requirements-appliance>`
for the minimum hardware requirements.

.. figure:: /images/install_appliance_instance-type.png
   :alt: Choose an instance type

   Choose an instance type

In this example, we picked *g4dn.2xlarge*, which provides 8 vCPUs, 32 GB
of memory and a single NVIDIA Tesla T4 GPU.

Click **Next: Configure Instance Details** to continue.

4. Configure the instance details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You do not need to customise any of the settings in the instance
details, but you can fine-tune things. For example, you might want to
put the instance onto a different VPC or subnet.

.. figure:: /images/install_appliance_configure-instance.png
   :alt: Configure the instance details

   Configure the instance details

Click **Next: Add Storage** to continue.

5. Add storage
~~~~~~~~~~~~~~

The Anbox Cloud instance requires sufficient storage to work correctly.
The root disk should have at minimum 50 GB and for best performance, you
should create an additional EBS volume of at least 50 GB. Anbox Cloud
uses the additional volume exclusively to store all of its data,
including containers. Using a separate volume isolates it from the
operating system, which increases performance. If no additional EBS
volume is added, the Anbox Cloud Appliance automatically creates an
image on the root disk, which is used to store any data. However, this
is not recommended.

.. figure:: /images/install_appliance_add-storage.png
   :alt: Add storage

   Add storage

In this example, we use three storage volumes:

-  ``/dev/sda1`` as root disk with a size of 50 GB.
-  An ephemeral ``/dev/nvme0n1`` disk (part of the g4dn instance), which
   is ignored by the Anbox Cloud Appliance.
-  ``/dev/sdb`` as EBS volume with a size of 100 GB.

If you don’t have any specific requirements, we recommend choosing the
same configuration.

Click **Next: Add Tags** and then **Next: Configure Security Group** to
continue.

6. Configure the security group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To allow external access, you must open several ports in the security
group attached to the AWS instance. The AMI already comes with the
required configuration, so you don’t need to do any changes. For
reference, all required ports are documented
:ref:`here <requirements>`.

.. figure:: /images/install_appliance_security-group.png
   :alt: Configure the security group

   Configure the security group

Click **Review and Launch** to continue.

7. Review and launch
~~~~~~~~~~~~~~~~~~~~

You should now review the instance configuration. If everything is
correct, click **Launch**.

You are prompted to select a key pair. You can choose an existing key
pair or create one if you don’t have one yet. Make sure to save the
private key in a secure location.

.. figure:: /images/install_appliance_launch-instances.png
   :alt: Confirm to launch instances

   Confirm to launch instances

Click **Launch Instances** to continue. AWS will verify your
configuration, subscribe you to the product and launch the instance.

.. figure:: /images/install_appliance_launch-status.png
   :alt: Launch status

   Launch status

When the instance is successfully launched, you can find its public IP
address in the instance details page. Use this IP address or the
corresponding DNS name to access the status web page (in the following
steps referred to as ``https://your-machine-address``).

Next, continue with the instructions in :ref:`tut_installing-appliance-initialise`.

.. _tut_installing-appliance-install-snap:

Install the snap
----------------

.. note::
   Skip this section when installing
   from the AWS Marketplace.

The following instructions guide you through all relevant steps to
install the Anbox Cloud Appliance from the
`snap <https://snapcraft.io/anbox-cloud-appliance>`_.

1. Attach your machine to the UA subscription
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Anbox Cloud Appliance requires a valid Ubuntu Advantage for
Applications subscription.

Before installing the appliance, you must attach the machine on which
you’re running the Anbox Cloud Appliance to your Ubuntu Advantage for
Applications subscription. To do so, run the following command,
replacing ** with your Ubuntu Advantage for Applications token:

::

   sudo ua attach <UA_token>

.. _install-the-snap-1:

2. Install the snap
~~~~~~~~~~~~~~~~~~~

Run the following command to install the ``anbox-cloud-appliance`` snap,
which handles the installation and deployment of the Anbox Cloud
Appliance:

::

   sudo snap install --classic anbox-cloud-appliance

.. _tut_installing-appliance-additional-tools:

3. Install additional tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The appliance requires a few additional tools. Run the following
commands to install them:

::

   sudo snap install amc
   sudo snap install --classic --channel=2.9/stable juju

.. note::
   See :ref:`Juju version <howto_update_upgrade-anbox-juju-version>`
   for information about which Juju version is required for your version of
   Anbox Cloud.

.. _tut_installing-appliance-initialise:

Initialise the appliance
========================

After the installation, access ``https://your-machine-address``. This
web page provides status information for the following initialisation
process.

.. note::
   By default, the Anbox Cloud
   Appliance uses self-signed certificates, which might cause a security
   warning in your browser. Use the mechanism provided by your browser to
   proceed to the web page.

.. figure:: /images/install_appliance_welcome-screen.png
   :alt: Appliance welcome screen

   Appliance welcome screen

The following instructions guide you through all relevant steps to
initialise the Anbox Cloud Appliance.

1. Log on to the machine
------------------------

Log on to the machine that hosts the appliance. If you installed on an
AWS instance, note that you must use the user name ``ubuntu`` and
provide the path to your private key file when connecting. See `Connect to your Linux instance using SSH <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html>`_
for instructions on how to connect.

2. Update your system
---------------------

Run the following commands to ensure that all installed packages on your
system are up-to-date:

::

   sudo apt update
   sudo apt upgrade

3. Start the initialisation process
-----------------------------------

Invoke the initialisation process of the Anbox Cloud Appliance:

::

   sudo anbox-cloud-appliance init

You will be asked a few questions. If you don’t want to make any
specific changes, you can safely stay with the offered default answers.

.. code:: bash

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

After the command has returned, the initialisation process will run
fully automatically in the background. You can watch the status web page
at ``https://your-machine-address`` for progress information.

.. figure:: /images/install_appliance_deployment.png
   :alt: Anbox Cloud deployment

   Anbox Cloud deployment

Alternatively, use the ``anbox-cloud-appliance status`` command to
monitor the progress information on the command line.

.. code:: bash

   status: initializing
   progress: 60
   update-available: false
   reboot-needed: false

.. _tut_installing-appliance-register:

Register with the dashboard
===========================

Once the initialisation process has finished, you are presented with a
welcome page on ``https://your-machine-address`` with instructions on
how to register a user account with your installation. This registration
is needed to access the :ref:`web dashboard <howto_manage_web-dashboard>`.

.. figure:: /images/install_appliance_register-sso.png
   :alt: Instructions for registering Ubuntu SSO account

   Instructions for registering Ubuntu SSO account

1. Register your Ubuntu SSO account
-----------------------------------

Register your Ubuntu SSO account by running the following command via
SSH on the machine that hosts the appliance:

::

   anbox-cloud-appliance dashboard register <your Ubuntu SSO email address>

The output provides a link that you must open in your web browser to
finish the account creation. By default, the registration link expires
after one hour. After registering, you can log into the appliance
dashboard with your Ubuntu SSO account.

Done!
=====

Your Anbox Cloud Appliance is now fully set up and ready to be used!
Next, you should check out the :ref:`tut_getting-started-dashboard`
or the :ref:`tut_getting-started` tutorial
to familiarise yourself with how to use Anbox Cloud.

You can find more information about how to use the appliance in the
documentation. The appliance installation is nearly identical to
installing via Juju, so all the commands and examples not relating
directly to Juju will apply.
