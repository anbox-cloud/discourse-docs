The AMS service manages a set of registered LXD nodes. All nodes are registered automatically when Juju sets them up.

> **Note:** It is possible to add and remove nodes manually but if you're using Juju to deploy Anbox Cloud you should avoid doing this as it will break the charm interplay and can leave you with a broken deployment.

In the next sections you will learn how to manage nodes in AMS.

## Prepare a Node
A node doesn't need much to be prepared to be registered with the AMS service. If you're using Juju to deploy Anbox Cloud please have a look at the guide to [add additional LXD nodes](https://discourse.ubuntu.com/t/adding-additional-lxd-nodes/17752).

If you want to setup a node manually you first have to install LXD. The 3.0 LTS version of
LXD is recommended.

```bash
$ snap install --channel=4.0 lxd
$ lxd waitready
```

Once LXD is installed and the initial configuration is completed we have to make the LXD service available to the outside and assign a trust password to prevent unauthorized access.
The IP address you configure here should be one which makes the LXD service available to the AMS service running on another machine.

```bash
$ lxc config set core.https_address 1.2.3.4:8443
```

The trust password can be freely defined but remember it as you need it to register the
node with AMS.

```bash
$ trust_password=$(pwgen 16 1)
$ lxc config set core.trust_password "$trust_password"
```

Now the LXD instance is ready to be registered with AMS.

 > Note: Do not configure the LXD instance with the `lxd init` command as suggested by the LXD documentation. AMS will take care to configure necessary networks, storage pools and profiles.

## Register a Node with AMS

AMS takes care of all aspects to set up a LXD node and adding it to a cluster of already known LXD nodes. To add the node the following things are necessary:

 * A name for the new node
 * IP address of the node which needs to be accessible from the machine AMS is running on
 * The trust password needed to access the LXD instance running on the node

Registering a node with the name `lxd1` which is available at address `192.168.1.15` is now possible with a single command:

```bash
$ amc node add --trust-password=mypassword lxd1 192.168.1.15
```

Depending on the load of the cluster the registration process can take a few seconds. Once done the node is available in the list of nodes AMS knows about:

```bash
$ amc node ls
+------+--------------+----------------+--------+-----------------+--------+
| NAME |   ADDRESS    | PUBLIC ADDRESS | STATUS | PORT FORWARDING | MASTER |
+------+--------------+----------------+--------+-----------------+--------+
| lxd1 | 192.168.1.15 | 192.168.1.15   | online | false           | true   |
+------+--------------+----------------+--------+-----------------+--------+
```

As last step to make the node fully usable we need to tell AMS about the resources the new node has. If we don't do this AMS will fail to schedule any containers onto the node as by default it does not provide any resources (`cpu-cores` and `memory` are set to zero).

In this example we have a node with 6 CPU cores and 16GB of memory.

```bash
$ amc node set lxd1 cpu-cores 6
$ amc node set lxd1 memory 16GB
```

Now the node is ready and can take containers.

> **Note:** If you want to learn more about why AMS needs to know about the resources available     on a specific node and what the information is being used for have a look at [Capacity Planing](https://discourse.ubuntu.com/t/capacity-planning/17765)

## Remove a Node from AMS

At times it is necessary to remove a not functioning and not needed node from AMS. The removal process will take care of removing all containers on the node and will also make it leave the formed cluster. Due to this the LXD instance needs to be removed and installed again if the node should be reused for another purpose afterwards. AMS doesn't give any guarantee that the LXD installation on the node is still functional after it removes the node from the cluster it manages.

If you're sure you want to remove an LXD node from AMS you can do this with the following command:

```bash
$ amc node remove lxd1

Do you really want to remove the node from the cluster? If you remove it
you have to manually reset LXD on the node machine to be able to let it join the
AMS cluster again.
The following node will be REMOVED:
- lxd0
Do you want to continue? [Y/n]: 
```

`AMS` will ask you for your approval before removing the node. If you want to bypass
manual approval you can use the `--yes` option. But be super careful with this and double
check you're removing the right node.
