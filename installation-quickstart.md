With this quick start guide and some tools from Canonical, you'll have an Anbox Cloud running on the cloud of your choice in minutes!

> **NOTE:** There is a difference between the full Anbox Cloud installation and the Anbox Cloud Appliance (see [Variants](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802#variants)). This section focuses on **Anbox Cloud**. For instructions on how to install the **Anbox Cloud Appliance**, see [Installing the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681).

## What you'll need

For the quickstart into Anbox Cloud you will need the following things:

* An Ubuntu 18.04 LTS or 20.04 LTS environment to run the commands (or another operating system which supports snaps - see [the snapcraft documentation](https://snapcraft.io/docs/installing-snapd))
* Account credentials for one of the following public clouds:
  * [Amazon Web Services](https://aws.amazon.com/), including AWS-China
  * [Google Cloud platform ](https://cloud.google.com/)
* Your *Ubuntu Advantage for **Applications*** token. If you don't have yours yet, get it from https://ubuntu.com/advantage or speak to your Canonical representative

> **WARNING:** The *Ubuntu Advantage for **Infrastructure*** token every user gets for free for personal use does **NOT** work and will result in a failed deployment!

> **NOTE:** If you don't meet these requirements, there are additional ways of installing the Anbox Cloud. See the more general [Customise the installation](https://discourse.ubuntu.com/t/installation-customizing/17747) for details.

### Install Juju

Juju is a tool for deploying, configuring and operating complex software on public or private clouds.

Anbox Cloud currently requires Juju 2.8 (see [Juju version](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750#juju-version) for more information). To install this version, enter the following command:

    sudo snap install --channel=2.8/stable juju

<!--It can be installed with a snap:

    sudo snap install juju --classic
-->

### Find Your Cloud

Juju has baked in knowledge of many public clouds such as AWS, Azure and Google. You can see which ones are ready to use by running this command:

    juju clouds

### Add Credentials

Most clouds require credentials so that the cloud knows which operations are authorised, so you will need to supply these for Juju. If you choose to use AWS, for example, you would run:

    juju add-credential aws

For a different cloud, just substitute the name from the previous list output by Juju. The data you need to supply will vary depending on the cloud.

### Add a Controller

The Juju controller is used to manage the software deployed through Juju, from deployment to upgrades to day-two operations. One Juju controller can manage multiple projects or workspaces, which in Juju are known as 'models'.

    juju bootstrap aws my-controller

### Add a Model

The model holds a specific deployment. It is a good idea to create a new one specifically for each deployment.

    juju add-model anbox-cloud

Remember that you can have multiple models on each controller, so you can deploy multiple versions of Anbox Cloud, or other applications.

## Ubuntu Advantage Subscription

Every deployment of Anbox Cloud needs to be attached to the Ubuntu Advantage service Canonical provides. This provides your deployment with the correct licences you're granted as part of your licence agreement with Canonical next to other services available through your subscription like [Livepatch](https://ubuntu.com/livepatch).

You can get your *Ubuntu Advantage for **Applications*** token at https://ubuntu.com/advantage after logging in. Please record the token as you will need it for every deployment of Anbox Cloud.

> **WARNING:** The free *Ubuntu Advantage for **Infrastructure*** token every user gets for free for personal use does **NOT** work and will result in a failed deployment!

In preparation for the next steps, please create an overlay file named `ua.yaml` for the deployment process via Juju.

For the `cs:~anbox-charmers/anbox-cloud` bundle, the `ua.yaml` file should look like this:

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

For the `cs:~anbox-charmers/anbox-cloud-core` bundle, the `ua.yaml` file should look like this:

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

You will use the overlay file in the next steps.

### Deploy Anbox Cloud

Deploy the Anbox Cloud bundle to the Juju model. This will add instances to the model and deploy the required applications.

The `anbox-cloud-core` bundle provides a minimised version of Anbox Cloud which is enough for smaller scale use cases, e.g. application testing or automation or if you generally don't want to use the Anbox Cloud streaming stack.

    juju deploy cs:~anbox-charmers/anbox-cloud-core --overlay ua.yaml

If you're interested in deploying Anbox Cloud with its streaming stack included, you need to use the `anbox-cloud` bundle instead:

    juju deploy cs:~anbox-charmers/anbox-cloud --overlay ua.yaml

### Custom machine configuration

To customise the machine configuration Juju will use for the deployment, you can create another overlay file. Here you can for example specify specific AWS instance types, change the size of the root disk or other things.

For the `anbox-cloud-core` bundle, such an `overlay.yaml` looks like this:

```
machines:
  '0':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '1':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
```

For the `anbox-cloud` bundle, the `overlay.yaml` includes one more machine in the default configuration:

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

To deploy with the bundle from above, add `--overlay overlay.yaml` to your deploy command:

    juju deploy cs:~anbox-charmers/anbox-cloud ... --overlay overlay.yaml

### Add GPU Support

Adding GPU support is on most clouds done by picking a specific instance type. For this example we will use  the *g4dn.xlarge* instance type on AWS which includes a Nvidia Tesla T4 GPU.

The `overlay.yaml` for the ` cs:~anbox-charmers/anbox-cloud` bundle looks like this:

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

To deploy with the bundle from above, add `--overlay overlay.yaml` to your deploy command:

    juju deploy cs:~anbox-charmers/anbox-cloud ... --overlay overlay.yaml

### Use Arm Instances

Some clouds, like AWS with their Graviton instances, provide support for Arm instance types. These can be used with Anbox Cloud by specifying the correct instance type in the `overlay.yaml` as well:

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

To deploy with the bundle from above, add `--overlay overlay.yaml` to your deploy command:

    juju deploy cs:~anbox-charmers/anbox-cloud ... --overlay overlay.yaml

### Monitor the Deployment

Juju is now busy creating instances, installing software and connecting the different parts of the cluster together, which can take several minutes. You can monitor what's going on by running:

    watch -c juju status --color

### Perform necessary reboots

In some cases a reboot of the LXD machines is necessary, for example when the Ubuntu 18.04 GA kernel is selected when deploying on AWS. This kernel is based on the upstream 4.15 release. As Anbox Cloud requires a Ubuntu kernel with a minimum version of 5.0, the kernel needs to be changed. The LXD charm already takes care of installing a newer kernel, but the final reboot has to be performed manually.

Check the output of the `juju status` command to see whether you need to reboot:

```sh
...
Unit       Workload  Agent  Machine  Public address  Ports  Message
lxd/0*     active    idle   3        10.75.96.23            reboot required to activate new kernel
...
```
To reboot the machine hosting LXD, you can perform the following command:

    juju ssh lxd/0 -- sudo reboot

When the machine is back running, you have to manually clear the status of the LXD units:

    juju run-action --wait lxd/0 clear-notification

Once done, the reboot operation is finished.

### Start using Anbox Cloud!

Congratulations! You have Anbox Cloud up and running - now let's use it! The link below takes you to the operations guide, detailing some of the common things you'll want to do next:

[Getting started](https://discourse.ubuntu.com/t/getting-started/17756)

> Note:  This guide gets you up and running with Anbox Cloud quickly. If you want to explore how to customise your install, please see [Customise the installation](https://discourse.ubuntu.com/t/installation-customizing/17747) for a more detailed guide.
