The Anbox Cloud Appliance comes with a command line tool that you can use to manage the appliance and its components.

Run `anbox-cloud-appliance --help` or `anbox-cloud-appliance <command> --help` to display usage information for the tool and its commands.

The available commands for the `anbox-cloud-appliance` tool are:

- `ams`

  Expose the AMS HTTPS service on the public endpoint of the machine on which the appliance is running. If you do this, you can [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774).
- `crashdump`

  Generate a tarball that contains debug information.
- `dashboard`

  Manage the web dashboard and access to it. By default, the dashboard is enabled and exposed, but you can disable it. You can also register new users for the web dashboard. See [Register a Ubuntu One account in Anbox Cloud Appliance](https://discourse.ubuntu.com/t/web-dashboard/20871#dashboard-access-appliance) for more information.
- `destroy`

  If you want to uninstall the Anbox Cloud Appliance, you must first destroy the deployment. Run this command before you uninstall the snap.

  [note type="caution" status="Warning"]This command resets the Anbox Cloud Appliance and destroys all data. Execution of the command cannot be undone.[/note]
- `gateway`

  Expose the HTTP API of the stream gateway and manage access to it. If the HTTP API is exposed, authenticated clients can connect to it. Authentication requires an access token that you can create with the `account create` subcommand. See [Access the stream gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784) for more information.
- `help`

  Display detailed information about a command.
- `init`

  Configure and initialise the Anbox Cloud Appliance. See [Start the initialisation process](https://discourse.ubuntu.com/t/install-appliance/22681#start-initialise) for more information.
- `monitor`

  Expose the monitoring dashboard. See [Monitor Anbox Cloud](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338).
- `status`

  Display status information for the Anbox Cloud Appliance.
- `upgrade`

  Upgrade the Anbox Cloud Appliance to the latest version. See [Upgrade the appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186) for more information.
