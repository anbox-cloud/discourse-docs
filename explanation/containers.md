Containers are the centre piece of the Anbox Cloud stack. A single container provides a full Android system.

Each container is hosted on a cluster of multiple nodes provided by the underlying LXD container hypervisor. The base for a container is an application. See [About applications](https://discourse.ubuntu.com/t/managing-applications/17760) for more information about applications.

## Data stored in containers

All containers in Anbox Cloud are ephemeral, which means that as soon as a container is stopped, all of its data is gone. Anbox Cloud **DOES NOT** back up any data from the Android or the outer Ubuntu container. Backup and restore of data must be implemented separately through the `backup` and `restore` hooks of [addons](https://discourse.ubuntu.com/t/managing-addons/17759/2).

## Possible container status

Throughout its lifetime, a container moves through different stages depending on the state it's currently in.

Status            |  Description
----------------|------------
`created`     | AMS has created an internal database object for the container and will schedule the container onto a suitable LXD node next.
`prepared` | AMS has decided on which LXD node the container will be placed.
`started` | The container was started and is now booting. During the boot sequence, possible hooks are executed. Only when all hooks have been executed, the container will switch to `running`.
`running` | The container is fully up an running.
`stopped` | The container is fully stopped and will be deleted by AMS.
`deleted` | The container is deleted and will be removed from the AMS database soon.
`error` | An error occurred while processing the container. The container is stopped. Further information about the error can be viewed via `amc show <container id>`.


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
