[note type="information" status="Note"]If you're interested in getting notified for the latest Anbox Cloud releases, make sure you subscribe to notifications on the [announcements category](https://discourse.ubuntu.com/c/anbox-cloud/announcements/55) on the Anbox Cloud discourse.[/note]

Anbox Cloud allows upgrades from older versions to newer version. This describes the steps necessary to perform the upgrade.

The upgrade instructions detail the revisions each charm needs to be upgraded to, to bring it to the latest version. Next to the upgrade of the charms any used images or addons need to be updated as well.

[note type="caution" status="Warning"]Before you perform the upgrade ensure that you perform a backup of critical data you don't want to lose.[/note]

## Upgrade OS

Before you run the upgrade of the charms, you should make sure all packages on the machines that are part of the deployment are up-to-date. To do so, run the following commands on each machine:

    sudo apt update
    sudo apt upgrade

## Check Juju version

Before you upgrade, check the required [Juju version](https://discourse.ubuntu.com/t/installation-requirements/17734#juju-version).

If your deployment uses an earlier Juju version, you must upgrade your controller and all models first. See the [Juju documentation](https://juju.is/docs/olm/upgrade-models) for instructions on how to upgrade the Juju controller and all models to a newer Juju version.

## Upgrade all charms

The deployed Juju charms need to be upgraded next.

[note type="information" status="Note"]

- You can find a list of all charm, snap and Debian package versions for each Anbox Cloud release in the [component versions](https://discourse.ubuntu.com/t/component-versions/21413) overview. This also includes the charm and bundle revisions and channels for each release.

- Starting with the 1.14 release, all charms come from [Charmhub](https://charmhub.io) and use the concept of [channels](https://snapcraft.io/docs/channels) to track particular versions. The instructions below address how to upgrade from a 1.13.x release, where charms were still from the old Juju charm store. The `--switch --channel=1.14/stable` arguments instruct Juju to switch to the [Charmhub](https://charmhub.io) version of the charm and track the right channel.

- Starting with the 1.15 release, AMS enforces TLS 1.3 on its HTTPS endpoint. Images older than 1.15.0 will fail to reach AMS in this case. To still allow older images to work with AMS, you can temporarily enable TLS 1.2 support again in AMS by setting the `force_tls12` [configuration option of the AMS charm](https://charmhub.io/ams/configure?channel=1.15/stable#force_tls12).

- If you want to deploy a particular revision of a charm, you can do so by adding `--revision=<rev>` to the `juju upgrade-charm` command.

[/note]

Run the following commands in the exact same order as listed here but skip those you don't use in your deployment:

    juju upgrade-charm easyrsa --revision=<rev>
    juju upgrade-charm etcd --revision<rev>
    juju upgrade-charm --switch --channel=1.15/stable lxd lxd
    juju upgrade-charm --switch --channel=1.15/stable ams ams
    juju upgrade-charm --switch --channel=1.15/stable ams-node-controller ams-node-controller
    juju upgrade-charm --switch --channel=1.15/stable aar aar

If you have the streaming stack deployed you have to upgrade also the following charms:

    juju upgrade-charm --switch --channel=1.15/stable anbox-stream-gateway anbox-stream-gateway
    juju upgrade-charm --switch --channel=1.15/stable anbox-stream-agent anbox-stream-agent
    juju upgrade-charm --switch --channel=1.15/stable coturn coturn
    juju upgrade-charm --switch --channel=1.15/stable nats nats

Once the commands are executed, Juju will perform all necessary upgrade steps automatically.

After Juju has settled the workload status will be marked as `blocked` and the status will show `UA token missing`.

Anbox Cloud requires a valid Ubuntu Pro token including the Anbox Cloud entitlement, thus a full Ubuntu Pro or a Ubuntu Pro (Apps-only) subscription. You can get your Ubuntu Pro token on [Ubuntu Pro](https://ubuntu.com/pro). Please speak with your Canonical account representative.

When you have your Ubuntu Pro token, you can apply it for all relevant charms with the following commands:

    juju config ams ua_token=<your token>
    juju config lxd ua_token=<your token>
    juju config ams-node-controller ua_token=<your token>
    juju config aar ua_token=<your token>
    juju config anbox-stream-gateway ua_token=<your token>
    juju config anbox-stream-agent ua_token=<your token>
    juju config anbox-cloud-dashboard ua_token=<your token>


When the token is set Juju will continue to upgrade Anbox Cloud and install the latest version of the software components.

## Upgrade Debian packages

Some parts of Anbox Cloud are distributed as Debian packages coming from the [Anbox Cloud Archive](https://archive.anbox-cloud.io). In order to apply all pending upgrades, run the following commands on your machines:

    sudo apt update
    sudo apt upgrade

or apply the updates via [Landscape](https://landscape.canonical.com/) if available.

## Upgrade LXD image

LXD images are automatically being fetched by AMS from the image server once they are published.

Existing applications will be automatically updated by AMS as soon as the new image is uploaded. Watch out for new versions being added for any of the existing applications based on the new image version.

You can check for the status of an existing application by running

    amc application show <application id or name>

## Image server access

Starting with Anbox Cloud 1.9.0 you do not need to manually configure the `images.auth` configuration option in AMS anymore with your personal username and password. Authentication to the image server is now fully automated via your Ubuntu Pro subscription.

Existing deployments will be automatically migrated to the new image server endpoint `https://images.anbox-cloud.io/stable/` and authentication based on your Ubuntu Pro subscription will be setup during the AMS charm upgrade process as well. All you need to have configured for this is the Ubuntu Pro token on the AMS charm you set during deploying with the deploying command:

    juju config ams ua_token=<your token>

To verify the migration you can validate that the `images.url` configuration option in AMS is now changed to `https://images.anbox-cloud.io/stable/` and the 1.10 images are successfully downloaded.
