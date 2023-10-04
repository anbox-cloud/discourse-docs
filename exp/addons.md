Addons provide a way to extend and customise images in Anbox Cloud. Once you have created addons, you can create [hooks](https://discourse.ubuntu.com/t/28555) for them that are triggered based on events in the life cycle of an [instance](https://discourse.ubuntu.com/t/17763). You can create addons independently and later attach it to individual applications.

To create or update an addon, you need a specific file structure for the directory containing your addon files. In the directory where you created your addon files, also create the following:

- A file named `manifest.yaml`. See [Addon manifest](https://discourse.ubuntu.com/t/25293) to learn about valid keys in an addon manifest file.
- A directory named `hooks`. This directory must contain at least one executable file with a valid hook name.

Other files in the addon directory are bundled with the addon. They can be accessed in a hook by using the `$ADDON_DIR` [environment variable](https://discourse.ubuntu.com/t/hooks/28555#env-variables).

For example:

```bash
cat "$ADDON_DIR"/public_key.pem >> ~/.ssh/authorized_keys
```

To create an addon, you must provide the Anbox Management Client (AMC) with either of the following:
* The addon directory
* A tarball containing the required addon file structure
* A zip archive containing the required addon file structure

## Best practices

Addons must be created with careful consideration to not affect performance adversely. A good addon is light-weight and targeted for the necessary applications.

Here are some good practices to consider when creating addons:

### Keep addons light
Addons are executed synchronously. Any addon that performs long-running operations (for example, downloading large files, installing packages on regular instances or querying unresponsive services) will delay an application from starting.

[note type="information" Status="Tip"]Use the `INSTANCE_TYPE` environment variable to run only on the specified instance type. Doing so runs the code in your hooks only when necessary.[/note]

### Use global addons sparingly
Addons that are enabled for all applications can be useful, but they can add up quickly because whenever a global addon gets updated, a new application version is created. So if you use a global addon and that addon gets updated often, the disk capacity fills up fast.

Try to attach addons to individual applications unless you need a [global addon](https://discourse.ubuntu.com/t/how-to-enable-an-addon-globally/25285).

### Clean up your addons
For base instances, if your addon needs additional tools and dependencies during its installation, make sure you remove them afterwards (as part of the [`post-stop` hook](https://discourse.ubuntu.com/t/hooks/28555)). This will make your application image lighter and all instances launched from it will start faster.


## Related information

* [Tutorial: Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284)
* [How to use addons](https://discourse.ubuntu.com/t/managing-addons/17759)
