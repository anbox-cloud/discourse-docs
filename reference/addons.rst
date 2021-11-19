.. _reference_addons:

======
Addons
======

Addons provide a way to extend and customise images in Anbox Cloud. See
:ref:`howto_addon_landing`
and the :ref:`tutorial_creating-addon`
tutorial for instructions on how to use them.

.. _reference_addons-file-structure:

File structure
==============

When creating or updating an addon, the directory containing your addon
files must contain:

-  A file named ``manifest.yaml``.
-  A directory named ``hooks``. This directory must contain at least one
   executable file with a valid hook name (see :ref:`Hooks <reference_addons-hooks>`
   below).

Other files in the addon directory are bundled with the addon. They can
be accessed in a hook by using the :ref:`$ADDON_DIR environment variable <reference_addons-env-variables>`). For example:

.. code:: bash

   cat "$ADDON_DIR"/public_key.pem >> ~/.ssh/authorized_keys

To create the addon, you must provide ``amc`` with either the directory
or a tarball containing the same file structure.

.. _reference_addons-manifest:

Addon manifest
==============

The following table lists the valid keys in an addon manifest:


.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Allowed values
   * - name
     - string
     - Name of the addon. Can be used to reference the addon.
     - All characters except for the following: ``< > : " / \ | - ? *``, as well as space.
   * - description
     - string
     - Description of the addon.
     -
   * - provides
     - object
     - Additional capabilities that this addon provides to the container. See individual items for details.
     -
   * - provides.abi-support
     - string array
     - Tells AMS that this addon adds support for the given architecture even if the application doesn’t support it natively. Use this when your addon brings instruction translation or provides libraries for other architectures.
     - \ ``arm64-v8a``, ``armeabi-v7a``, ``armeabi``\


.. _reference_addons-env-variables:

Environment variables
=====================

When addon hooks are invoked, several environment variables are set to
provide context to the addon.

The following variables are available:


.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Possible values
   * - ADDON_DIR
     - Directory of the addon whose hook is currently running.
     -
   * - ANBOX_DIR
     - Path to the Anbox directory.
     - \ ``/var/lib/anbox``\
   * - ANDROID_ROOTFS
     - Path to the Android RootFS.
     - \ ``/var/lib/anbox/rootfs``\
   * - BOOT_PACKAGE
     - Boot package of the APK.
     -
   * - CONTAINER_TYPE
     - Type of container being run.
     - \ ``regular`` (container running an application or a raw image)\ ``base`` (container bootstrapping, thus creating or updating, an application)
   * - ANBOX_EXIT_CODE
     - \ *``post-stop`` hook only:* Exit code of the Anbox process.
     - \ ``0`` if no error occurred, otherwise set to the actual return code.


.. _reference_addons-hooks:

Hooks
=====

An addon is a collection of hooks that are invoked at different points
in time in the life cycle of a container. A hook can be any executable
file as long as its name is one of the following:


.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - pre-start
     - Executed **before** Android is started. If the hook crashes, the container fails to start.
   * - post-start
     - Executed **after** Android is started. If the hook crashes, the container stops.
   * - post-stop
     - Executed **after** Android is stopped. If the container crashes, this hook might not be invoked.
   * - install (deprecated)
     - DEPRECATED: Use ``pre-start`` instead. Executed during the application bootstrap when the addon is installed.
   * - prepare (deprecated)
     - DEPRECATED: Use ``post-start`` instead. Executed during the application bootstrap when Android is running.
   * - restore (deprecated)
     - DEPRECATED: Use ``pre-start`` instead. Executed before Android starts.
   * - backup (deprecated)
     - DEPRECATED: Use ``post-stop`` instead. Executed after Android shuts down.


The following figure shows when the different hooks are executed in the
life cycle of a container (base container or regular container).

.. figure:: /images/addons-reference-hook-order.svg
   :alt: Hooks execution in the life cycle of a container

   Hooks execution in the life cycle of a container

Hook timeouts
-------------

All hooks are subject to a 5 minute timeout to avoid blocking a
container for too long.

A hook that runs into a timeout exits with an error.
