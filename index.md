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

### About

- [Home](https://discourse.ubuntu.com/t/anbox-cloud-documentation/17029)
- [Overview](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802)

### Installation

  * [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734)
  * [Install Appliance](https://discourse.ubuntu.com/t/install-appliance/22681)
  * [Install with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744)

### Operations

  * [Customizations](https://discourse.ubuntu.com/t/installation-customizing/17747)
  * [Application Registry](https://discourse.ubuntu.com/t/installation-application-registry/17749)
  * [Upgrading](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750)
  * [High Availability](https://discourse.ubuntu.com/t/high-availability/17754)
  * [Validation](https://discourse.ubuntu.com/t/validation/20329)

### Managing Anbox Cloud

 * [Getting started](https://discourse.ubuntu.com/t/getting-started/17756)
 * [Dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)
 * [Images](https://discourse.ubuntu.com/t/managing-images/17758)
 * [Applications](https://discourse.ubuntu.com/t/managing-applications/17760)
 * [Addons](https://discourse.ubuntu.com/t/managing-addons/17759)
 * [Application Registry](https://discourse.ubuntu.com/t/application-registry/17761)
 * [Containers](https://discourse.ubuntu.com/t/managing-containers/17763)
 * [Capacity Planning](https://discourse.ubuntu.com/t/capacity-planning/17765)
 * [GPU Support](https://discourse.ubuntu.com/t/gpu-support/17768)
 * [Logging](https://discourse.ubuntu.com/t/managing-logs/17771)
 * [AMS Access](https://discourse.ubuntu.com/t/managing-ams-access/17774)
 * [Container access](https://discourse.ubuntu.com/t/container-access/17772)
 * [Benchmarking a deployment](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770)
 * [Streaming Android Applications](https://discourse.ubuntu.com/t/streaming-android-applications/17769)
 * [LXD Auto Scaling](https://discourse.ubuntu.com/t/lxd-auto-scaling/21351)

### Using Anbox Cloud
* [Container configuration](https://discourse.ubuntu.com/t/usecase-container-configuration/17782)
* [Port Android application to Anbox Cloud](https://discourse.ubuntu.com/t/usecase-port-android-application-to-anbox-cloud/17776)
* [Anbox Streaming SDK](https://discourse.ubuntu.com/t/usecase-streaming-sdk/17783)
    * [Native streaming client](https://discourse.ubuntu.com/t/implement-android-native-streaming-client/21833)
    * [Web-based streaming client](https://discourse.ubuntu.com/t/implement-web-based-streaming-client/21835)
    * [Out-of-band data](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)
    * [Client-side virtual keyboard](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643)
* [Application testing](https://discourse.ubuntu.com/t/usecase-application-testing/17775)
* [Virtual Devices](https://discourse.ubuntu.com/t/virtual-devices/19069)

### Monitoring
  * [Installation](https://discourse.ubuntu.com/t/monitoring-installation/17786)
  * [Grafana](https://discourse.ubuntu.com/t/monitoring-grafana/17787)
  * [Nagios](https://discourse.ubuntu.com/t/monitoring-nagios/17788)

### Reference
* [AMS HTTP API](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801)
* [Anbox HTTP API](https://discourse.ubuntu.com/t/anbox-http-api-reference/17819/2)
* [Anbox Stream Gateway HTTP API](https://anbox-cloud.github.io/1.9/anbox-stream-gateway/index.html)
* [Anbox Platform SDK](https://anbox-cloud.github.io/1.9/anbox-platform-sdk/index.html)
* [AMS SDK API](https://discourse.ubuntu.com/t/ams-sdk-api-reference/17845)
* [AMS Configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)
* [Instance Types](https://discourse.ubuntu.com/t/instance-types-reference/17764)
* [Anbox Platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)
* [Prometheus Metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)

### Other things
* [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)
* [Roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)
 * [Component Versions](https://discourse.ubuntu.com/t/component-versions/21413)
* [Supported Versions](https://discourse.ubuntu.com/t/supported-versions/21046)
* [SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844)
* [FAQ](https://discourse.ubuntu.com/t/anbox-cloud-faq/17837)


## URLs

[details=Mapping table]
| Topic | Path |
| -- | -- |
| https://discourse.ubuntu.com/t/anbox-cloud-documentation/17029 | /docs |
|https://discourse.ubuntu.com/t/anbox-cloud-overview/17802|/docs/overview|
|https://discourse.ubuntu.com/t/anbox-cloud-installation/17835|/docs/installation|
|https://discourse.ubuntu.com/t/installation-requirements/17734|/docs/installation/installation-requirements|
|https://discourse.ubuntu.com/t/installation-quickstart/17744|/docs/installation/installation-quickstart|
|https://discourse.ubuntu.com/t/installation-customizing/17747|/docs/installation/installation-customizing|
|https://discourse.ubuntu.com/t/installation-application-registry/17749|/docs/installation/installation-application-registry|
|https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750|/docs/installation/upgrading-from-previous-versions|
|https://discourse.ubuntu.com/t/adding-additional-lxd-nodes/17752|/docs/installation/adding-additional-lxd-nodes|
|https://discourse.ubuntu.com/t/charm-configuration/17751|/docs/installation/charm-configuration|
|https://discourse.ubuntu.com/t/registering-a-deployment/17748|/docs/installation/registering-a-deployment|
|https://discourse.ubuntu.com/t/metrics-collection/17753|/docs/installation/metrics-collection|
|https://discourse.ubuntu.com/t/high-availability/17754|/docs/installation/high-availability|
|https://discourse.ubuntu.com/t/validation/20329|/docs/installation/validation|
|https://discourse.ubuntu.com/t/getting-started/17756|/docs/manage/getting-started|
|https://discourse.ubuntu.com/t/web-dashboard/20871|/docs/manage/web-dashboard|
|https://discourse.ubuntu.com/t/managing-lxd-nodes/17757|/docs/manage/managing-lxd-nodes|
|https://discourse.ubuntu.com/t/managing-images/17758|/docs/manage/managing-images|
|https://discourse.ubuntu.com/t/managing-applications/17760|/docs/manage/managing-applications|
|https://discourse.ubuntu.com/t/managing-addons/17759|/docs/manage/managing-addons|
|https://discourse.ubuntu.com/t/application-registry/17761|/docs/manage/application-registry|
|https://discourse.ubuntu.com/t/managing-containers/17763|/docs/manage/managing-containers|
|https://discourse.ubuntu.com/t/instance-types-reference/17764|/docs/manage/instance-types-reference|
|https://discourse.ubuntu.com/t/capacity-planning/17765|/docs/manage/capacity-planning|
|https://discourse.ubuntu.com/t/gpu-support/17768|/docs/manage/gpu-support|
|https://discourse.ubuntu.com/t/managing-logs/17771|/docs/manage/managing-logs|
|https://discourse.ubuntu.com/t/managing-ams-access/17774|/docs/manage/managing-ams-access|
|https://discourse.ubuntu.com/t/container-access/17772|/docs/manage/container-access|
|https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770|/docs/manage/benchmarking-a-deployment|
|https://discourse.ubuntu.com/t/streaming-android-applications/17769|/docs/manage/streaming-android-applications|
|https://discourse.ubuntu.com/t/usecase-container-configuration/17782|/docs/usage/usecase-container-configuration|
|https://discourse.ubuntu.com/t/usecase-port-android-application-to-anbox-cloud/17776|/docs/usage/usecase-port-android-application-to-anbox-cloud|
|https://discourse.ubuntu.com/t/usecase-streaming-sdk/17783|/docs/usage/usecase-streaming-sdk|
|https://discourse.ubuntu.com/t/usecase-application-testing/17775|/docs/usage/usecase-application-testing|
|https://discourse.ubuntu.com/t/monitoring/17785|/docs/monitoring/monitoring|
|https://discourse.ubuntu.com/t/monitoring-installation/17786|/docs/monitoring/monitoring-installation|
|https://discourse.ubuntu.com/t/monitoring-grafana/17787|/docs/monitoring/monitoring-grafana|
|https://discourse.ubuntu.com/t/monitoring-nagios/17788|/docs/monitoring/monitoring-nagios|
|https://discourse.ubuntu.com/t/ams-rest-api-reference/17801|/docs/reference/ams-rest-api-reference|
|https://discourse.ubuntu.com/t/anbox-http-api-reference/17819/2|/docs/reference/anbox-http-api-reference|
|https://discourse.ubuntu.com/t/ams-sdk-api-reference/17845|/docs/reference/ams-sdk-api-reference|
|https://discourse.ubuntu.com/t/anbox-platforms/18733|/docs/reference/anbox-platforms|
|https://discourse.ubuntu.com/t/prometheus-metrics/19521|/docs/reference/prometheus-metrics|
|https://discourse.ubuntu.com/t/release-notes/17842|/docs/changelog|
|https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844|/docs/sdks|
|https://discourse.ubuntu.com/t/anbox-cloud-faq/17837|/docs/faq|
|https://discourse.ubuntu.com/t/virtual-devices/19069|/docs/usage/usecase-virtual-devices|
|https://discourse.ubuntu.com/t/release-roadmap/19359|/docs/roadmap|
|https://discourse.ubuntu.com/t/ams-configuration/20872|/docs/ams-configuration|
|https://discourse.ubuntu.com/t/supported-versions/21046|/docs/supported-versions|
|https://discourse.ubuntu.com/t/lxd-auto-scaling/21351|/docs/lxd-auto-scaling|
|https://discourse.ubuntu.com/t/component-versions/21413|/docs/component-versions|
|https://discourse.ubuntu.com/t/implement-android-native-streaming-client/21833|/docs/implement-android-native-streaming-client|
|https://discourse.ubuntu.com/t/implement-web-based-streaming-client/21835|/docs/implement-web-based-streaming-client|
|https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834|/docs/exchange-out-of-band-data|
|https://discourse.ubuntu.com/t/install-appliance/22681|/docs/install-appliance|
|https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643|/docs/integrate-keyboard|
[/details]
