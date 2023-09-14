Anbox Cloud enables running Android apps on any cloud platform at scale. It uses system containers to run the nested Android containers and [Juju](https://juju.is/) for deployment in a cloud environment.

Anbox Cloud supports x86 and Arm64 hardware, providing the same set of features for both architectures.

Since Anbox Cloud uses system containers to emulate Android systems, you can achieve the isolation and security level of a virtual machine without the associated overhead. Therefore, compared to other Android emulation solutions, Anbox Cloud can provide at least twice the container density and can serve up to 100 Android instances per server.

Due to its highly scalable nature and performance optimisation, delivering device-agnostic mobile applications is very easy. Popular use cases of Anbox Cloud include mobile game streaming services, corporate application streaming, application automation and testing.

## In this documentation
| | |
|--|--|
|  [Tutorials](https://discourse.ubuntu.com/t/tutorials/28826)</br>  Get started - a hands-on introduction to Anbox Cloud for new users </br> |  [How-to guides](https://discourse.ubuntu.com/t/how-to-guides/28827) </br> Step-by-step guides covering key operations and common tasks |
|  [Explanation](https://discourse.ubuntu.com/t/explanation/28829) </br> Concepts - discussion and clarification of key topics, architecture  | [Reference](https://discourse.ubuntu.com/t/reference/28828) </br> Technical information - specifications, APIs |

<a name="project-community"></a>
## Project and community

Anbox Cloud is a Canonical product. It originally grew out of the [Anbox open-source project](https://github.com/anbox), but its code base is now completely independent.

- [Get support through Ubuntu Pro](https://ubuntu.com/support)
- Forums:
    - [Ask questions about Anbox Cloud](https://discourse.ubuntu.com/c/anbox-cloud/users/148)
    - [Contribute to Anbox Cloud documentation](https://discourse.ubuntu.com/c/anbox-cloud/documentation/50)
    - [Follow Anbox Cloud release announcements](https://discourse.ubuntu.com/c/anbox-cloud/announcements/55)
- [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)
- [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)
- [Troubleshoot](https://discourse.ubuntu.com/t/how-to-troubleshoot-anbox-cloud/17837) and [report](https://bugs.launchpad.net/anbox-cloud/+bugs) issues with Anbox Cloud

Thinking about using Anbox Cloud for your next project? [Get in touch!](https://anbox-cloud.io/contact-us)

## Navigation

[details=Navigation]
| Level | Path | Navlink |
| -- | -- | -- |
| 0 | / | [Anbox Cloud documentation](https://discourse.ubuntu.com/t/anbox-cloud-documentation/17029) |
| 0 | | |
| 1 | tut/landing | [Tutorials](https://discourse.ubuntu.com/t/tutorials/28826) |
| 2 | tut/installing-appliance | [1. Install the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) |
| 2 | tut/getting-started-dashboard | [2. Get started using the web dashboard](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958)|
| 2 | tut/getting-started | [3. Get started using the CLI](https://discourse.ubuntu.com/t/getting-started/17756)|
| 2 | tut/stream-client | [4. Set up a stream client (Optional)](https://discourse.ubuntu.com/t/set-up-a-stream-client/37328) |
| 2 | tut/creating-addon | [5. Create an addon (Optional)](https://discourse.ubuntu.com/t/creating-an-addon/25284)|
| 0 | | |
| 1 | howto/landing | [How-to guides](https://discourse.ubuntu.com/t/how-to-guides/28827) |
| 2 | howto/install-appliance/landing | [Install the appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702) |
| 3 | howto/install-appliance/aws | [Install on AWS](https://discourse.ubuntu.com/t/how-to-install-the-appliance-on-aws/29703) |
| 3 | howto/install-appliance/azure | [Install on Azure](https://discourse.ubuntu.com/t/how-to-install-the-appliance-on-azure/30824) |
| 3 | howto/install-appliance/google-cloud | [Install on Google Cloud](https://discourse.ubuntu.com/t/36254) |
| 2 | howto/install/landing | [Install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336)|
| 3 | howto/install/deploy-juju | [Deploy with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) |
| 3 | howto/install/deploy-bare-metal | [Deploy on bare metal](https://discourse.ubuntu.com/t/deploy-anbox-cloud-on-bare-metal/26378) |
| 3 | howto/install/customise | [Customise the installation](https://discourse.ubuntu.com/t/installation-customizing/17747)|
| 3 | howto/install/high-availability | [Enable High Availability](https://discourse.ubuntu.com/t/high-availability/17754)|
| 3 | howto/install/validate | [Validate the deployment](https://discourse.ubuntu.com/t/validation/20329)|
| 2 | howto/update/landing | [Update an installation](https://discourse.ubuntu.com/t/update-your-installation/24331)|
| 3 | howto/update/control | [Control updates](https://discourse.ubuntu.com/t/control-updates/24959)|
| 3 | howto/update/upgrade-appliance | [Upgrade the appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186)|
| 3 | howto/update/upgrade-anbox | [Upgrade Anbox Cloud](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750)|
| 2 | howto/manage/landing| [Manage Anbox Cloud](https://discourse.ubuntu.com/t/manage-anbox-cloud/24337) |
| 3 | howto/manage/manage-appliance | [Manage the appliance](https://discourse.ubuntu.com/t/manage-the-anbox-cloud-appliance/26725) |
| 3 | howto/manage/tls-for-appliance | [Set up TLS for appliance](https://discourse.ubuntu.com/t/set-up-tls-for-the-anbox-cloud-appliance/28552) |
| 3 | howto/manage/images | [Manage Anbox Cloud images](https://discourse.ubuntu.com/t/managing-images/17758)|
| 3 | howto/manage/ams-access | [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774)|
| 3 | howto/manage/benchmarks | [Run benchmarks](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770)|
| 3 | howto/manage/resize-storage | [Resize LXD storage](https://discourse.ubuntu.com/t/resize-lxd-storage/32569)|
| 2 | howto/dashboard/web-dashboard | [Use the web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)|
| 2 | howto/application/landing | [Manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) |
| 3 | howto/application/create | [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)|
| 3 | howto/application/wait | [Wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202)|
| 3 | howto/application/resources | [Configure available resources](https://discourse.ubuntu.com/t/configure-available-resources/24960)|
| 3 | howto/application/list | [List applications](https://discourse.ubuntu.com/t/list-applications/24200)|
| 3 | howto/application/userdata | [Pass custom data](https://discourse.ubuntu.com/t/how-to-pass-custom-data-to-an-application/30368)|
| 3 | howto/application/test | [Test your application](https://discourse.ubuntu.com/t/usecase-application-testing/17775)|
| 3 | howto/application/update | [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201)|
| 3 | howto/application/delete | [Delete an application](https://discourse.ubuntu.com/t/delete-an-application/24199)|
| 3 | howto/application/extend | [Extend an application](https://discourse.ubuntu.com/t/extand-an-application/28554)|
| 2 | howto/application/virtual-devices | [Create a virtual device](https://discourse.ubuntu.com/t/virtual-devices/19069)|
| 2 | howto/aar/landing | [Manage AAR](https://discourse.ubuntu.com/t/manage-aar/36807)|
| 3 | howto/aar/deploy | [Deploy an AAR](https://discourse.ubuntu.com/t/installation-application-registry/17749)|
| 3 | howto/aar/configure | [Configure an AAR](https://discourse.ubuntu.com/t/configure-an-aar/24319)|
| 3 | howto/aar/revoke | [Revoke an AAR client](https://discourse.ubuntu.com/t/revoke-an-aar-client/24320)|
| 2 | howto/port/landing | [Port Android apps](https://discourse.ubuntu.com/t/port-android-apps/17776)|
| 3 | howto/port/permissions | [Grant permissions](https://discourse.ubuntu.com/t/grant-runtime-permissions/26054)|
| 3 | howto/port/architecture | [Choose APK architecture](https://discourse.ubuntu.com/t/choose-apk-architecture/26055)|
| 3 | howto/port/obb-files | [Port APKs with OBB files](https://discourse.ubuntu.com/t/port-apks-with-obb-files/26056)|
| 3 | howto/port/configure-watchdog | [Configure the watchdog](https://discourse.ubuntu.com/t/configure-the-watchdog/26057)|
| 3 | howto/port/install-system-app | [Install APK as a system app](https://discourse.ubuntu.com/t/install-an-apk-as-a-system-app/27086)|
| 2 | howto/container/landing | [Manage containers](https://discourse.ubuntu.com/t/work-with-containers/24335) |
| 3 | howto/container/create | [Create a container](https://discourse.ubuntu.com/t/launch-a-container/24327)|
| 3 | howto/container/start | [Start a container](https://discourse.ubuntu.com/t/how-to-start-a-container/33924)|
| 3 | howto/container/wait | [Wait for a container](https://discourse.ubuntu.com/t/wait-for-a-container/24330)|
| 3 | howto/container/access | [Access a container](https://discourse.ubuntu.com/t/container-access/17772)|
| 3 | howto/container/list | [List containers](https://discourse.ubuntu.com/t/list-containers/24328)|
| 3 | howto/container/geographic-location | [Configure geographic location](https://discourse.ubuntu.com/t/usecase-container-configuration/17782)|
| 3 | howto/container/logs | [View the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329)|
| 3 | howto/container/stop | [Stop a container](https://discourse.ubuntu.com/t/how-to-stop-a-container/33925)|
| 3 | howto/container/backup-and-restore | [Back up and restore application data](https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183)|
| 3 | howto/container/delete | [Delete a container](https://discourse.ubuntu.com/t/delete-a-container/24325)|
| 3 | howto/container/expose-services | [Expose services](https://discourse.ubuntu.com/t/expose-services-on-a-container/24326)|
| 2 | howto/addons/landing | [Use addons](https://discourse.ubuntu.com/t/managing-addons/17759)|
| 3 | howto/addons/enable-globally | [Enable globally](https://discourse.ubuntu.com/t/enable-an-addon-globally/25285)|
| 3 | howto/addons/update | [Update addons](https://discourse.ubuntu.com/t/update-addons/25286)|
| 3 | howto/addons/migrate | [Migrate from previous versions](https://discourse.ubuntu.com/t/migrate-from-previous-addon-versions/25287)|
| 3 | howto/addons/install-tools | [Example: Install tools](https://discourse.ubuntu.com/t/example-install-tools/25288)|
| 3 | howto/addons/backup-and-restore | [Example: Back up data](https://discourse.ubuntu.com/t/example-back-up-data/25289)|
| 3 | howto/addons/customise-android | [Example: Customise Android](https://discourse.ubuntu.com/t/example-customise-android/25290)|
| 3 | howto/addons/emulate-platforms | [Example: Emulate platforms](https://discourse.ubuntu.com/t/example-emulate-platforms/25291)|
| 3 | howto/addons/best-practices | [Best practices](https://discourse.ubuntu.com/t/best-practices-for-addons/25292)|
| 2 | howto/stream/landing | [Implement streaming](https://discourse.ubuntu.com/t/implement-streaming/24332) |
| 3 | howto/stream/access | [Access the stream gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784) |
| 3 | howto/stream/oob-data | [Exchange OOB data](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)|
| 3 | howto/stream/client-side-keyboard | [Use a client-side keyboard](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643)|
| 2 | howto/cluster/landing | [Manage the cluster](https://discourse.ubuntu.com/t/manage-cluster-nodes/24334) |
| 3 | howto/cluster/appliance | [Join a machine to the appliance](https://discourse.ubuntu.com/t/how-to-join-a-machine-to-the-anbox-cloud-appliance/29054) |
| 3 | howto/cluster/configure-nodes | [Configure cluster nodes](https://discourse.ubuntu.com/t/configure-cluster-nodes/28716) |
| 3 | howto/cluster/scale-up | [Scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322)|
| 3 | howto/cluster/scale-down | [Scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323)|
| 2 | howto/anbox/landing | [Work with the Anbox runtime](https://discourse.ubuntu.com/t/how-to-work-with-the-anbox-runtime/33098) |
| 3 | howto/anbox/develop-platform | [Develop a platform plugin](https://discourse.ubuntu.com/t/how-to-develop-a-platform-plugin/33099) |
| 3 | howto/anbox/develop-addon | [Develop and test addons](https://discourse.ubuntu.com/t/develop-and-test-addons-in-development-mode/36914) |
| 2 | howto/troubleshoot/landing | [Troubleshoot Anbox Cloud](https://discourse.ubuntu.com/t/how-to-troubleshoot-anbox-cloud/17837)|
| 3 | howto/troubleshoot/initial-setup | [Troubleshoot initial setup](https://discourse.ubuntu.com/t/troubleshoot-issues-with-initial-setup/35704)|
| 3 | howto/troubleshoot/logs | [View logs](https://discourse.ubuntu.com/t/managing-logs/17771)|
| 3 | howto/troubleshoot/application-creation | [Troubleshoot application creation](https://discourse.ubuntu.com/t/troubleshoot-issues-with-application-creation/35702)|
| 3 | howto/troubleshoot/container-failures | [Troubleshoot container failures](https://discourse.ubuntu.com/t/troubleshoot-container-failures/35703)|
| 3 | howto/troubleshoot/lxd-cluster | [Troubleshoot LXD cluster](https://discourse.ubuntu.com/t/troubleshoot-issues-with-lxd-clustering/35705)|
| 3 | howto/troubleshoot/dashboard-issues | [Troubleshoot dashboard issues](https://discourse.ubuntu.com/t/36105)
| 3 | howto/troubleshoot/streaming-issues | [Troubleshoot streaming issues](https://discourse.ubuntu.com/t/how-to-debug-streaming-issues/31341)|
| 2 | howto/monitor/landing | [Monitor Anbox Cloud](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338) |
| 3 | howto/monitor/telegraf | [Configure Telegraf](https://discourse.ubuntu.com/t/how-to-configure-telegraf/30365)
| 3 | howto/monitor/collect-metrics | [Example: Collect metrics](https://discourse.ubuntu.com/t/monitoring-grafana/17787)|
| 3 | howto/monitor/monitor-status | [Example: Monitor status](https://discourse.ubuntu.com/t/monitoring-nagios/17788)|
| 0 | | |
| 1 | ref/landing | [Reference](https://discourse.ubuntu.com/t/reference/28828) |
| 2 | ref/releases-versions | [Releases and versions](https://discourse.ubuntu.com/t/releases-and-versions/37993) |
| 3 | ref/roadmap | [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)|
| 3 | ref/release-notes | [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)|
| 3 | ref/supported-versions | [Supported versions](https://discourse.ubuntu.com/t/supported-versions/21046) |
| 3 | ref/component-versions | [Component versions](https://discourse.ubuntu.com/t/component-versions/21413)|
| 2 | ref/requirements | [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) |
| 2 | ref/provided-images | [Provided images](https://discourse.ubuntu.com/t/provided-images/24185)|
| 2 | ref/supported-rendering-resources | [Supported rendering resources](https://discourse.ubuntu.com/t/supported-rendering-resources/37322) |
| 2 | ref/supported-codecs | [Supported codecs](https://discourse.ubuntu.com/t/37323)|
| 2 | ref/android-features | [Supported Android features](https://discourse.ubuntu.com/t/supported-android-features/28825)|
| 2 | ref/ams-configuration | [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)|
| 2 | ref/application-manifest | [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)|
| 2 | ref/api-reference | [APIs](https://discourse.ubuntu.com/t/api-reference/24339) |
| 3 | ref/ams-http-api | [AMS HTTP API](https://anbox-cloud.github.io/latest/ams/)|
| 3 | ref/anbox-https-api | [Anbox HTTP API](https://discourse.ubuntu.com/t/anbox-http-api-reference/17819)|
| 3 | ref/anbox-stream-gateway | [Stream Gateway API](https://anbox-cloud.github.io/latest/anbox-stream-gateway/)|
| 3 | ref/anbox-platform-sdk-api | [Anbox Platform SDK API](https://anbox-cloud.github.io/latest/anbox-platform-sdk/)|
| 2 | ref/sdks | [Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844)|
| 2 | ref/network-ports | [Network ports](https://discourse.ubuntu.com/t/network-ports/33650)|
| 2 | ref/addons | [Addons](https://discourse.ubuntu.com/t/addons/25293)|
| 2 | ref/hooks | [Hooks](https://discourse.ubuntu.com/t/hooks/28555)|
| 2 | ref/webrtc-streamer | [WebRTC streamer](https://discourse.ubuntu.com/t/webrtc-streamer/30195)|
| 2 | ref/prometheus | [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)|
| 2 | ref/perf-benchmarks | [Performance benchmarks](https://discourse.ubuntu.com/t/performance-benchmarks/24709)|
| 2 | ref/license-information | [License information](https://discourse.ubuntu.com/t/license-information/36649) |
| 2 | ref/glossary | [Glossary](https://discourse.ubuntu.com/t/glossary/26204)|
| 0 | | |
| 1 | exp/landing | [Explanation](https://discourse.ubuntu.com/t/explanation/28829) |
| 2 | exp/anbox-cloud | [Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) |
| 2 | exp/rendering-architecture | [Rendering architecture](https://discourse.ubuntu.com/t/about-rendering-architecture/35129)
| 2 | exp/security | [Security](https://discourse.ubuntu.com/t/about-security/31217)|
| 2 | exp/ams | [AMS](https://discourse.ubuntu.com/t/about-ams/24321)|
| 2 | exp/aar | [AAR](https://discourse.ubuntu.com/t/application-registry/17761)|
| 2 | exp/applications | [Applications](https://discourse.ubuntu.com/t/managing-applications/17760)|
| 2 | exp/application-streaming | [Application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769)|
| 2 | exp/containers | [Containers](https://discourse.ubuntu.com/t/managing-containers/17763)|
| 2 | exp/platforms | [Platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)|
| 2 | exp/gpus-containers | [GPUs and containers](https://discourse.ubuntu.com/t/17768)|
| 2 | exp/clustering | [Clustering](https://discourse.ubuntu.com/t/capacity-planning/17765)|
| 2 | exp/performance | [Performance](https://discourse.ubuntu.com/t/about-performance/29416) |
| 2 | exp/capacity-planning | [Capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) |
| 2 | exp/production | [Production planning](https://discourse.ubuntu.com/t/about-production-planning/34648) |
| 0 | | |
|   | release-notes/1.19.1 | [Release notes-Anbox Cloud 1.19.1](https://discourse.ubuntu.com/t/38595)|
|   | release-notes/1.19.0-fix1 | [Hotfix release announcement](https://discourse.ubuntu.com/t/38250)|
|   | release-notes/1.19.0 | [Release notes-Anbox Cloud 1.19.0](https://discourse.ubuntu.com/t/37849)|
|   | release-notes/1.18.2 | [Release notes-Anbox Cloud 1.18.2](https://discourse.ubuntu.com/t/36916)|
|   | release-notes/1.18.1 | [Release notes-Anbox Cloud 1.18.1](https://discourse.ubuntu.com/t/36309)|
|   | release-notes/1.18.0 | [Release notes-Anbox Cloud 1.18.0](https://discourse.ubuntu.com/t/35812)|
|   | release-notes/1.17.2 | [Release notes-Anbox Cloud 1.17.2](https://discourse.ubuntu.com/t/35195)|
|   | release-notes/1.17.1 | [Release notes-Anbox Cloud 1.17.1](https://discourse.ubuntu.com/t/34573)|
|   | release-notes/1.17.0 | [Release notes-Anbox Cloud 1.17.0](https://discourse.ubuntu.com/t/33927)|
|   | release-notes/1.16.4 | [Release notes-Anbox Cloud 1.16.4](https://discourse.ubuntu.com/t/33437)|
|   | release-notes/1.16.3 | [Release notes-Anbox Cloud 1.16.3](https://discourse.ubuntu.com/t/33261)|
|   | release-notes/1.16.2 | [Release notes-Anbox Cloud 1.16.2](https://discourse.ubuntu.com/t/33161)|
|   | release-notes/1.16.1 | [Release notes-Anbox Cloud 1.16.1](https://discourse.ubuntu.com/t/32733)|
|   | release-notes/1.16.0 | [Release notes-Anbox Cloud 1.16.0](https://discourse.ubuntu.com/t/32264)|
|   | release-notes/1.15.3 | [Release notes-Anbox Cloud 1.15.3](https://discourse.ubuntu.com/t/31616)|
|   | release-notes/1.15.2 | [Release notes-Anbox Cloud 1.15.2](https://discourse.ubuntu.com/t/31322)|
|   | release-notes/1.15.1 | [Release notes-Anbox Cloud 1.15.1](https://discourse.ubuntu.com/t/30585)|
|   | release-notes/1.15.0 | [Release notes-Anbox Cloud 1.15.0](https://discourse.ubuntu.com/t/30196)|
|   | release-notes/1.14.2 | [Release notes-Anbox Cloud 1.14.2](https://discourse.ubuntu.com/t/29553)|
|   | release-notes/1.14.1 | [Release notes-Anbox Cloud 1.14.1](https://discourse.ubuntu.com/t/28952)|
|   | release-notes/1.14.0 | [Release notes-Anbox Cloud 1.14.0](https://discourse.ubuntu.com/t/28557)|
|   | release-notes/1.13.2 | [Release notes-Anbox Cloud 1.13.2](https://discourse.ubuntu.com/t/27701)|
|   | release-notes/1.13.1 | [Release notes-Anbox Cloud 1.13.1](https://discourse.ubuntu.com/t/27254)|
|   | release-notes/1.13.0 | [Release notes-Anbox Cloud 1.13.0](https://discourse.ubuntu.com/t/26857)|
|   | release-notes/1.12.5 | [Release notes-Anbox Cloud 1.12.5](https://discourse.ubuntu.com/t/26380)|
|   | release-notes/1.12.4 | [Release notes-Anbox Cloud 1.12.4](https://discourse.ubuntu.com/t/26263)|
|   | release-notes/1.12.3 | [Release notes-Anbox Cloud 1.12.3](https://discourse.ubuntu.com/t/26252)|
|   | release-notes/1.12.2 | [Release notes-Anbox Cloud 1.12.2](https://discourse.ubuntu.com/t/25819)|
|   | release-notes/1.12.1 | [Release notes-Anbox Cloud 1.12.1](https://discourse.ubuntu.com/t/25542)|
|   | release-notes/1.12.0 | [Release notes-Anbox Cloud 1.12.0](https://discourse.ubuntu.com/t/25295)|
|   | release-notes/1.11.5 | [Release notes-Anbox Cloud 1.11.5](https://discourse.ubuntu.com/t/26739)|
|   | release-notes/1.11.4 | [Release notes-Anbox Cloud 1.11.4](https://discourse.ubuntu.com/t/25018)|
|   | release-notes/1.11.3 | [Release notes-Anbox Cloud 1.11.3](https://discourse.ubuntu.com/t/24705)|
|   | release-notes/1.11.2 | [Release notes-Anbox Cloud 1.11.2](https://discourse.ubuntu.com/t/24293)|
|   | release-notes/1.11.1 | [Release notes-Anbox Cloud 1.11.1](https://discourse.ubuntu.com/t/23772)|
|   | release-notes/1.11.0 | [Release notes-Anbox Cloud 1.11.0](https://discourse.ubuntu.com/t/23590)|
|   | release-notes/1.10.3 | [Release notes-Anbox Cloud 1.10.3](https://discourse.ubuntu.com/t/23267)|
|   | release-notes/1.10.2 | [Release notes-Anbox Cloud 1.10.2](https://discourse.ubuntu.com/t/22692)|
|   | release-notes/1.10.1 | [Release notes-Anbox Cloud 1.10.1](https://discourse.ubuntu.com/t/22280)|
|   | release-notes/1.10.0 | [Release notes-Anbox Cloud 1.10.0](https://discourse.ubuntu.com/t/22205)|
|   | release-notes/1.9.5 | [Release notes-Anbox Cloud 1.9.5](https://discourse.ubuntu.com/t/22259)|
|   | release-notes/1.9.4 | [Release notes-Anbox Cloud 1.9.4](https://discourse.ubuntu.com/t/22148)|
|   | release-notes/1.9.3 | [Release notes-Anbox Cloud 1.9.3](https://discourse.ubuntu.com/t/21795)|
|   | release-notes/1.9.2 | [Release notes-Anbox Cloud 1.9.2](https://discourse.ubuntu.com/t/21420)|
|   | release-notes/1.9.1 | [Release notes-Anbox Cloud 1.9.1](https://discourse.ubuntu.com/t/21232)|
|   | release-notes/1.9.0 | [Release notes-Anbox Cloud 1.9.0](https://discourse.ubuntu.com/t/20870)|
|   | release-notes/1.8.3 | [Release notes-Anbox Cloud 1.8.3](https://discourse.ubuntu.com/t/20435)|
|   | release-notes/1.8.2 | [Release notes-Anbox Cloud 1.8.2](https://discourse.ubuntu.com/t/19951)|
|   | release-notes/1.8.1 | [Release notes-Anbox Cloud 1.8.1](https://discourse.ubuntu.com/t/19319)|
|   | release-notes/1.8.0 | [Release notes-Anbox Cloud 1.8.0](https://discourse.ubuntu.com/t/19200)|
|   | release-notes/1.7.4 | [Release notes-Anbox Cloud 1.7.4](https://discourse.ubuntu.com/t/18812)|
|   | release-notes/1.7.3 | [Release notes-Anbox Cloud 1.7.3](https://discourse.ubuntu.com/t/18458)|
|   | release-notes/1.7.2 | [Release notes-Anbox Cloud 1.7.2](https://discourse.ubuntu.com/t/18265)|
|   | release-notes/1.7.1 | [Release notes-Anbox Cloud 1.7.1](https://discourse.ubuntu.com/t/17977)|
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
| /docs/howto/stream/web-client | /docs/tut/stream-client |
| /docs/exchange-out-of-band-data | /docs/howto/stream/oob-data |
| /docs/integrate-keyboard | /docs/howto/stream/client-side-keyboard |
| /docs/faq | /docs/howto/troubleshoot/landing |
| /docs/howto/troubleshoot/collect-info | /docs/howto/troubleshoot/landing |
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
| /docs/exp/gpu-support | /docs/exp/gpus-containers |
| /docs/manage/benchmarking-a-deployment | /docs/exp/benchmarking |
| /docs/manage/streaming-android-applications | /docs/exp/application-streaming |
| /docs/usage/usecase-port-android-application-to-anbox-cloud | /docs/exp/porting-issues |
| /docs/installation/installation-requirements | /docs/requirements |
| /docs/exp/porting-issues | /docs/howto/port/landing |
| /docs/exp/benchmarking | /docs/howto/manage/benchmarks |
| /docs/changelog | /docs/release-notes |
| /docs/howto/monitor/grafana | /docs/howto/monitor/collect-metrics |
| /docs/howto/monitor/nagios | /docs/howto/monitor/monitor-status |
| /docs/howto/container/launch | /docs/howto/container/create |
| /docs/howto/stream/debug | /docs/howto/troubleshoot/streaming-issues |
| /docs/howto/manage/web-dashboard | /docs/howto/dashboard/web-dashboard |
| /docs/howto/manage/logs | /docs/howto/troubleshoot/logs |
| /docs/ref/platforms | /docs/exp/platforms |
| /docs/requirements | /docs/ref/requirements |
| /docs/release-notes | /docs/ref/release-notes |
| /docs/roadmap | /docs/ref/roadmap |
| /docs/component-versions | /docs/ref/component-versions |
| /docs/supported-versions | /docs/ref/supported-versions |
| /docs/ref/instance-types | /docs/ref/application-manifest |
| /docs/ref/supported-video-codecs | /docs/ref/supported-codecs |
[/details]
