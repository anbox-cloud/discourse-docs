Addons provide a way to extend and customise images in Anbox Cloud. You can create [hooks](https://discourse.ubuntu.com/t/28555) for addons that are triggered based on events in the container life cycle.

You can create addons independently and later attach it to individual applications.
Creating or updating an addon requires a specific file structure. The directory containing your addon files must contain:

- A file named `manifest.yaml`.
- A directory named `hooks`. This directory must contain at least one executable file with a valid hook name.

Other files in the addon directory are bundled with the addon. They can be accessed in a hook by using the `$ADDON_DIR` [environment variable](https://discourse.ubuntu.com/t/hooks/28555#env-variables). For example:
```bash
cat "$ADDON_DIR"/public_key.pem >> ~/.ssh/authorized_keys
```

To create an addon, you must provide `amc` with either of the following:
* The directory 
* A tarball containing the same file structure
* A zip archive containing the same file structure

<a name='manifest'></a>
## Addon manifest

The following table lists the valid keys in an addon manifest:

| Name                  | Type         | Description    | Allowed values  |
|-----------------------|--------------|----------------|-----------------|
| `name`                | string       | Name of the addon. Can be used to reference the addon.| All characters except for the following: `< > : " / \ \| ? *`, as well as space. |
| `description`         | string       | Description of the addon.   |        |
| `provides`            | object       | Additional capabilities that this addon provides to the container. See individual items for details.          |             |
| `provides.abi-support`| string array | Tells AMS that this addon adds support for the given architecture even if the application doesn't support it natively. Use this when your addon brings instruction translation or provides libraries for other architectures. | `arm64-v8a`, `armeabi-v7a`, `armeabi` |
| `hooks.timeout`| string | Execution timeout for each hook that is included in an addon. By default, the timeout is set to 5 minutes. It can be extended to up to 15 minutes. Configure this option if a hook takes longer than 5 minutes to finish. | `10m` |


## Related information

* [Tutorial: Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284)
* [How to use addons](https://discourse.ubuntu.com/t/managing-addons/17759)