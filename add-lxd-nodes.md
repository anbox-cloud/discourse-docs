New LXD units need to have a dedicated machine, so we need to configure a new machine as we did for the first one.

Since the Anbox Cloud 1.8 release,  AMS supports multiple architectures, which means a mix of amd64 and arm64 -based machines can work together in the connected LXD cluster. When adding a new lxd node to the cluster, you can choose the best-fit architecture to your cluster as needed.

Once the new machine is ready to be used, juju has to learn about it first. You can add it (assuming the IP for that new machine is `192.168.1.11`) with the following command:

```bash
$ juju add-machine ssh:ubuntu@192.168.1.11
```

In case of a cloud provider, as the machine is created on demand, you can simply:

```bash
$ juju add-machine
```

or even let the provider creating the machines as they are needed.

The command will take a moment as it installs

> **Note:**  `ubuntu` is the user that can ssh to these machines, it can be `root` too depending
    on how the operating system on the machine is setup.

List the available machines to confirm it has been added:

```bash
$ juju list-machines
Machine  State    DNS           Inst id              Series AZ Message
0    	  started  192.168.1.9   manual:192.168.1.9   bionic  Manually provisioned machine
1    	  started  192.168.1.10  manual:192.168.1.10  bionic  Manually provisioned machine
2    	  started  192.168.1.11  manual:192.168.1.11  bionic  Manually provisioned machine
```

As before, take care that a new machine is in the `started` state before you proceed. If
still in `down` state, please wait until it switches to `started`.

When the environment is ready, you can add the additional LXD node by requesting Juju to add a new unit of the LXD charm onto machine 2:

```bash
$ juju add-unit lxd --to 2
```

Once the unit is deployed it is added automatically added to AMS as a new LXD node.
