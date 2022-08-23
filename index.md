Anbox Cloud makes it possible to run Android apps in the cloud and supports all kinds of different use cases, including high-performance streaming of graphics to desktop and mobile client devices.

Using container technology, Anbox Cloud manages the application life cycle while optimising for high density, performance and fast container boot times. It is scalable from a single-machine installation that can run scores of single Android systems to an entire cluster of machines. Anbox Cloud supports x86 and Arm64 hardware, providing the same set of features for both architectures. Deploying the solution is simple and straightforward, and it is based on powerful and battle-proven software from Canonical like [LXD](https://linuxcontainers.org/) and [Juju](https://jujucharms.com/).

Anbox Cloud uses system containers to emulate Android systems. This method results in an isolation and security level similar to virtual machines with an overhead as low as process containers. Therefore, Anbox Cloud can provide at least twice the container density compared to other Android emulation solutions, and can serve up to 100 Android instances per server.

You should consider using Anbox Cloud if you want to deliver mobile applications that don't depend on the capabilities of your user's devices and that offload compute, storage and energy-intensive applications from the end device to the cloud. Typical use cases include mobile game streaming services, corporate application streaming, application automation and Android application testing.

| | |
|--|--|
|  [Tutorials](https://discourse.ubuntu.com/t/tutorials/28826)</br>  Get started - a hands-on introduction to Anbox Cloud for new users </br> |  [How-to guides](https://discourse.ubuntu.com/t/how-to-guides/28827) </br> Step-by-step guides covering key operations and common tasks |
|  [Explanation](https://discourse.ubuntu.com/t/explanation/28829) </br> Concepts - discussion and clarification of key topics  | [Reference](https://discourse.ubuntu.com/t/reference/28828) </br> Technical information - specifications, APIs, architecture |

## What's new

Along with bug fixes and general improvements, Anbox Cloud 1.15 includes the following changes:

* The Anbox Cloud Appliance now supports Ubuntu 22.04
* [Out-of-band data version 2](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)
* Audio-only streaming support
* Development mode support in AMS for containers

For detailed information, see the [Release notes](https://discourse.ubuntu.com/t/release-notes/17842).

## Project and community

Anbox Cloud is a Canonical product. It originally grew out of the Anbox open-source project, but its code base is now completely independent.

- [Get support through Ubuntu Advantage](https://ubuntu.com/support)
- [Join the Discourse forum to ask questions](https://discourse.ubuntu.com/c/anbox-cloud/49)
- [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)

Thinking about using Anbox Cloud for your next project? [Get in touch!](https://anbox-cloud.io/contact-us)

## Navigation

[details=Navigation]
| Level | Path | Navlink |
| -- | -- | -- |
| 0 | / | [Anbox Cloud documentation](https://discourse.ubuntu.com/t/anbox-cloud-documentation/17029) |
| 0 | | |
| 1 | tut/landing | [Tutorials](https://discourse.ubuntu.com/t/tutorials/28826) |
| 2 | tut/installing-appliance | [Install the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) |
| 2 | tut/getting-started-dashboard | [Get started (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958)|
| 2 | tut/getting-started | [Get started (CLI)](https://discourse.ubuntu.com/t/getting-started/17756)|
| 2 | tut/creating-addon | [Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284)|
| 0 | | |
| 1 | howto/landing | [How-to guides](https://discourse.ubuntu.com/t/how-to-guides/28827) |
| 2 | howto/install/landing | [Install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336)|
| 3 | howto/install/deploy-juju | [Deploy with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) |
| 3 | howto/install/deploy-bare-metal | [Deploy on bare metal](https://discourse.ubuntu.com/t/deploy-anbox-cloud-on-bare-metal/26378) |
| 3 | howto/install/customise | [Customise the installation](https://discourse.ubuntu.com/t/installation-customizing/17747)|
| 3 | howto/install/high-availability | [Enable High Availability](https://discourse.ubuntu.com/t/high-availability/17754)|
| 3 | howto/install/validate | [Validate the deployment](https://discourse.ubuntu.com/t/validation/20329)|
| 2 | howto/install-appliance/landing | [Install the appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702) |
| 3 | howto/install-appliance/aws | [Install on AWS](https://discourse.ubuntu.com/t/how-to-install-the-appliance-on-aws/29703) |
| 3 | howto/install-appliance/finalise | [Finalise the installation](https://discourse.ubuntu.com/t/how-to-finalise-the-installation/29704) |
| 2 | howto/update/landing | [Update your installation](https://discourse.ubuntu.com/t/update-your-installation/24331)|
| 3 | howto/update/control | [Control updates](https://discourse.ubuntu.com/t/control-updates/24959)|
| 3 | howto/update/upgrade-appliance | [Upgrade the appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186)|
| 3 | howto/update/upgrade-anbox | [Upgrade Anbox Cloud](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750)|
| 2 | howto/manage/landing| [Manage Anbox Cloud](https://discourse.ubuntu.com/t/manage-anbox-cloud/24337) |
| 3 | howto/manage/manage-appliance | [Manage the appliance](https://discourse.ubuntu.com/t/manage-the-anbox-cloud-appliance/26725) |
| 3 | howto/manage/tls-for-appliance | [Set up TLS for appliance](https://discourse.ubuntu.com/t/set-up-tls-for-the-anbox-cloud-appliance/28552) |
| 3 | howto/manage/web-dashboard | [Use the web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)|
| 3 | howto/manage/images | [Manage images](https://discourse.ubuntu.com/t/managing-images/17758)|
| 3 | howto/manage/logs | [View logs](https://discourse.ubuntu.com/t/managing-logs/17771)|
| 3 | howto/manage/ams-access | [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774)|
| 3 | howto/manage/benchmarks | [Run benchmarks](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770)|
| 2 | howto/application/landing | [Manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) |
| 3 | howto/application/create | [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)|
| 3 | howto/application/wait | [Wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202)|
| 3 | howto/application/update | [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201)|
| 3 | howto/application/resources | [Configure available resources](https://discourse.ubuntu.com/t/configure-available-resources/24960)|
| 3 | howto/application/delete | [Delete an application](https://discourse.ubuntu.com/t/delete-an-application/24199)|
| 3 | howto/application/list | [List applications](https://discourse.ubuntu.com/t/list-applications/24200)|
| 3 | howto/aar/deploy | [Deploy an AAR](https://discourse.ubuntu.com/t/installation-application-registry/17749)|
| 3 | howto/aar/configure | [Configure an AAR](https://discourse.ubuntu.com/t/configure-an-aar/24319)|
| 3 | howto/aar/revoke | [Revoke an AAR client](https://discourse.ubuntu.com/t/revoke-an-aar-client/24320)|
| 3 | howto/application/test | [Test your application](https://discourse.ubuntu.com/t/usecase-application-testing/17775)|
| 3 | howto/application/virtual-devices | [Create a virtual device](https://discourse.ubuntu.com/t/virtual-devices/19069)|
| 3 | howto/application/extend | [Extend an application](https://discourse.ubuntu.com/t/extand-an-application/28554)|
| 2 | howto/port/landing | [Port Android apps](https://discourse.ubuntu.com/t/port-android-apps/17776)|
| 3 | howto/port/permissions | [Grant permissions](https://discourse.ubuntu.com/t/grant-runtime-permissions/26054)|
| 3 | howto/port/architecture | [Choose APK architecture](https://discourse.ubuntu.com/t/choose-apk-architecture/26055)|
| 3 | howto/port/obb-files | [Port APKs with OBB files](https://discourse.ubuntu.com/t/port-apks-with-obb-files/26056)|
| 3 | howto/port/configure-watchdog | [Configure the watchdog](https://discourse.ubuntu.com/t/configure-the-watchdog/26057)|
| 3 | howto/port/install-system-app | [Install APK as a system app](https://discourse.ubuntu.com/t/install-an-apk-as-a-system-app/27086)|
| 2 | howto/container/landing | [Work with containers](https://discourse.ubuntu.com/t/work-with-containers/24335) |
| 3 | howto/container/launch | [Launch a container](https://discourse.ubuntu.com/t/launch-a-container/24327)|
| 3 | howto/container/wait | [Wait for a container](https://discourse.ubuntu.com/t/wait-for-a-container/24330)|
| 3 | howto/container/access | [Access a container](https://discourse.ubuntu.com/t/container-access/17772)|
| 3 | howto/container/expose-services | [Expose services](https://discourse.ubuntu.com/t/expose-services-on-a-container/24326)|
| 3 | howto/container/logs | [View the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329)|
| 3 | howto/container/delete | [Delete a container](https://discourse.ubuntu.com/t/delete-a-container/24325)|
| 3 | howto/container/list | [List containers](https://discourse.ubuntu.com/t/list-containers/24328)|
| 3 | howto/container/geographic-location | [Configure geographic location](https://discourse.ubuntu.com/t/usecase-container-configuration/17782)|
| 3 | howto/container/backup-and-restore | [Back up and restore application data](https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183)|
| 2 | howto/addons/landing | [Use addons](https://discourse.ubuntu.com/t/managing-addons/17759)|
| 3 | howto/addons/enable-globally | [Enable globally](https://discourse.ubuntu.com/t/enable-an-addon-globally/25285)|
| 3 | howto/addons/update | [Update addons](https://discourse.ubuntu.com/t/update-addons/25286)|
| 3 | howto/addons/migrate | [Migrate from previous versions](https://discourse.ubuntu.com/t/migrate-from-previous-addon-versions/25287)|
| 3 | howto/addons/install-tools | [Example: Install tools](https://discourse.ubuntu.com/t/example-install-tools/25288)|
| 3 | howto/addons/backup-and-restore | [Example: Back up data](https://discourse.ubuntu.com/t/example-back-up-data/25289)|
| 3 | howto/addons/customise-android | [Example: Customise Android](https://discourse.ubuntu.com/t/example-customise-android/25290)|
| 3 | howto/addons/emulate-platforms | [Example: Emulate platforms](https://discourse.ubuntu.com/t/example-emulate-platforms/25291)|
| 3 | howto/addons/best-practices | [Best practices](https://discourse.ubuntu.com/t/best-practices-for-addons/25292)|
| 2 | howto/monitor/landing | [Monitor Anbox Cloud](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338) |
| 3 | howto/monitor/collect-metrics | [Example: Collect metrics](https://discourse.ubuntu.com/t/monitoring-grafana/17787)|
| 3 | howto/monitor/monitor-status | [Example: Monitor status](https://discourse.ubuntu.com/t/monitoring-nagios/17788)|
| 2 | howto/stream/landing | [Implement streaming](https://discourse.ubuntu.com/t/implement-streaming/24332) |
| 3 | howto/stream/access | [Access the stream gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784) |
| 3 | howto/stream/web-client | [Implement a web-based client](https://discourse.ubuntu.com/t/implement-web-based-streaming-client/21835)|
| 3 | howto/stream/oob-data | [Exchange OOB data](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)|
| 3 | howto/stream/client-side-keyboard | [Use a client-side keyboard](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643)|
| 2 | howto/cluster/landing | [Manage cluster nodes](https://discourse.ubuntu.com/t/manage-cluster-nodes/24334) |
| 3 | howto/cluster/appliance | [Join a machine to the appliance](https://discourse.ubuntu.com/t/how-to-join-a-machine-to-the-anbox-cloud-appliance/29054) |
| 3 | howto/cluster/configure-nodes | [Configure cluster nodes](https://discourse.ubuntu.com/t/configure-cluster-nodes/28716) |
| 3 | howto/cluster/scale-up | [Scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322)|
| 3 | howto/cluster/scale-down | [Scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323)|
| 2 | howto/troubleshoot/landing | [Troubleshoot Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-faq/17837)|
| 0 | | |
| 1 | ref/landing | [Reference](https://discourse.ubuntu.com/t/reference/28828) |
| 2 | ref/provided-images | [Provided images](https://discourse.ubuntu.com/t/provided-images/24185)|
| 2 | ref/android-features | [Supported Android features](https://discourse.ubuntu.com/t/supported-android-features/28825)|
| 2 | ref/sdks | [Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844)|
| 2 | ref/api-reference | [API reference](https://discourse.ubuntu.com/t/api-reference/24339) |
| 3 | ref/ams-http-api | [AMS HTTP API](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801)|
| 3 | ref/anbox-https-api | [Anbox HTTP API](https://discourse.ubuntu.com/t/anbox-http-api-reference/17819)|
| 3 | ref/anbox-stream-gateway | [Stream Gateway API](https://anbox-cloud.github.io/latest/anbox-stream-gateway/)|
| 3 | ref/anbox-platform-sdk-api | [Anbox Platform SDK API](https://anbox-cloud.github.io/latest/anbox-platform-sdk/)|
| 2 | ref/instance-types | [Instance types](https://discourse.ubuntu.com/t/instance-types-reference/17764)|
| 2 | ref/platforms | [Anbox platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)|
| 2 | ref/prometheus | [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)|
| 2 | ref/ams-configuration | [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)|
| 2 | ref/application-manifest | [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)|
| 2 | ref/addons | [Addons](https://discourse.ubuntu.com/t/addons/25293)|
| 2 | ref/hooks | [Hooks](https://discourse.ubuntu.com/t/hooks/28555)|
| 2 | ref/perf-benchmarks | [Performance benchmarks](https://discourse.ubuntu.com/t/performance-benchmarks/24709)|
| 2 | ref/webrtc-streamer | [WebRTC streamer](https://discourse.ubuntu.com/t/webrtc-streamer/30195)|
| 2 | ref/lxd-docs | [LXD documentation](https://linuxcontainers.org/lxd/docs/latest/index)|
| 2 | ref/glossary | [Glossary](https://discourse.ubuntu.com/t/glossary/26204)|
| 0 | | |
| 1 | exp/landing | [Explanation](https://discourse.ubuntu.com/t/explanation/28829) |
| 2 | exp/anbox-cloud | [About Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) |
| 2 | exp/ams | [About the AMS](https://discourse.ubuntu.com/t/about-ams/24321)|
| 2 | exp/applications | [About applications](https://discourse.ubuntu.com/t/managing-applications/17760)|
| 2 | exp/aar | [About the AAR](https://discourse.ubuntu.com/t/application-registry/17761)|
| 2 | exp/containers | [About containers](https://discourse.ubuntu.com/t/managing-containers/17763)|
| 2 | exp/clustering | [About clustering](https://discourse.ubuntu.com/t/capacity-planning/17765)|
| 2 | exp/performance | [About performance](https://discourse.ubuntu.com/t/about-performance/29416)
| 2 | exp/capacity-planning | [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) |
| 2 | exp/gpu-support | [About GPU support](https://discourse.ubuntu.com/t/gpu-support/17768)|
| 2 | exp/application-streaming | [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769)|
| 0 | | |
| 1 | anbox/landing | [About the project](https://discourse.ubuntu.com/t/about-the-project/28830) |
| 2 | requirements | [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) |
| 2 | release-notes | [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)|
| 2 | roadmap | [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)|
| 2 | supported-versions | [Supported versions](https://discourse.ubuntu.com/t/supported-versions/21046)|
| 2 | component-versions | [Component versions](https://discourse.ubuntu.com/t/component-versions/21413)|
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
