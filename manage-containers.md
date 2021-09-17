Containers are the center piece of the Anbox Cloud stack. A single container full Android system. Each container is hosted on a cluster of multiple nodes provided by the underlying LXD container hypervisor. The base for a container is an application which is described in [Application Management](https://discourse.ubuntu.com/t/managing-applications/17760) in more detail.

## Data stored in Containers

All containers in Anbox Cloud are ephemeral. That means that as soon as a container is stopped all of its data is gone. Anbox Cloud **DOES NOT** backup any data from the Android or the outer Ubuntu container. Backup and restore of data needs to be implemented separately via the the use of the `backup` and `restore` hooks of [addons](https://discourse.ubuntu.com/t/managing-addons/17759/2).

## Possible Container Status

Throughout its lifetime a container can have different status values depending on the state it's currently in.

Status            |  Description
----------------|------------
`created`     | AMS has created an internal database object for the container and will schedule the container onto a suitable LXD node next.
`prepared` | AMS has decided on which LXD node the container should be placed on.
`started` | The container was started and is now booting. During the boot sequence possible hooks are executed. Only when all hooks are executed the container will switch to `running`
`running` | The container is fully up an running
`stopped` | The container is fully stopped and will be remove next by AMS
`deleted` | The container is deleted and will be removed from the AMS database soon
`error` | An error occurred while processing the container. The container is stopped and further information about the error can be shown via `amc show <container id>`

## List Active Containers

To get an overview of which and how many containers are currently running on an Anbox Cloud deployment you can run the following command:

```bash
$ amc ls
+----------------------+----------------+---------+---------+------+---------------+------------------------+
|          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
| bdpaqaqhmss611ruq6kg |     candy      | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
|                      |                |         |         |      |               | 10.103.46.41:10000/tcp |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
```

This will list all containers with their status and additional information, for example on which LXD node in the cluster the containers are running on.

## Launch a Container

Launching a container is normally done by another service over the REST API the AMS service provides. However the `amc` utility allows launching a container manually for experiments or development purposes. By default the container will run headless and does not provide an entry point for a user to connect. Containers can be launched for either an registered application or image.

When launching a container from an application or an image directly, a regular container will execute the following steps in order upon its creation.

  * Configure network interface and gateway
  * Install addons on demand if [lauching a raw container](#heading--raw-containers)
    * Execute the `install` hook provided by the installed addons
  * Expose services on demand
  * Execute the `restore` hook provided by the installed addons before launching Android container
  * Launch Android container
  * Execute the `prepare` hook provided by the installed addons if [lauching a raw container](#heading--raw-containers)
  * Execute the `backup` hook provided by the installed addons after the container is terminated

![container-launch|690x401](upload://exw6GWcRvMzkIztcUIrizFg0oJz.png)

The whole launch process will be successful only if all of the above steps succeed.

When something went wrong during the container launch process, the status of the container changes to `error` status. You can [show all available logs](#heading--show-container-logs) from the container for diagnosing the root cause of the problem.

### Launch Application Containers

Launching a container for an registered application can be achieved with the
following command:

```bash
$ amc launch <application id>
```

As argument you have to provide the ID of the application you want to launch. You can
list all available applications with the following command:

```bash
$ amc application ls
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
|          ID          |      NAME      | INSTANCE TYPE | ADDONS | PUBLISHED | STATUS |    LAST UPDATED     |
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
| bdp7kmahmss3p9i8huu0 |      candy     | a2.3          | ssh    | false     | ready  | 2018-08-14 08:44:41 |
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
```


If the application you want to launch a container for is not yet published (see [Application Management](https://discourse.ubuntu.com/t/managing-applications/17760) for more details) the launch command will fail as it will only allow launching a container for a published application. However you can still get around this by specifying a specific version of an application:

```bash
$ amc launch --application-version=0 bcmap7u5nof07arqa2ag
```

<h3 id="heading--raw-containers">Launch Raw Containers</h3>

The command for launching a container from an image is:

```bash
$ amc launch --raw <image id>
```

As argument you have to provide the ID or name of the image you want to launch a container for See [Image Management](https://discourse.ubuntu.com/t/managing-images/17758) for more details about how images are managed by AMS.

You can list all available images with the following command:

```bash
$ amc image ls
+----------------------+---------+--------+----------+----------------------+
|          ID          |  NAME   | STATUS | VERSIONS |       USED BY        |
+----------------------+---------+--------+----------+----------------------+
| bh01n90j1qm6416q0ul0 | default | active | 1        |                      |
+----------------------+---------+--------+----------+----------------------+
```

### Launch Container on a Specific Node

By default every container is scheduled by AMS onto a LXD node. Alternatively it is possible to launch a container directly on a specific node:

```bash
$ amc launch --node=lxd0 bcmap7u5nof07arqa2ag
```

> **Note:** AMS will still verify that the selected node has enough resources to host the container. If not the container will fail to launch.

### Launch Container with different Anbox Platform

By default every container starts with the `null` platform (see [Anbox Platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)). The selected platform cannot be changed at runtime and has to be selected when the container is created. For example a container can be launched with the `swrast` platform like this:

```bash
$ amc launch -p swrast <application-id>
```

If you have build your own platform named `foo` and built it via an addon into the container images, you can launch a container with the platform the same way:

```bash
$ amc launch -p foo <application-id>
```

## Wait for a Container

When launching a container, the container should not be considered started until it reaches the running state. Sometimes if you want to interact with the container by `amc shell` command for example, you need to wait until the container reaches a "running" status.

With `amc wait` command, it enables to wait for a container to reach a specific condition. If the condition is not satisfied within the specified time (5 minutes by default), a timeout error will be returned by AMS.

The supported conditions for a container are as follows:

Name            |  Value
----------------|------------
`app`           |  Application name or ID
`type`          |  Container type, possible values: "base", "regular"
`node`          |  Node on which the container runs
`status`        |  Container status, possible values: "created", "prepared", "started", "stopped", "running", "error", "deleted", "unknown"

E.g. to wait for the container to reach state "running":

```bash
$ amc wait -c status=running bdpaqaqhmss611ruq6kg
```


## Expose Services on a Container

AMS allows a container to expose a service to the outer network. For that it provides a feature called container services which let you define a port to expose on the container endpoints. The set of services to expose is defined when the container is launched. For example the following command exposes port `22` on the containers private endpoint:

```bash
$ amc launch -s tcp:22 bdp7kmahmss3p9i8huu0
```

> **Note:** The specified port is only exposed on the IP address the container itself has. As the     container is normally not accessible from outside the LXD node it is running on AMS sets up port forwarding rules on the node and maps the specified port to one in a higher port range (`10000 - 110000`).

The list of containers will now show the container and the exposed port `22`:

```bash
$ amc ls
+----------------------+----------------+---------+---------+------+---------------+------------------------+
|          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
| bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
|                      |                |         |         |      |               | 10.103.46.41:10000/tcp |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
```

As describe above the port `22` is only exposed on the IP address the container itself has.
Next to that it was mapped onto port `10000` on the address of the LXD node `lxd0`.

To help identifying services later on you can give them a name. For the example above we can simply name the service `ssh`:

```bash
$ amc launch -s ssh:tcp:22 bdp7kmahmss3p9i8huu0
```

This will help to identify which endpoint is used for which service:

```bash
$ amc ls
+----------------------+----------------+---------+---------+------+---------------+----------------------------+
|          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS            |
+----------------------+----------------+---------+---------+------+---------------+----------------------------+
| bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | ssh:192.168.100.2:22/tcp   |
|                      |                |         |         |      |               | ssh:10.103.46.41:10000/tcp |
+----------------------+----------------+---------+---------+------+---------------+----------------------------+
```

If we want instead exposing the service on the public endpoint of an LXD node we have to slightly change the service definition when the container is launched:

```bash
$ amc launch -s +tcp:22 bdp7kmahmss3p9i8huu0
```

Notice the `+` in front of the port definition. This tells AMS to expose the service on the public endpoint of the LXD node the container is scheduled onto. The container list then shows the public address of the node the container is running on in the list of endpoints:

```bash
$ amc ls
+----------------------+----------------+---------+---------+------+---------------+------------------------+
|          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
| bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
|                      |                |         |         |      |               | 147.3.23.6:10000/tcp   |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
```

## Delete a Container

A container can be deleted which will cause any connected user to be disconnected immediately. The following command deletes a single container:

```bash
$ amc delete bcqbicqhmss0448iie2g
```

The ID given is the one of the container you want to delete.

In some cases it is helpful to delete all containers currently available.
The `amc` command provides a `--all` flag for this, but be careful with this!

```bash
$ amc delete --all
```

## Access a Container

In some cases it might be necessary to access an individual container for debugging reasons. The `amc` command provides simple shell access to any container managed by AMS. To access a specific container you only need its id:

```bash
$ amc shell <id>
```

This will open a bash shell inside the container. To access the nested Android container you need to use the `anbox-shell` command inside the new shell. If you combined the `anbox-shell` command with `amc exec` you can get direct access to the Android container via

```bash
$ amc exec <id> -- anbox-shell
```

If you only want to watch the Android log output you can use the following command

```bash
$ amc exec <id> -- anbox-shell logcat
```

`amc shell` and `amc exec` open various possibilities for automation use cases. Please see the help output of the commands for further details.

<h2 id="heading--show-container-logs"> Show Container Logs </h2>

In case that a container fails to start or a runtime error occurs, AMS will collect relevantlog files from the container and make them available for inspection.

Available logs can be listed with the `amc` command:

```bash
$ amc show bh03th0j1qm6416q0v30
id: bh03th0j1qm6416q0v30
name: ams-bh03th0j1qm6416q0v30
status: error
node: lxd0
created_at: 1970-01-01T00:00:00Z
application:
  id: bh03tgoj1qm6416q0v2g
network:
  address: 192.168.100.2
  public_address: 10.226.4.63
  services: []
stored_logs:
- container.log
- system.log
- android.log
error_message: 'Failed to install application com.canonical.candy: exit status 1'
```

The container in this example failed to install the application as indicated by the `error_message` field. There are three log files being stored which can be shown as follows:

```bash
$ amc show-log bh03th0j1qm6416q0v30 system.log
-- Logs begin at Thu 2019-01-17 08:37:56 UTC, end at Thu 2019-01-17 08:38:58 UTC. --
Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd-journald[38]: Journal started
Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd-journald[38]: Runtime journal (/run/log/journal/2c8dee797148423b8f8987009ee28eab) is 8.0M, max 99.6M, 91.6M free.
Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd[1]: Starting Flush Journal to Persistent Storage...
....
Jan 17 08:38:57 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:57 Extracting application package ...
Jan 17 08:38:58 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:58 Waiting for Android container
Jan 17 08:38:58 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:58 Installing application com.canonical.candy from app.apk ...
```

> **Note:** AMS does not support runtime log collection. Logs are currently only being collected from a container which failed to start or had an error at runtime.

## Filter Containers

`amc ls` accepts `--filter` flag to filter and group containers.

The filter flag accepts a key-value pair as the filtering value. The following attributes are valid keys:

Name            |  Value
----------------|------------
`app`           |  Application name or ID
`type`          |  Container type, possible values: "base", "regular"
`node`          |  Node on which the container runs
`status`        |  Container status, possible values: "created", "prepared", "started", "stopped", "running", "error", "deleted", "unknown"


To list all regular containers:

```bash
$ amc ls --filter type=regular
```

If you need to apply multiple filters, you could pass multiple flags:

```bash
$ amc ls --filter type=regular --filter node=lxd0
```

This will query all regular containers that are placed on the node with the name `lxd0`.
