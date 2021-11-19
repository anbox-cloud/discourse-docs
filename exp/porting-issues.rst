.. _explanation_porting-issues:

================================
Issues when porting Android apps
================================

When porting an Android application to Anbox Cloud usually in the form
of APK, there are a few issues that can cause an application to not
function properly, they are:

-  Missing Dependency
-  Missing Runtime Permissions
-  Mismatched Architecture
-  Strict Watchdog Restriction
-  Support OBB Files

Missing Dependency
==================

Google Play services are not supported by Anbox Cloud. If an application
requires Google Play services to run, then it can **not** be ported to
Anbox Cloud.

Missing Runtime Permissions
===========================

An application can not automatically grant themselves permissions upon
its creation. When creating an application in AMS, you have to specify
the runtime permissions that are required by an application to run in
the Anbox Cloud.

To list all required runtime permissions of an application, you can use
the `AAPT2 <https://developer.android.com/studio/command-line/aapt2>`_
to find out:

.. code:: bash

   $ aapt2 dump permissions <path to apk>

Then add the required permissions to top-level key
``required-permissions`` in the application ``manifest.yaml``, for
example:

.. code:: yaml

   ....
   required-permissions:
     - android.permission.WRITE_EXTERNAL_STORAGE
     - android.permission.READ_EXTERNAL_STORAGE
     - android.permission.INTERNET
   ....

A convenient way of granting all required runtime permissions to an
application is following:

.. code:: yaml

   ....
   required-permissions:  ['*']
   ....

Anbox will grant all permissions automatically when creating an
application in AMS.

Mismatched Architecture
=======================

In most cases, an Android application is not distributed as a universal
APK. If the application contains native libraries, the `ABI split approach <https://developer.android.com/studio/build/configure-apk-splits>`_
is used to produce different APK files for the different architectures.
Before creating an application in AMS, you need to know the supported
architecture by the APK which is used for AMS application creation.
There are quite a few ways to detect what architecture an APK’s native
libraries are built for. Since an APK file is no more than a zip file,
one straight forward way to check that is to unzip the APK file and see
the subfolders inside the ``libs`` folder. Typically they are:

-  ``armeabi-v7a``: native code compiled for the ARMv7 architecture CPUs
   (32-bit)
-  ``arm64-v8a``: native code compiled for the ARMv8 architecture CPUs
   (64-bit)
-  ``x86``: native code compiled for the x86 architecture CPUs (32-bit)
-  ``x86_64``: native code compiled for x86-64 architecture CPUs
   (64-bit)

Depends on your Anbox Cloud deployment architecture, if the container
layer is running on 64-bit x86 hardware, The APKs that support ``x86``
and ``x86_64`` architectures can be used to create an AMS application.
If the container layer is running on 64-bit Arm hardware, only
``armeabi-v7a`` and ``arm64-v8a`` based APKs can.

Support OBB Files
=================

Android `has a 100MB limit on applications <https://developer.android.com/google/play/expansion-files.html>`_.
Applications under that limit can be created using the regular
:ref:`method <howto_application_create>`.
Larger applications however need to be split up into the main part as an
APK file and the expansion part as an OBB file.

-  APK - Contains the executables and native libraries (``*.so`` files),
   plug-ins, basic assets, and data required by the application to load
   for the first time.
-  OBB - Contains the remaining assets (high-fidelity graphics, media
   files, or other large resource files) for full application user
   experience.

Creating this type of application in AMS is supported but requires a few
more steps.

Let’s assume that you have an application which consists of APK file and
an OBB file separately, they are:

.. code:: bash

   .
   ├── com.foo.bar.apk
   └── main.203779.com.foo.bar.obb

Rename ``com.foo.bar.apk`` to ``app.apk`` and create a sub-folder named
``extra-data`` where you need to move the ``.obb`` file. Declare the obb
file as an extra data in the application manifest.

The final application folder should look like the following:

.. code:: bash

   .
   ├── app.apk
   ├── extra-data
   │   └── main.203779.com.foo.bar.obb
   ├── manifest.yaml

And its manifest.yaml like this:

.. code:: yaml

   name: com.foo.bar
   instance-type: a2.3
   required-permissions: ['*']
   extra-data:
     main.203779.com.foo.bar.obb:
       target: /sdcard/Android/obb/com.foo.bar/

Then create the application:

.. code:: bash

   $ amc application create .

Upon application installation, the ``.obb`` file will be copied to the
destination folder as defined in ``manifest.yaml``. Then when launching
a regular container from the created application, the ``.obb`` file will
be automatically loaded on startup.

The destination location of ``.obb`` file may vary depending on the
applications. Some applications load the obb file from the SD card
``/sdcard/Android/obb/``, but some load it from device internal storage
``/data/media/obb``. If an obb file is not properly installed in the
container, an application may not function as expected. Some
applications exit immediately once the required obb file is not found,
which triggers the
:ref:`watchdog <reference_application-manifest-watchdog>`
in the end and cause the container to end up in an error state.

Strict Watchdog Restriction
===========================

The
:ref:`watchdog <reference_application-manifest-watchdog>`
is enabled by default upon application creation. It’s tricky to identify
a problem or debug a porting issue when a watchdog is enabled since a
container will be terminated when a watchdog is triggered.

To overcome the problem introduced by watchdog and facilitate
application porting, it’s recommended to disable the watchdog settings
for the time being upon application creation. This can be done with the
top-level key ``watchdog`` in the application ``manifest.yaml``:

.. code:: yaml

   ...
   watchdog:
     disabled: true
   ...

If the application porting is complete, please enable watchdog again so
that Anbox can collect tombstones or
`ANR <https://developer.android.com/topic/performance/vitals/anr>`_
once a crash happens during the application runtime and terminate the
container in time.

Some applications require to interact with other apps for something like
account setup or permission grants in Android settings application.
Calling another application from the boot application would move the
running application to the background and cause a watchdog to trigger.
In this case, you can extend the allowed packages list for watchdog by
specifying ``allowed-packages`` under the top-level key ``watchdog`` in
the application ``manifest.yaml``, For example:

.. code:: yaml

   ...
   watchdog:
     disabled: false
     allowed-packages:
       - com.android.settings
   ...

This will allow boot application to launch Android setting application
during its runtime but not triggering a watchdog.
