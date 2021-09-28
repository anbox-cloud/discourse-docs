This document provides a complete reference on addons in Anbox Cloud.

<a id='file-structure'></a>
## File structure
When creating or updating an addon, the directory containing your addon files **MUST**:

- Contain a file named `manifest.yaml`.
- Contain a directory named `hooks`.
    - `hooks` **MUST** contain at least one executable file with a valid hook name (see *Hooks* below)

Other files are bundled with the addon and can be accessed in hooks under `$ADDON_DIR` (see [*Environment variables*](#env-variables)).
```bash
cat "$ADDON_DIR"/public_key.pem >> ~/.ssh/authorized_keys
```

You can also provide `amc` with a tarball containing the same file structure

<a id='manifest'></a>
## Addon manifest

The following table references the valid keys in an addon manifest.

| Name                 | Type         | Description                                                                                                                                                                                                                   | Allowed values                        |
|----------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| name                 | string       | Name of the addon. Can be used to reference the addon. A few special characters are not allowed: ‘< > : " / \ \| ? *’, as well as space.                                                                                      |                                       |
| description          | string       | Description of the addon.                                                                                                                                                                                                     |                                       |
| provides             | object       | Additional capabilities that this addon provides to the container. See individual items for details.                                                                                                                          |                                       |
| provides.abi-support | string array | Tells AMS that this addon adds support for the given architecture even if the application doesn't support it natively. Use this when your addon brings instruction translation or provides libraries for other architectures. | `arm64-v8a`, `armeabi-v7a`, `armeabi` |


<a id='env-variables'></a>
## Environment variables
When addon hooks are invoked, several environment variables are set to provide context to the addon.

The following variables are available.

| Name            | Description                                                                                                                                                                      | Possible values         |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| ADDON_DIR       | Directory of the addon whose hook is currently running                                                                                                                           |                         |
| ANBOX_DIR       | Path to the Anbox directory                                                                                                                                                      | `/var/lib/anbox`        |
| ANDROID_ROOTFS  | Path to the Android RootFS                                                                                                                                                       | `/var/lib/anbox/rootfs` |
| BOOT_PACKAGE    | Boot package of the APK                                                                                                                                                          |                         |
| CONTAINER_TYPE  | Type of container being run.</br>    - `regular`: container running an application or a raw image</br>  - `base`: container bootstrapping (aka creating/updating) an application | `regular`, `base`       |
| ANBOX_EXIT_CODE | `post-stop` hook only. Exit code of the Anbox process. `0` if no error occurred, otherwise set to the actual return code.                                                        |                         |

<a id='hooks'></a>
## Hooks
An addon is a collection of hooks that are invoked at different point in time in the lifecycle of a container. A hook can be any executable file as long as its name is one the following:


| Name                 | Description                                                                                                |
|----------------------|------------------------------------------------------------------------------------------------------------|
| pre-start            | Executed **before** Android is started. If the hook crashes, the container fails to start.                 |
| post-start           | Executed **after** Android is started. If the hook crashes, the container stops.                           |
| post-stop            | Executed **after** Android is stopped. If the container crashes, this hook might not be invoked.           |
| install (deprecated) | DEPRECATED: use `pre-start` instead. Executed when the addon is installed during the application bootstrap |
| prepare (deprecated) | DEPRECATED: use `post-start` instead. Executed during the application bootstrap when Android is running    |
| restore (deprecated) | DEPRECATED: use `pre-start` instead. Executed before Android starts                                        |
| backup (deprecated)  | DEPRECATED: use `post-stop` instead. Execute after Android shuts down                                      |

The following figure represents the moment in time in the lifecycle of a container where the different hooks are executed
![alt text](../images/addons-reference-hook-order.svg)

### Hook timeouts
All hooks are subject to a **5 minutes** timeout to avoid blocking a container for too long.  
A hook that runs into a timeout exits with an error.
