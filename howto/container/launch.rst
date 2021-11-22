.. _howto_container_launch:

==================
Launch a container
==================

You can launch a container for a registered application or image (see
:ref:`Application containers vs. raw containers <exp_containers-application-vs-raw>`),
either by using the ``amc`` tool or through another service over the
REST API that the AMS service provides.

By default, the container will run headless. See :ref:`howto_container_access` for
instructions on how to access it for debugging purposes, and :ref:`exp_application-streaming`
for information about the streaming stack.

.. _howto_container_launch-application-containers:

Launch application containers
=============================

Launching a container for a registered application can be achieved with
the following command:

::

   amc launch <application id>

As argument, provide the ID of the application that you want to launch.
You can list all available applications with the ``amc application ls``
command:

.. code:: bash

   +----------------------+----------------+---------------+--------+-----------+--------+---------------------+
   |          ID          |      NAME      | INSTANCE TYPE | ADDONS | PUBLISHED | STATUS |    LAST UPDATED     |
   +----------------------+----------------+---------------+--------+-----------+--------+---------------------+
   | bdp7kmahmss3p9i8huu0 |      candy     | a2.3          | ssh    | false     | ready  | 2018-08-14 08:44:41 |
   +----------------------+----------------+---------------+--------+-----------+--------+---------------------+

If the application for which you want to launch a container is not yet
published (see :ref:`howto_application_update`
for more details), the launch command will fail as it only allows
launching a container for a published application. However, you can work
around this by specifying a specific version of an application:

::

   amc launch --application-version=0 bcmap7u5nof07arqa2ag

.. _howto_container_launch-raw-containers:

Launch raw containers
=====================

The command for launching a raw container from an image is:

::

   amc launch --raw <image id>

As argument, provide the ID or name of the image for which you want to
launch a container. See :ref:`ref_provided-images` for a
list of images that are available in Anbox Cloud.

You can also list all available images with the ``amc image ls``
command:

.. code:: bash

   +----------------------+---------+--------+----------+----------------------+
   |          ID          |  NAME   | STATUS | VERSIONS |       USED BY        |
   +----------------------+---------+--------+----------+----------------------+
   | bh01n90j1qm6416q0ul0 | default | active | 1        |                      |
   +----------------------+---------+--------+----------+----------------------+

Launch a container on a specific node
=====================================

By default, every container is scheduled by AMS onto a LXD node.
Alternatively, you can launch a container directly on a specific node:

::

   amc launch --node=lxd0 bcmap7u5nof07arqa2ag

.. note::
   AMS will still verify that the
   selected node has enough resources to host the container. If not, the
   container will fail to launch.

Launch a container with a different Anbox platform
==================================================

By default, every container starts with the ``null`` platform (see
:ref:`ref_platforms`).
The selected platform cannot be changed at runtime and must be selected
when the container is created. For example, you can launch a container
with the ``swrast`` platform like this:

::

   amc launch -p swrast <application-id>

If you have built your own platform named ``foo`` and you built it via
an addon into the container images, you can launch a container with the
platform the same way:

::

   amc launch -p foo <application-id>
