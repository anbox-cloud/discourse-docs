The `monitor` command allows managing the monitoring dashboard. You can expose or unexpose the monitoring dashboard using the subcommands. By default, the monitoring dashboard is exposed.

    anbox-cloud-appliance monitor <subcommand>

## Subcommands

### `account`
Manages accounts that can access the monitoring dashboard.

    anbox-cloud-appliance monitor account <subcommand>

The `account` command can be used with two subcommands - `create` and `delete`:

The monitoring dashboard is configured with basic authentication and hence you need to create an account to access it. The `account create` command creates a new account to access the monitoring dashboard.

    anbox-cloud-appliance monitor account create <account-name> [--password=<value>] [--email=<email>] [--role=viewer|admin|editor] [options]

The following options can be used with the `account create` command:

|Option | Description |
|-------|-------------|
| `-e`, `--email <email>`|Email address of the monitor account|
| `-p`, `--password <value>`|Password of the monitor account|
| `-r`, `--role <value>`|Role of the monitor account can be either of these three options: viewer/admin/editor. The default role is viewer.|

The `account delete` command deletes the specified account and removes access to the monitoring dashboard for the mentioned account.

    anbox-cloud-appliance monitor account delete <account-name>

### `expose`
Enables external access to the monitoring dashboard.

    anbox-cloud-appliance monitor expose

### `unexpose`
Disables external access to the monitoring dashboard.

    anbox-cloud-appliance monitor unexpose
