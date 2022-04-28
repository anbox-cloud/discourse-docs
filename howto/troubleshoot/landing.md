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

See [How to view the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329) for instructions on how to access the container log files.

### Published application version not found

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> When launching a container for an application, I get an error about the "published application version not found". Why?

If you launch a container by only specifying the application ID and the application has no published version yet, you must explicitly specify the version that you want to launch or publish a version of the application. See [How to launch application containers](https://discourse.ubuntu.com/t/launch-a-container/24327#application-containers) and [How to publish application versions](https://discourse.ubuntu.com/t/update-an-application/24201#publish-application-versions) for more information.

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

## LXD cluster

The following issues might occur if you use clustering.

<a name="ams-lxd-relation-changed-failed"></a>
### AMS hook failed: "lxd-relation-changed"

*Applies to: Anbox Cloud*

> I see an error message like the following in the output of `juju debug-log --include ams`:
>
> ```
> unit-ams-0: 13:30:51 INFO unit.ams/0.juju-log Error adding LXD node lxd5 to AMS: 1 - Flag --timeout has been deprecated, Using the timeout argument has no longer an effect as cancelling cluster operations is not supported
> Error: Get "https://10.25.83.151:8443": Unable to connect to: 10.25.83.151:8443
> unit-ams-0: 13:30:51 ERROR unit.ams/0.juju-log Hook error:
> Traceback (most recent call last):
>   File "/var/lib/juju/agents/unit-ams-0/.venv/lib/python3.8/site-packages/charms/reactive/__init__.py", line 74, in main
>     bus.dispatch(restricted=restricted_mode)
>   File "/var/lib/juju/agents/unit-ams-0/.venv/lib/python3.8/site-packages/charms/reactive/bus.py", line 390, in dispatch
>     _invoke(other_handlers)
>   File "/var/lib/juju/agents/unit-ams-0/.venv/lib/python3.8/site-packages/charms/reactive/bus.py", line 359, in _invoke
>     handler.invoke()
>   File "/var/lib/juju/agents/unit-ams-0/.venv/lib/python3.8/site-packages/charms/reactive/bus.py", line 181, in invoke
>     self._action(*args)
>  File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 356, in endpoint_lxd_changed
>     process_cluster_changes(lxd)
>   File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 333, in process_cluster_changes
>     update_lxd_nodes_in_service(nodes, use_node_state=True)
>   File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 966, in update_lxd_nodes_in_service
>     if add_lxd_node_to_service(n) and use_node_state:
>   File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 1061, in add_lxd_node_to_service
>     raise ex
>   File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 1050, in add_lxd_node_to_service
>     check_output(cmd, stderr=STDOUT)
>   File "/usr/lib/python3.8/subprocess.py", line 415, in check_output
>     return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
>   File "/usr/lib/python3.8/subprocess.py", line 516, in run
>     raise CalledProcessError(retcode, process.args,
> subprocess.CalledProcessError: Command '['amc', 'node', 'add', 'lxd5', '10.25.83.151', '--storage-device', 'dir', '--network-bridge-mtu', '1500', '--timeout', '5m']' returned non-zero exit status 1.
> ```
> What is the problem, and how can I fix it?

This error indicates a faulty LXD node. Most likely, something went wrong when AMS tried adding a new LXD node to the cluster, either because the LXD node was not available on the network or it joining the cluster failed for unknown reasons.

The easiest way to make the AMS unit work again is to remove the faulty LXD node (`lxd/5` in this example) by running the following command:

    juju remove-unit --force lxd/5

[note type="information" status="Note"]Add `--destroy-storage` to the command if you allocated dedicated storage for LXD.[/note]

After the LXD unit is successfully removed, resolve the failed hook of the AMS unit. For that, first disable
automatic retries to prevent Juju from re-running the failed hook:

    juju model-config automatically-retry-hooks=false

Wait for any pending hook execution to finish. Check `juju status` to monitor the status.

Once the model has settled, resolve the failed hook by running the following command:

    juju resolve ams/0 --no-retry

Check the `juju status` output. The status of the `ams/0` unit should switch back to `active`.

To verify that the LXD cluster is still correctly in place, compare the output of `juju ssh ams/0 -- amc node ls`
and `juju ssh lxd/0 -- lxc cluster ls`. Both commands should list the same LXD nodes.

Finally, enable automatic retries again:

    juju model-config automatically-retry-hooks=true
