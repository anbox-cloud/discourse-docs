AMS provides various configuration items to customise its behaviour. The following table lists the available configuration items and their meaning.


| Name | Type | Default |  Description            |
|------|------|---------|-------------------------|
| `application.addons` | string | -  | Comma-separated list of addons that every application managed by AMS will use. See [How to enable an addon globally](https://discourse.ubuntu.com/t/enable-an-addon-globally/25285). |
| `application.auto_publish` | bool | true | If set to `true`, AMS automatically published new application versions when the bootstrap process is finished. `false` disables this. See [Publish application versions](https://discourse.ubuntu.com/t/update-an-application/24201#publish-application-versions). |
| `application.auto_update` | bool | true | If set to `true`, AMS automatically updates applications whenever any dependencies (parent image, addons, global configuration) change. `false` disables this. See [Disable automatic application updates](https://discourse.ubuntu.com/t/update-an-application/24201#disable-automatic-updates). |
| `application.default_abi` | string | - | Default Android ABI that applications should use. See [Android ABIs](https://developer.android.com/ndk/guides/abis) for a list of available ABIs. |
| `application.max_published_versions` | integer | 3 | Maximum number of published versions per application. If the number of versions of an application exceeds this configuration, AMS will automatically clean up older versions. |
| `container.default_platform` | string | -  | The name of the platform that Anbox uses by default to launch containers. |
| `container.features` | string | - | Comma-separated list of features to enable (see list below). |
| `container.network_proxy` | string | - | Network proxy to use inside the containers. |
| `container.security_updates` | bool | true | If set to `true`, automatic Ubuntu security updates are applied during the application bootstrap process. `false` disables this. |
| `core.proxy_http` | string | - | HTTP proxy to use for HTTP requests that AMS performs. |
| `core.proxy_https` | string | - | HTTPS proxy to use for HTTPS requests that AMS performs. |
| `core.proxy_ignore_hosts` | string | - | Comma-separated list that defines the hosts for which a configured proxy is not used. |
| `core.trust_password` | string | - | The AMS trust password. |
| `gpu.allocation_mode` | string | `all` | Method of allocating GPUs: `all` tells AMS to allocate all available GPUs on a system to a container. `single` allocates only a single GPU. |
| `gpu.type` | string | `none` | Type of GPU: `none`, `intel`, `nvidia`, `amd` |
| `images.allow_insecure`| bool | false | If set to `true`, AMS allows accepting untrusted certificates provided by the configured image server. |
| `images.auth` | string | - | Authentication details for AMS to access the image server. When reading this configuration, a Boolean value that indicates whether the item is set is returned, to avoid exposing credentials. |
| `images.update_interval` | string | `5m` | Frequency of image updates (for example: 1h, 30m). |
| `images.url` | string | `https://images.anbox-cloud.io/stable/` | URL of the image server to use. |
| `images.version_lockstep` | bool | true | Whether to put the version of the latest pulled image and the AMS version in a lockstep. This ensures that a deployment is not automatically updated to newer image versions if AMS is still at an older version. This only applies for new major and minor but not patch version updates. |
| `node.queue_size` | integer | 100 | Maximum size of the queue containing requests to start and stop container per LXD node. Changing the value requires a restart of AMS. |
| `node.workers_per_queue` | integer | 4 | Number of workers processing container start and stop requests. Changing the value requires a restart of AMS. |
| `registry.filter` | string |  - | Comma-separated list of tags to filter for when applications are fetched from the [Anbox Application Registry](https://discourse.ubuntu.com/t/application-registry/17761). If empty, no filter is applied. |
| `registry.fingerprint` | string | - | Fingerprint of the certificate that the [Anbox Application Registry](https://discourse.ubuntu.com/t/application-registry/17761) uses to TLS-secure its HTTPS endpoint. This is used by AMS for mutual TLS authentication with the registry. |
| `registry.mode` | string | `pull` | Mode in which the [Anbox Application Registry](https://discourse.ubuntu.com/t/application-registry/17761) client in AMS operates: `manual`, `pull`, `push` |
| `registry.update_interval` | string | `1h` | Frequency of [Anbox Application Registry](https://discourse.ubuntu.com/t/application-registry/17761) updates (for example: 1h, 30m). |
| `registry.url` | string | - | URL of the [Anbox Application Registry](https://discourse.ubuntu.com/t/application-registry/17761) to use. |
| `scheduler.strategy` | string | `spread` | Strategy that the internal container scheduler in AMS uses to distribute containers across available LXD nodes: `binpack`, `spread` |

<a name="node-specific"></a>
## Node-specific configuration

In a cluster setup, there are configuration items that can be customised for each node. The following table lists the available configuration items and their meaning.

| Name | Type | Default |  Description            |
|------|------|---------|-------------------------|
| `cpu-allocation-rate` | integer | 4 | CPU allocation rate used for [over-committing resources](https://discourse.ubuntu.com/t/about-capacity-planning/28717#overcommitting). |
| `cpus` | integer | all available | Number of CPUs dedicated to Anbox containers. |
| `gpu-encoder-slots` | integer | 0 (for nodes without GPU or with AMD GPU)<br/>32 (for nodes with NVIDIA GPU)<br/>10 (for nodes with Intel GPU)| Number of GPU encoder slots available on the node. |
| `gpu-slots` | integer | 0 (for nodes without GPU)<br/>32 (for nodes with NVIDIA GPU)<br/>10 (for nodes with AMD or Intel GPU)| Number of [GPU slots](https://discourse.ubuntu.com/t/about-capacity-planning/28717#gpu-slots) available on the node. |
| `memory` | integer | all available | Memory dedicated to Anbox containers. |
| `memory-allocation-rate` | integer | 2 | Memory allocation rate used for [over-committing resources](https://discourse.ubuntu.com/t/about-capacity-planning/28717#overcommitting). |
| `public-address` | string | - | The public, reachable address of the node. |
| `subnet` | string | - | The network subnet of the machine where the node runs. |
| `tags` | string | - | Tags to identify the node. |
| `unscheduable` | bool | false | If set to `true`, the node cannot be scheduled, which prevents new containers from being launched on it. |

See [Configure cluster nodes](https://discourse.ubuntu.com/t/configure-cluster-nodes/28716) for instructions on how to set these configuration items.

## Features

Anbox Cloud includes some features which are not enabled by default but can be conditionally enabled. The features are enabled by flags which are configured through AMS. You can configure the feature flags either globally for all containers or per application.

To configure a feature globally for all containers, use a command similar to the following:

    amc config set container.feature foo,bar

To configure a feature for one application in the manifest, use a syntax similar to the following:

    name: my-app
    instance-type: a4.3
    features: ["foo", "bar"]

#### System UI

*since 1.10.2*

By default, Anbox hides the Android system UI when an application is running in foreground mode. In some use cases, however, it's required to have the system UI available for navigation purposes. This can be enabled with the `enable_system_ui` feature flag.

The feature flag will be considered by all new launched containers once set.

#### Virtual Keyboard

*since 1.9.0*

The Android virtual keyboard is disabled by default but can be enabled with the `enable_virtual_keyboard` feature flag.

For the feature to be considered, applications must be manually updated, because changes to allow the feature to work are only applied during the [application bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap).

#### Client-Side Virtual Keyboard

*since 1.11.0*

The client-side virtual keyboard is disabled by default but can be enabled with the `enable_anbox_ime` feature flag. It requires the client application to embed [Anbox WebView](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643) which interacts with the client-side virtual keyboard for text editing and sends the text to the Android container.

For the feature to be considered, applications must be manually updated, because changes to allow the feature to work are only applied during the [application bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap).

#### WiFi

*since 1.12.0*

WiFi support can be optionally enabled with the `enable_wifi` feature flag. Anbox will then set up a virtual WiFi device, which sits on top of an Ethernet connection and simulates a real WiFi connection.

The feature flag will be considered by all newly launched containers once set.

### Android reboot

*since 1.12.0*

By default, Android is not allowed to reboot. With the `allow_android_reboot` feature flag, this can be allowed.

Note that you must disable the [watchdog](https://discourse.ubuntu.com/t/application-manifest/24197#watchdog) if reboots are allowed.

The feature flag will be considered by all newly launched containers once set.