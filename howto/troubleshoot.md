This section covers some of the most commonly encountered problems and gives instructions for resolving them.

## Initial setup

You might encounter the following issues while setting up your system.

### Juju hook installation failure

*Applies to: Anbox Cloud*

> Several Juju units of my deployment show `hook: installation failure`. Why?

You used the wrong Ubuntu Advantage token. Most likely, you used the Ubuntu Advantage for **Infrastructure** token that every user gets for free limited personal use.

To deploy Anbox Cloud, you need a commercial subscription for Ubuntu Advantage for **Applications**. Using a different token will result in a failed deployment. This failure is currently not recoverable.

### Socket permission error for `amc`

*Applies to: Anbox Cloud*

> I receive the following socket permission error when trying to use the `amc` command:
>
> ```text
> Post http://unix/1.0/images: dial unix /var/snap/ams/common/server/unix.socket: connect: permission denied
> ```
>
> What is wrong?

Most likely, you are trying to run the `amc` command as a user that is not part of the `ams` group. The socket has its ownership set to `root:ams`, so that only `root` or users that are part of the `ams` group are allowed to use the Unix domain socket.

By default, Anbox Cloud automatically adds the `ubuntu` user to the `ams` group during the installation. You can manually add further users to the `ams` group with the following command:

    sudo gpasswd -a <user_name> ams

To apply the change, you might need to log out and back in.

## Debugging container failures

The following issues should help you determining why your container failed.

### More information about failures

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> A container failed to start. Where can I find more information why it failed to start?

If a container fails to start, its status is set to `error`. AMS automatically fetches several log files from the container and makes them available for further inspection. From the log files, you can find out what went wrong. The reason is not always straightforward, because several things play into the container startup, for example, the application that the container is hosting or any installed addons.

See [View the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329) for instructions on how to access the container log files.

### Published application version not found

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> When launching a container for an application, I get an error about the "published application version not found". Why?

If you launch a container by only specifying the application ID and the application has no published version yet, you must explicitly specify the version that you want to launch or publish a version of the application. See [Launch application containers](https://discourse.ubuntu.com/t/launch-a-container/24327#application-containers) and [Publish application versions](https://discourse.ubuntu.com/t/update-an-application/24201#publish-application-versions) for more information.

## Creating applications

You might encounter the following issues when creating an application.

### Application manifest

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> Is there an automatic way to create a manifest for an application?

No. The application manifest describes necessary metadata on top of the APK, which AMS needs. You can simplify the manifest to only contain the `name` field, but you will lose a lot of control about how your application is being executed.

### No such file or directory

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> When creating an application, I get an error that there is “no such file or directory”. Why?

Due to Snap strict confinement, the folder or tarball file must be located in the home directory. There is no workaround for this requirement. The same requirement applies to addon creation.
