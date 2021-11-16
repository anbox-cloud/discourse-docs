Containers are the centre piece of the Anbox Cloud stack. Every time you launch an application or an image, Anbox Cloud creates a container for it. Every container provides a full Android system.

## Regular containers vs. base containers

Anbox Cloud differentiates between two types of containers: regular containers and base containers. The container type is visible in the output of the `amc ls` command.

Regular containers are containers that are launched from either an application or an image. They exist until they are deleted.

Base containers are temporary containers that are used when [bootstrapping an application](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap). They are automatically deleted when the application bootstrap is completed.

When we refer to containers in this documentation without specifying the container type, we mean regular containers.

<a name="application-vs-raw"></a>
## Application containers vs. raw containers

Containers are based on either [applications](https://discourse.ubuntu.com/t/managing-applications/17760) or [images](https://discourse.ubuntu.com/t/provided-images/24185). That means that if you launch an application or an image, AMS automatically creates a container for it.

Application containers, thus containers created when launching an application, run the full Android system. If the application is based on an Android app (an APK package), this app is launched after the system boots and monitored by the [watchdog](https://discourse.ubuntu.com/t/application-manifest/24197#watchdog). With the default configuration, you will see only the app and not the Android launcher.

Containers that are created when launching an image are called raw containers. They run the full Android system, without any additional apps installed.

## Data stored in containers

All containers in Anbox Cloud are ephemeral, which means that as soon as a container is stopped, all of its data is gone. Anbox Cloud **DOES NOT** back up any data from the Android or the outer Ubuntu container. Backup and restore of data must be implemented separately through [addons](https://discourse.ubuntu.com/t/addons/25293). See [Example: Back up data](https://discourse.ubuntu.com/t/example-back-up-data/25289) for information on how to do this.

## Container life cycle

When you create a container by launching an application or an image, it executes the following steps in order:

1. Configure the network interface and gateway.
2. Only raw containers: Install addons that are specified with `--addons`.
3. Expose services that are specified with `--service` or through the application manifest.
4. Execute the `pre-start` hook provided by the installed addons.
5. Launch the Android container.
6. Execute the `post-start` hook provided by the installed addons.

![Container start|566x528](upload://bp1BNo5CKGjLmesP5TXj59faclr.png)

The whole launch process is successful only if all of the above steps succeed.

If anything goes wrong during the container launch process, the status of the container changes to the `error` status. You can [view the available logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329) from the container for diagnosing the root cause of the problem.

When a container is stopped, either because you deleted it or because an error occurred, it executes the following steps in order:

1. Stop the Android container.
2. Execute the `post-stop` hook provided by the installed addons.
3. Shut down the container.

![Container stop|551x385](upload://tqRdCg34qOVjmlJOZwiXqijXeov.png)

### Possible container status

Throughout its lifetime, a container moves through different stages depending on the state it's currently in.

Status            |  Description
----------------|------------
`created`     | AMS has created an internal database object for the container and will schedule the container onto a suitable LXD node next.
`prepared` | AMS has decided on which LXD node the container will be placed.
`started` | The container was started and is now booting. During the boot sequence, possible hooks are executed. Only when all hooks have been executed, the container will switch to `running`.
`running` | The container is fully up and running.
`stopped` | The container is fully stopped and will be deleted by AMS.
`deleted` | The container is deleted and will be removed from the AMS database soon.
`error` | An error occurred while processing the container. The container is stopped. Further information about the error can be viewed with `amc show <container id>`.


## Managing containers

 * [Launch a container](https://discourse.ubuntu.com/t/launch-a-container/24327)
 * [Wait for a container](https://discourse.ubuntu.com/t/wait-for-a-container/24330)
 * [Access a container](https://discourse.ubuntu.com/t/access-containers-remotely/17772)
 * [Expose services on a container](https://discourse.ubuntu.com/t/expose-services-on-a-container/24326)
 * [View the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329)
 * [Delete a container](https://discourse.ubuntu.com/t/delete-a-container/24325)
 * [List containers](https://discourse.ubuntu.com/t/list-containers/24328)
 * [Configure geographic location](https://discourse.ubuntu.com/t/usecase-container-configuration/17782)
 * [Back up and restore application data](https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183)
