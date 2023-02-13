A running container can be stopped using the `amc stop` command:

    amc stop <container id>

`<container id>` is the ID of the container that you want to stop.

By default, the `amc stop` command waits 5 minutes for a container to stop before the operation times out. If you want to specify a custom wait time, you can do so by using the `--timeout` option in the `amc stop` command.

    amc stop <container id> --timeout 10m
