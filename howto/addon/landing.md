Addons can be used to customise the images used for the containers. An addon has [hooks](tbd#hooks) that are invoked at various points in the life cycle of a container. Addons are created independently and can be attached to individual applications.

See [Addons](tbd) for more information and a complete reference on addons. Follow the [Creating an addon](tutorial here) tutorial to learn how to write a simple addon.

You can use addons to, for example:
- Enable SSH access for automation tools (see [Creating an addon](tbd))
- Set up user-specific data when starting an application
- Install additional tools in the container (see [Example: Install tools](tbd))
- Back up data when the container is stopping (see [Example: Back up data](tbd))
- Configure the Android system before running the application (see [Example: Customise Android](tbd))
- Provide support for other platforms (see [Example: Emulate platforms](tbd))

If you have used addons before Anbox Cloud 1.12, see the [migration guide](migration guide here) to update your addons to use the new hooks.
