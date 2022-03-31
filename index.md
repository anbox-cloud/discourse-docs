Anbox Cloud provides a rich software stack that enables you to run Android applications in the cloud for all kinds of different use cases, including high-performance streaming of graphics to desktop and mobile client devices.

Using container technology, Anbox Cloud is scalable from a single-machine installation that can run scores of single Android systems to an entire cluster of machines. It is based on powerful and battle-proven software from Canonical like [LXD](https://linuxcontainers.org/) and [Juju](https://jujucharms.com/).

## Core features

* Simple and straightforward deployment
* Management of the container and application life cycle while optimising for high density, performance and fast container boot times
* Platform integration tools to allow, for example, integration of existing streaming solutions
* Support for both x86 and Arm64 hardware, providing the same set of features

See the [official Anbox Cloud website](https://anbox-cloud.io/) for more information.

## Get started

|  |  |
|--|--|
| [About Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) | Learn about the differences between Anbox Cloud and the Anbox Cloud Appliance and about the components and architecture of the offering |
| [About AMS](https://discourse.ubuntu.com/t/about-ams/24321) | Understand the Anbox Management Service (AMS), which handles all aspects of the application and container life cycle |
| [Installing the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681) | Install the Anbox Cloud Appliance, which is well suited for initial prototype and small scale deployments |
| [Deploy Anbox Cloud with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) | Deploy the full Anbox Cloud solution to a public cloud |
| [Getting started with Anbox Cloud (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958)<br>[Getting started with Anbox Cloud (CLI)](https://discourse.ubuntu.com/t/getting-started/17756) | Go through the first steps of launching and accessing an Android container to familiarise yourself with Anbox Cloud, by using either the web dashboard or the command line interface |


## What's new

Along with bug fixes and general improvements, Anbox Cloud 1.13 comes with:

* Direct rendering for Intel and AMD GPUs
* OpenGL ES 3.2 support

|  |  |
|--|--|
| [Release notes](https://discourse.ubuntu.com/t/release-notes/17842) | All new features, improvements and bug fixes |
| [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359) | Planned updates and features for upcoming releases |

## Navigation

[details=Navigation]
| Level | Path | Navlink |
| -- | -- | -- |
| 0 | | Tutorials |
| 1 | tut/installing-appliance | [Installing the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) |
| 1 | tut/getting-started-dashboard | [Getting started (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958)|
| 1 | tut/getting-started | [Getting started (CLI)](https://discourse.ubuntu.com/t/getting-started/17756)|
| 1 | tut/creating-addon | [Creating an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284)|
| 0 | | How to |
| 1 | howto/install/landing | [Install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336)|
| 2 | howto/install/deploy-juju | [Deploy with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) |
| 2 | howto/install/deploy-bare-metal | [Deploy on bare metal](https://discourse.ubuntu.com/t/deploy-anbox-cloud-on-bare-metal/26378) |
| 2 | howto/install/customise | [Customise the installation](https://discourse.ubuntu.com/t/installation-customizing/17747)|
| 2 | howto/install/high-availability | [Enable High Availability](https://discourse.ubuntu.com/t/high-availability/17754)|
| 2 | howto/install/validate | [Validate the deployment](https://discourse.ubuntu.com/t/validation/20329)|
| 1 | howto/update/landing | [Update your installation](https://discourse.ubuntu.com/t/update-your-installation/24331)|
| 2 | howto/update/control | [Control updates](https://discourse.ubuntu.com/t/control-updates/24959)|
| 2 | howto/update/upgrade-appliance | [Upgrade the appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186)|
| 2 | howto/update/upgrade-anbox | [Upgrade Anbox Cloud](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750)|
| 1 | howto/manage/landing| [Manage Anbox Cloud](https://discourse.ubuntu.com/t/manage-anbox-cloud/24337) |
| 2 | howto/manage/manage-appliance | [Manage the appliance](https://discourse.ubuntu.com/t/manage-the-anbox-cloud-appliance/26725) |
| 2 | howto/manage/web-dashboard | [Use the web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)|
| 2 | howto/manage/images | [Manage images](https://discourse.ubuntu.com/t/managing-images/17758)|
| 2 | howto/manage/logs | [View logs](https://discourse.ubuntu.com/t/managing-logs/17771)|
| 2 | howto/manage/ams-access | [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774)|
| 2 | howto/manage/benchmarks | [Run benchmarks](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770)|
| 1 | howto/application/landing | [Manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) |
| 2 | howto/application/create | [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)|
| 2 | howto/application/wait | [Wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202)|
| 2 | howto/application/update | [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201)|
| 2 | howto/application/resources | [Configure available resources](https://discourse.ubuntu.com/t/configure-available-resources/24960)|
| 2 | howto/application/delete | [Delete an application](https://discourse.ubuntu.com/t/delete-an-application/24199)|
| 2 | howto/application/list | [List applications](https://discourse.ubuntu.com/t/list-applications/24200)|
| 2 | howto/aar/deploy | [Deploy an AAR](https://discourse.ubuntu.com/t/installation-application-registry/17749)|
| 2 | howto/aar/configure | [Configure an AAR](https://discourse.ubuntu.com/t/configure-an-aar/24319)|
| 2 | howto/aar/revoke | [Revoke an AAR client](https://discourse.ubuntu.com/t/revoke-an-aar-client/24320)|
| 2 | howto/application/test | [Test your application](https://discourse.ubuntu.com/t/usecase-application-testing/17775)|
| 2 | howto/application/virtual-devices | [Create a virtual device](https://discourse.ubuntu.com/t/virtual-devices/19069)|
| 1 | howto/port/landing | [Port Android apps](https://discourse.ubuntu.com/t/port-android-apps/17776)|
| 2 | howto/port/permissions | [Grant permissions](https://discourse.ubuntu.com/t/grant-runtime-permissions/26054)|
| 2 | howto/port/architecture | [Choose APK architecture](https://discourse.ubuntu.com/t/choose-apk-architecture/26055)|
| 2 | howto/port/obb-files | [Port APKs with OBB files](https://discourse.ubuntu.com/t/port-apks-with-obb-files/26056)|
| 2 | howto/port/configure-watchdog | [Configure the watchdog](https://discourse.ubuntu.com/t/configure-the-watchdog/26057)|
| 2 | howto/port/install-system-app | [Install APK as a system app](https://discourse.ubuntu.com/t/install-an-apk-as-a-system-app/27086)|
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
| 2 | howto/addons/enable-globally | [Enable globally](https://discourse.ubuntu.com/t/enable-an-addon-globally/25285)|
| 2 | howto/addons/update | [Update addons](https://discourse.ubuntu.com/t/update-addons/25286)|
| 2 | howto/addons/migrate | [Migrate from previous versions](https://discourse.ubuntu.com/t/migrate-from-previous-addon-versions/25287)|
| 2 | howto/addons/install-tools | [Example: Install tools](https://discourse.ubuntu.com/t/example-install-tools/25288)|
| 2 | howto/addons/backup-and-restore | [Example: Back up data](https://discourse.ubuntu.com/t/example-back-up-data/25289)|
| 2 | howto/addons/customise-android | [Example: Customise Android](https://discourse.ubuntu.com/t/example-customise-android/25290)|
| 2 | howto/addons/emulate-platforms | [Example: Emulate platforms](https://discourse.ubuntu.com/t/example-emulate-platforms/25291)|
| 2 | howto/addons/best-practices | [Best practices](https://discourse.ubuntu.com/t/best-practices-for-addons/25292)|
| 1 | howto/monitor/landing | [Monitor Anbox Cloud](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338) |
| 2 | howto/monitor/collect-metrics | [Example: Collect metrics](https://discourse.ubuntu.com/t/monitoring-grafana/17787)|
| 2 | howto/monitor/monitor-status | [Example: Monitor status](https://discourse.ubuntu.com/t/monitoring-nagios/17788)|
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
| 2 | ref/anbox-platform-sdk-api | [Anbox Platform SDK API](https://anbox-cloud.github.io/1.13/anbox-platform-sdk/index.html)|
| 1 | ref/instance-types | [Instance types](https://discourse.ubuntu.com/t/instance-types-reference/17764)|
| 1 | ref/platforms | [Anbox platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)|
| 1 | ref/prometheus | [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)|
| 1 | ref/ams-configuration | [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)|
| 1 | ref/application-manifest | [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)|
| 1 | ref/addons | [Addons](https://discourse.ubuntu.com/t/addons/25293)|
| 1 | ref/perf-benchmarks | [Performance benchmarks](https://discourse.ubuntu.com/t/performance-benchmarks/24709)|
| 1 | ref/lxd-docs | [LXD documentation](https://linuxcontainers.org/lxd/docs/master/index)|
| 1 | ref/glossary | [Glossary](https://discourse.ubuntu.com/t/glossary/26204)|
| 0 | | Explanation |
| 1 | exp/anbox-cloud | [About Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) |
| 1 | exp/ams | [About AMS](https://discourse.ubuntu.com/t/about-ams/24321)|
| 1 | exp/applications | [About applications](https://discourse.ubuntu.com/t/managing-applications/17760)|
| 1 | exp/aar | [About the AAR](https://discourse.ubuntu.com/t/application-registry/17761)|
| 1 | exp/containers | [About containers](https://discourse.ubuntu.com/t/managing-containers/17763)|
| 1 | exp/clustering | [About clustering](https://discourse.ubuntu.com/t/capacity-planning/17765)|
| 1 | exp/gpu-support | [About GPU support](https://discourse.ubuntu.com/t/gpu-support/17768)|
| 1 | exp/application-streaming | [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769)|
| 0 | | About the project |
| 1 | requirements | [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) |
| 1 | release-notes | [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)|
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
| /docs/manage/managing-ams-access | /docs/howto/manage/ams-access |
| /docs/installation/installation-application-registry | /docs/howto/aar/deploy |
| /docs/usage/usecase-application-testing | /docs/howto/application/test |
| /docs/usage/usecase-virtual-devices | /docs/howto/application/virtual-devices |
| /docs/manage/container-access | /docs/howto/container/access |
| /docs/howto/container/view-log | /docs/howto/container/logs |
| /docs/usage/usecase-container-configuration | /docs/howto/container/geographic-location |
| /docs/howto/containers/backup-and-restore | /docs/howto/container/backup-and-restore |
| /docs/monitoring/monitoring-installation | /docs/howto/monitor/landing |
| /docs/howto/monitor/install | /docs/howto/monitor/landing |
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
| /docs/manage/managing-addons | /docs/howto/addons/landing |
| /docs/manage/application-registry | /docs/exp/aar |
| /docs/manage/managing-containers | /docs/exp/containers |
| /docs/manage/capacity-planning | /docs/exp/clustering |
| /docs/manage/gpu-support | /docs/exp/gpu-support |
| /docs/manage/benchmarking-a-deployment | /docs/exp/benchmarking |
| /docs/manage/streaming-android-applications | /docs/exp/application-streaming |
| /docs/usage/usecase-port-android-application-to-anbox-cloud | /docs/exp/porting-issues |
| /docs/installation/installation-requirements | /docs/requirements |
| /docs/exp/porting-issues | /docs/howto/port/landing |
| /docs/exp/benchmarking | /docs/howto/manage/benchmarks |
| /docs/changelog | /docs/release-notes |
| /docs/howto/monitor/grafana | /docs/howto/monitor/collect-metrics |
| /docs/howto/monitor/nagios | /docs/howto/monitor/monitor-status |
[/details]
