.. _explanation_containers:

================
About containers
================

Containers are the centre piece of the Anbox Cloud stack. Every time you
launch an application or an image, Anbox Cloud creates a container for
it. Every container provides a full Android system.

Regular containers vs. base containers
======================================

Anbox Cloud differentiates between two types of containers: regular
containers and base containers. The container type is visible in the
output of the ``amc ls`` command.

Regular containers are containers that are launched from either an
application or an image. They exist until they are deleted.

Base containers are temporary containers that are used when
:ref:`bootstrapping an application <explanation_applications-bootstrap>`.
They are automatically deleted when the application bootstrap is
completed.

When we refer to containers in this documentation without specifying the
container type, we mean regular containers.

.. _explanation_containers-application-vs-raw:

Application containers vs. raw containers
=========================================

Containers are based on either
:ref:`applications <explanation_applications>`
or :ref:`images <reference_provided-images>`.
That means that if you launch an application or an image, AMS
automatically creates a container for it.

Application containers, thus containers created when launching an
application, run the full Android system. If the application is based on
an Android app (an APK package), this app is launched after the system
boots and monitored by the
:ref:`watchdog <reference_application-manifest-watchdog>`.
With the default configuration, you will see only the app and not the
Android launcher.

Containers that are created when launching an image are called raw
containers. They run the full Android system, without any additional
apps installed.

Data stored in containers
=========================

All containers in Anbox Cloud are ephemeral, which means that as soon as
a container is stopped, all of its data is gone. Anbox Cloud **DOES
NOT** back up any data from the Android or the outer Ubuntu container.
Backup and restore of data must be implemented separately through
:ref:`addons <reference_addons>`. See :ref:`howto_addon_backup-and-restore` for
information on how to do this.

Container life cycle
====================

When you create a container by launching an application or an image, it
executes the following steps in order:

1. Configure the network interface and gateway.
2. Only raw containers: Install addons that are specified with
   ``--addons``.
3. Expose services that are specified with ``--service`` or through the
   application manifest.
4. Execute the ``pre-start`` hook provided by the installed addons.
5. Launch the Android container.
6. Execute the ``post-start`` hook provided by the installed addons.

.. figure:: /images/container_start.svg
   :alt: Container start

   Container start

The whole launch process is successful only if all of the above steps
succeed.

If anything goes wrong during the container launch process, the status
of the container changes to the :ref:`error status. You can view the available logs <howto_container_logs>`
from the container for diagnosing the root cause of the problem.

When a container is stopped, either because you deleted it or because an
error occurred, it executes the following steps in order:

1. Stop the Android container.
2. Execute the ``post-stop`` hook provided by the installed addons.
3. Shut down the container.

.. figure:: /images/container_stop.svg
   :alt: Container stop

   Container stop

Possible container status
-------------------------

Throughout its lifetime, a container moves through different stages
depending on the state it’s currently in.


.. list-table::
   :header-rows: 1

   * - Status
     - Description
   * - \ ``created``\
     - AMS has created an internal database object for the container and will schedule the container onto a suitable LXD node next.
   * - \ ``prepared``\
     - AMS has decided on which LXD node the container will be placed.
   * - \ ``started``\
     - The container was started and is now booting. During the boot sequence, possible hooks are executed. Only when all hooks have been executed, the container will switch to ``running``.
   * - \ ``running``\
     - The container is fully up and running.
   * - \ ``stopped``\
     - The container is fully stopped and will be deleted by AMS.
   * - \ ``deleted``\
     - The container is deleted and will be removed from the AMS database soon.
   * - \ ``error``\
     - An error occurred while processing the container. The container is stopped. Further information about the error can be viewed with ``amc show <container id>``.


Managing containers
===================

-  :ref:`howto_container_launch`
-  :ref:`howto_container_wait`
-  :ref:`howto_container_access`
-  :ref:`Expose services on a container <howto_container_expose-services>`
-  :ref:`howto_container_logs`
-  :ref:`howto_container_delete`
-  :ref:`howto_container_list`
-  :ref:`howto_container_geographic-location`
-  :ref:`howto_container_backup-and-restore`
