The `cluster` command allows management of manage cluster members for the Anbox Cloud Appliance. Using this command, you can join additional nodes to an existing installation or to remove existing nodes.

 See [How to join a machine to the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/29054) for more information.

 ## Usage

    anbox-cloud-appliance cluster <subcommand>

## Subcommands

### `add`
Adds a new member to the cluster

#### Usage

    anbox-cloud-appliance cluster add <member-name>

### `remove`
Removes a member from the cluster

#### Usage

    `anbox-cloud-appliance cluster remove <member-name> <options>`

#### Options

 `--force` to force remove members on non interactive terminals
