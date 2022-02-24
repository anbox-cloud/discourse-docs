:hide-toc:

.. _ref_glossary:

========
Glossary
========

Terms, concepts and abbreviations that are relevant for Anbox Cloud.

.. glossary::

Addon
  A piece of code that can be used to extend and customise images in Anbox Cloud.

  See https://discourse.ubuntu.com/t/addons/25293.

Amazon Web Services (AWS)
  A cloud platform provided by Amazon that can be used to host Anbox Cloud.

  See [the AWS website](https://aws.amazon.com/).

AMS Node Controller
  A service that runs on every LXD node and puts the appropriate firewall rules in place when a container is started or stopped.

AMS SDK
  An SDK that provides Go language bindings for connecting to AMS through the exposed REST API.

  See [AMS SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#ams-sdk).

Anbox
  A component of Anbox Cloud that facilitates booting an Android system on a regular GNU/Linux system. The concepts of the Anbox component in Anbox Cloud are similar to the [Anbox open source project](https://github.com/anbox/anbox), but the Anbox open source project is an independent project that is not related to or used in Anbox Cloud.

Anbox Application Manager (AAM)
  A utility (`aam`) that is installed in the Anbox image and that can be used for various tasks, for example, to back up and restore Android application data.

  See https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183.

Anbox Application Registry (AAR)
  A central repository for applications created in Anbox Cloud. Using an AAR is very useful for larger deployments to keep applications in sync.

  See https://discourse.ubuntu.com/t/anbox-application-registry-aar/17761.

Anbox Cloud
  A rich software stack that enables you to run Android applications in the cloud for all kinds of different use cases, including high-performance streaming of graphics to desktop and mobile client devices.

  See https://discourse.ubuntu.com/t/about-anbox-cloud/17802.

Anbox Cloud Appliance
  A self-contained, single-machine deployment variant of Anbox Cloud.

  See [Variants](https://discourse.ubuntu.com/t/about-anbox-cloud/17802#variants).

Anbox Management Client (AMC)
  The command line interface that is used to manage the Anbox Management Service (AMS).

Anbox Management Service (AMS)
  The service that handles all aspects of the application and container life cycle in Anbox Cloud. AMS is responsible for managing containers, applications, addons, updates and more, ensuring high density, performance and fast container startup times.

  AMS uses [etcd](https://etcd.io/) as database. It connects to LXD over its REST API.

  See https://discourse.ubuntu.com/t/anbox-management-service-ams/24321.

Anbox Platform SDK
  A C/C++ SDK that provides support for developing custom platform plugins, which allows users to integrate Anbox with their existing infrastructure.

  See [Anbox Platform SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#anbox-platform-sdk).

Anbox shell
  A command-line tool (`anbox-shell`) that provides an ADB shell with root permissions granted, which you can use to access the Android system in the container.

  See [Access a container with amc](https://discourse.ubuntu.com/t/access-a-container/17772#amc).

Anbox Streaming SDK
  An SDK that allows the development of custom streaming clients, using JavaScript or C/C++.

  See [Anbox Streaming SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#streaming-sdk).

Android app
  An application for the Android mobile operating system, usually provided as APK. To distinguish Android apps from Anbox Cloud applications, this documentation refers to Android apps as "apps", not "applications".

Android Archive (AAR)
  A compiled version of an Android library that can be used as a dependency for an Android app module.

  See [Create an Android library](https://developer.android.com/studio/projects/android-library) in the Android developer documentation.

Android Debug Bridge (ADB)
  A command-line tool that is included in the Android SDK Platform-Tools package and that allows to connect to and communicate with an Android device from your computer.

  See [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb) in the Android developer documentation.

Android Package Kit (APK)
  The file format used to package apps for the Android operating system.

Appium
  An open-source test automation tool that can be used to test native, mobile and hybrid web applications on Android.

  See [the Appium website](http://appium.io/).

Application
  One of the main objects of Anbox Cloud. An application encapsulates an Android app and manages it within the Anbox Cloud cluster.

  See https://discourse.ubuntu.com/t/about-applications/17760.

Application container
  A container that is created when launching an application.

  See [Application containers vs. raw containers](https://discourse.ubuntu.com/t/about-containers/17763#application-vs-raw).

Application manifest
  A file that defines the attributes of an Anbox Cloud application.

  See https://discourse.ubuntu.com/t/application-manifest/24197.

Base container
  A temporary container that is used when bootstrapping an application. It is automatically deleted when the application bootstrap is completed.

  See https://discourse.ubuntu.com/t/about-containers/17763#regular-vs-base.

Boot package
  The package to launch in an application container once the system has booted.

Bootstrap process
  The process that builds the application and optimises it to run on Anbox Cloud.

  See [Bootstrap process](https://discourse.ubuntu.com/t/about-applications/17760#bootstrap).

Container
  One of the main objects of Anbox Cloud. Every time you launch an application or image, Anbox Cloud creates a container for it. Every container provides a full Android system.

  See https://discourse.ubuntu.com/t/about-containers/17763.

Core stack
  The core parts of the Anbox Cloud stack that are required for all deployments. As a bare minimum, an Anbox Cloud deployment requires the following services:

  - AMS
  - etcd
  - At least 1 LXD worker
  - 1 AMS Node Controller per LXD worker
  - Easy-RSA

  See https://discourse.ubuntu.com/t/about-anbox-cloud/17802.

Coturn
  An open-source implementation of a STUN/TURN server needed for WebRTC to work behind NATs and firewalls.

  See [the Coturn project on GitHub](https://github.com/coturn/coturn).

Grafana
  A tool for analytics and monitoring that allows to query and visualise the metrics of the cluster or individual containers and generate alerts based on the data.

  See https://discourse.ubuntu.com/t/use-grafana/17787 and [the Grafana website](https://grafana.com/).

Graphics Processing Unit (GPU)
  A specialised processor that is designed to accelerate image processing and graphics rendering for output to a display device.

High availability (HA)
  The characteristic of a system to continuously be available without failing for a higher-than-normal period of time. Anbox Cloud ensures high availability by keeping replicas of every service, which avoids having a single point of failure.

  See https://discourse.ubuntu.com/t/enable-high-availability/17754.

Hook
  Code that is invoked at different points in time in the life cycle of a container. Hooks are part of addons.

  See [Hooks](https://discourse.ubuntu.com/t/addons/25293#hooks).

Image
  The base for a container, which contains all necessary components like Anbox or the Android root file system. Anbox Cloud provides images based on different Android and Ubuntu versions and different architectures.

  See https://discourse.ubuntu.com/t/manage-images/17758 and https://discourse.ubuntu.com/t/provided-images/24185.

Instance type
  An abstraction for a set of resources that is available to a container.

  See https://discourse.ubuntu.com/t/instance-types/17764.

Juju
  A charmed operator framework that helps you deploy, integrate and manage applications across multiple environments. Anbox Cloud is installed using Juju. The Anbox Cloud Appliance uses Juju under the hood.

  See [the Juju website](https://juju.is/).

LXD
  A system container and virtual machine manager that offers a unified user experience around full Linux systems running inside containers or virtual machines. Anbox Cloud is based on LXD.

  See [the LXD website](https://linuxcontainers.org/).

Monitoring stack
  A reference implementation for basic monitoring functionality based on Prometheus, Grafana and Telegraf. Anbox Cloud does not provide a full monitoring solution, but the reference implementation can be used as a starting point for implementing a custom solution.

  See https://discourse.ubuntu.com/t/install-the-monitoring-stack/17786.

Nagios
  A tool for monitoring the status of critical infrastructure like networks, servers and applications.

  See [the Nagios website](https://www.nagios.org/).

Neural Autonomic Transport System (NATS)
  An open-source messaging system that the components of the streaming stack use to communicate.

  See [the NATS website](https://nats.io/).

Platform
  An abstraction layer that is provided by Anbox to access the hardware resources of the host system from the Android system. Anbox Cloud supports three platforms: null (without rendering), webrtc (WebRTC) and swrast (software rendering).

  See https://discourse.ubuntu.com/t/anbox-platforms/18733.

Prometheus
  An open-source application used for event monitoring and alerting, which records real-time metrics about system events.

  See [the Prometheus website](https://prometheus.io/).

Raw container
  A container that is created when launching an image. It runs the full Android system, without any additional apps installed.

  See [Application containers vs. raw containers](https://discourse.ubuntu.com/t/about-containers/17763#application-vs-raw).

Regular container
  A container that is launched from either an application or an image. It exists until it is deleted.

  See https://discourse.ubuntu.com/t/about-containers/17763#regular-vs-base.

Scrcpy
  An open-source screen mirroring application that allows displaying and controlling Android devices from a desktop computer.

  See [the scrcpy project on GitHub](https://github.com/Genymobile/scrcpy).

Session
  The interaction between a streaming client and the application container during streaming. A session contains, among other information, user data and application information and provides an entry point for both the client and the container to start the signalling process.

  See https://discourse.ubuntu.com/t/about-application-streaming/17769.

Snap
  A software package for a desktop, cloud or IoT application that is easy to install, secure, cross‐platform and dependency‐free.

  See [the Snapcraft website](https://snapcraft.io/).

Software Rasterization (swrast)
  An LLVMpipe-based software rendering platform that is useful for visual tests but does not provide audio input/output.

  See https://discourse.ubuntu.com/t/anbox-platforms/18733.

Stream agent
  The software running on a server connected to Anbox Cloud, which connects AMS to the stream gateway and allows distribution from the gateway to multiple independent AMS installations.

  See https://discourse.ubuntu.com/t/about-application-streaming/17769.

Stream gateway
  The central component that connects clients with stream agents. Its role is to choose the best possible region depending on the user location and server capacities.

  See https://discourse.ubuntu.com/t/about-application-streaming/17769.

Streaming stack
  A collection of components designed to run containers and stream their visual output to clients via WebRTC. Streaming can happen through GPUs or through software rendering.

  See https://discourse.ubuntu.com/t/about-application-streaming/17769.

STUN/TURN server
  A server that finds the most optimal network path between a client and the container running its application.

Ubuntu Advantage for Applications
  Canonical’s service package for Ubuntu that provides enterprise security and support for open-source applications, with managed service offerings available. Note the difference between Ubuntu Advantage for Infrastructure and Ubuntu Advantage for Applications; Anbox Cloud requires a Ubuntu Advantage for Applications subscription.

  See [Ubuntu Advantage](https://ubuntu.com/support).

Ubuntu One
  A central user account system used by all Canonical sites and services. You need a Ubuntu One account to purchase the Ubuntu Advantage for Applications subscription that is required to run Anbox Cloud, and to log into the web dashboard.

  See [Ubuntu One](https://login.ubuntu.com/).

Watchdog
  A software component that monitors the app in a container and terminates the container if the app crashes or is moved to the background.

  See [Watchdog settings](https://discourse.ubuntu.com/t/application-manifest/24197#watchdog).

Web dashboard
  A web GUI for Anbox Cloud from where developers can create, manage and stream applications from their web browser.

  See https://discourse.ubuntu.com/t/use-the-web-dashboard/20871.

WebRTC
  A standard for media capture devices and peer-to-peer connectivity that can be used to add real-time communication capabilities to an application. It supports video, voice, and generic data to be sent between peers.

  See [the WebRTC website](https://webrtc.org/).
