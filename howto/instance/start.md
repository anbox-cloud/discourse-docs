When an instance is either initialised with the `amc init` (see [Create an instance](https://discourse.ubuntu.com/t/24327)) command or stopped with the `amc stop` command (See [Stop an instance](https://discourse.ubuntu.com/t/33925)), you must start it explicitly with the `amc start` command:

    amc start <instance_id>

`<instance_id>` is the ID of the instance that you want to start.

[note type="information" status="Important"]
Do not use the `lxc` command to manage an instance. Always use the `amc` command instead. Anbox Cloud instances have their own life cycle and using the `lxc` command to manage an instance can cause the instance to be out of sync.
[/note]

By default, the `amc start` command waits 5 minutes for an instance to run before the operation times out. When starting an instance, you can specify a custom wait time with the `--timeout` option.

    amc start <instance_id> --timeout 10m

When the `--no-wait` option is specified, the `amc start` command exits immediately after the instance starts and will not wait till it is running.

    amc start <instance_id> --no-wait

[note type="information" status="Important"]
Starting an instance that has stopped with an error status is is not allowed. Doing so would cause the `amc start` command to fail.
[/note]
