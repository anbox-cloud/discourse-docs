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
| 0 | | About |
| 1 | | [Home](https://discourse.ubuntu.com/t/anbox-cloud-documentation/17029) |
| 1 | overview | [Overview](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) |
| 0 | installation | [Installation](/t/anbox-cloud-installation/17835)|
| 1 | installation/installation-requirements | [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) |
| 1 | installation/installation-appliance | [Install Appliance](https://discourse.ubuntu.com/t/install-appliance/22681) |
| 1 | installation/installation-quickstart | [Install with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) |
| 0 | | Operations |
| 1 | installation/installation-customizing | [Customizations](https://discourse.ubuntu.com/t/installation-customizing/17747)|
| 1 | installation/installation-application-registry | [Application Registry](https://discourse.ubuntu.com/t/installation-application-registry/17749)|
| 1 | installation/upgrading-from-previous-versions | [Upgrade Anbox Cloud](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750)|
| 1 | howto/upgrade/upgrade-appliance | [Upgrade Anbox Cloud Appliance](tbd)|
| 1 | installation/high-availability | [High Availability](https://discourse.ubuntu.com/t/high-availability/17754)|
| 1 | installation/validation | [Validation](https://discourse.ubuntu.com/t/validation/20329)|
| 0 | | Managing Anbox Cloud |
| 1 | manage/getting-started | [Getting started](https://discourse.ubuntu.com/t/getting-started/17756)|
| 1 | manage/web-dashboard | [Dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)|
| 1 | manage/managing-images | [Images](https://discourse.ubuntu.com/t/managing-images/17758)|
| 2 | ref/provided-images | [Provided Images](tbd)|
| 1 | manage/managing-applications | [Applications](https://discourse.ubuntu.com/t/managing-applications/17760)|
| 1 | manage/managing-addons | [Addons](https://discourse.ubuntu.com/t/managing-addons/17759)|
| 1 | manage/application-registry | [Application Registry](https://discourse.ubuntu.com/t/application-registry/17761)|
| 1 | manage/managing-containers | [Containers](https://discourse.ubuntu.com/t/managing-containers/17763)|
| 1 | manage/capacity-planning | [Capacity Planning](https://discourse.ubuntu.com/t/capacity-planning/17765)|
| 1 | manage/gpu-support | [GPU Support](https://discourse.ubuntu.com/t/gpu-support/17768)|
| 1 | manage/managing-logs | [Logging](https://discourse.ubuntu.com/t/managing-logs/17771)|
| 1 | manage/managing-ams-access | [AMS Access](https://discourse.ubuntu.com/t/managing-ams-access/17774)|
| 1 | manage/container-access | [Container access](https://discourse.ubuntu.com/t/container-access/17772)|
| 1 | manage/benchmarking-a-deployment | [Benchmarking a deployment](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770)|
| 1 | manage/streaming-android-applications | [Streaming Android Applications](https://discourse.ubuntu.com/t/streaming-android-applications/17769)|
| 1 | lxd-auto-scaling | [LXD Auto Scaling](https://discourse.ubuntu.com/t/lxd-auto-scaling/21351)|
| 0 | | Using Anbox Cloud |
| 1 | usage/usecase-container-configuration | [Configure geographic location](https://discourse.ubuntu.com/t/usecase-container-configuration/17782)|
| 1 | howto/containers/backup-and-restore | [Back up and restore application data](tbd)|
| 1 | usage/usecase-port-android-application-to-anbox-cloud | [Port Android application to Anbox Cloud](https://discourse.ubuntu.com/t/usecase-port-android-application-to-anbox-cloud/17776)|
| 1 | usage/usecase-streaming-sdk | [Anbox Streaming SDK](https://discourse.ubuntu.com/t/usecase-streaming-sdk/17783)|
| 2 | implement-android-native-streaming-client | [Native streaming client](https://discourse.ubuntu.com/t/implement-android-native-streaming-client/21833)|
| 2 | implement-web-based-streaming-client | [Web-based streaming client](https://discourse.ubuntu.com/t/implement-web-based-streaming-client/21835)|
| 2 | exchange-out-of-band-data | [Out-of-band data](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)|
| 2 | integrate-keyboard | [Client-side virtual keyboard](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643)|
| 1 | usage/usecase-application-testing | [Application testing](https://discourse.ubuntu.com/t/usecase-application-testing/17775)|
| 1 | usage/usecase-virtual-devices | [Virtual Devices](https://discourse.ubuntu.com/t/virtual-devices/19069)|
| 0 | | Monitoring |
| 1 | monitoring/monitoring-installation | [Installation](https://discourse.ubuntu.com/t/monitoring-installation/17786)|
| 1 | monitoring/monitoring-grafana | [Grafana](https://discourse.ubuntu.com/t/monitoring-grafana/17787)|
| 1 | monitoring/monitoring-nagios | [Nagios](https://discourse.ubuntu.com/t/monitoring-nagios/17788)|
| 0 | | Reference |
| 1 | reference/ams-rest-api-reference | [AMS HTTP API](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801)|
| 1 | reference/anbox-http-api-reference | [Anbox HTTP API](https://discourse.ubuntu.com/t/anbox-http-api-reference/17819/2)|
| 1 | reference/anbox-stream-gateway-reference | [Anbox Stream Gateway HTTP API](https://anbox-cloud.github.io/1.9/anbox-stream-gateway/index.html)|
| 1 | reference/ams-sdk-api-reference | [AMS SDK API](https://discourse.ubuntu.com/t/ams-sdk-api-reference/17845)|
| 1 | ams-configuration | [AMS Configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)|
| 1 | manage/instance-types-reference | [Instance Types](https://discourse.ubuntu.com/t/instance-types-reference/17764)|
| 1 | reference/anbox-platforms | [Anbox Platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)|
| 1 | reference/prometheus-metrics | [Prometheus Metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)|
| 0 | | Other things |
| 1 | changelog | [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)|
| 1 | roadmap | [Roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)|
| 1 | component-versions | [Component Versions](https://discourse.ubuntu.com/t/component-versions/21413)|
| 1 | supported-versions | [Supported Versions](https://discourse.ubuntu.com/t/supported-versions/21046)|
| 1 | sdks | [SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844)|
| 1 | faq | [FAQ](https://discourse.ubuntu.com/t/anbox-cloud-faq/17837)|
| | installation/adding-additional-lxd-nodes | https://discourse.ubuntu.com/t/adding-additional-lxd-nodes/17752|/docs/installation/adding-additional-lxd-nodes |
| | installation/charm-configuration | https://discourse.ubuntu.com/t/charm-configuration/17751|/docs/installation/charm-configuration |
| | installation/registering-a-deployment | https://discourse.ubuntu.com/t/registering-a-deployment/17748|/docs/installation/registering-a-deployment |
| | installation/metrics-collection | https://discourse.ubuntu.com/t/metrics-collection/17753|/docs/installation/metrics-collection |
| | manage/managing-lxd-nodes | https://discourse.ubuntu.com/t/managing-lxd-nodes/17757|/docs/manage/managing-lxd-nodes |
| | monitoring/monitoring | https://discourse.ubuntu.com/t/monitoring/17785|/docs/monitoring/monitoring |
[/details]
