Addons can be used to customise the images used for the containers. An addon has [hooks](tbd#hooks) that are invoked at various points in the life cycle of a container. Addons are created independently and can be attached to individual applications.

See [Addons](https://discourse.ubuntu.com/t/addons/25293) for more information and a complete reference on addons. Follow the [Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284) tutorial to learn how to write a simple addon.

You can use addons to, for example:
- Enable SSH access for automation tools (see [Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284))
- Set up user-specific data when starting an application (see [How to restore data](https://discourse.ubuntu.com/t/example-back-up-data/25289#restore))
- Install additional tools in the container (see [Example: Install tools](https://discourse.ubuntu.com/t/example-install-tools/25288))
- Back up data when the container is stopping (see [Example: Back up data](https://discourse.ubuntu.com/t/example-back-up-data/25289))
- Configure the Android system before running the application (see [Example: Customise Android](https://discourse.ubuntu.com/t/example-customise-android/25290))
- Provide support for other platforms (see [Example: Emulate platforms](https://discourse.ubuntu.com/t/example-emulate-platforms/25291))

If you have used addons before Anbox Cloud 1.12, see the [migration guide](https://discourse.ubuntu.com/t/migrate-from-previous-addon-versions/25287) to update your addons to use the new hooks.
