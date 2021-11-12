.. _howto_container_list:

===============
List containers
===============

To get an overview of which and how many containers are currently
running on an Anbox Cloud deployment, run the ``amc ls`` command:

.. code:: bash

   +----------------------+----------------+---------+---------+------+---------------+------------------------+
   |          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
   +----------------------+----------------+---------+---------+------+---------------+------------------------+
   | bdpaqaqhmss611ruq6kg |     candy      | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
   |                      |                |         |         |      |               | 10.103.46.41:10000/tcp |
   +----------------------+----------------+---------+---------+------+---------------+------------------------+

This will list all containers with their status and additional
information, for example, on which LXD node in the cluster the
containers are running.

Filter containers
=================

``amc ls`` accepts a ``--filter`` flag to filter and group containers.

The filter flag accepts a key-value pair as the filtering value. The
following attributes are valid keys:


.. list-table::
   :header-rows: 1

   * - Name
     - Value
   * - \ ``app``\ 
     - Application name or ID
   * - \ ``type``\ 
     - Container type, possible values: “base”, “regular”
   * - \ ``node``\ 
     - Node on which the container runs
   * - \ ``status``\ 
     - Container status, possible values: “created”, “prepared”, “started”, “stopped”, “running”, “error”, “deleted”, “unknown”


To list all regular containers:

::

   amc ls --filter type=regular

If you need to apply multiple filters, pass multiple flags:

::

   amc ls --filter type=regular --filter node=lxd0

This will query all regular containers that are placed on the node with
the name ``lxd0``.
