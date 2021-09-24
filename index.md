Anbox Cloud offers a software stack that runs Android applications in any cloud enabling high-performance streaming of graphics to desktop and mobile client devices.

At its heart, it uses lightweight container technology instead of full virtual machines to achieve higher density and better performance per host while ensuring security and isolation of each container. Depending on the target platform, payload, and desired application performance (e.g. frame rate), more than 100 containers can be run on a single machine.

For containerization of Android, Anbox Cloud uses the well established and secure container hypervisor [LXD](https://linuxcontainers.org/). LXD is secure by design, scales to a large number of containers and provides advanced resource management for hosted containers.

Also have a look at the [official Anbox Cloud website](https://anbox-cloud.io/) for more information.

## What Anbox Cloud offers
Anbox Cloud provides management of an entire cluster of machines running the Anbox Cloud software and maintains a single Android system per container. It is based on powerful and battle proven software from Canonical like [LXD](https://linuxcontainers.org/) or [Juju](https://jujucharms.com/).

Its core features are:
* Simple and straightforward deployment using [Juju](https://jujucharms.com/) on any cloud
* Specialized management service to handle all aspects of the container and application lifecycle while optimizing the cluster for high density, performance and faster container boot times
* Platform integration tools including a rich SDK to allow integration of existing streaming solutions in the Anbox Cloud platform
* Support for both x86 and Arm64 hardware
* Integrates with 3rd party solutions for binary translation solutions on Arm64-only hardware

## What's new in 1.11?

Along with bugfixes and general improvements, Anbox Cloud 1.11 comes with:

* Client-side virtual keyboard
* Hardware accelerated video decoding (H.264, Nvidia GPUs only)
* Experimental WiFi support

Check the [release notes](https://discourse.ubuntu.com/t/release-notes/17842) for more details.

## Navigation

[details=Navigation]
| Level | Path | Navlink |
| -- | -- | -- |
| 0 | | Anbox Cloud |
| 1 | installation/installation-requirements | [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) |
| 1 | changelog | [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)|
| 1 | roadmap | [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)|
| 1 | supported-versions | [Supported versions](https://discourse.ubuntu.com/t/supported-versions/21046)|
| 1 | component-versions | [Component versions](https://discourse.ubuntu.com/t/component-versions/21413)|
| 0 | | Tutorials |
| 1 | installation/installation-appliance | [Installing the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) |
| 1 | manage/getting-started | [Getting started](https://discourse.ubuntu.com/t/getting-started/17756)|
| 0 | | How to |
| 1 | howto/install/landing | [Install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336)|
| 2 | installation/installation-quickstart | [Deploy with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) |
| 2 | installation/installation-customizing | [Customise the installation](https://discourse.ubuntu.com/t/installation-customizing/17747)|
| 2 | installation/high-availability | [Enable High Availability](https://discourse.ubuntu.com/t/high-availability/17754)|
| 2 | installation/validation | [Validate the deployment](https://discourse.ubuntu.com/t/validation/20329)|
| 1 | howto/update/landing | [Update your installation](https://discourse.ubuntu.com/t/update-your-installation/24331)|
| 2 | howto/update/upgrade-appliance | [Upgrade the appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186)|
| 2 | installation/upgrading-from-previous-versions | [Upgrade Anbox Cloud](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750)|
| 1 | howto/manage/landing| [Manage Anbox Cloud](https://discourse.ubuntu.com/t/manage-anbox-cloud/24337) |
| 2 | howto/manage/web-dashboard | [Use the web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)|
| 2 | howto/manage/managing-images | [Manage images](https://discourse.ubuntu.com/t/managing-images/17758)|
| 2 | howto/manage/managing-addons | [Create addons](https://discourse.ubuntu.com/t/managing-addons/17759)|
| 2 | howto/manage/managing-logs | [View logs](https://discourse.ubuntu.com/t/managing-logs/17771)|
| 2 | howto/manage/managing-ams-access | [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774)|
| 1 | howto/application/landing | [Manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) |
| 2 | howto/application/create | [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)|
| 2 | howto/application/wait | [Wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202)|
| 2 | howto/application/update | [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201)|
| 2 | howto/application/delete | [Delete an application](https://discourse.ubuntu.com/t/delete-an-application/24199)|
| 2 | howto/application/list | [List applications](https://discourse.ubuntu.com/t/list-applications/24200)|
| 2 | installation/installation-application-registry | [Deploy an AAR](https://discourse.ubuntu.com/t/installation-application-registry/17749)|
| 2 | howto/aar/configure | [Configure an AAR](https://discourse.ubuntu.com/t/configure-an-aar/24319)|
| 2 | howto/aar/revoke | [Revoke an AAR client](https://discourse.ubuntu.com/t/revoke-an-aar-client/24320)|
| 2 | usage/usecase-application-testing | [Test your application](https://discourse.ubuntu.com/t/usecase-application-testing/17775)|
| 2 | usage/usecase-virtual-devices | [Create a virtual device](https://discourse.ubuntu.com/t/virtual-devices/19069)|
| 1 | howto/container/landing | [Work with containers](https://discourse.ubuntu.com/t/work-with-containers/24335) |
| 2 | howto/container/launch | [Launch a container](https://discourse.ubuntu.com/t/launch-a-container/24327)|
| 2 | howto/container/wait | [Wait for a container](https://discourse.ubuntu.com/t/wait-for-a-container/24330)|
| 2 | manage/container-access | [Access a container](https://discourse.ubuntu.com/t/container-access/17772)|
| 2 | howto/container/expose-services | [Expose services](https://discourse.ubuntu.com/t/expose-services-on-a-container/24326)|
| 2 | howto/container/view-log | [View the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329)|
| 2 | howto/container/delete | [Delete a container](https://discourse.ubuntu.com/t/delete-a-container/24325)|
| 2 | howto/container/list | [List containers](https://discourse.ubuntu.com/t/list-containers/24328)|
| 2 | usage/usecase-container-configuration | [Configure geographic location](https://discourse.ubuntu.com/t/usecase-container-configuration/17782)|
| 2 | howto/containers/backup-and-restore | [Back up and restore application data](https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183)|
| 1 | howto/monitor/landing | [Monitor Anbox Cloud](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338) |
| 2 | monitoring/monitoring-installation | [Install the monitoring stack](https://discourse.ubuntu.com/t/monitoring-installation/17786)|
| 2 | monitoring/monitoring-grafana | [Use Grafana](https://discourse.ubuntu.com/t/monitoring-grafana/17787)|
| 2 | monitoring/monitoring-nagios | [Use Nagios](https://discourse.ubuntu.com/t/monitoring-nagios/17788)|
| 1 | howto/stream/landing | [Implement streaming](https://discourse.ubuntu.com/t/implement-streaming/24332) |
| 2 | howto/stream/access | [Access the stream gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784) |
| 2 | implement-android-native-streaming-client | [Implement a native client](https://discourse.ubuntu.com/t/implement-android-native-streaming-client/21833)|
| 2 | implement-web-based-streaming-client | [Implement a web-based client](https://discourse.ubuntu.com/t/implement-web-based-streaming-client/21835)|
| 2 | exchange-out-of-band-data | [Exchange OOB data](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)|
| 2 | integrate-keyboard | [Use a client-side keyboard](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643)|
| 1 | howto/cluster/landing | [Manage cluster nodes](https://discourse.ubuntu.com/t/manage-cluster-nodes/24334) |
| 2 | howto/cluster/scale-up | [Scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322)|
| 2 | howto/cluster/scale-down | [Scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323)|
| 1 | faq | [Troubleshoot Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-faq/17837)|
| 0 | | Reference |
| 1 | ref/provided-images | [Provided images](https://discourse.ubuntu.com/t/provided-images/24185)|
| 1 | sdks | [Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844)|
| 1 | ref/api-reference | [API reference](https://discourse.ubuntu.com/t/api-reference/24339) |
| 2 | reference/ams-rest-api-reference | [AMS HTTP API](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801)|
| 2 | reference/anbox-http-api-reference | [Anbox HTTP API](https://discourse.ubuntu.com/t/anbox-http-api-reference/17819)|
| 2 | reference/anbox-stream-gateway-reference | [Stream Gateway API](https://anbox-cloud.github.io/1.10/anbox-stream-gateway/index.html)|
| 2 | ref/anbox-platform-sdk-api | [Anbox Platform SDK API](https://anbox-cloud.github.io/1.10/anbox-platform-sdk/index.html)|
| 1 | manage/instance-types-reference | [Instance types](https://discourse.ubuntu.com/t/instance-types-reference/17764)|
| 1 | reference/anbox-platforms | [Anbox platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)|
| 1 | reference/prometheus-metrics | [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)|
| 1 | ams-configuration | [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)|
| 1 | ref/application-manifest | [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)|
| 1 | ref/lxd-docs | [LXD documentation](https://linuxcontainers.org/lxd/docs/master/index)|
| 0 | | Explanation |
| 1 | overview | [About Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) |
| 1 | exp/ams | [About AMS](https://discourse.ubuntu.com/t/about-ams/24321)|
| 1 | manage/managing-applications | [About applications](https://discourse.ubuntu.com/t/managing-applications/17760)|
| 1 | manage/application-registry | [About the AAR](https://discourse.ubuntu.com/t/application-registry/17761)|
| 1 | manage/managing-containers | [About containers](https://discourse.ubuntu.com/t/managing-containers/17763)|
| 1 | manage/capacity-planning | [About clustering](https://discourse.ubuntu.com/t/capacity-planning/17765)|
| 1 | manage/gpu-support | [About GPU support](https://discourse.ubuntu.com/t/gpu-support/17768)|
| 1 | manage/benchmarking-a-deployment | [About benchmarking](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770)|
| 1 | manage/streaming-android-applications | [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769)|
| 1 | usage/usecase-port-android-application-to-anbox-cloud | [Issues when porting apps](https://discourse.ubuntu.com/t/usecase-port-android-application-to-anbox-cloud/17776)|
[/details]

## Redirects

[details=Mapping table]
| Path | Location |
| ---- | -------- |
| /docs/install-appliance | /docs/installation/installation-appliance |
| /docs/lxd-auto-scaling | /docs/manage/capacity-planning |
| /docs/usage/usecase-streaming-sdk | /docs/sdks |
| /docs/reference/ams-sdk-api-reference | /docs/sdks |
[/details]
