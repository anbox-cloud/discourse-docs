When a container is either initialised with the `amc init` (see [Create a container](https://anbox-cloud.io/docs/howto/container/launch)) command or stopped with the `amc stop` command (See [Stop a container](TBD)), you must start it explicitly with the `amc start` command:

    amc start <container id>

`<container id>` is the ID of the container that you want to start.

By default, the `amc start` command waits 5 minutes for a container to run before the operation times out. When starting a container, you can specify a custom wait time with the `--timeout` option.

    amc start <container id> --timeout 10m

When the `--no-wait` option is specified, the `amc start` command exits immediately after the container starts and will not wait till it is running.

    amc start <container id> --no-wait

[note type="information" status="Important"]
Starting a container that has stopped with an error status is is not allowed. Doing so would cause the `amc start` command to fail.
[/note]
