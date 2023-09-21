Before you upgrade the Anbox Cloud Appliance, you should make sure all packages on the machines that are part of the deployment are up-to-date. To do so, run the following commands on each machine:

    sudo apt update
    sudo apt upgrade

The Anbox Cloud Appliance includes an `upgrade` command which will perform all relevant upgrade steps to a newer version of the appliance.  First, run `anbox-cloud-appliance status` to check if an update is available:

    status: ready
    update-available: true
    reboot-needed: false
    version: 1.19.0

[note type="information" status="Important"]While the upgrade process is active API endpoints and the dashboard will not be available. Anbox Cloud instances will stay active and existing streams will also not be interrupted.[/note]

In the command output above the `update-available` field indicates an update is available. The upgrade process can now be initiated by running the `upgrade` command:

    anbox-cloud-appliance upgrade

The appliance will now perform all necessary steps to upgrade to the newer available version. 

[note type="information" status="Note"]In case automatic updates are disabled for applications, Anbox Management Service (AMS) cannot update the application. See [Configure automatic application updates](https://discourse.ubuntu.com/t/24201#configure-automatic-updates) to enable automatic updates or to manually update the applications.[/note]

You can watch the upgrade progress on the web interface:

![Upgrade the appliance|690x435](https://assets.ubuntu.com/v1/1093e239-update_appliance.png)

 or with the `anbox-cloud-appliance status` command you used above:

    status: maintenance
    progress: 40
    update-available: false
    reboot-needed: true
    version: 1.19.1

When the upgrade has finished the appliance is again available for regular use.
