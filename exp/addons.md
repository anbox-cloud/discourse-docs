Addons provide a way to extend and customise images in Anbox Cloud. Once you have created addons, you can create [hooks](https://discourse.ubuntu.com/t/28555) for them that are triggered based on events in the container life cycle. You can create addons independently and later attach it to individual applications.

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

Addons must be created with careful consideration to not affect performance adversely. A good addon is light-weight and are targeted for the necessary applications. 

Here are some good practices to consider when creating addons:

### Keep addons light
Addons are executed synchronously. Any addon that performs long-running operations (for example, downloading large files, installing packages on regular containers or querying unresponsive services) will delay an application from starting.

[note type="information" Status="Tip"]Use the `CONTAINER_TYPE` environment variable to run only the necessary code in your hooks.[/note]

### Use global addons sparingly
Addons that are enabled for all applications can be useful, but they can add up quickly. Try to attach addons to individual applications unless you need a global addon and you are sure that it won't slow down containers.

### Clean up your addons
If your addon needs additional tools and dependencies during its installation, make sure you remove them afterwards. This will make your addon lighter and all applications using it will start faster.


## Related information

* [Tutorial: Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284)
* [How to use addons](https://discourse.ubuntu.com/t/managing-addons/17759)
