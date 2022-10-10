AMS provides various configuration items to customise its behaviour. The following table lists the available configuration items and their meaning.

<!-- GENERATED_TABLE all -->

<a name="node-specific"></a>
## Node-specific configuration

In a cluster setup, there are configuration items that can be customised for each node. The following table lists the available configuration items and their meaning.

<!-- GENERATED_TABLE node -->

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
