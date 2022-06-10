An existing Anbox Cloud Appliance can be extended with additional machines to extend available container capacity.

This does currently not include support for high availability (HA).

## Allow internal network communication

The appliance will use [FAN networking](https://wiki.ubuntu.com/FanNetworking) to spawn an overlay network to allow containers to communicate with each other. For that to work we need to allow incoming traffic on the internal network the machines sit on so they can communicate with each other.

On AWS you can modify the security group attached to the instance to allow all incoming traffic on the internal subnet it sits on:

![AWS security group](images/appliance_multi_node_aws_ports.png)

In this example incoming traffic is allowed when it orginates in the internal subnet `172.31.16.0/20`.

## Generate join token

First, we have to generate a token on the existing machine running the Anbox Cloud Appliance to provide necessary information and authentication details for the new machine we want to join:

    anbox-cloud-appliance cluster add <name>

The name you pick here is important as it will represent the name which will be used to identify the node in both LXD and AMS.

## Join new machine

For joining a new machine to an existing Anbox Cloud Appliance we have to run through the init process as normal but this time have to answer the question about clustering with "yes" and provide the join token we have previously generated:

    ubuntu@ip-172-31-31-72:~$ sudo anbox-cloud-appliance init
    Welcome to the Anbox Cloud Appliance!

    The following questions will guide you through the initial setup of the
    appliance. If you don't care about answering any of them you can just
    accept the defaults.

    For any further questions please have a look a the official Anbox Cloud
    documentation at https://anbox-cloud.io/docs

    Are you joining this node to an existing Anbox Cloud Appliance installation? (EXPERIMENTAL) [default=no] yes
    Please enter the join token: eyJsdCI6ImV5SnpaWEoyWlhKZmJtRnRaU0k2SW14NFpERWlMQ0ptYVc1blpYSndjbWx1ZENJNkltWXhPVEpqTm1Ga09XVm1PVGRoTXpnNU9XVmxOelF6WW1NeU5ESmxaak5sWkRaaVpXTm1abUV4T0dFNFlqRTVNalE1TjJaalkyRTBaREUzWlRRMk5HWWlMQ0poWkdSeVpYTnpaWE1pT2xzaU1UY3lMak14TGpJeExqVTZPRFEwTXlKZExDSnpaV055WlhRaU9pSmxOMlZrTldZd00yWTVPVEF5WXpKbVpETmlNRFV6TmpJeE5tTmpOV1JsWmprelptVTVPV05pTWpBM1lqRXlOekk1TVRneU1UTTVOV1EwTWpNeVpqQXdJbjA9IiwianQiOiJNRTRUQ1d4NFpERXROMkUyWXpBVUV4SXlOREF1TWpFdU5TNHlNelk2TVRjd056QUVJSmhzeVo5QjlrWGRKX0dOOWJQd09pTHlLV1VXdXM1Y092cDdST29INzdIWEV3bGhjSEJzYVdGdVkyVUEiLCJmIjp7Im0iOnRydWV9fQ==

    ...

Afterwards the machine will automatically connect to the existing appliance and set everything up. The initialization process should run much quicker than for the first machine and should finish with a few minutes at maximum.

Once the initialization process has finished, the second machine is ready to be used.
