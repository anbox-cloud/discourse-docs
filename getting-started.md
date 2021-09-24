This guide provides the first steps to using Anbox Cloud. If you haven't installed Anbox Cloud, please refer to [Installing the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) or [Deploy Anbox Cloud with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) first.

## Access to AMS

For all subsequent commands using the `amc` tool to work you need to access the `ams/0` machine on a regular Anbox Cloud deployment. You can do this by opening an SSH session with the `juju` command:

    juju ssh ams/0

If you're running the Anbox Cloud Appliance instead, you can find the `amc` tool directly on the host and it's already set up to talk to the deployed AMS service.

Alternatively you can also install the `amc` command on your local Ubuntu-based development machine. See [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774) for more details.

## Ensure images are available

As a next step you can check that AMS has synchronised all images from the Canonical hosted image server. You can list all synchronised images with the `amc image ls` command:

```bash
+----------------------+-----------------------------+--------+----------+--------------+---------+
| ID                   | NAME                        | STATUS | VERSIONS | ARCHITECTURE | DEFAULT |
+----------------------+-----------------------------+--------+----------+--------------+---------+
| c4b4djkrorjohh948dfg | bionic:android11:arm64      | active | 1        | aarch64      | true    |
+----------------------+-----------------------------+--------+----------+--------------+---------+
| c4b4ev4rorjohh948dg0 | bionic:android10:arm64      | active | 1        | aarch64      | false   |
+----------------------+-----------------------------+--------+----------+--------------+---------+
```

If the images are not yet available, wait a few more minutes.

## Launch a container
If you simply want to get a raw container without any application for a specific Android version, you can do this via:

    amc launch -r bionic:android11:amd64

Or on ARM64:

    amc launch -r bionic:android10:arm64

You can watch the container starting with the following command:

    amc ls

Once it is up and running you can get a shell inside the container with:

    amc shell <container id>

See the information under [Work with containers](https://discourse.ubuntu.com/t/work-with-containers/24335) for more details.

## Create an application

You can create applications through the web-based dashboard or on the command line.

Both alternatives require you to provide the name and the [instance type](https://discourse.ubuntu.com/t/instances-types-reference/17764) of the application. If you want to run a specific Android application, you need to provide its APK.

> **Hint**: If your application requires the use of a GPU for rendering and video encoding, select an instance type with GPU support like `g2.3`. For other instance types, the container will use a GPU if available or software encoding otherwise.

### Create an application through the web dashboard

The web dashboard is available if you installed [Anbox Cloud with the streaming stack](https://discourse.ubuntu.com/t/install-with-juju/17744) or the [Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681). See [Use the web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871) for more information about the dashboard.

To create an application through the web dashboard, open `https://<your-machine-address>/applications` in your browser. Click **Add Application** and enter the required information. If you want to run a specific Android application, upload its APK.

### Create an application on the command line

To create and manage an application from the command line, use `amc`.

You must provide a `manifest.yaml` file for your application. In its simplest form, the manifest looks like this:

```yaml
name: com.my.game
instance-type: a2.3
```

It defines the name of the application and which instance type the application should use. The manifest can also contain more advanced configuration like [Addons](https://discourse.ubuntu.com/t/managing-addons/17759), permissions and others. You can find more details about the manifest format and the available instance types in the [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197) and [Instance types](https://discourse.ubuntu.com/t/instances-types-reference/17764) sections.

To create an application, place the `manifest.yaml` file in a directory of your choice. If you want to run a specific Android application, place its APK in the same directory. Then run the following command, replacing */path/to/manifest/directory/* with the path to your directory:

    amc application create /path/to/manifest/directory/

The tool will now run through a bootstrap process for the application to allow for faster boot times of the application later on.

You can use the `amc application show <app name>` command to display the status of your application. To continually monitor the progress of the application, enter the following command:

    watch -n 1 amc application ls

When processing is done, you can start a container for your new application by launching the application:

    amc launch <app name>
