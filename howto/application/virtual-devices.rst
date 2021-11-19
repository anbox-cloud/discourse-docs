.. _howto_application_virtual-devices:

=======================
Create a virtual device
=======================

Anbox Cloud allows you to stream the whole Android experience next to
just individual applications. The following sections will show how to
setup such a virtual Android device experience on top of an existing
Anbox Cloud deployment.

Create an Application for the Virtual Device
============================================

In order to create a virtual device experience we first have to create
an application with AMS. This application will not contain any APK and
with that will start directly into the Android system launcher and
provide the full Android experience.

A very simple application manifest for such an application looks like
this:

.. code:: bash

   $ cat manifest.yaml
   name: vdev
   instance-type: a4.3

.. note::
   If you want to use a GPU for
   containers created for you new vdev application, use an :ref:`instance type <reference_instance-types>`
   with GPU support like ``g4.3``.

Extend the Application with Addons
==================================

You can also extend the application with
:ref:`addons <reference_addons>` which install
additional applications you want to offer as part of your default
experience. You can for example replace the standard Android launcher
with a custom one like `Lawnchair <https://lawnchair.app/>`_.

.. code:: bash

   $ mkdir -p vdev-support/hooks
   $ cd vdev-support
   $ curl -o lawnchair.apk https://f-droid.org/repo/ch.deletescape.lawnchair.plah_2001.apk
   $ cat << EOF > manifest.yaml
   name: vdev-support
   description: |
     Addon installing and configuring the Lawnchair launcher as the systems default one
   $ touch hooks/post-start hooks/pre-start
   $ cat << EOF > hooks/pre-start
   #!/bin/sh -ex
   exit 0
   EOF
   $ cat << EOF > hooks/post-start
   #!/bin/sh -ex
   cp "$ADDON_DIR"/lawnchair.apk /var/lib/anbox/data/
   anbox-shell pm install -g -t /data/lawnchair.apk

   # We need to wait until the system has settled after the package installation
   sleep 10

   # Setup lawnchair as our default launcher
   LAUNCHER_ACTIVITY="ch.deletescape.lawnchair.plah/ch.deletescape.lawnchair.Launcher"
   anbox-shell cmd package set-home-activity "$LAUNCHER_ACTIVITY"

   # Once we applied all of our changes we give Android a moment. If we directly
   # return here the Android container will be immediately shutdown.
   sleep 20
   EOF

   $ chmod +x hooks/*
   $ amc addon add vdev-support .

Once the addon is uploaded to AMS, you can reference it from your
application manifest:

.. code:: bash

   $ cat manifest.yaml
   name: vdev
   instance-type: a4.3
   addons: [vdev-support]

The application will now include the
`Lawnchair <https://lawnchair.app/>`_ and has it configured as the
default system launcher.

Launching the new Application
=============================

Now that we have the application created in AMS we can go ahead and
stream it through the UI of the Anbox Stream Gateway (see :ref:`Getting started with Anbox Cloud (web dashboard) <tutorial_getting-started-dashboard>`
for more details) or your own custom client application built with the
:ref:`Anbox Streaming SDK <reference_sdks-streaming-sdk>`.

.. figure:: /images/virtual_device_launch.png
   :alt: Launch a virtual device

   Launch a virtual device
