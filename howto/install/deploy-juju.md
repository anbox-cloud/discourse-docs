Anbox Cloud supports various public clouds, such as AWS, Azure and Google. To deploy Anbox Cloud in a cloud environment, you use Juju.

See the following sections for detailed instructions. If you want to install Anbox Cloud on bare metal instead of a public cloud, see [How to deploy Anbox Cloud on bare metal](https://discourse.ubuntu.com/t/deploy-anbox-cloud-on-bare-metal/26378) instead.

[note type="information" status="Note"]
There are differences between the full Anbox Cloud installation and the Anbox Cloud Appliance (see [Variants](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802#variants)). This section focuses on **Anbox Cloud**. For instructions on how to install the **Anbox Cloud Appliance**, see [How to install the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702) or the [Install the Anbox Cloud Appliance on your local machine](https://discourse.ubuntu.com/t/install-appliance/22681) tutorial.
[/note]

## Prerequisites

Before you start the installation, ensure that you have the required credentials and prerequisites:

* An Ubuntu 18.04 LTS or 20.04 LTS environment to run the commands (or another operating system that supports snaps - see the [Snapcraft documentation](https://snapcraft.io/docs/installing-snapd)).
* Account credentials for one of the following public clouds:
  * [Amazon Web Services](https://aws.amazon.com/) (including AWS-China)
  * [Google Cloud platform ](https://cloud.google.com/)
  * [Microsoft Azure](https://azure.microsoft.com/)
* Your *Ubuntu Advantage for **Applications*** token. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a UA Applications token, sign in on https://ubuntu.com/advantage to retrieve it.
  [note type="caution" status="Warning"]The *Ubuntu Advantage for **Infrastructure*** token that every user gets for free for personal use does **NOT** work and will result in a failed deployment. You must purchase a *Ubuntu Advantage for **Applications*** subscription by [contacting Canonical](https://anbox-cloud.io/contact-us).[/note]

## Install Juju

Juju is a tool for deploying, configuring and operating complex software on public or private clouds.

To install Juju 2.9, enter the following command:

    sudo snap install --channel=2.9/stable juju

See [Juju version](https://discourse.ubuntu.com/t/installation-requirements/17734#juju-version) for information about which Juju version is required for your version of Anbox Cloud.

## Authenticate with your cloud

Juju has baked in knowledge of many public clouds, such as AWS, Azure and Google. You can see which ones are ready to use by running the following command:

    juju clouds

Most clouds require credentials so that the cloud knows which operations are authorised, so you will need to supply these for Juju. If you choose to use AWS, for example, you would run:

    juju add-credential aws

For a different cloud, just substitute the cloud name (use the name returned by  the `juju clouds` command). The data you need to supply varies depending on the cloud.

## Add a controller and model

The [Juju controller](https://juju.is/docs/olm/controllers) is used to manage the software deployed through Juju, from deployment to upgrades to day-two operations. One Juju controller can manage multiple projects or workspaces, which in Juju are known as [models](https://juju.is/docs/olm/models).

For example, run the following command to bootstrap the controller for AWS:

    juju bootstrap aws my-controller

A Juju model holds a specific deployment. It is a good idea to create a new one specifically for each deployment:

    juju add-model anbox-cloud

You can have multiple models on each controller, which means that you can deploy multiple versions of Anbox Cloud, or other applications.

<a name="ua-overlay"></a>
## Attach your Ubuntu Advantage subscription

Every deployment of Anbox Cloud must be attached to the Ubuntu Advantage service Canonical provides. This provides your deployment with the correct licences you're granted as part of your licence agreement with Canonical, next to other services available through your subscription like [Livepatch](https://ubuntu.com/livepatch).

You can retrieve your *Ubuntu Advantage for **Applications*** token at https://ubuntu.com/advantage after logging in. You should record the token as you will need it for every deployment of Anbox Cloud.

[note type="caution" status="Warning"]The *Ubuntu Advantage for **Infrastructure*** token that every user gets for free for personal use does **NOT** work and will result in a failed deployment. You must purchase a *Ubuntu Advantage for **Applications*** subscription by [contacting Canonical](https://anbox-cloud.io/contact-us).[/note]

To provide your token when deploying with Juju, you need an [overlay file](https://discourse.ubuntu.com/t/installation-customizing/17747#overlay-files) named `ua.yaml`. For the `anbox-cloud` bundle, the `ua.yaml` file should look like this:

```yaml
applications:
  ams:
    options:
      ua_token: <your token>
  ams-node-controller:
    options:
      ua_token: <your token>
  lxd:
    options:
      ua_token: <your token>
  anbox-stream-agent:
    options:
      ua_token: <your token>
  anbox-stream-gateway:
    options:
      ua_token: <your token>
  anbox-cloud-dashboard:
    options:
      ua_token: <your token>
```

For the `anbox-cloud-core` bundle, the `ua.yaml` file should look like this:

```yaml
applications:
  ams:
    options:
      ua_token: <your token>
  ams-node-controller:
    options:
      ua_token: <your token>
  lxd:
    options:
      ua_token: <your token>
```

You will use the overlay file during the deployment.

## Deploy Anbox Cloud

To install Anbox Cloud, deploy the suitable Anbox Cloud bundle to the Juju model. This will add instances to the model and deploy the required applications.

Choose between the available [Juju bundles](https://discourse.ubuntu.com/t/about-anbox-cloud/17802#juju-bundles):

* For a minimised version of Anbox Cloud without the streaming stack, run the following command to deploy the `anbox-cloud-core` bundle:

        juju deploy anbox-cloud-core --overlay ua.yaml

* For the full version of Anbox Cloud, run the following command to deploy the `anbox-cloud` bundle:

        juju deploy anbox-cloud --overlay ua.yaml

## Customise the hardware configuration

To customise the machine configuration Juju will use for the deployment, create another [overlay file](https://discourse.ubuntu.com/t/installation-customizing/17747#overlay-files). Here you can, for example, specify AWS instance types, change the size of the root disk or other things.

For the `anbox-cloud-core` bundle, such an `overlay.yaml` file looks like this:

```
machines:
  '0':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '1':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
```

For the `anbox-cloud` bundle, the `overlay.yaml` file includes one more machine in the default configuration:

```
machines:
  '0':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '1':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '2':
    series: focal
    constraints: "instance-type=m4.2xlarge root-disk=50G"
```

To deploy, add `--overlay overlay.yaml` to your deploy command. For example:

    juju deploy anbox-cloud --overlay ua.yaml --overlay overlay.yaml

### Add GPU support

On most clouds, adding GPU support is done by picking a specific instance type. The following example uses the `g4dn.xlarge` instance type on AWS, which includes an NVIDIA Tesla T4 GPU.

The `overlay.yaml` file for the `anbox-cloud` bundle looks like this:

```
machines:
  '0':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '1':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '2':
    series: focal
    constraints: "instance-type=g4dn.2xlarge root-disk=50G"
```

To deploy, add `--overlay overlay.yaml` to your deploy command. For example:

    juju deploy anbox-cloud --overlay ua.yaml --overlay overlay.yaml

### Use Arm instances

Some clouds, like AWS with their Graviton instances, provide support for Arm instance types. These can be used with Anbox Cloud by specifying the correct instance type in the `overlay.yaml`:

```
applications:
  lxd:
    # With Juju >= 2.9.0 we must specify the architecture of the underlying machine
    # in the constraints of the application
    constraints: "arch=arm64"
machines:
  ...
  '2':
    series: focal
    constraints: "instance-type=m6g.2xlarge root-disk=50G"
```

To deploy, add `--overlay overlay.yaml` to your deploy command. For example:

    juju deploy anbox-cloud --overlay ua.yaml --overlay overlay.yaml

## Monitor the deployment

After starting the deployment, Juju will create instances, install software and connect the different parts of the cluster together. This can take several minutes. You can monitor what's going on by running the following command:

    watch -c juju status --color

## Perform necessary reboots

In some cases, a reboot of the LXD machines is necessary.

For example, a reboot is required when the Ubuntu 18.04 GA kernel is selected when deploying on AWS. This kernel is based on the upstream 4.15 release. As Anbox Cloud requires a Ubuntu kernel with a minimum version of 5.0, the kernel needs to be changed. The LXD charm already takes care of installing a newer kernel, but the final reboot must be performed manually.

Check the output of the `juju status` command to see whether you need to reboot:

```sh
...
Unit       Workload  Agent  Machine  Public address  Ports  Message
lxd/0*     active    idle   3        10.75.96.23            reboot required to activate new kernel
...
```
To reboot the machine hosting LXD, run the following command:

    juju ssh lxd/0 -- sudo reboot

When the machine is back running, you must manually clear the status of the LXD units:

    juju run-action --wait lxd/0 clear-notification

Once done, the reboot operation is finished.
