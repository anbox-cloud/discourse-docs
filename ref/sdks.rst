.. _reference_sdks:

================
Anbox Cloud SDKs
================

Anbox Cloud provides a series of Software Development Kits (SDKs) to
facilitate integrating and extending Anbox Cloud for different use
cases:

-  :ref:`Anbox Platform SDK <reference_sdks-anbox-platform-sdk>`
-  :ref:`AMS SDK <reference_sdks-ams-sdk>`
-  :ref:`Anbox Streaming SDK <reference_sdks-streaming-sdk>`

.. _reference_sdks-anbox-platform-sdk:

Anbox Platform SDK
==================

The Anbox Platform SDK provides support for developing custom platform
plugins, which allows cloud providers to integrate Anbox with their
existing infrastructure. The SDK provides several integration points for
things like rendering, audio or input processing.

For more details about custom platform plugins, refer to the `Anbox Platform SDK API documentation <https://anbox-cloud.github.io/1.10/anbox-platform-sdk/index.html>`_.

Download and installation
-------------------------

The Anbox Platform SDK can be downloaded via Git from GitHub:

::

   git clone https://github.com/anbox-cloud/anbox-platform-sdk.git

You need the following build dependencies:

::

   sudo apt install cmake-extras libavcodec-dev libavformat-dev libelf-dev libegl1-mesa-dev

Examples
--------

The Anbox Platform SDK provides a collection of example platform plugins
to help developers get started with plugin development. The following
examples are included:

-  ``minimal`` - A platform plugin that provides a dummy implementation
   of a minimal platform plugin to demonstrate the general plugin
   layout.
-  ``audio_streaming`` - A platform plugin that provides a more advanced
   example of how a platform plugin can process audio and input data.

.. _reference_sdks-ams-sdk:

AMS SDK
=======

The AMS SDK offers a set of `Go <https://golang.org/>`_ packages and
utilities for any external `Go <https://golang.org/>`_ code to be able
to connect to the AMS service through the exposed REST API.

See the `AMS SDK documentation <https://github.com/anbox-cloud/ams-sdk>`_ on GitHub for
more information.

.. _download-and-installation-1:

Download and installation
-------------------------

The AMS SDK can be downloaded via Git from GitHub:

::

   git clone https://github.com/anbox-cloud/ams-sdk.git

To start using the SDK, simply add the content of the provided SDK zip
file into your projects ``vendor/`` directory or your ``GOPATH``.

.. _examples-1:

Examples
--------

The AMS SDK comes with a set of examples demonstrating the capabilities
of the SDK. You can find them in the ``examples`` directory of the AMS
source.

Authentication setup
--------------------

Clients must authenticate to AMS before communicating with it. For more
information, see :ref:`howto_manage_ams-access`
and the `AMS SDK documentation <https://github.com/anbox-cloud/ams-sdk>`_ on GitHub.

.. _reference_sdks-streaming-sdk:

Anbox Streaming SDK
===================

The Anbox Streaming SDK allows the development of custom streaming
clients, using JavaScript or C/C++.

Components
----------

The Anbox Streaming SDK provides the following alternative SDKs:

-  A JavaScript SDK designed to help you get started with the
   development of a web-based client. This SDK handles all aspects of
   streaming, from the WebRTC protocol to handling controls, game pads,
   speakers and screen resolutions.
-  A native SDK offering a C API that provides the same full-featured
   video streaming as the JavaScript SDK, but aims for a low latency for
   your application based on Anbox Cloud. The native SDK is intended for
   C and C++ based applications. It currently supports Android and
   Linux.

Features
~~~~~~~~


.. list-table::
   :header-rows: 1

   * - Feature
     - JavaScript SDK
     - Native SDK
   * - Video streaming
     - ✓
     - ✓
   * - Audio streaming
     - ✓
     - ✓
   * - Microphone support
     - ✓
     - ✓
   * - Dynamically change Android foreground activity
     - ✓
     - ✓
   * - Send commands to the Android container
     - ✓
     - ✓
   * - Game pad support
     - ✓
     - ✓
   * - Camera support
     - ✓
     - 
   * - Sensor support
     - 
     - 
   * - Location support
     - ✓
     - 
   * - Supported platforms
     - All
     - Linux, Android
   * - Zero Copy rendering and decoding
     - ✓
     - 
   * - Supported codecs
     - VP8, H.264
     - VP8, H.264 (Android only)


.. _download-and-installation-2:

Download and installation
-------------------------

To use the Anbox Streaming SDK, you must have :ref:`deployed the Anbox Streaming Stack <howto_install_deploy-juju>`.

You can download the Anbox Streaming SDK via Git from GitHub:

::

   git clone https://github.com/anbox-cloud/anbox-streaming-sdk.git

.. _examples-2:

Examples
--------

The Anbox Streaming SDK comes bundled with examples to help you get
started. They are located in the ``examples`` directory.
