A running instance can be stopped using the `amc stop` command:

    amc stop <instance_id>

`<instance_id>` is the ID of the instance that you want to stop.

[note type="information" status="Important"]
Do not use the `lxc` command to manage an instance. Always use the `amc` command instead. In Anbox Cloud, instances have their own life cycle and using the `lxc` command to manage an instance can cause the instance to be out of sync.
[/note]

By default, the `amc stop` command waits 5 minutes for an instance to stop before the operation times out. If you want to specify a custom wait time, you can do so by using the `--timeout` option in the `amc stop` command.

    amc stop <instance_id> --timeout 10m
