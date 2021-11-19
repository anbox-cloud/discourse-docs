.. _explanation_clustering:

================
About clustering
================

While it is possible to install Anbox Cloud on a single machine, you
usually want to distribute the load over several machines in a cluster.
In such a clustering setup, one node is dedicated to host the AMS
service (the management node). If you use the streaming stack, two
additional nodes are dedicated to host the extra services required for
streaming. All other nodes are used as worker nodes.

Each worker node runs `LXD <https://linuxcontainers.org/>`__ in
clustering mode, and this LXD cluster is used to host the Android
containers.

Capacity planning
=================

Anbox Cloud is optimised to provide containers at high density per host.
However, to provide enough underlying resources for a specific number of
containers, you need to do some calculations to find out how many LXD
machines (thus worker nodes) with how many resources you need.

Each container will take a specific amount of resources defined by the
instance type used by the application it is launched for. If an
application uses the ``a2.3`` instance type, it requires 2 CPU cores and
3 GB of memory and 3 GB of disk space (see :ref:`reference_instance-types` for
details on how much resources each instance type requires). AMS
internally summarises the amount of resources used by containers on a
single machine and disallows launching additional containers when all
resources are used.

For a machine with 8 CPU cores and 16 GB of memory, you could only
launch 4 containers before you run out of resources. As a single
container will not use the dedicated CPU cores all time at 100%, AMS
allows overcommitting available resources.

Each node has two configuration items called ``cpu-allocation-rate`` and
``memory-allocation-rate`` of type float which define the multiplier
used for overcomitting resources. By default, AMS sets
``cpu-allocation-rate`` to ``4`` and ``memory-allocation-rate`` to 2.
This sums up the available resources to
``4 * 8 CPU cores = 36 CPU Cores`` and
``2 * 16 GB memory = 32 GB memory``, which will allow 10 containers on
the node.

The currently configured allocation rates for a specific node can be
shown via the following command:

::

   amc node show lxd0

This command will return output similar to the following:

.. code:: bash

   name: lxd0
   status: online
   disk:
       size: 100GB
   network:
       address: 10.119.216.34
       bridge-mtu: 1500
   config:
       public-address: 10.119.216.34
       use-port-forwarding: true
       cpu-cores: 8
       cpu-allocation-rate: 4
       memory: 16GB
       memory-allocation-rate: 2
       gpu-slots: 10
       gpu-encoder-slots: 0
       tags: []

Based on this you can calculate the amount of resources you need to run
a specific number of containers. For example, if you have a Qualcomm
Centriq 2400 which has 48 CPU cores and you want to run 100 containers
of instance type ``a2.3``:

.. code:: bash

   CPU allocation rate = 100 * 2 CPU cores / 48 CPU cores ~= 5
   Memory needed = 100 * 3 GB / 2 = 150 GB
   Disk space needed = 100 * 3 GB = 300 GB

In this example, we used a memory allocation rate of ``2``.

Which CPU allocation rate makes sense always depends on which type of
application will be running inside the containers and which amount of
CPU it needs. For low CPU intensive applications a higher and for high
CPU intensive applications a lower allocation rate makes sense.

.. _explanation_clustering-gpu-slots:

GPU slots
---------

An additional aspect to take into account when planning your resources
is the number of required GPU slots (see :ref:`explanation_gpu-support` for more
information).

GPUs have limited capacity that can be shared amongst multiple
containers, and GPU slots are a way to fine-tune how many containers can
run on a given node.

In short, each LXD node has a certain amount of GPU slots available, and
each application can define a number of GPU slots it needs. Both are
configurable.

GPU slots for LXD nodes
~~~~~~~~~~~~~~~~~~~~~~~

Each GPU equipped LXD node has its own number of GPU slots configured.
You can see that number by running the ``amc node show lxd0`` command:

.. code:: bash

   ...
   config:
       ...
       gpu-slots: 0

You can change the number of GPU slots of each node with the following
command:

::

   amc node set lxd0 gpu-slots 10

.. note::
   Determining the correct number of
   GPU slots for a specific GPU model depends on various things. The
   following just gives an idea of what should drive the decision for the
   right number of GPU slots: - Memory a GPU provides - Memory a container
   uses - Number of parallel encoding pipelines a GPU offers
   
   Finding the right number of GPU slots requires benchmarking and testing
   of the intended workload.

Launching a container on that node will reserve some of those GPU slots
and mark them as unavailable until the container is terminated. If your
node has no GPU slot available, containers requiring a GPU will not be
launched on it. Containers not requiring a GPU can still be launched.

GPU slots for application
~~~~~~~~~~~~~~~~~~~~~~~~~

Applications can declare how many GPU slots they require. This number is
set by default when specifying the :ref:`instance type <reference_instance-types>`, but it
can be overridden using
:ref:`resources <reference_application-manifest>`.

.. code:: bash

   name: android
   instance-type: g4.3
   resources:
     gpu-slots: 3

In this case, the application will use three GPU slots instead of one as
defined in the instance type.

Increasing the number of GPU slots does **NOT** guarantee that more GPU
resources are allocated to that application container. *For example: An
intensive game configured with one GPU slot will still consume more
resources than a photo gallery app configured with five GPU slots.*

However, it means that less containers will be launched on that node,
reducing contention for GPU resources.

Containers can be configured to use a hardware or software video encoder
for video encoding. This can be done through the ``video-encoder`` field
declared in the manifest file when creating an application as well. See
:ref:`Video encoder <reference_application-manifest-video-encoder>`
for more details.

LXD auto scaling
================

Different use cases for Anbox Cloud require elasticity of the LXD
cluster to deal with dynamic user demand throughout a certain time
period. This involves increasing the number of nodes of the LXD cluster
when demand increases and reducing the number of nodes when demand
decreases. As Anbox Cloud provides fine grained capacity planning to
have tight control over how many users / containers are running on a
single node, the driving factor for an auto scaling implementation
cannot be deduced from CPU, memory or GPU load but from the planned
capacity of the currently available nodes in the cluster.

The current release of Anbox Cloud has no builtin auto scaling
implementation but comes with all needed primitives to build one. In a
future version, Anbox Cloud will provide an auto scaling framework that
will simplify various aspects of an implementation.

Guidelines for auto scaling
---------------------------

The following guidelines are both recommended and must-have aspects of
an auto scaling implementation. Make sure that your auto scaling
implementation follows these to stay within a supported and tested
scope.

1. Don’t scale the LXD cluster below three nodes. You should keep three
   active nodes at all times to ensure the database LXD uses can achieve
   a quorum and is highly available. If you run below three nodes, your
   cluster is very likely to get into a non-functional state or be lost
   completely (see `LXD documentation <https://linuxcontainers.org/lxd/docs/master/clustering#recover-from-quorum-loss>`_
   for more information).
2. A single LXD cluster should take no more than 40 nodes.
3. If you need more than 40 nodes, you should create a separate cluster
   in a separate Juju model with its own AMS.
4. Scaling a cluster up with multiple new nodes in parallel is fine and
   recommended if you need to quickly increase your cluster capacity.
5. Scaling down **MUST** strictly happen in a sequential order with no
   other scaling operations (for example, scale up) running in parallel.
6. You **MUST NOT** remove a LXD database node (check ``lxc cluster ls``
   on any LXD node) when scaling down. Due to issues in
   `LXD <https://linuxcontainers.org/lxd/introduction/>`__ and its `raft implementation <https://github.com/canonical/raft>`__, this might
   lead to an unhealthy cluster in some cases. These issues are
   currently (March 2021) being worked on by the LXD engineering team.
7. Before removing a LXD node from the cluster you **MUST** delete all
   containers on it first.

Scaling up or down
------------------

See :ref:`howto_cluster_scale-up`
and :ref:`howto_cluster_scale-down`
for instructions on how to add or remove nodes from the cluster.

When to scale up or down the cluster?
=====================================

Answering the question when to scale a cluster up and down is not simple
and is different for each use case. The traditional approach to measure
CPU, memory or GPU load does not apply for Anbox Cloud as capacity is
well planned and the number of containers per node is configured ahead
of time. Furthermore, user patterns are hard to predict and will be
different in each case. For that reason, custom logic is required to
take a decision when a cluster should be scaled up or down.

Anbox Cloud provides various metrics to help decide when to scale up or
down. See the :ref:`relevant documentation <reference_prometheus>`
for a list of available metrics that can be used to take a decision.
Based on this together with data from a production system, you can build
a model trying to predict when auto scaling should trigger or not.

Future versions of Anbox Cloud will provide a framework which will help
to implement such a model.
