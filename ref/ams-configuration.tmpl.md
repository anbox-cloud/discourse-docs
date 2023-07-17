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

By default, Anbox hides the Android system UI when an application is running in foreground mode. In some use cases, however, it's required to have the system UI available for navigation purposes. This can be enabled with the `enable_system_ui` feature flag.

The feature flag will be considered by all new launched containers once set.

#### Virtual Keyboard

The Android virtual keyboard is disabled by default but can be enabled with the `enable_virtual_keyboard` feature flag.

For the feature to be considered, applications must be manually updated, because changes to allow the feature to work are only applied during the [application bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap).

#### Client-Side Virtual Keyboard

The client-side virtual keyboard is disabled by default but can be enabled with the `enable_anbox_ime` feature flag. It requires the client application to embed [Anbox WebView](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643) which interacts with the client-side virtual keyboard for text editing and sends the text to the Android container.

For the feature to be considered, applications must be manually updated, because changes to allow the feature to work are only applied during the [application bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap).

#### WiFi

WiFi support can be optionally enabled with the `enable_wifi` feature flag. Anbox will then set up a virtual WiFi device, which sits on top of an Ethernet connection and simulates a real WiFi connection.

The feature flag will be considered by all newly launched containers once set.

#### Android reboot

By default, Android is not allowed to reboot. With the `allow_android_reboot` feature flag, this can be allowed.

Note that you must disable the [watchdog](https://discourse.ubuntu.com/t/application-manifest/24197#watchdog) if reboots are allowed.

The feature flag will be considered by all newly launched containers once set.

#### AV1 software encoder

*since 1.17.0*

The AV1 software encoder is disabled by default but can be enabled with the `experimental.force_av1_software_encoding` feature flag. To transcode the video stream encoded in AV1 codec, all clients must support AV1 decoding.

Once set, this feature flag will be considered by all newly launched containers.

#### Development settings

*since 1.18.0*

The Android development settings (which include an ADB connection) are enabled by default. Some applications require these settings to be disabled, which you can do with the `disable_development_settings` feature flag.

Once set, this feature flag will be considered by all newly launched containers.

#### Custom Android ID

*since 1.18.0*

To enable the Android container to use a custom Android ID, add the feature flag `android.allow_custom_android_id` upon application creation. A system app can influence the Android ID of a specific app during the Android runtime by setting the system property in the format of:
  ```
  `anbox.custom_android_id.<index>=<package_name>:<android_id>`
  ```

 * The `<index>` is a number in the range from 0 to 126, which allows you to have multiple overrides for different packages. If the same `<package_name>` with the different `<android_id>` is given for multiple system properties `anbox.custom_android_id.<index>`, the Android ID read from the system property which has the highest suffixing index that will be used in the end.
 * The `<package_name>` is the package name of the application.
 * The `<android_id>` is a unique ID that represents the Android ID for the targeting application. It must be at least 16 characters in length.

Once set, this feature flag will be considered by all newly launched containers.

#### Disable cgroup v1 Emulation

*since 1.19.0*

Android requires a number of cgroup v1 controllers, which Anbox emulates on top of cgroup v2. If your kernel still has support for cgroup v1, you can disable cgroup v1 emulation by setting the `disable_cgroup_emulation` feature flag.

Once set, this feature flag will be considered by all newly launched containers.
