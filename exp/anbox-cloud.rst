.. _exp_anbox-cloud:

=================
About Anbox Cloud
=================

Anbox Cloud provides a rich software stack that enables you to run
Android applications in the cloud for all kinds of different use cases,
including high-performance streaming of graphics to desktop and mobile
client devices.

At its heart, it uses lightweight container technology instead of full
virtual machines and maintains a single Android system per container.
This approach allows for higher density and better performance per host
while ensuring security and isolation of each container. Depending on
the target platform, payload and desired application performance (for
example, frame rate), Anbox Cloud can run more than 100 containers on a
single machine.

For containerisation of Android, Anbox Cloud uses the well established
and secure container hypervisor `LXD <https://linuxcontainers.org/>`__.
LXD is secure by design, scales to a large number of containers and
provides advanced resource management for hosted containers.

.. _exp_anbox-cloud-variants:

Variants
========

Anbox Cloud comes in two different variants that serve different
purposes:

**Anbox Cloud Appliance**

The Anbox Cloud Appliance is a self-contained, single-machine deployment
variant of Anbox Cloud. It uses a sensible standard configuration to
hide the complexity and flexibility of `Juju <https://juju.is/>`_. In
this way, the Anbox Cloud Appliance allows simple and fast development
and prototyping.

**Anbox Cloud**

The regular Anbox Cloud uses `Juju <https://juju.is/>`_ for deployment
and operations. It provides rich features and is ready made for a large
scale deployment.

See the following table for a comparison of features for the different
variants:


.. list-table::
   :header-rows: 1

   * - Feature
     - Anbox Cloud Appliance
     - Anbox Cloud
   * - :ref:`Streaming capabilities <exp_application-streaming>`
     - ✓
     - ✓
   * - :ref:`Web dashboard <howto_manage_web-dashboard>`
     - ✓
     - ✓
   * - :ref:`Android API version <ref_provided-images>`
     - 10, 11
     - 10, 11
   * - `Security updates <https://ubuntu.com/support>`_
     - ✓
     - ✓
   * - `Community support <https://discourse.ubuntu.com/c/anbox-cloud/>`_
     - ✓
     - ✓
   * - `Vendor support <https://anbox-cloud.io/contact-us>`_
     -
     - ✓
   * - :ref:`Monitoring <howto_monitor_landing>`
     -
     - ✓


Which of both variants you choose depends on your needs.
The appliance is well suited for quick prototyping and development or small scale deployments, whereas the regular Anbox Cloud is best to scale big.

.. tip::
   We recommend to always start with
   the Anbox Cloud Appliance for first tests. You can then expand to a full
   Anbox Cloud installation later.

Components
==========

Anbox Cloud is composed of different components that interact with one
another.

Core stack
----------

Anbox Cloud takes care of all management aspects and provides both a
fully functional implementation and an integration model to support
existing infrastructure and service implementations.

The following figure gives an overview of the different components and
their responsibility within the core stack of Anbox Cloud.

.. figure:: /images/anbox-core-overview.svg
   :alt: Anbox Cloud core stack

   Anbox Cloud core stack

At the heart of Anbox Cloud sits the :ref:`Anbox Management Service (AMS) <exp_ams>`. **AMS** has
the job to handle all aspects of the application and container life
cycle (including application and image updates) while ensuring high
density, performance and fast container startup times.

A developer or system administrator will manage **AMS** through the
**command line interface (AMC)** or through custom-built tools
interacting with the :ref:`ref_ams-http-api`.

For example, a simple Android application testing service would provide
a user-facing interface dealing with things like authentication and user
management, and would communicate with the REST API to add applications
or start and stop containers when a user asks to.

Anbox Cloud can be heavily customised and extended via :ref:`platform plugins <ref_sdks-anbox-platform-sdk>`
and :ref:`addons <howto_addons_landing>`.
Platform plugins and addons can be built to add specific streaming
capabilities, perform operations within Android containers and much
more. One example of a platform plugin is the :ref:`Anbox WebRTC Platform <ref_platforms>` used
in the Anbox Streaming Stack. Addons are ways to customise the base
image by installing additional software and running scripts on different
life cycle hooks.

Streaming stack
---------------

Starting from 1.4, Anbox Cloud comes with an easy to use streaming
solution. The :ref:`Anbox Streaming Stack <exp_application-streaming>`
is a collection of components designed to run containers on GPU-equipped
machines and stream their visual output to clients via
`WebRTC <https://webrtc.org/>`_.

The following figure shows an overview of how the different components
work together to enable this.

.. figure:: /images/anbox_cloud_streaming_stack.svg
   :alt: Streaming stack overview

   Streaming stack overview

The main components powering the streaming stack in Anbox Cloud are:

**Agent**: Software running on a server equipped with a GPU connected to
Anbox Cloud. It serves as an entry point that the gateway can connect
to.

**Anbox Stream Gateway**: The central component that connects clients
with agents. Its role is to choose the best possible region depending on
the user location and server capacities.

**Client**: The end user application that will display the stream. It
can be a desktop application, a website, a mobile application, a TV, a
car system or anything capable of handling a WebRTC stream. Anbox Cloud
provides an SDK along with the streaming stack to simplify integration
with web-based applications.

**TURN/STUN servers**: Servers that find the most optimal network path
between a client and the container running its application. The
streaming stack provides secure STUN and TURN servers, but you can use
public ones as well.

**NATS**: A messaging system that the different components use to
communicate (see the `project page <https://github.com/nats-io>`_).
