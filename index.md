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
| 0 | | Tutorials |
| 1 | tut/installing-appliance | [Installing the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) |
| 1 | tut/getting-started | [Getting started](https://discourse.ubuntu.com/t/getting-started/17756)|
| 1 | tut/creating-addon | [Creating an addon](tbd)|
| 0 | | How to |
| 1 | howto/install/landing | [Install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336)|
| 2 | howto/install/deploy-juju | [Deploy with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) |
| 2 | howto/install/customise | [Customise the installation](https://discourse.ubuntu.com/t/installation-customizing/17747)|
| 2 | howto/install/high-availability | [Enable High Availability](https://discourse.ubuntu.com/t/high-availability/17754)|
| 2 | howto/install/validate | [Validate the deployment](https://discourse.ubuntu.com/t/validation/20329)|
| 1 | howto/update/landing | [Update your installation](https://discourse.ubuntu.com/t/update-your-installation/24331)|
| 2 | howto/update/upgrade-appliance | [Upgrade the appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186)|
| 2 | howto/update/upgrade-anbox | [Upgrade Anbox Cloud](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750)|
| 1 | howto/manage/landing| [Manage Anbox Cloud](https://discourse.ubuntu.com/t/manage-anbox-cloud/24337) |
| 2 | howto/manage/web-dashboard | [Use the web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)|
| 2 | howto/manage/images | [Manage images](https://discourse.ubuntu.com/t/managing-images/17758)|
| 2 | howto/manage/logs | [View logs](https://discourse.ubuntu.com/t/managing-logs/17771)|
| 2 | howto/manage/ams-access | [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774)|
| 1 | howto/application/landing | [Manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) |
| 2 | howto/application/create | [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)|
| 2 | howto/application/wait | [Wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202)|
| 2 | howto/application/update | [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201)|
| 2 | howto/application/delete | [Delete an application](https://discourse.ubuntu.com/t/delete-an-application/24199)|
| 2 | howto/application/list | [List applications](https://discourse.ubuntu.com/t/list-applications/24200)|
| 2 | howto/aar/deploy | [Deploy an AAR](https://discourse.ubuntu.com/t/installation-application-registry/17749)|
| 2 | howto/aar/configure | [Configure an AAR](https://discourse.ubuntu.com/t/configure-an-aar/24319)|
| 2 | howto/aar/revoke | [Revoke an AAR client](https://discourse.ubuntu.com/t/revoke-an-aar-client/24320)|
| 2 | howto/application/test | [Test your application](https://discourse.ubuntu.com/t/usecase-application-testing/17775)|
| 2 | howto/application/virtual-devices | [Create a virtual device](https://discourse.ubuntu.com/t/virtual-devices/19069)|
| 1 | howto/container/landing | [Work with containers](https://discourse.ubuntu.com/t/work-with-containers/24335) |
| 2 | howto/container/launch | [Launch a container](https://discourse.ubuntu.com/t/launch-a-container/24327)|
| 2 | howto/container/wait | [Wait for a container](https://discourse.ubuntu.com/t/wait-for-a-container/24330)|
| 2 | howto/container/access | [Access a container](https://discourse.ubuntu.com/t/container-access/17772)|
| 2 | howto/container/expose-services | [Expose services](https://discourse.ubuntu.com/t/expose-services-on-a-container/24326)|
| 2 | howto/container/logs | [View the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329)|
| 2 | howto/container/delete | [Delete a container](https://discourse.ubuntu.com/t/delete-a-container/24325)|
| 2 | howto/container/list | [List containers](https://discourse.ubuntu.com/t/list-containers/24328)|
| 2 | howto/container/geographic-location | [Configure geographic location](https://discourse.ubuntu.com/t/usecase-container-configuration/17782)|
| 2 | howto/container/backup-and-restore | [Back up and restore application data](https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183)|
| 1 | howto/addons/landing | [Use addons](https://discourse.ubuntu.com/t/managing-addons/17759)|
| 2 | howto/addons/enable-globally | [Enable globally](tbd)|
| 2 | howto/addons/update | [Update addons](tbd)|
| 2 | howto/addons/migrate | [Migrate from previous versions](tbd)|
| 2 | howto/addons/install-tools | [Example: Install tools](tbd)|
| 2 | howto/addons/backup-and-restore | [Example: Back up data](tbd)|
| 2 | howto/addons/customise-android | [Example: Customise Android](tbd)|
| 2 | howto/addons/emulate-platforms | [Example: Emulate platforms](tbd)|
| 2 | howto/addons/best-practices | [Best practices](tbd)|
| 1 | howto/monitor/landing | [Monitor Anbox Cloud](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338) |
| 2 | howto/monitor/install | [Install the monitoring stack](https://discourse.ubuntu.com/t/monitoring-installation/17786)|
| 2 | howto/monitor/grafana | [Use Grafana](https://discourse.ubuntu.com/t/monitoring-grafana/17787)|
| 2 | howto/monitor/nagios | [Use Nagios](https://discourse.ubuntu.com/t/monitoring-nagios/17788)|
| 1 | howto/stream/landing | [Implement streaming](https://discourse.ubuntu.com/t/implement-streaming/24332) |
| 2 | howto/stream/access | [Access the stream gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784) |
| 2 | howto/stream/native-client | [Implement a native client](https://discourse.ubuntu.com/t/implement-android-native-streaming-client/21833)|
| 2 | howto/stream/web-client | [Implement a web-based client](https://discourse.ubuntu.com/t/implement-web-based-streaming-client/21835)|
| 2 | howto/stream/oob-data | [Exchange OOB data](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)|
| 2 | howto/stream/client-side-keyboard | [Use a client-side keyboard](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643)|
| 1 | howto/cluster/landing | [Manage cluster nodes](https://discourse.ubuntu.com/t/manage-cluster-nodes/24334) |
| 2 | howto/cluster/scale-up | [Scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322)|
| 2 | howto/cluster/scale-down | [Scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323)|
| 1 | howto/troubleshoot/landing | [Troubleshoot Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-faq/17837)|
| 0 | | Reference |
| 1 | ref/provided-images | [Provided images](https://discourse.ubuntu.com/t/provided-images/24185)|
| 1 | ref/sdks | [Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844)|
| 1 | ref/api-reference | [API reference](https://discourse.ubuntu.com/t/api-reference/24339) |
| 2 | ref/ams-http-api | [AMS HTTP API](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801)|
| 2 | ref/anbox-https-api | [Anbox HTTP API](https://discourse.ubuntu.com/t/anbox-http-api-reference/17819)|
| 2 | ref/anbox-stream-gateway | [Stream Gateway API](https://anbox-cloud.github.io/1.10/anbox-stream-gateway/index.html)|
| 2 | ref/anbox-platform-sdk-api | [Anbox Platform SDK API](https://anbox-cloud.github.io/1.10/anbox-platform-sdk/index.html)|
| 1 | ref/instance-types | [Instance types](https://discourse.ubuntu.com/t/instance-types-reference/17764)|
| 1 | ref/platforms | [Anbox platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)|
| 1 | ref/prometheus | [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)|
| 1 | ref/ams-configuration | [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)|
| 1 | ref/application-manifest | [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)|
| 1 | ref/addons | [Addons](tbd)|
| 1 | ref/lxd-docs | [LXD documentation](https://linuxcontainers.org/lxd/docs/master/index)|
| 0 | | Explanation |
| 1 | exp/anbox-cloud | [About Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) |
| 1 | exp/ams | [About AMS](https://discourse.ubuntu.com/t/about-ams/24321)|
| 1 | exp/applications | [About applications](https://discourse.ubuntu.com/t/managing-applications/17760)|
| 1 | exp/aar | [About the AAR](https://discourse.ubuntu.com/t/application-registry/17761)|
| 1 | exp/containers | [About containers](https://discourse.ubuntu.com/t/managing-containers/17763)|
| 1 | exp/clustering | [About clustering](https://discourse.ubuntu.com/t/capacity-planning/17765)|
| 1 | exp/gpu-support | [About GPU support](https://discourse.ubuntu.com/t/gpu-support/17768)|
| 1 | exp/benchmarking | [About benchmarking](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770)|
| 1 | exp/application-streaming | [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769)|
| 1 | exp/porting-issues | [Issues when porting apps](https://discourse.ubuntu.com/t/usecase-port-android-application-to-anbox-cloud/17776)|
| 0 | | Anbox Cloud |
| 1 | requirements | [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) |
| 1 | changelog | [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)|
| 1 | roadmap | [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)|
| 1 | supported-versions | [Supported versions](https://discourse.ubuntu.com/t/supported-versions/21046)|
| 1 | component-versions | [Component versions](https://discourse.ubuntu.com/t/component-versions/21413)|
[/details]

## Redirects

[details=Mapping table]
| Path | Location |
| ---- | -------- |
| /docs/install-appliance | /docs/tut/installing-appliance |
| /docs/lxd-auto-scaling | /docs/exp/clustering |
| /docs/usage/usecase-streaming-sdk | /docs/ref/sdks |
| /docs/reference/ams-sdk-api-reference | /docs/ref/sdks |
| /docs/installation/installation-appliance | /docs/tut/installing-appliance |
| /docs/manage/getting-started | /docs/tut/getting-started |
| /docs/installation/installation-quickstart | /docs/howto/install/deploy-juju |
| /docs/installation/installation-customizing | /docs/howto/install/customise |
| /docs/installation/high-availability | /docs/howto/install/high-availability |
| /docs/installation/validation | /docs/howto/install/validate |
| /docs/installation/upgrading-from-previous-versions | /docs/howto/update/upgrade-anbox |
| /docs/howto/manage/managing-images | /docs/howto/manage/images |
| /docs/howto/manage/managing-addons | /docs/howto/addons/landing |
| /docs/howto/manage/managing-logs | /docs/howto/manage/logs |
| /docs/howto/manage/managing-ams-access | /docs/howto/manage/ams-access |
| /docs/installation/installation-application-registry | /docs/howto/aar/deploy |
| /docs/usage/usecase-application-testing | /docs/howto/application/test |
| /docs/usage/usecase-virtual-devices | /docs/howto/application/virtual-devices |
| /docs/manage/container-access | /docs/howto/container/access |
| /docs/howto/container/view-log | /docs/howto/container/logs |
| /docs/usage/usecase-container-configuration | /docs/howto/container/geographic-location |
| /docs/howto/containers/backup-and-restore | /docs/howto/container/backup-and-restore |
| /docs/monitoring/monitoring-installation | /docs/howto/monitor/install |
| /docs/monitoring/monitoring-grafana | /docs/howto/monitor/grafana |
| /docs/monitoring/monitoring-nagios | /docs/howto/monitor/nagios |
| /docs/implement-android-native-streaming-client | /docs/howto/stream/native-client |
| /docs/implement-web-based-streaming-client | /docs/howto/stream/web-client |
| /docs/exchange-out-of-band-data | /docs/howto/stream/oob-data |
| /docs/integrate-keyboard | /docs/howto/stream/client-side-keyboard |
| /docs/faq | /docs/howto/troubleshoot/landing |
| /docs/sdks | /docs/ref/sdks |
| /docs/reference/ams-rest-api-reference | /docs/ref/ams-http-api |
| /docs/reference/anbox-http-api-reference | /docs/ref/anbox-https-api |
| /docs/reference/anbox-stream-gateway-reference | /docs/ref/anbox-stream-gateway |
| /docs/manage/instance-types-reference | /docs/ref/instance-types |
| /docs/reference/anbox-platforms | /docs/ref/platforms |
| /docs/reference/prometheus-metrics | /docs/ref/prometheus |
| /docs/ams-configuration | /docs/ref/ams-configuration |
| /docs/overview | /docs/exp/anbox-cloud |
| /docs/manage/managing-applications | /docs/exp/applications |
| /docs/manage/application-registry | /docs/exp/aar |
| /docs/manage/managing-containers | /docs/exp/containers |
| /docs/manage/capacity-planning | /docs/exp/clustering |
| /docs/manage/gpu-support | /docs/exp/gpu-support |
| /docs/manage/benchmarking-a-deployment | /docs/exp/benchmarking |
| /docs/manage/streaming-android-applications | /docs/exp/application-streaming |
| /docs/usage/usecase-port-android-application-to-anbox-cloud | /docs/exp/porting-issues |
| /docs/installation/installation-requirements | /docs/requirements |
[/details]
