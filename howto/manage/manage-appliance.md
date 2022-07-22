The Anbox Cloud Appliance comes with a command line tool that you can use to manage the appliance and its components.

Run `anbox-cloud-appliance --help` or `anbox-cloud-appliance <command> --help` to display usage information for the tool and its commands.

The available commands for the `anbox-cloud-appliance` tool are:

- `ams`

  Expose the AMS HTTPS service on the public endpoint of the machine on which the appliance is running. If you do this, you can [control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774).
- `cluster`

  Manage cluster members for the Anbox Cloud Appliance by generating join tokens for new members or removing members from the cluster. See [How to join a machine to the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-join-a-machine-to-the-anbox-cloud-appliance/29054) for more information.
- `crashdump`

  Generate a tarball that contains debug information.
- `dashboard`

  Manage the web dashboard and access to it. By default, the dashboard is enabled and exposed, but you can disable it. You can also register new users for the web dashboard. See [Register a Ubuntu One account in Anbox Cloud Appliance](https://discourse.ubuntu.com/t/web-dashboard/20871#dashboard-access-appliance) for more information.
- `destroy`

  If you want to uninstall the Anbox Cloud Appliance, you must first destroy the deployment. Run this command before you uninstall the snap.

  [note type="caution" status="Warning"]This command resets the Anbox Cloud Appliance and destroys all data. Execution of the command cannot be undone.[/note]
- `gateway`

  Expose or unexpose the HTTP API of the stream gateway and manage access to it. If the HTTP API is exposed (which is the default), authenticated clients can connect to it. Authentication requires an access token that you can create with the `anbox-cloud-appliance gateway account create` command. See [How to access the stream gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784) for more information.
- `help`

  Display detailed information about a command.
- `init`

  Configure and initialise the Anbox Cloud Appliance. See [Initialise the appliance](tbd#initialise) for more information.
- `monitor`

  Expose or unexpose the monitoring dashboard, if you deployed it during the initialisation. By default, the monitoring dashboard is exposed.
- `status`

  Display status information for the Anbox Cloud Appliance.
- `upgrade`

  Upgrade the Anbox Cloud Appliance to the latest version. See [How to upgrade the appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186) for more information.
