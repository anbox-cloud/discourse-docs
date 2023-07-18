Hooks are scripts that automatically trigger actions based on an event performed in the container life cycle. A hook can be any executable file that is placed in the `hooks` directory of an addon or an application folder as long as its name is one of the following:

| Name                 | Description                                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------------|
| pre-start            | Executed **before** Android is started. If the hook fails to execute, the container fails to start due to an error.  |
| post-start           | Executed **after** Android is started. If the hook fails to execute, the container stops with an error.              |
| post-stop            | Executed **after** Android is stopped. If the container fails to start, this hook will not be invoked. If the hook fails to execute, the container stops with an error.  |
| install (deprecated) | DEPRECATED: Use `pre-start` instead. Executed during the application bootstrap when the addon is installed.          |
| prepare (deprecated) | DEPRECATED: Use `post-start` instead. Executed during the application bootstrap when Android is running.             |
| restore (deprecated) | DEPRECATED: Use `pre-start` instead. Executed before Android starts.                                                 |
| backup (deprecated)  | DEPRECATED: Use `post-stop` instead. Executed after Android shuts down.                                              |

A failed hook will cause the container to stop immediately and end up in an error state. In this case, [view the container logs](https://anbox-cloud.io/docs/howto/container/logs) to further investigate the causes of failure.

The following figure shows when the different hooks are executed in the life cycle of a container (base container or regular container).

![Hooks execution in the life cycle of a container|471x601](https://assets.ubuntu.com/v1/bc9b1291-addons-reference-hook-order.png)

<a name='env-variables'></a>
## Environment variables
When hooks are invoked, several environment variables are set to provide context to the addon.

The following variables are available:

| Name             | Description                                             | Possible values         |
|------------------|---------------------------------------------------------|-------------------------|
| `ADDON_DIR`      | Directory of the addon whose hook is currently running. |                         |
| `APP_DIR`        | Path to the Anbox application directory.                | `/var/lib/anbox/app`    |
| `ANBOX_DIR`      | Path to the Anbox directory.                            | `/var/lib/anbox`        |
| `ANDROID_ROOTFS` | Path to the Android RootFS.                             | `/var/lib/anbox/rootfs` |
| `BOOT_PACKAGE`   | Boot package of the APK.                                |                         |
| `CONTAINER_TYPE` | Type of container being run.                            | `regular` (container running an application or a raw image)<br/>`base` (container bootstrapping, thus creating or updating, an application)|
| `ANBOX_EXIT_CODE`| *`post-stop` hook only:* Exit code of the Anbox process.| `0` if no error occurred, otherwise set to the actual return code.|

<a name='hook-timeouts'></a>
## Hook timeouts
By default, all hooks are subject to a 5 minute timeout to avoid blocking a container for too long. The timeout can be configured through the `hooks.timeout` key in the addon or application manifest. For example:

```yaml
...
hooks:
  timeout: 15m
...
```

A hook that runs into a timeout exits with an error. Timeout values longer than 15 minutes are considered invalid.
