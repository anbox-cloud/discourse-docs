.. _howto_container_expose-services:

===============
Expose services
===============

AMS allows a container to expose a service to the outer network. For
that, it provides a feature called container services which let you
define a port to expose on the container endpoints. The set of services
to expose is defined when the container is launched. For example, the
following command exposes port ``22`` on the container’s private
endpoint:

::

   amc launch -s tcp:22 bdp7kmahmss3p9i8huu0

.. note::
   The specified port is exposed
   only on the IP address that the container itself has. As the container
   is normally not accessible from outside, the LXD node it is running on
   AMS sets up port forwarding rules on the node and maps the specified
   port to one in a higher port range (``10000 - 110000``).

The list of containers (``amc ls``) will now show the container and the
exposed port ``22``:

.. code:: bash

   +----------------------+----------------+---------+---------+------+---------------+------------------------+
   |          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
   +----------------------+----------------+---------+---------+------+---------------+------------------------+
   | bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
   |                      |                |         |         |      |               | 10.103.46.41:10000/tcp |
   +----------------------+----------------+---------+---------+------+---------------+------------------------+

As described above, the port ``22`` is exposed only on the IP address
the container itself has. In addition, it was mapped onto port ``10000``
on the address of the LXD node ``lxd0``.

To help identifying services later on you can give them a name. For the
example above we can simply name the service ``ssh``:

::

   amc launch -s ssh:tcp:22 bdp7kmahmss3p9i8huu0

This will help to identify which endpoint is used for which service:

.. code:: bash

   +----------------------+----------------+---------+---------+------+---------------+----------------------------+
   |          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS            |
   +----------------------+----------------+---------+---------+------+---------------+----------------------------+
   | bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | ssh:192.168.100.2:22/tcp   |
   |                      |                |         |         |      |               | ssh:10.103.46.41:10000/tcp |
   +----------------------+----------------+---------+---------+------+---------------+----------------------------+

If we want to expose the service on the public endpoint of a LXD node
instead we must slightly change the service definition when the
container is launched:

::

   amc launch -s +tcp:22 bdp7kmahmss3p9i8huu0

Notice the ``+`` in front of the port definition. This tells AMS to
expose the service on the public endpoint of the LXD node the container
is scheduled onto. The container list then shows the public address of
the node the container is running on in the list of endpoints:

.. code:: bash

   +----------------------+----------------+---------+---------+------+---------------+------------------------+
   |          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
   +----------------------+----------------+---------+---------+------+---------------+------------------------+
   | bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
   |                      |                |         |         |      |               | 147.3.23.6:10000/tcp   |
   +----------------------+----------------+---------+---------+------+---------------+------------------------+
