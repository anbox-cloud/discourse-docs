The `monitor` command allows managing the monitoring dashboard. You can expose or unexpose the monitoring dashboard using the subcommands. By default, the monitoring dashboard is exposed.

## Usage

    anbox-cloud-appliance monitor <subcommand>

## Subcommands

### `account`
Manages accounts that can access the monitoring dashboard.

#### Usage

    anbox-cloud-appliance monitor account <subcommand>

#### Subcommands

##### `create`
Creates a new account to access the monitoring dashboard. The monitoring dashboard is configured with basic authentication and hence you need to create an account to access it.

###### Usage

    anbox-cloud-appliance monitor account create <account-name> [--password=<value>] [--email=<email>] [--role=viewer|admin|editor] [options]

###### Options

|Option | Description |
|-------|-------------|
| `-e`, `--email <email>`|Email address of the monitor account|
| `-p`, `--password <value>`|Password of the monitor account|
| `-r`, `--role <value>`|Role of the monitor account can be either of these three options: viewer/admin/editor. The default role is viewer.|

##### `delete`
Deletes the specified account and removes access to the monitoring dashboard for the mentioned account.

###### Usage

    anbox-cloud-appliance monitor account delete <account-name>

### `expose`
Enables external access to the monitoring dashboard.

#### Usage

    anbox-cloud-appliance monitor expose

### `unexpose`
Disables external access to the monitoring dashboard.

    anbox-cloud-appliance monitor unexpose
