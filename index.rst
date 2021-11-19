=========================
Anbox Cloud documentation
=========================

Anbox Cloud provides a rich software stack that enables you to run
Android applications in the cloud for all kinds of different use cases,
including high-performance streaming of graphics to desktop and mobile
client devices.

Using container technology, Anbox Cloud is scalable from a
single-machine installation that can run scores of single Android
systems to an entire cluster of machines. It is based on powerful and
battle-proven software from Canonical like
`LXD <https://linuxcontainers.org/>`__ and
`Juju <https://jujucharms.com/>`_.

Core features
=============

-  Simple and straightforward deployment
-  Management of the container and application life cycle while
   optimising for high density, performance and fast container boot
   times
-  Platform integration tools to allow, for example, integration of
   existing streaming solutions
-  Support for both x86 and Arm64 hardware, providing the same set of
   features

See the `official Anbox Cloud website <https://anbox-cloud.io/>`_ for
more information.

Get started
===========


.. list-table::
   :header-rows: 1

   * -
     -
   * - :ref:`explanation_anbox-cloud`
     - Learn about the differences between Anbox Cloud and the Anbox Cloud Appliance and about the components and architecture of the offering
   * - :ref:`explanation_ams`
     - Understand the Anbox Management Service (AMS), which handles all aspects of the application and container life cycle
   * - :ref:`tutorial_installing-appliance`
     - Install the Anbox Cloud Appliance, which is well suited for initial prototype and small scale deployments
   * - :ref:`howto_install_deploy-juju`
     - Deploy the full Anbox Cloud solution to a public cloud
   * - :ref:`tutorial_getting-started-dashboard`

       :ref:`tutorial_getting-started`
     - Go through the first steps of launching and accessing an Android container to familiarise yourself with Anbox Cloud, by using either the web dashboard or the command line interface


What’s new
==========

Along with bug fixes and general improvements, Anbox Cloud 1.12 comes
with:

-  Android 12
-  Improved density for NVIDIA GPUs


.. list-table::
   :header-rows: 1

   * -
     -
   * - :ref:`release-notes`
     - All new features, improvements and bug fixes
   * - :ref:`roadmap`
     - Planned updates and features for upcoming releases


.. toctree::
   :titlesonly:
   :hidden:

   Home <self>
   tut/landing
   howto/landing
   ref/landing
   exp/landing
   anbox/landing
