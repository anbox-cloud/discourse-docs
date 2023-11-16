Scaling down a LXD cluster involves more checks than scaling up.

There are two important requirements when scaling down:
 - The node you remove must not have any instances left.
 - You must wait for a node to be fully removed before you can start removing another one.

## Prepare the node for removal

First, pick the node you want to remove and tell AMS to stop considering this node for new instances:

    amc node set lxd0 unschedulable true

Now the node won't be considered for any further instances launches.

The node might still have instances running. You can decide to either kill all instances or wait for your users to disconnect.
Use the following command to check if the node still hosts instances:

    amc ls --filter node=lxd0

Note that a node must have no instances left on it before you can remove it.

If you want to kill all instances immediately, run the following command:

    amc delete --all --yes

## Remove the node

When the node is ready to be removed, use the following Juju command, where `<id>` is the number of the unit you are removing:

    juju remove-unit lxd/<id>

Once you invoke the removal of the node, you **MUST** wait for the node to be fully removed before you attempt to remove the next node or add a new one. You can do that with a combination of `juju wait` and the following script (which is the inverse of the one for scaling up):

```bash
#!/bin/bash -ex
unit=$1
# Drop slash from the unit name
node_name=${unit/\//}
while true; do
  if ! juju ssh ams/0 -- /snap/bin/amc node ls | grep -q "$node_name" ; then
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
    ./wait-for-unit.sh "lxd/<id>"

Once the unit is fully removed, you can continue to remove the next one.
