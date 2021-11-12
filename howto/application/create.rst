.. _howto_application_create:

=====================
Create an application
=====================

Every application which should be available on an Anbox Cloud cluster
must be created first.

The internal process will prepare a container based on the currently
available image with the application package installed. This container
is then used for any newly launched containers to support fast boot
times.

Preparation
===========

To create an application, you need an Android package (APK) with support
for the target architecture. Additionally, you must select one of the
available instance types for the application. The instance type defines
CPU/RAM constraints put onto the container launch for the application.

.. note::
   See :ref:`reference_instance-types`
   for a list of available instance types.

To create a new application, you must first create a manifest file to
define the various attributes the new application should have. The
manifest is a simple `YAML <http://yaml.org/>`_ file and looks like
this:

.. code:: yaml

   name: candy
   instance-type: a2.3
   image: default
   boot-activity: com.canonical.candy.GameApp
   required-permissions:
     - android.permission.WRITE_EXTERNAL_STORAGE
     - android.permission.READ_EXTERNAL_STORAGE
   addons:
     - ssh
   tags:
     - game
   extra-data:
     com.canonical.candy.obb:
       target: /data/app/com.canonical.candy-1/lib
     game-data-folder:
       target: /sdcard/Android/data/com.canonical.candy/
   watchdog:
     disabled: false
     allowed-packages:
       - com.android.settings
   services:
     - name: adb
       port: 5559
       protocols: [tcp]
       expose: false
   resources:
     memory: 4GB
     disk-size: 8GB

See :ref:`reference_application-manifest`
for detailed information about all available attributes.

Create from a directory
=======================

When creating an application from a directory, the directory should
contain the required components for the creation:

-  ``manifest.yaml``
-  ``app.apk``
-  ``extra-data`` (optional)

.. note::
   Due to Snap strict confinement,
   the directory must be located in the home directory.

With everything in place, create the application by entering the
following command:

::

   amc application create <path/to/application-content>

When the ``create`` command returns, the application package is uploaded
to the AMS service and the :ref:`bootstrap process <explanation_applications-bootstrap>`
is started. The application is not yet ready to be used. You can watch
the status of the application with the following command:

::

   amc application show bcmap7u5nof07arqa2ag

The returned output looks similar to the following:

.. code:: bash

   id: bcmap7u5nof07arqa2ag
   name: candy
   status: initializing
   published: false
   config:
     instance-type: a2.3
     boot-package: com.canonical.candy
   versions:
     0:
       image: bf7u4cqkv5sg5jd5b2k0 (version 0)
       published: false
       status: initializing
       addons:
       - ssh
       boot-activity: com.canonical.candy.GameApp
       required-permissions:
       - android.permission.WRITE_EXTERNAL_STORAGE
       - android.permission.READ_EXTERNAL_STORAGE
       extra-data:
         com.canonical.candy.obb:
           target: /data/app/com.canonical.candy-1/lib
         game-data-folder:
           target: /sdcard/Android/data/com.canonical.candy/
       watchdog:
         disabled: false
         allowed-packages:
         - com.android.settings
       services:
       - port: 5559
         protocols:
         - tcp
         expose: false
         name: adb
   resources:
     memory: 4GB
     disk-size: 8GB

Once the status of the application switches to ``ready``, the
application is ready and can be used. See :ref:`howto_application_wait`
for information about how to monitor the application status.

Create from a tarball
=====================

An application can also be created from a tarball file. The tarball file
must be compressed with bzip2 and must use the same components and
structure as the directory.

.. note::
   Due to Snap strict confinement,
   the tarball file must be located in the home directory.

For example, a tarball can be created with the following command:

::

   tar cvjf foo.tar.bz2 -C <package-folder-path> app.apk extra-data manifest.yaml

Once the tarball is created, you can create the application:

::

   amc application create foo.tar.bz2

The AMS service now starts the application :ref:`bootstrap process <explanation_applications-bootstrap>`.
See :ref:`howto_application_wait`
for information about how to monitor the application status.
