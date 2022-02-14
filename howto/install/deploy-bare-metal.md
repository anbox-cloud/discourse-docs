To deploy Anbox Cloud on a public cloud (such as AWS, Azure or Google) or using MAAS or OpenStack, see the instructions in [Deploy Anbox Cloud with Juju](https://discourse.ubuntu.com/t/deploy-anbox-cloud-with-juju/17744).

Alternatively, you can follow the instructions in this document to use the [manual cloud provider](https://jaas.ai/docs/manual-cloud) that Juju offers. This method allows you to deploy Anbox Cloud with Juju on a set of SSH connected machines.

## Prerequisites

Before you start the installation, ensure that you have the required prerequisites:

* At least three Ubuntu 20.04 LTS machines. See [Minimum hardware](https://discourse.ubuntu.com/t/requirements/17734#minimum-hardware) for details and recommendations.
* Your *Ubuntu Advantage for **Applications*** token. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a UA Applications token, sign in on https://ubuntu.com/advantage to retrieve it.
  [note type="caution" status="Warning"]The *Ubuntu Advantage for **Infrastructure*** token that every user gets for free for personal use does **NOT** work and will result in a failed deployment. You must purchase a *Ubuntu Advantage for **Applications*** subscription by [contacting Canonical](https://anbox-cloud.io/contact-us).[/note]

## Install Juju

Juju is a tool for deploying, configuring and operating complex software on public or private clouds.

You must install a Juju client on the machine that you use to run the deployment commands. To install Juju 2.9, enter the following command:

    sudo snap install --channel=2.9/stable juju

See [Juju version](https://discourse.ubuntu.com/t/installation-requirements/17734#juju-version) for information about which Juju version is required for your version of Anbox Cloud.

## Add a controller and model

The [Juju controller](https://juju.is/docs/olm/controllers) is used to manage the software deployed through Juju, from deployment to upgrades to day-two operations. One Juju controller can manage multiple projects or workspaces, which in Juju are known as [models](https://juju.is/docs/olm/models).

You should dedicate one machine as the Juju controller. Run the following command to bootstrap the controller onto that machine:

    juju bootstrap manual/<user>@<controller IP address> anbox-cloud

Juju will connect to the machine via SSH as the specified user and install all necessary requirements.

When the controller is set up, create a model to hold the Anbox Cloud deployment:

    juju add-model main

## Add all machines

Before starting the deployment, you must add all machines to the Juju model. See [Minimum hardware](https://discourse.ubuntu.com/t/requirements/17734#minimum-hardware) for the list of machines that you need.

When adding the machines, start with the machine that you want to host the management layer of Anbox Cloud. Then add all LXD worker nodes. Run the following command for each machine:

    juju add-machine ssh:<user>@<machine IP address>

The user (for example, `ubuntu`) must have administrator rights on the machine and have permission to SSH to the machine.

[note type="caution" status="Warning"]Make sure to add the machines by their IP addresses rather than their DNS names. Adding a machine by DNS name does currently not work.[/note]

Juju will add the machines to its list of usable machines, which you can display with the `juju list-machines` command. Make sure that all machines are in the `started` state before you proceed. If any of the machines are still in `down` state, wait until they switch to `started`:

    Machine  State    DNS           Inst id              Series AZ Message
    0        started  192.168.1.9   manual:192.168.1.9   bionic    Manually provisioned machine
    1        started  192.168.1.10  manual:192.168.1.10  bionic    Manually provisioned machine

## Attach your Ubuntu Advantage subscription

Create an `ua.yaml` overlay file as described in [Deploy Anbox Cloud with Juju](https://discourse.ubuntu.com/t/deploy-anbox-cloud-with-juju/17744#ua-overlay).

You must provide this file when deploying Anbox Cloud.

## Determine the machine mapping

When running the deployment command, you must map the machines to the ones described in the [Juju bundle](https://discourse.ubuntu.com/t/about-anbox-cloud/17802#juju-bundles) that you are deploying.

Run `juju list-machines` to display the available machines:

    Machine  State    DNS            Inst id              Series  AZ             Message
    0        started  192.168.0.9   i-09a2fdb5e7a2e8385   bionic  localhost-1a   running
    1        started  192.168.0.10  i-00a05065e2768be5d   bionic  localhost-1b   running

The `anbox-cloud-core` deployment bundle requires two machines: `0` and `1`. `0` is supposed to host the AMS service. `1` is used for LXD. See the [bundle.yaml](https://api.jujucharms.com/charmstore/v5/~anbox-charmers/bundle/anbox-cloud-core/archive/bundle.yaml) file for details.

The `anbox-cloud` bundle requires an additional machine to host the extra services required for streaming. See the [bundle.yaml](https://api.jujucharms.com/charmstore/v5/~anbox-charmers/bundle/anbox-cloud/archive/bundle.yaml) file for details.

The `--map-machine` argument for the `juju deploy` command maps the machines defined inside the bundle to those your Juju controller has registered in the model. See the [Juju documentation](https://jaas.ai/docs/charm-bundles) for more details. If you added the machines in the order Juju expects them, the mapping is very straight-forward: `--map-machines 0=0,1=1` for the `anbox-cloud-core` bundle or `--map-machines 0=0,1=1,2=2` for the `anbox-cloud` bundle.

## Deploy Anbox Cloud

Now you can deploy Anbox Cloud. The deployment is entirely handled by Juju and does not need any manual involvement other than running the actual deploy command.

Choose between the available [Juju bundles](https://discourse.ubuntu.com/t/about-anbox-cloud/17802#juju-bundles):

* For a minimised version of Anbox Cloud without the streaming stack, run the following command to deploy the `anbox-cloud-core` bundle:

        juju deploy cs:~anbox-charmers/anbox-cloud-core --overlay ua.yaml --map-machines 0=0,1=1

* For the full version of Anbox Cloud, run the following command to deploy the `anbox-cloud` bundle:

        juju deploy cs:~anbox-charmers/anbox-cloud --overlay ua.yaml --map-machines 0=0,1=1,2=2

You can watch the status of the deployment with the following command:

     watch -c juju status --color --relations=true
