Addons are used to customize the images used for the containers. An addon has *hooks* that are
invoked at various points in the lifecycle of a container.

Addons are created independently, and can be attached to individual applications.

You can use addons to:
- Enable SSH access for automation tools
- Setup user specific data when starting an application
- Backup data when the container is stopping
- Installing additional tools in the container
- Configure the Android system before running the application
- And much more...

Follow the [tutorial](tutorial here) to learn how to write a simple addon.

See more advanced use cases on the [how-to guides](how-to here)

A complete reference on addons can be found on the [reference page](reference here)

If you have been using addons before 1.12, see the [migration guide](migration guide here) to move to
the new hooks