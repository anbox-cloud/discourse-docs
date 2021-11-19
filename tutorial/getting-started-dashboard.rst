.. _tutorial_getting-started-dashboard:

===============================
Getting started (web dashboard)
===============================

This tutorial guides you through the first steps of using Anbox Cloud.
You will learn how to create and access a virtual Android device or an
application using the :ref:`web dashboard <howto_manage_web-dashboard>`.

The web dashboard provides an easy-to use interface to Anbox Cloud.
However, it currently supports a limited set of functionality, which
means that it might not be sufficient for all use cases. If you want to
learn how to manage Anbox Cloud from the command line, see the :ref:`Getting started with Anbox Cloud (CLI) <tutorial_getting-started>`
tutorial.

.. important::
   If you haven’t installed
   Anbox Cloud or the Anbox Cloud Appliance yet, you must do so before you
   can continue with this tutorial. See the following documentation for
   installation instructions:

   -  :ref:`Installing the Anbox Cloud Appliance <tutorial_installing-appliance>`
   -  :ref:`howto_install_landing`
      (note that you must install the streaming stack for the web dashboard
      to be available)

.. _tutorial_getting-started-dashboard-virtual-device:

1. Create a virtual device
==========================

Let’s start exploring what Anbox Cloud can do by launching a virtual
device that runs a specific Android version.

.. note::
   With “virtual device” we mean a
   simulated device that runs a plain Android operating system without any
   special apps installed. Technically speaking, Anbox Cloud treats such a
   virtual device as an “empty” application, thus an application that is
   not running a specific APK.

Complete the following steps to create a virtual device:

1. Open ``https://<your-machine-address>/applications`` in your browser.

   .. note::
      By default, the Anbox Cloud
      Appliance uses self-signed certificates, which might cause a security
      warning in your browser. Use the mechanism provided by your browser
      to proceed to the web page.
2. Click **Add Application**.
3. Enter a name for the application, for example,
   ``virtual-device-web``.
4. Keep the pre-selected instance type.
5. Select the Android image that you want to use, for example,
   ``bionic:android11:arm64``.
6. Do not upload an APK file.
7. Click **Add Application**.

   .. figure:: /images/gs_dashboard_add_virtual_device.png
      :alt: Add a virtual device

      Add a virtual device
8. Wait until the application status changes to ``ready``.

2. Launch and test the virtual device
=====================================

When the application has been initialised and its status changes to
``ready``, complete the following steps to launch and test the virtual
device:

1. In the list of applications, click the play button (labelled **New
   session**) for the application to start a new session.

   .. figure:: /images/gs_dashboard_new_session.png
      :alt: Start a new session

      Start a new session
2. Accept the default settings and click **New Session**.

   .. figure:: /images/gs_dashboard_start_session.png
      :alt: Start with default settings

      Start with default settings
3. When the stream has loaded, you can interact with your virtual
   device.

3. Create an application from an APK
====================================

To create an application for a specific Android app, follow the steps in
:ref:`1. Create a virtual device <tutorial_getting-started-dashboard-virtual-device>`, but upload the APK of
the Android app.

.. important::
   Not all Android apps are
   compatible with Anbox Cloud. See :ref:`Issues when porting Android apps <explanation_porting-issues>`
   for more information.

Choose an :ref:`instance type <reference_instance-types>`
that is suitable for your application. If your instance is equipped with
a GPU and your application requires the use of the GPU for rendering and
video encoding, select an instance type with GPU support like ``g2.3``.
For other instance types, the container will use a GPU if available or
software encoding otherwise.

.. figure:: /images/gs_dashboard_add_application.png
   :alt: Add an application

   Add an application

You can launch and test the application in the same way as you did for
the virtual device.

4. Update an application
========================

You can have several versions of an application. See :ref:`howto_application_update`
for detailed information.

Complete the following steps to add a new version to your application:

1. Open ``https://<your-machine-address>/applications`` in your browser.
2. Click the **Edit application** button next to the application for
   which you want to add a new version.

   .. figure:: /images/gs_dashboard_edit_application.png
      :alt: Update an application

      Update an application
3. Upload a new APK, or do other changes to the configuration.
4. Click **Update application**.

Done!
=====

You now know how to use the web dashboard to create, launch and test
applications in Anbox Cloud.

If you are interested in more advanced use cases, check out the :ref:`Getting started with Anbox Cloud (CLI) <tutorial_getting-started>` tutorial
to learn how to use Anbox Cloud from the command line.

Also see the documentation about :ref:`how to manage applications <howto_application_landing>`
and :ref:`how to work with containers <howto_container_landing>`.
