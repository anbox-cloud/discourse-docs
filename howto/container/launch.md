You can launch a container for a registered application or image (see [Application containers vs. raw containers](https://discourse.ubuntu.com/t/managing-containers/17763#application-vs-raw)), either by using the `amc` tool or through another service over the REST API that the AMS service provides.

By default, the container will run headless. See [How to access a container](https://discourse.ubuntu.com/t/container-access/17772) for instructions on how to access it for debugging purposes, and [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769) for information about the streaming stack.

<a name="application-containers"></a>
## Launch application containers

Launching a container for a registered application can be achieved with the
following command:

    amc launch <application id>

As argument, provide the ID of the application that you want to launch. You can
list all available applications with the `amc application ls` command:

```bash
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
|          ID          |      NAME      | INSTANCE TYPE | ADDONS | PUBLISHED | STATUS |    LAST UPDATED     |
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
| bdp7kmahmss3p9i8huu0 |      candy     | a4.3          | ssh    | false     | ready  | 2018-08-14 08:44:41 |
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
```
If the application for which you want to launch a container is not yet published (see [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201) for more details), the launch command will fail as it only allows launching a container for a published application. However, you can work around this by specifying a specific version of an application:

    amc launch --application-version=0 bcmap7u5nof07arqa2ag

<a name="raw-containers"></a>
## Launch raw containers

The command for launching a raw container from an image is:

    amc launch --raw <image id>

As argument, provide the ID or name of the image for which you want to launch a container. See [Provided images](https://discourse.ubuntu.com/t/provided-images/24185) for a list of images that are available in Anbox Cloud.

You can also list all available images with the `amc image ls` command:

```bash
+----------------------+---------+--------+----------+----------------------+
|          ID          |  NAME   | STATUS | VERSIONS |       USED BY        |
+----------------------+---------+--------+----------+----------------------+
| bh01n90j1qm6416q0ul0 | default | active | 1        |                      |
+----------------------+---------+--------+----------+----------------------+
```

## Launch a container on a specific node

By default, every container is scheduled by AMS onto a LXD node. Alternatively, you can launch a container directly on a specific node:

    amc launch --node=lxd0 bcmap7u5nof07arqa2ag

[note type="information" status="Note"]AMS will still verify that the selected node has enough resources to host the container. If not, the container will fail to launch.[/note]

## Launch a container with a different Anbox platform

By default, containers start with the `webrtc` platform if `--enable-graphics` is specified and with the `null` platform otherwise (see [Anbox platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)). To select a different platform, specify it with the `-p` flag. The selected platform cannot be changed at runtime and must be selected when the container is created. For example, you can launch a container with the `webrtc` platform like this:

    amc launch -p webrtc <application-id>

If you have built your own platform named `foo` and you built it via an addon into the container images, you can launch a container with the platform the same way:

    amc launch -p foo <application-id>

## Launch a container with development mode enabled

You can launch containers with additional development features turned on. This development mode must be enabled when a container is launched, and it cannot be turned off afterwards. You should never enable development mode for containers used in a production environment.

To launch a container with development mode enabled, add the `--devmode` flag to the launch command:

    amc launch --devmode <application-id>
