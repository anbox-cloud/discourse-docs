Addons provide a way to extend and customise images in Anbox Cloud. See [How to use addons](https://discourse.ubuntu.com/t/managing-addons/17759) and the [Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284) tutorial for instructions on how to use them.

<a name='file-structure'></a>
## File structure
When creating or updating an addon, the directory containing your addon files must contain:

- A file named `manifest.yaml`.
- A directory named `hooks`. This directory must contain at least one executable file with a valid hook name (see [Hooks](#hooks) below).

Other files in the addon directory are bundled with the addon. They can be accessed in a hook by using the `$ADDON_DIR` [environment variable](tbd#env-variables)). For example:
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
| `hooks.timeout`| string | Execution timeout for each hook that is included in an addon. By default, the timeout is set to 5 minutes. It can be extended to up to 15 minutes. Configure this option if a hook takes longer than 5 minutes to finish. | `10m` |


<a name='hooks'></a>
## Hooks
An addon is a collection of hooks that are invoked at different points in time in the life cycle of a container. See [Hooks](tbd) for more details about the usage of hooks in an addon.
