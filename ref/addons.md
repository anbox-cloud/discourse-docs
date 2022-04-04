Addons provide a way to extend and customise images in Anbox Cloud. See [Use addons](https://discourse.ubuntu.com/t/managing-addons/17759) and the [Creating an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284) tutorial for instructions on how to use them.

<a name='file-structure'></a>
## File structure
When creating or updating an addon, the directory containing your addon files must contain:

- A file named `manifest.yaml`.
- A directory named `hooks`. This directory must contain at least one executable file with a valid hook name (see [Hooks](#hooks) below).

Other files in the addon directory are bundled with the addon. They can be accessed in a hook by using the `$ADDON_DIR` [environment variable](#env-variables)). For example:
```bash
cat "$ADDON_DIR"/public_key.pem >> ~/.ssh/authorized_keys
```

To create the addon, you must provide `amc` with either the directory or a tarball containing the same file structure.

<a name='manifest'></a>
## Addon manifest

The following table lists the valid keys in an addon manifest:

| Name                  | Type         | Description                                                                                                                                                                                                                   | Allowed values                        |
|-----------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `name`                | string       | Name of the addon. Can be used to reference the addon.                                                                                       | All characters except for the following: `< > : " / \ \| ? *`, as well as space. |
| `description`         | string       | Description of the addon.                                                                                                                                                                                                     |                                       |
| `provides`            | object       | Additional capabilities that this addon provides to the container. See individual items for details.                                                                                                                          |                                       |
| `provides.abi-support`| string array | Tells AMS that this addon adds support for the given architecture even if the application doesn't support it natively. Use this when your addon brings instruction translation or provides libraries for other architectures. | `arm64-v8a`, `armeabi-v7a`, `armeabi` |


<a name='env-variables'></a>
## Environment variables
When addon hooks are invoked, several environment variables are set to provide context to the addon.

The following variables are available:

| Name             | Description                                             | Possible values         |
|------------------|---------------------------------------------------------|-------------------------|
| `ADDON_DIR`      | Directory of the addon whose hook is currently running. |                         |
| `ANBOX_DIR`      | Path to the Anbox directory.                            | `/var/lib/anbox`        |
| `ANDROID_ROOTFS` | Path to the Android RootFS.                             | `/var/lib/anbox/rootfs` |
| `BOOT_PACKAGE`   | Boot package of the APK.                                |                         |
| `CONTAINER_TYPE` | Type of container being run.                            | `regular` (container running an application or a raw image)<br/>`base` (container bootstrapping, thus creating or updating, an application)|
| `ANBOX_EXIT_CODE`| *`post-stop` hook only:* Exit code of the Anbox process.| `0` if no error occurred, otherwise set to the actual return code.|

<a name='hooks'></a>
## Hooks
An addon is a collection of hooks that are invoked at different points in time in the life cycle of a container. A hook can be any executable file as long as its name is one of the following:


| Name                 | Description                                                                                                |
|----------------------|------------------------------------------------------------------------------------------------------------|
| pre-start            | Executed **before** Android is started. If the hook crashes, the container fails to start.                 |
| post-start           | Executed **after** Android is started. If the hook crashes, the container stops.                           |
| post-stop            | Executed **after** Android is stopped. If the container crashes, this hook might not be invoked.           |
| install (deprecated) | DEPRECATED: Use `pre-start` instead. Executed during the application bootstrap when the addon is installed.|
| prepare (deprecated) | DEPRECATED: Use `post-start` instead. Executed during the application bootstrap when Android is running.   |
| restore (deprecated) | DEPRECATED: Use `pre-start` instead. Executed before Android starts.                                       |
| backup (deprecated)  | DEPRECATED: Use `post-stop` instead. Executed after Android shuts down.                                    |

The following figure shows when the different hooks are executed in the life cycle of a container (base container or regular container).

![Hooks execution in the life cycle of a container|471x601](https://assets.ubuntu.com/v1/bc9b1291-addons-reference-hook-order.png)

### Hook timeouts
All hooks are subject to a 5 minute timeout to avoid blocking a container for too long.

A hook that runs into a timeout exits with an error.
