This section covers some of the most commonly encountered problems and attempts to resolve them.

### Several Juju units of my deployment show `hook: installation failure`. Why?

You use the wrong Ubuntu Advantage token. Most likely you used  the *Ubuntu Advantage for **Infrastructure*** which every use gets for free limited personal use.

In order to deploy Anbox Cloud you will need a commercial subscription for *Ubuntu Advantage for **Applications***. Using a different token will result in a failed deployment and is currently not recoverable.

### A container failed to start. Where can I find more information why it failed to start?

If a container failed to start its status is set to `error`. The AMS service automatically fetches several log files from the container and makes them available for further inspection. From the log files you can find out what went wrong. The reason is not always clear as several things play into the container startup, like the application the container is hosting, any installed addons etc.

See [View the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329) for more details on how to access the container log files.

### I receive a socket permission error when trying to use the `amc` command. What is wrong?

If you receive an error like

```text
Post http://unix/1.0/images: dial unix /var/snap/ams/common/server/unix.socket: connect: permission denied
```

after you tried to use the `amc` command line utility you're mostly likely trying to run the command as a user which is not part of the `ams` group. The socket has its ownership set to `root:ams` so that only `root` or users part of the `ams` group are allowed to use the Unix domain socket.

By default Anbox Cloud automatically adds the `ubuntu` user to the `ams` group on installation. You can manually add any further user to the `ams` group with a command like

```bash
$ sudo gpasswd -a <your user> ams
```

You make the change effective you may have to log out and back in.

### Is there an automatic way to create a manifest for an application?

No. The application manifest describes necessary meta data on top of the Android application package which AMS needs. You can simplify the manifest to only container the `name` field but then loose a lot of control about how your application is being executed.

### When launching a container for an application I get "Published application version not found". Why?

If you launch a container by only specifying the application ID and the application has no publish version yet, you need to explicitly specify the version you want to launch or publish a version of the application. See [Launch application containers](https://discourse.ubuntu.com/t/launch-a-container/24327#application-containers).

### When creating an application I get an error like “no such file or directory”. Why?

Due to Snap strict confinement, no matter which approaches you're going to take,  the folder or tarball file must be located home directory. The same applied to addon creation as well.

### Why I failed to dump logs to a single file with the  \`amc show-log\` command alongside with `>` operator?

Due to a [bug](https://bugs.launchpad.net/snapd/+bug/1835805) in snapd, redirecting stdout and stderr to a single file with **>** operator won't work. Because of this, when you want to dump logs to a single file via `amc show-log` command, you now have to work around it by using tee command like this:

```bash
$ amc show-log <container-id> system.log | tee system.log
```
