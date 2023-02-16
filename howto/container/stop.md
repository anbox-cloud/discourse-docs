A running container can be stopped using the `amc stop` command:

    amc stop <container id>

`<container id>` is the ID of the container that you want to stop.

[note type="information" status="Important"]
Do not use the `lxd` command to stop a container. Always use the `amc` command instead. Anbox Cloud containers have their own lifecycle and using the `lxd` command to stop a container can cause the container to be out of sync.
[/note]

By default, the `amc stop` command waits 5 minutes for a container to stop before the operation times out. If you want to specify a custom wait time, you can do so by using the `--timeout` option in the `amc stop` command.

    amc stop <container id> --timeout 10m
