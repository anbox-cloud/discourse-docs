Instances are the centre piece of the Anbox Cloud stack. Every time you launch an application or an image, Anbox Cloud creates an instance for it. Every instance provides a full Android system.

All instances in Anbox Cloud are ephemeral, which means that as soon as an instance is stopped, all of its data is deleted. Anbox Cloud **DOES NOT** back up any data from the Android or the outer Ubuntu instance. Backup and restore of data must be implemented separately through [addons](https://discourse.ubuntu.com/t/addons/25293). See [Example: Back up data](https://discourse.ubuntu.com/t/example-back-up-data/25289) for information on how to do this.

<a name="regular-vs-base"></a>
## Regular instances vs. base instances

Anbox Cloud differentiates between two types of instances: regular and base. The instance type is visible in the output of the `amc ls` command.

Regular instances are containers or virtual machines that are launched from either an application or an image. They exist until they are deleted.

Base instances are temporary containers or virtual machines that are used when [bootstrapping an application](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap). They are automatically deleted when the application bootstrap is completed.

When we refer to instances in this documentation without specifying the instance type, we mean regular instances.

<a name="application-vs-raw"></a>
## Application instances vs. raw instances

Instances are based on either [applications](https://discourse.ubuntu.com/t/managing-applications/17760) or [images](https://discourse.ubuntu.com/t/provided-images/24185). So if you launch an application or an image, Anbox Management Service (AMS) automatically creates an instance for it.

Application instances are containers or virtual machines created when launching an application and run the full Android system. If the application is based on an Android app (an APK package), this app is launched after the system boots and monitored by the [watchdog](https://discourse.ubuntu.com/t/application-manifest/24197#watchdog). With the default configuration, you will see only the app and not the Android launcher.

Raw instances are containers or virtual machines created when launching an image. They run the full Android system, without any additional apps installed.

## Life cycle of an Anbox Cloud instance

### Creating an instance

When you [create an instance](https://discourse.ubuntu.com/t/launch-a-container/24327) by either launching or initialising an application or an image, AMS schedules the instance on a LXD node. The instance then executes the following steps in order:

1. Configure the network interface and gateway.
1. (Only for raw instances) Install addons that are specified with `--addons`.
1. Expose services that are specified with `--service` or through the application manifest.
1. Execute the `pre-start` hook provided by the installed addons.
1. Launch the Android container.
1. Execute the `post-start` hook provided by the installed addons.

![Container start|584x646](https://assets.ubuntu.com/v1/230fd172-container_start.png)

Launching an instance is successful only if all of the above steps succeed. If there are issues during the process, the status of the instance changes to `error`. You can [view the available logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329) from the container for further troubleshooting.

### Stopping an instance

Anbox Cloud instances can be stopped because of the following scenarios:

- You stopped it.
- You deleted it.
- An error occurred.

When an instance is stopped, it executes the following steps in order:

1. Stop the Android container.
2. Execute the `post-stop` hook provided by the installed addons.
3. Shut down the instance.

Beyond that, the instance will be removed from AMS either because you deleted it or because an error occurred during its runtime.
![Container stop|575x521](https://assets.ubuntu.com/v1/0377512e-container_stop.png)

### Possible instance status

An instance moves through different stages and correspondingly can have the following status depending on its current state.

Status            |  Description
----------------|------------
`created`     | AMS has created an internal database object for the instance and will next schedule the instance onto a suitable LXD node.
`prepared` | AMS has decided the LXD node on which it will schedule the instance.
`started` | The instance is started and now booting. During the boot sequence, possible hooks are executed. Only when all hooks have been executed, the instance will switch to `running`.
`running` | The instance is fully up and running.
`stopped` | The instance is fully stopped and will be deleted by AMS.
`deleted` | The instance is deleted and will be removed from the AMS database soon.
`error` | An error occurred while processing the instance. The instance is stopped. Further information about the error can be viewed with `amc show <instance id>`.

<a name="dev-mode"></a>
## Development mode

AMS allows to start an instance in development mode. This mode turns off some features that are usually active in an instance. It is mainly useful when developing addons inside an instance.

When development mode is enabled, the instance sends status updates to AMS when the Anbox runtime is terminated, however, AMS allows the instance to continue running. This allows you to restart the Anbox runtime inside the instance, providing an easy way to test [addons](https://discourse.ubuntu.com/t/addons/25293) or develop a [platform plugin](https://anbox-cloud.github.io/latest/anbox-platform-sdk/).

To check whether development mode is enabled, run `amc show <instance_ID>` or look at the `/var/lib/anbox/session.yaml` file in the instance. If the `devmode` field in the configuration file is set to `true`, development mode is active.

## Related information

 * [How to create a container](https://discourse.ubuntu.com/t/launch-a-container/24327)
 * [How to start a container](https://discourse.ubuntu.com/t/how-to-start-a-container/33924)
 * [How to wait for a container](https://discourse.ubuntu.com/t/wait-for-a-container/24330)
 * [How to access a container](https://discourse.ubuntu.com/t/access-containers-remotely/17772)
 * [How to expose services on a container](https://discourse.ubuntu.com/t/expose-services-on-a-container/24326)
 * [How to view the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329)
 * [How to stop a container](https://discourse.ubuntu.com/t/how-to-stop-a-container/33925)
 * [How to delete a container](https://discourse.ubuntu.com/t/delete-a-container/24325)
 * [How to list containers](https://discourse.ubuntu.com/t/list-containers/24328)
 * [How to configure geographic location](https://discourse.ubuntu.com/t/usecase-container-configuration/17782)
 * [How to back up and restore application data](https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183)
