Scaling down a LXD cluster involves more checks than scaling up.

First, you must pick a suitable candidate node. When a node is removed, all still running containers on it are stopped and potentially connected users are disconnected. To avoid this, AMS provides a feature to mark a node as unschedulable so that it will not be considered for any further container launches.

You can mark a node as unschedulable with the following command:

    amc node set lxd0 unscheduable true

(Note that the typo in the command will be fixed in a future Anbox Cloud release.)

Now the node won't be considered for any further container launches. As it might still host containers, you can decide to either kill all containers or wait for your users to disconnect. You can check with the following command if the node still hosts containers:

    amc ls --filter node=lxd0 --format=csv | wc -l

If you want to kill all containers immediately, run the following command:

    for id in $(amc ls --filter node=lxd0 --format=csv | cut -d, -f1) ; do amc delete -y "$id" ; done

When the node is ready to be removed, remove it by using Juju:

    juju remove-unit lxd/0

Once you invoke the removal of the node, you **MUST** wait for the node to be fully removed before you attempt to remove the next node or add a new one. You can do that with a combination of `juju wait` and the following script (which is the inverse of the one for scaling up):

```bash
#!/bin/sh -ex
unit=$1
# Drop slash from the unit name
node_name=${unit/\//}
while true; do
  if ! juju ssh ams/0 -- /snap/bin/amc node ls | grep -q “$node_name”
    break
  fi
  sleep 5
done
while true ; do
  if ! juju ssh "$unit" -- lxc cluster ls ; then
    break
  fi
  sleep 5
done
```

Save the script with the file name `wait-for-unit.sh` and run it with the following commands:

    chmod +x wait-for-unit.sh
    ./wait-for-unit.sh "lxd/1"

Once the unit is fully removed, you can continue to remove the next one.
