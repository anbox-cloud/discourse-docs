[note type="information" status="Note"]If you're interested in getting notified for the latest Anbox Cloud releases, make sure you subscribe to notifications on the [announcements category](https://discourse.ubuntu.com/c/anbox-cloud/announcements/55) on the Anbox Cloud discourse.[/note]

See [How to upgrade Anbox Cloud](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750) or [How to upgrade the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186) for
instructions on how to update your Anbox Cloud deployment.

[Details=1.16.3]

## 1.16.3 (January 17 2023)

#### New features & improvements

n/a

#### Bugs

* [LP #2002776](https://bugs.launchpad.net/charm-grafana/+bug/2002776): Grafana APT repository key was rotated and charm needs to adapt

[/Details]

[Details=1.16.2]

## 1.16.2 (January 12 2023)

#### New features & improvements

* Included Android security updates for January 2023 (see [Android Security Bulletin - January 2023](https://source.android.com/security/bulletin/2023-01-01) for more information).
* Updated Android WebView to [108.0.5359.128](https://chromereleases.googleblog.com/2022/12/chrome-for-android-update_13.html).

#### Bugs

* AC-1276 `finalrd.service`: Failed with result 'exit-code'.
* AC-1277 The pre-start/install hook to modify Android's root file system always failed
* [LP #2002020](https://bugs.launchpad.net/charm-etcd/+bug/2002020): `anbox-cloud-core`: `etcd/jammy`: hook failed: "install" due to `error in Tempita setup command: use_2to3 is invalid.`

[/Details]

[Details=1.16.1]

## 1.16.1 (December 14 2022)

#### New features & improvements

* Included Android security updates for December 2022 (see [Android Security Bulletin - December 2022](https://source.android.com/security/bulletin/2022-12-01) for more information).
* Updated Android WebView to [108.0.5359.79](https://chromereleases.googleblog.com/2022/12/chrome-for-android-update.html).

#### Bugs

* AC-1222 `ext4` online metadata check service is active but should not be
* AC-1229 Appliance bootstrap doesn't fail when an Juju unit ends up in an error status
* AC-1230 The `gpu-slots` remains 0 occasionally even after AMS detects NVIDIA GPU type
* AC-1235 ANGLE for `null` platform attempts to initialise Vulkan renderer
* AC-1264 Fatal exception occurred to `com.android.systemui` when launching an application (Android 13 based) with boot package
* AC-1267 Data channels fail to connect

[/Details]

[Details=1.16.0]

# 1.16.0 (November 16 2022)

#### New features & improvements

* Added support for Android 13.
* Updated Anbox to provide a serial ID derived from the container ID to satisfy Android's conformance requirements.
* Switched the AMD and Intel GPU support to be based on Vulkan and to use [ANGLE](https://chromium.googlesource.com/angle/angle) as the EGL/OpenGL ES frontend driver.
* Updated Mesa for AMD and Intel GPUs to the [22.2.2](https://docs.mesa3d.org/relnotes/22.2.2.html) release.
* Split Android's system and vendor directories.
* Added a bug report utility inside the Anbox container.
* Included various WebRTC streaming improvements.
* Introduced the WebRTC data proxy server to enable full-duplex bidirectional data transmission between Android and a WebRTC-based client.
* Added full support for Ubuntu 22.04 for regular and appliance deployments.
* Updated AMS to allow configuring a custom APT mirror for all containers.
* Added a new AMS charm configuration `use_network_acl` to allow for experimental use of [LXD network ACLs](https://linuxcontainers.org/lxd/docs/latest/howto/network_acls/) instead of the AMS node controller to restrict network access of Anbox containers.
* Included Android security updates for November 2022 (see [Android Security Bulletin - November 2022](https://source.android.com/docs/security/bulletin/2022-11-01) for more information).
* Updated Android WebView to [107.0.5304.105](https://chromereleases.googleblog.com/2022/11/chrome-for-android-update.html).
* Updated the used NVIDIA driver series to [515](https://docs.nvidia.com/datacenter/tesla/index.html), which is supported until May 2023.
* Updated the appliance to deploy LXD containers based on Ubuntu 22.04 on new deployments (existing deployments keep their existing containers based on Ubuntu 20.04).
* Updated the [`ams-lxd`](https://charmhub.io/ams-lxd) Juju charm and the Anbox Cloud Appliance to automatically detect AMD GPU support and configure the kernel `amdgpu` driver for best performance and support.
* Added support for the [AWS `g4ad` instance types](https://aws.amazon.com/ec2/instance-types/g4/) (equipped with AMD v520 GPUs) to the [Anbox Cloud Appliance images](https://aws.amazon.com/marketplace/pp/prodview-3lx6xyaapstz4) that are available through the AWS marketplace.
* Updated the appliance so that it can be initialised as any Ubuntu user, not just the `ubuntu` one.

#### Bugs

* AC-1066 Security rules are not applied properly when deploying Anbox Cloud with clustering set up
* AC-1101 Fingerprint support is marked as enabled
* AC-1102 Android has `ro.serialno` not set
* AC-1181 RenderThread is stopped when `/dev/anbox_sync` cannot be opened
* AC-1197 WebRTC data proxy fails with `4/NOPERMISSION` on stop
* AC-1204 The agent sets incorrect region value for provided metrics
* AC-1205 Playout delay set via RTP header causes error/warning on receiver
* AC-1207 Supervisor does not reconnect after agent was down for longer and terminates Anbox
* AC-1208 `MESA_GLSL_CACHE_DIR` is deprecated; use `MESA_SHADER_CACHE_DIR` instead

[/Details]

[Details=1.15.3]

# 1.15.3 (October 20 2022)

#### New features & improvements

* Work around a bug in Juju 2.9.35 that prevents the Anbox Cloud Appliance from deploying its software stack entirely. The workaround makes the deployment process independent of the Juju snap that is installed on the host system by including a Juju binary of a previous release inside the appliance snap.

#### Bugs

* [LP:1993137](https://bugs.launchpad.net/juju/+bug/1993137) Juju 2.9.35 breaks LXD deployment

[/Details]

[Details=1.15.2]

# 1.15.2 (October 12 2022)

#### New features & improvements

* Included Android security updates for October 2022 (see [Android Security Bulletin - October 2022](https://source.android.com/security/bulletin/2022-10-01) for more information).

## Known issues

n/a

#### Bugs

* AC-1136 All containers were gone after the appliance snap got refreshed
* AC-1130 Cannot reconnect to stream session after client with unsupported video codecs tried
* AC-1087 Can't delete an application when the application bootstrap ends up in an error state

[/Details]

[Details=1.15.1]

## 1.15.1 (September 14 2022)

#### New features & improvements

* Included Android security updates for September 2022 (see [Android Security Bulletin - September 2022](https://source.android.com/security/bulletin/2022-09-01) for more information).
* Updated Android WebView to [105.0.5195.79](https://chromereleases.googleblog.com/2022/09/chrome-for-android-update_5.html).

## Known issues

n/a

#### Bugs

* AC-1087 Can't delete an application when the application bootstrap ends up in an error state
* AC-1079 Not possible to stream container anymore after Android rebooted
* AC-1078 No input is possible after rebooting Android
* AC-1069 Transport channel closed error occurred when disconnecting a stream on Android client

[/Details]

[Details=1.15.0]

## 1.15.0 (August 24 2022)

#### New features & improvements

* All snaps are now based on the [`core20`](https://snapcraft.io/core20) snap.
* AMS now provides support for a [development mode](https://anbox-cloud.io/docs/exp/containers#dev-mode).
* TLS 1.3 is now enforced by default by AMS.
* New `cpu.limit_mode` AMS configuration option allows to enable CPU core pinning.
* Configuration of an external load balancer for containers spawned by AMS.
* The [WebRTC streamer configuration](https://anbox-cloud.io/docs/ref/webrtc-streamer) can now be customised.
* A new HTTP `/1.0/platform` API allows runtime configuration of the currently loaded platform.
* Anbox now uses the recently released [LXC 5.0](https://discuss.linuxcontainers.org/t/lxc-5-0-lts-has-been-released/14381).
* The WebRTC streamer now allows streaming only audio, only video or neither of them.
* Anbox now uses [`jemalloc`](https://github.com/jemalloc/jemalloc) as memory allocator.
* A new OOB version 2 implementation allows bi-directional communication with the Anbox container through the use of data channels.
* Added Android security updates for August 2022 (see [Android Security Bulletin - August 2022](https://source.android.com/docs/security/bulletin/2022-08-01) for more information).
* Updated the Android WebView to [103.0.5060.129](https://chromereleases.googleblog.com/2022/07/chrome-for-android-update_01510389319.html).
* Updated the Mesa graphics driver stack to [22.0.5](https://docs.mesa3d.org/relnotes/22.0.5.html).
* The `ashmem` kernel module is now optional for all supported Android versions.
* Updated Dqlite to its latest [1.11.1 release](https://github.com/canonical/dqlite/releases/tag/v1.11.1).
* The Anbox Cloud Appliance now supports deployment on Ubuntu 22.04.
* The minimum required storage size is now 20 GB for the Anbox Cloud Appliance.
* On Ubuntu 22.04, the NVIDIA driver is now installed from the Ubuntu archive on arm64 systems instead of from the NVIDIA CUDA archive.
* The WebRTC benchmark tool (`anbox-cloud-tests.benchmark`) can now:
  * Attach to existing sessions (`--session=<id>`).
  * Mark sessions to be kept alive after the benchmark is done (`--keep-session`).
  * Set the WebRTC log level to gain low-level insight (`--log-level=<level>`).

## Known issues

n/a

## Bug fixes

* AC-1036 A native crash happens when streaming from the camera on Safari (iOS device)
* AC-1034 Fix race condition between `init.ranchu.rc` and SurfaceFlinger causing a crash
* AC-1028 User-defined resources are overridden when both `instance-type` and `resources` specs are specified in `session.yaml`
* AC-1015 Can't access the service that is exposed internally over IP forward
* AC-1003 The network endpoint and port persist in the database even after the container is deleted from AMS
* AC-966 Anbox tries to initialise the video decoder when a stream is being established

[/Details]

[Details=1.14.2]

## 1.14.2 (July 18 2022)

#### New features & improvements

* Included Android security updates for July 2022 (see [Android Security Bulletin - July 2022](https://source.android.com/security/bulletin/2022-07-01) for more information).
* Updated Android WebView to [103.0.5060.71](https://chromereleases.googleblog.com/2022/07/chrome-for-android-update.html).
* [Join URLs](https://anbox-cloud.github.io/latest/anbox-stream-gateway/#/session/handle-join-session) handed out by the Anbox Stream Gateway to the Anbox container instances will now not expire anymore. This allows sessions to run forever, if needed.
* The Anbox Cloud Appliance now supports deploying behind a HTTP proxy through the `--proxy` argument available for the `anbox-cloud-appliance init` command.

### Known issues

n/a

#### Bugs

* AC-945 An unhandled exception is raised when starting Anbox
* AC-943 No WebRTC metrics data are collected in the Grafana dashboard of the appliance
* AC-932 Anbox aborts due to assert in `libsoup` being triggered

[/Details]

[Details=1.14.1]

## 1.14.1 (June 16 2022)

#### New features & improvements

* Android security updates for June 2022 (see [Android Security Bulletin - June 2022](https://source.android.com/security/bulletin/2022-06-01) for more information)
* Android WebView has been updated to [102.0.5005.78](https://chromereleases.googleblog.com/2022/05/chrome-for-android-update_28.html)
* The Android [system app installation process](https://discourse.ubuntu.com/t/how-to-install-an-apk-as-a-system-app/27086) now supports the [APK Signature Scheme v2](https://source.android.com/security/apksigning/v2)

### Known issues

n/a

#### Bugs

* AC-930 AMS doesn't retry stripping a container when LXD returns not matching ETag
* AC-936 AMS is misbehaving when LXD cluster fails to process requests
* AC-929 Node controller doesn't start due to missing route utility
* AC-928 Use the `ip` command rather than `ifconfig` to parse the IP address of the network device in Anbox container
* AC-917 Anbox inside jammy images doesn't start on the jammy 5.15 kernel
* AC-913 Dashboard ended up to a blank screen when stopping a session at times
* AC-909 AAR leaves `aar_upload_*` files in `/tmp`
* AC-905 Images are not synchronised on 1.14 appliance
* AC-818 Show Android boot animation properly
* LP #1971945 Anbox Cloud WebRTC handshake failed error

[/Details]

[Details=1.14.0]

## 1.14.0 (May 23 2022)

### New features & improvements

* Migrated all charms to [Charmhub](https://charmhub.io).
* Added Anbox images based on Ubuntu 22.04.
* Added hook support for AMS applications.
* Added Vulkan support for AMD and Intel GPUs.
* Added multi-node support for the Anbox Cloud Appliance (experimental).
* Made the NVIDIA 510.x driver series the default.
* Implemented syscall interception through LXC `seccomp` notification support. This enables Anbox to handle different syscalls like `setpriority` or `sched_set_scheduler` for processes inside the Android container.
* Unified the pointer input model by using pointer events to handle mouse and touch events.
* Switched the memory allocator from `glibc` (the default) to `tcmalloc`, to decrease the memory footprint and optimise the memory consumption for the Anbox session.
* Added Android security updates for May 2022 (see [Android Security Bulletin - May 2022](https://source.android.com/security/bulletin/2022-05-01) for more information).
* Updated Android WebView to [101.0.4951.41](https://chromereleases.googleblog.com/2022/04/stable-channel-update-for-desktop_26.html).
* Updated Anbox Cloud to default to the 5.0 LTS release of LXD for all new deployments. The 4.0 release of LXD remains supported, so existing deployments can continue to use 4.0.

### Known issues

n/a

#### Bugs

* AC-877 Fix the bugs of JS SDK after the recent refactor
* AC-867 Android 12 image ships `com.android.emulator.multidisplay`
* AC-836 `vkcube` crashes without support for `HAL_PIXEL_FORMAT_RGBA_1010102`
* AC-835 Memory leaks happened to Anbox session process after a container running for a long time
* AC-833 Anbox host not set in `/etc/hosts` in Android 12
* AC-832 Android CTS tests report `/proc` isn't mounted with `hidepid=2`
* AC-821 CTS test cases for system features fail
* AC-814 AMS dashboard doesn't load on the Appliance
* AC-810 Failing gateway docs build fails and doesn't stop CI from succeeding
* AC-741 End touch/mouse events when leaving the SDK container
* AC-699 `dEQP-GLES3.functional.texture.shadow.cube.linear.greater_or_equal_depth24_stencil8` fails on `swrast`
* AC-693 SDK is broken on iOS on 4G only
* AC-548 Colours with direct software rendering in scrcpy are incorrect

[/Details]

[Details=1.13.2]

## 1.13.2 (April 13 2022)

### New features & improvements

* Android security updates for April 2022 (see [Android Security Bulletin - April 2022](https://source.android.com/security/bulletin/2022-04-01) for more information)
* Android WebView has been updated to [100.0.4896.79](https://chromereleases.googleblog.com/2022/04/chrome-for-android-update.html)
* The JavaScript Anbox Streaming SDK now has a `rotate` method to allow rotating the screen of the Android instance
* Addons can now specify an overall timeout for their hooks by setting the `hooks.timeout` key in the `manifest.yaml`

### Known issues

n/a

#### Bugs

* AC-830 On a multi GPU system default number of slots is split across all GPUs
* AC-829 AMS leaks ports for already removed containers
* AC-828 Changing the parent image of an application in AMS returns with error
* AC-811 Anbox `hwcomposer` crashes on highly loaded system with `wl_abort`
* AC-809 Empty device name is shown up when running `adb shell getevent`
* AC-788 DrArm is showing just a black screen
* AC-782 Add support for missing GL parameter sizes
* AC-765 Minetest crashes on 1.13.0 with SEGV in Anbox
* AC-725 A segfault occurred from the WebRTC stack during the Anbox session runtime
* AC-646 1.12 hooks: $CONTAINER_TYPE is empty for regular containers
* AC-827 Failed to create an arm64 based application when Anbox Cloud deployment is capable with multiple architectures

[/Details]

[Details=1.13.1]

## 1.13.1 (March 21 2022)

### New features & improvements

 * Android security updates for March 2022 (see [Android Security Bulletin - March 2022](https://source.android.com/security/bulletin/2022-03-01) for more information)
 * Android WebView has been updated to [99.0.4844.58](https://chromereleases.googleblog.com/2022/03/stable-channel-update-for-desktop.html)

### Known issues

n/a

#### Bugs

 * AC-786 Anbox crashes while a Wayland resource is released
 * AC-780 Appliance fails to deploy when monitoring is disabled
 * AC-777 The command `anbox-cloud-appliance gateway account create <account>` returned a slice of bytes in the output
 * AC-773 Redundant services fields displayed in the output of `amc show <container_id>`
 * AC-768 Coturn has 2x `external-ip` entries
 * AC-763 Task failed to be marked as failed when context has expired/got cancelled
 * AC-762 AMS fails to cancel container start/stop operations as they cannot be cancelled
 * AC-759 Stored artefacts have incorrect permissions
 * AC-758 AMS consumes too much memory during application creation
 * AC-746 The `hwservicemanager` can't find `android.hardware.vibrator@1.0::IVibrator/default` in either framework or device manifest
 * AC-739 Dashboard fails to load when application failed
 * AC-738 The scaling of the video frame that is captured from the camera is incorrect
 * AC-717 SDK: `experimental.disableBrowserBlock` is not properly verified and not taken into account
 * AC-713 Immersive mode confirmation dialog keeps popping up
 * AC-705 AMS suddenly increases memory consumption and causes OOM kill
 * AC-704 Mesa shader cache directory isn't accessible

[/Details]

[Details=1.13.0]

## 1.13.0 (February 24 2022)

#### New features & improvements

* OpenGL ES 3.2 support for NVIDIA GPUs
* Direct rendering for AMD and Intel GPUs
* Android security updates for February 2022 (see [Android Security Bulletin - February 2022](https://source.android.com/security/bulletin/2022-02-01) for more information)
* Android WebView has been updated to [98.0.4758.101](https://chromereleases.googleblog.com/2022/02/chrome-for-android-update_0839135123.html)

### Known issues

n/a

#### Bugs

* AC-732 Anbox session(WebRTC platform) crashed when reconnecting the signaller(stream gateway)
* AC-731 Stream SDK: `getId()` returns invalid ID
* AC-727 Cast player: add implementation for `canonicalLogout`
* AC-726 The AAM inject-system-signature exited with an error when injecting system signature from an APK comes with none default RSA and SF files
* AC-724 LXD cluster looses its `ams0` storage pool when node failed to get added to the cluster
* AC-719 Anbox session aborted due to stack smashing detected
* AC-715 [Doc] Fix "Deploy on bare metal"
* AC-712 Android crash in Mesa on not allowed `sched_getaffinity` syscall
* AC-710 node-controller: add health check for LXD event listener
* AC-709 AMS charm attempts to use the service before it is ready which fails HA deployment
* AC-707 gateway-multiple-clients deploys charm from charm store rather than the local one
* AC-706 AMS becomes stuck and doesn't process objects after leadership handover
* AC-703 Node remains marked as online even if it is removed from the LXD cluster
* AC-698 Android prints `glUtilsParamSize: unknow param 0x0000826d` when running `deqp` tests
* AC-697 Application versions are not correctly handled when two versions share the same image
* AC-696 NewPipe fails to load some videos
* AC-695 Audio recording app cannot playback m4a recordings
* AC-694 BombSquad has artefacts at start because of invalid gyro
* AC-692 Image alias of app version sharing image with another version is not removed
* AC-690 Plex fails to reach server
* AC-688 NewPipe fails to load any video
* AC-686 Weather app fails to connect to the internet
* AC-685 Recorder app crashes when saving the recording
* AC-683 Streaming restart is delayed unnecessarily by a second
* AC-682 Container shuts down when peer connection switches into failed state
* AC-681 Can't stream video from NewPipe application
* AC-680 Android log is spammed with `glUtilsParamSize unknown param` warning when running Firefox
* AC-673 Android reports "Native format mismatch" error when running with Mesa and `swrast`
* AC-670 Android crashes with dangling file descriptor in Mesa
* AC-664 Application watchdog was triggered in some cases when enabling the virtual keyboard
* AC-656 Deleting an instance fails with FormatException
* AC-655 Resuming instances fails with "instance is still active"
* AC-653 spread/multiple-gateway-clients broken when using `ua_source`
* AC-652 Remove deprecated `enable_dev_ui` option
* AC-651 Anbox crashes in `IOStream::read`
* AC-637 AMS Cannot Use AAR And Push Application To S3 : `EntityTooLarge`
* AC-621 Anbox shutdown hangs in `anbox::webrtc::metrics::TelegrafBackend::~TelegrafBackend`
* AC-620 Anbox session does not generate crashdump on crash
* AC-600 Anbox leaks memory on NVIDIA GPUs
* AC-586 Android 10 fails to boot up
* AC-579 BPF support is enabled but should not
* AC-577 Android 12 aborts in SurfaceFlinger with direct rendering on AMD GPUs
* AC-574 Only restart Coturn when necessary
* AC-567 Node controller leaves old iptables rules
* AC-565 camera-support:`swrast` test case fails with serious error
* AC-559 SurfaceFlinger fails to start at times
* AC-558 Anbox crashes in `glBindFramebuffer` or `swrast`
* AC-540 Race in the gateway signaller
* AC-490 Fix documentation on scaling down
* AC-473 Addons are not listed in the output of `amc application ls` for the bootstrapping application
* AC-405 Collector logs many "Previous status (…) for container .. differs from cache" errors
* AC-396 `amc benchmark` removes containers it hasn't created

[/Details]

[Details=1.11.5]

## 1.11.5 (February 15 2022)

#### New features & improvements

None.

#### Bugs

* AC-662 Android containers fail to start on Linux 5.13.x

[/Details]

[Details=1.12.5]

## 1.12.5 (January 28 2022)

#### New features & improvements

None.

#### Bugs

* AC-676 Launching containers on a specific node fails with "node not found"
* AC-671 Application that was signed with a custom system image can't access hidden APIs
* AC-667 Multi touch is not working when streaming from WebRTC platform
* AC-663 Latest Firefox doesn't render in 1.12.x
* AC-662 Android containers fail to start on Linux 5.13.x

[/Details]

[Details=1.12.4]

## 1.12.4 (January 21 2022)

#### New features & improvements

None.

#### Bugs

* AC-657 Traefik listens on port 8080 for incoming API requests

[/Details]


[Details=1.12.3]

## 1.12.3 (January 20 2022)

### New features & improvements

 * Android security updates for January 2022 (see [Android Security Bulletin - January 2022](https://source.android.com/security/bulletin/2022-01-01) for more information)
 * Android WebView has been updated to [97.0.4692.87](https://chromereleases.googleblog.com/2022/01/stable-channel-update-for-desktop.html)

### Bugs

* AC-649 Don't return an error if `JoinSession` is called without a body
* AC-648 Dashboard ends up with no certificates
* AC-644 LP#1955986 Application version got stuck to "initialising" when changing an application attribute via `amc application set`
* AC-627 GPU ends up with zero slots when added after initial node creation
* AC-625 `nvidia_drm` kernel module isn't loaded after appliance upgrade
* AC-277 LP #1922889: The `system.log` and `android.log` are missing and not collected by AMS when the container ran into an error
* AC-621 Anbox shutdown hangs in `anbox::webrtc::metrics::TelegrafBackend::~TelegrafBackend`
* AC-559 SurfaceFlinger fails to start at times

[/Details]

[Details=1.12.2]

## 1.12.2 (December 16 2021)

### New features & improvements

 * Anbox container termination time was shortened by improving internal timeouts
 * Explicit CUDA context selection on NVIDIA GPUs avoids cross-GPU usage of a single container
 * Android security updates for December 2021 (see [Android Security Bulletin - December 2021](https://source.android.com/security/bulletin/2021-12-01) for more information)
 * Android WebView has been updated to [96.0.4664.45](https://chromereleases.googleblog.com/2021/11/stable-channel-update-for-desktop.html)

### Bugs

* AC-313 Dashboard: self signed certificate cause web browser to print a warning
* AC-402 Accessing the appliance via the public AWS IP address rather than DNS name breaks streaming
* AC-408 Improve appliance upgrade message
* AC-496 Coturn charm doesn't detect changed public address after machine stop / start on AWS
* AC-578 Settings app crashes when clicking on "Connected Devices"
* AC-580 Android 12: Unhandled netlink message warnings in system log

[/Details]

[Details=1.12.1]

## 1.12.1 (November 30 2021)

### New features & improvements

 * Improved graphics stability on Arm64 machines with NVIDIA GPUs

### Known issues

* The Android 12 image currently comes without a functioning WebView. The WebView will become functional with the 1.12.2 release.

### Bugs

* AC-472 A native crash occurred to `webview.apk` after upgrading it to 94.0.4606.80
* AC-505 WebRTC platform crashes in `rtc::SocketDispatcher`
* AC-503 CUDA resources are not correctly freed
* AC-508 Units in stats overlay are incorrect
* AC-545 Find patch in Mesa which fixes the crash
* AC-553 no Audio output after rejoining a session
* AC-555 Telegraf fails to run iptables commands

[/Details]

[Details=1.12.0]

## 1.12.0 (November 16 2021)

### New features & improvements

* Android 12 images
* Improved density for NVIDIA GPUs
* Improved WiFi support
* Rebooting Android is now possible
* Additional life-cycle hooks
* Port ranges support in AMS
* Container tags
* Android security updates for November 2021 (see [Android Security Bulletin - November 2021](https://source.android.com/security/bulletin/2021-11-01) for more information)

### Known issues

* The Android 12 image currently comes without a functioning WebView. The WebView will become functional with the 1.12.1 release.

### Bug fixes

* AC-467 AMS fails to import image with multiple instances
* AC-174 LP #1927233 `anbox-stream-gateway-lb` has no open ports when deployed via Juju 2.9
* AC-293 Anbox leaks after `CtsGraphicsTestCases` has finished
* AC-294 WebRTC platform crashes on `glDeleteTextures`
* AC-446 Container fails to start: This operation can't be cancelled
* AC-453 Dashboard charm fails to deploy
* AC-466 `amc application set` fails with `argument cpu is invalid`
* AC-501 A kernel crash occurred in `virt_wifi` kernel module
* AC-502 Grafana fails in dashboard-relation-joined
* AC-504 LXD nodes fail to be added if relation hook is run before AMS is configured
* LP #1922918 LXD charm crashes with TypeError in `count_lxd_nodes_in_cluster`
* LP #1926118 Using invalid UA token causes hook error instead of proper error

[/Details]

[Details=1.11.4]

## 1.11.4 (November 1 2021)

### New features & improvements

None.

### Bugs

A bug in the Anbox runtime caused random WebView-based applications to crash when upgrading the `WebView.apk` to [94.0.4606.80](https://chromereleases.googleblog.com/2021/10/chrome-for-android-update.html). For this reason, we downgraded the WebView version to [93.0.4577.82](https://chromereleases.googleblog.com/2021/09/chrome-for-android-update.html) for stability, and we are planning to provide a fix in the Anbox Cloud 1.12 release.

[/Details]

[Details=1.11.3]

## 1.11.3 (October 18 2021)

### New features & improvements

 * Android security updates for October 2021 (see [Android Security Bulletin - October 2021](https://source.android.com/security/bulletin/2021-10-01) for more information)
 * Android WebView has been updated to [94.0.4606.80](https://chromereleases.googleblog.com/2021/10/chrome-for-android-update.html)
 * The shared memory transport used for the `null` platform is now disabled by default for increased stability
 * ANGLE libraries used for `null` platform are updated to increase stability and cause Anbox to not crash in certain situations

### Bugs

 * AC-321 Deploying multiple AMS units at the same time causes problems
 * AC-343 ANDROID_EMU_* extensions are visible for Android applications
 * AC-384 Fix steam view in the dashboard

[/Details]

[Details=1.11.2]

## 1.11.2 (September 20 2021)

### New features & improvements

 * Android security updates for September 2021 (see [Android Security Bulletin - September 2021](https://source.android.com/security/bulletin/2021-09-01) for more information)
 * Android WebView has been updated to [93.0.4577.82](https://chromereleases.googleblog.com/2021/09/chrome-for-android-update.html)
 * The AMS node controller now synchronises its internal state to disk more often to avoid getting out of sync with the actual running containers across restarts
 * Client-side virtual keyboard is now supported on Android 11
 * The default instance type of an application in the dashboard is now selected based on the available GPU support

#### Bugs

 * LP #1938761 Anbox WebView lost focus for unknown reasons and causes client side virtual keyboard hidden in the end
 * LP #1940807 Failed to launch Anbox sessions with WebRTC platform (`drm` backend)
 * LP #1940853 `anbox-cloud-dashboard-51` charm fails to deploy
 * LP #1942677 Audio/Video recording is broken on Anbox `swrast` platform
 * AC-304 Dashboard reports "Could not get response from Anbox Stream Gateway"
 * AC-303 Dashboard lists non active images in application form
 * AC-342 Connecting second ADB server breaks existing one

[/Details]

[Details=1.11.1]

## 1.11.1 (August 17 2021)

### New features & improvements

 * Android security updates for August 2021 (see [Android Security Bulletin - August 2021](https://source.android.com/security/bulletin/2021-08-01) for more information)

### Bugs

* LP #1939277 `lxc-attach` fails on sendfile with EINVAL on 5.11
* LP #1938877 Native crash occurred when creating an application from Android 11 after finishing application bootstrap
* LP #1939274 Anbox crashes after "Failed to put memory protection in place"
* LP #1939666 Bootstrap fails because of missing `/dev/fd0`
* LP #1939129 The `anbox-stream-sdk.js` file is missing from Android WebView based projects
* LP #1938901 Appliance upgrade fails with Juju 2.9.x

[/Details]

[Details=1.11.0]

## 1.11.0 (August 5 2021)

### New features & improvements

* Client side virtual keyboard
* Hardware accelerated video decoding (H.264, NVIDIA GPUs only)
* Experimental WiFi support
* Automatic application updates can now be disabled in AMS
* Old image versions can now be imported in AMS
* Feature flags can now be encoded in the AMS application manifest
* AMS now uses a larger /20 network subnet for Anbox containers to allow more than 255 containers per host

### Bug fixes

* LP #1926148 Anbox Session crashed when running with null platform (Angle EGL/GL drivers))
* LP #1927313 Fail to launch more than 44 containers on two NVIDIA GPUs
* LP #1936345 Appliance fails to bootstrap when NIC is on a /22 network
* LP #1936799 text should be instantly shown up in the input edit widget when it's sent from the client side virtual keyboard
* LP #1936835 Audio processing is enabled in WebRTC
* LP #1936934 Ensure Ubuntu user is allowed to talk to LXD
* LP #1937005 AMS crashed when updating an image with the same fingerprint
* LP #1938118 A refresh container that was launched from an application contains `tombstone_00` file
* LP #1938288 Outbound audio stream remains after microphone is disabled
* LP #1938533 Appliance bootstrap fails too late when LXD is not setup by us
* LP #1938701 Trailing slash is causing problems
* LP #1913597 AMS enable people to remove last version of an addon
* LP #1926702 Image architecture is not taken from simplestreams in AMS
* LP #1930935 Anbox cloud dashboard fails at install hook
* LP #1933489 Camera is not connected after rejoin
* LP #1935809 Appliance `init` command can be run again while the appliance is initialising
* LP #1936171 Missing `ISoundTriggerHw` in Android 11 images
* LP #1936801 Support to run hooks after Anbox session is fully up and running
* LP #1937266 Web socket connect to gateway fails with "Invalid UTF-8 sequence in header value" on iOS
* LP #1913425 Provide an informative message when removing a certificate by running `amc config trust remove`
* LP #1913560 Image version deletion only supports to perform the operation with image id
* LP #1919136 [AMS] `hasImageWithIDOrName` uses app cache

[/Details]

[Details=1.10.3]

## 1.10.3 (Jul 14 2021)

### New features & improvements

 * Android security updates for July 2021 (see [here](https://source.android.com/security/bulletin/2021-07-01) for more information)
 * WebView based on [upstream 91.0.4472.134 release](https://chromereleases.googleblog.com/2021/06/chrome-for-android-update_0579445428.html)

### Bug fixes

 * LP #1933195 Sensor device doesn't handle sync and guest_sync commands
 * LP #1932362 [appliance] public address of the LXD node in AMS is not set
 * LP #1934877 A wrong main activity was used for some APKs

[/Details]

[Details=1.10.2]

## 1.10.2 (June 13 2021)

### New features & improvements

 * Android security updates for June 2021 (see [here](https://source.android.com/security/bulletin/2021-06-01) for more information)
 * WebView based on [upstream 90.0.4430.91 release](https://chromereleases.googleblog.com/2021/06/chrome-for-android-update.html)
 * Android System UI can now be enabled for applications via a new feature flag `enable_system_ui`

### Bug fixes

 * LP #1924715 System gets blocked by `sensorservice` not responding
 * LP #1926397 Appliance bootstrap log is missing output of various commands
 * LP #1926694 Metrics reported by AMS are incorrect
 * LP #1929031 Failed bootstrap doesn't terminate container
 * LP #1930079 camera service crashed from time to time when executing spread tests in our Jenkins
 * LP #1930282 Enable `vertical_accuracy` and `horizontal_accuracy` configurable for GPS data
 * LP #1931202 Gateway fails to join just created session
 * LP #1928719 Tombstone is detected twice
 * LP #1929005 Gallery2 application crashed when editing an picture
 * LP #1929151 Appliance storage size is wrong and doesn't reflect the value of snap configuration `storage.size`
 * LP #1928703 Silence spammy `eglMakeCurrent` debug message

[/Details]

[Details=1.10.1]

## 1.10.1 (May 13 2021)

### New features & improvements

 * Properly shut down containers when they are still writing to a ZFS data set.
 * Android security updates for May 2021 (see [here](https://source.android.com/security/bulletin/2021-05-01) for more information)

### Bug fixes

* LP #1926695 Task reaper fails to deleted container because of "target is busy"
* LP #1927234 `sysctl` settings for new LXD nodes are not applied
* LP #1927910 Public status endpoint of the appliance returns internal endpoints without authentication
* LP #1927342 `wifi-service.odex` is marked as imported but is not found for Android 11

[/Details]

[Details=1.9.5]

## 1.9.5(May 11 2021)

### New features & improvements

No features were added in this release.

### Bug fixes

* LP #1927676 No image is imported in AMS when deploying 1.9.x based Anbox Cloud

With Anbox Cloud 1.10 packages are now version specific which allows users to deploy older versions of Anbox Cloud while a newer version is available. Due to a bug in AMS 1.9.x no images were imported as the 1.10 ones were always seen as newer (when `images.version_lockstep` is set to `true`) and older 1.9.x images were not considered. With 1.9.5 AMS will now correctly download the latest 1.9.x image and ignore any newer one.

Existing deployments based on 1.9.x are not affected by this bug.

[/Details]

[Details=1.10.0]

## 1.10.0 (May 6 2021)

### New features & improvements

* Android 11 was released back in 2020 by Google and is now available and fully supported in Anbox Cloud. With Android 11 various [new features](https://developer.android.com/about/versions/11/features) become available for developers and applications. From an Anbox perspective Android 11 provides the same feature set as for the existing Android 10 images and will be provided with monthly security updates starting with 1.10.1
* In earlier Anbox Cloud versions the Juju charms and bundles for Anbox Cloud where only available after allow-listing user accounts for access. With 1.10 all charms and bundles are not available in the public on the Juju Charmstore.
* Before 1.10 a deployment might have been automatically updated through a system package update to the next major or minor version of Anbox Cloud. With 1.10 this is no longer possible and upgrading to a new minor version of Anbox Cloud requires an explicit update to a newer charm as specified in [component versions](https://anbox-cloud.io/docs/component-versions).
* Up until 1.10 streaming sessions managed by the Anbox Stream Gateway could be joined but new clients had to wait before an existing client disconnected to establish a connection. With 1.10 the Anbox Stream Gateway has gotten a new API which allows to force disconnect any currently connected client from an active session.
* With 1.10 Anbox Cloud now by default uses the [server optimised NVIDIA GPU drivers](https://launchpad.net/ubuntu/+source/nvidia-graphics-drivers-460-server) as packaged in the Ubuntu archive by default on amd64 systems. On arm64 systems the NVIDIA drivers are still coming from the NVIDIA provided [CUDA archive](https://developer.nvidia.com/cuda-downloads).
* Applications can now be managed from the Anbox Cloud Dashboard. The feature was already available in 1.9 but disabled by default due to a few limitations. As part of 1.10 this is now fully available by default and allows the creation, modification and deletion of applications via simple web based user interface.
* If a container has multiple service endpoints defined, allocation of node ports is now quicker. For containers with a high number of service endpoints (100+) the startup time was delayed by more than 70 seconds and is now down to a couple of seconds at maximum.
* A `juju crashdump` now collects additional debug information from LXD and AMS about available containers, addons, applications and cluster configuration
* The LLVMpipe software renderer used by Anbox as part of the `swrast` and `webrtc` platforms is now limited in the number of threads it creates for rendering to the number of vCPUs which are assigned to the container. This helps to improve its efficiency and adjusts performance to match the assigned vCPUs.
* WebView based on [upstream 90.0.4430.91 release](https://chromereleases.googleblog.com/2021/04/chrome-for-android-update_27.html)

### Known issues

* With 1.10.0 Juju 2.9 is not yet fully supported. It is recommended to stick to Juju 2.8 until explicit support for Juju 2.9 is added and called out in the release notes.

### Bug fixes

* LP #1883526 NATs reconnects quite often on a LXD deployment
* LP #1912172 WebRTC platform hangs forever on peer connection release
* LP #1885708 AMS fails to start on deploy
* LP #1920999 IP addresses of LXD containers used by the appliance change after a reboot
* LP #1921835 On systems with multiple NVIDIA GPUs Anbox fails to start with WebRTC platform
* LP #1922208 `juju config lxd images_compression_algorithm` does not work
* LP #1923204 Handle Juju timeout error
* LP #1923300 Shader compilation error in Android 11 because of missing GL_OES_EGL_image_external in `swrast`/`webrtc`
* LP #1924234 Failed to trigger action even if the proper actions were given
* LP #1924891 Appliance CF template misses AWS regions
* LP #1925121 The incompatible CUDA libraries were installed when deploying Anbox Cloud on a NVIDIA GPU supported environment
* LP #1926113 AMS is still leaking FDS when constantly scaling LXD cluster
* LP #1926696 Currently synchronised images never show up in `amc image ls`
* LP #1905747 Check for Debian package before attempting to remove it
* LP #1915139 Grafana dashboard doesn't provide Regions selector
* LP #1915297 Dashboard fails to install on fresh 1.9.0 deployment
* LP #1920930 Appliance status page is missing favicon
* LP #1923205 Appliance status page shows incorrect year 2020
* LP #1924931 Android 11: `android.app.cts.SystemFeaturesTest#testCameraFeatures` fails
* LP #1885112 Anbox reports incorrect path for ANR and tombstones
* LP #1904414 Stream gateway fails to stop if gateway wasn't installed
* LP #1914433 images.version_lockstep value is printed as a string instead of a Boolean in `amc config show`
* LP #1915803 `amc ls --format=json` returns `null` on an empty list, would have expected `[]`

[/Details]

[Details=1.9.4]

## 1.9.4 (May 3 2021)

### New features & improvements

The 1.9.4 release adapts the AMS service to work with LXD newer than 4.0.5. LXD recently changed
which certificate is being used on the API endpoint when running clustered. With newer LXD versions AMS fails to setup the initial LXD node within a cluster. For subsequently added nodes the problem does not exist. With the 1.9.4 release AMS now correctly uses the new certificate used by LXD and allows the initial LXD cluster bootstrap to succeed.

### Bug fixes

No bugs were fixed in this release.

[/Details]

[Details=1.9.3]

## 1.9.3 (April 13 2021)

### New features & improvements

* The LXD charm can now take a LXD-binary resource which allows attaching and detaching custom build LXD binaries
* `amc delete` has now a `--force` flag which allows deleting container without gracefully stopping them
* The number of internal workers in AMS responsible to delete and stop containers in parallel is now increased to 10
* The Android `rild` service is now disabled but default as it was never intended to be active
* WebView based on [upstream 89.0.4389.105 release](https://chromereleases.googleblog.com/2021/03/chrome-for-android-update_22.html)
* Android security updates for April 2021 (see [here](https://source.android.com/security/bulletin/2021-04-01) for more details)

### Bug fixes

* LP #1917768 A crash occurred in the glib main loop thread during the streaming
* LP #1918601 Metrics reported by AMS are out-of-sync
* LP #1919443 LXD charm fails to stop when unit has active containers
* LP #1920129 Allow mounts to be injected into Android container at runtime
* LP #1920207 `ImagesSuite.TestDoesntUpdateWhenNoNewVersion` fails at times
* [ ] LP #1921060 Application can't access its isolated folder under SD card even after it's granted `android.permission.WRITE_EXTERNAL_STORAGE` and `android.permission.READ_EXTERNAL_STORAGE` permissions
* LP #1921372 Anbox hangs on shutdown after crash
* LP #1922198 Gateway patch application is racy in 1.9.x
* LP #1922343 Native crash happened at time in WebRTC platform when restarting a session
* LP #1922655 Configured GPU slots are overridden
* LP #1922722 Backup hook doesn't get executed properly when a container ran into an error
* LP #1923411 None active sensors shown up after Android fully get started
* LP #1923414 WebRTC session gets restarted in a busy loop even after a session has gone
* LP #1923623 AMS end up with embedded etcd when deployed in HA
* LP #1875542 The spread test `aam-backup-restore:exclude_files` is flaky sometimes
* LP #1899948 Stream gateway: DB patches can run into race conditions
* LP #1912757 Anbox Streaming Stack dashboard does not show "Agents" pane
* LP #1920120 AMS charm should not try to manage the cluster when related to `lxd-integrator`
* LP #1922311 Anbox HTTP API server accepts empty sensor data
* LP #1922313 `rild` service auto-started when Android system fully boot-up
* LP #1916047 Daemon subcommand of the appliance is not hidden

[/Details]

[Details=1.9.2]

## 1.9.2 (March 17 2021)

### New features & improvements

* Stability and reliability improvements in AMS and the Juju charms for auto scaling of the LXD cluster. See the [documentation](https://anbox-cloud.io/docs/lxd-auto-scaling) for recommendations and guidelines on how to implement auto scaling.

### Bug fixes

* LP #1910676 AMS leaks FDS
* LP #1917862 AMS charm tries to add/remove node when AMS service is not available
* LP #1917867 LXD charm doesn't respect configured channel
* LP #1917869 AMS fails to get started due to error `tls: private key does not match public key` when multiple AMS units are deployed
* LP #1918089 Failed to remove LXD node from cluster
* LP #1918431 Container logs are missing in a HA AMS
* LP #1918675 Image synchronisation is not triggered in AMS when relevant configuration items change
* LP #1918676 Image server configuration can be stale in HA AMS

[/Details]

[Details=1.9.1]

## 1.9.1 (March 2021)

### New features & improvements

* The Coturn charm is now able to figure out the public address of a manually added
  machine in a Juju model when deployed on AWS
* The Coturn charm does now allow customising the UDP relay port range
* The AMS charm now has a `storage_pool` configuration option allowing AMS to configure
  LXD to use an existing storage pool
* WebView based on [upstream 88.0.4324.181 release](https://chromereleases.googleblog.com/2021/02/chrome-for-android-update_16.html)
* Android security updates for March 2021 (see [here](https://source.android.com/security/bulletin/2021-03-01) for more details)

### Bug fixes

* LP #1917578 Dashboards crashes in CI when ran on AWS because it can't reach metadata service
* LP #1913565 Exposing services on private endpoint makes them not accessible
* LP #1915183 [RFE] Support Manual Provider on top of AWS
* LP #1915244 Dashboard should not listen on 0.0.0.0
* LP #1915258 Camera support does not work in dashboard
* LP #1915461 Dashboard missed an APT update before upgrading
* LP #1915564 Container launch is not aborted when no free port is found
* LP #1915691 Gateway fails to update session status to error due to timeout
* LP #1915720 Anbox does not fallback to software encoder when all GPU encoder slots are used
* LP #1915812 Dashboard charm fails to deploy with AttributeError
* LP #1916006 Session cannot be connected again after gateway is restarted
* LP #1916474 The 1.9 benchmark fails to collect any metrics
* LP #1916535 Unable to locate package `cuda-libraries-11-0`
* LP #1916894 Multiple AMS instances race around cluster cert generation
* LP #1917281 A wrong camera(front) is used by WebRTC platform when a camera-based application is open up
* LP #1917296 Touch doesn't work on safari when streaming on iOS
* LP #1917434 Native Stream SDK crashes when stopped
* LP #1917526 Native SDK crashes when signalling server uses DNS name instead of IP address
* LP #1915245 UA layer doesn't print the "Missing UA Token" when deploying Anbox Cloud
* LP #1915600 AMS configuration is not updated when port range is changed
* LP #1917053 `linux-modules-extra` package should be installed as the dependency of `anbox-module-dkms` when bootstrap LXD charm
* LP #1917286 no audio output for streaming on iOS and Mac OS

[/Details]

[Details=1.9.0]

## 1.9.0 (February 2021)

### Deprecations

* The Android 7 (`bionic:android7:arm64` and `bionic:android7:amd64`) images are now deprecated and will no longer be available starting with Anbox Cloud 1.10 which will be released in April 2021
* The UI included in the Anbox Stream Gateway service will be dropped in Anbox Cloud 1.10 as it's being replaced with the new dashboard

### Known issues

* At times the `anbox-cloud-dashboard` charm reports a `error` as workload status due to too many units trying to use `apt` on the machine at the same time. Juju will retry the installation after some time automatically and the problem will fix itself. The issue can be identified in the output of `juju debug-log --include anbox-cloud-dashboard`. This will be improved in the upcoming 1.9.1 release
* If for the initial deployment not Ubuntu Advantage token is configured via an `overlay.yaml` the status messages reported by the charms once they become idle is not set to `UA token missing`. There is no impact in terms of functionality. Applying the UA token via `juju config <application> ua_token=<token>` will work as usual.

### New features & improvements

* New web based dashboard to manage applications and streaming sessions in Anbox Cloud
* WebView based on [upstream 88.0.4324.152 release](https://chromereleases.googleblog.com/2021/02/chrome-for-android-update_4.html)
* Android security updates for February 2021 (see [here](https://source.android.com/security/bulletin/2021-02-01) for more details)
* Out of band data allowing to send custom data from applications running inside the Android container to the client connected over WebRTC
* Support for streaming the clients camera to the Android container over WebRTC
* Hardware video encoding support for NVIDIA on Arm
* Support in AMS for existing LXD clusters
* New recursive=<bool> parameter to GET /sessions on the Stream Gateway to return the full session objects rather than just their ID
* Streaming sessions can now be deleted in batch and asynchronously
* Introduce the container.features configuration item in AMS to enable specified features in Android container
* Bump key size to 4096 to work with 20.04 stronger security defaults
* Anbox now uses Vulkan as a backend renderer API on NVIDIA GPUs on both x86 and Arm. This improves performance, stability and compatibility.
* Improved density on NVIDIA Tesla T4 cards. With Anbox Cloud < 1.9.0 the maximum of containers possible was around 10-12 due to bugs in the GPU firmware when using the OpenGL ES client API. With the switch to Vulkan the firmware bugs are no longer triggered and up to a maximum of 32 simultaneous containers are possible (subject to their actual use of the GPU)
* Updated NVIDIA GPU driver to the 460 series for both x86 and Arm
* A default virtual keyboard is now included in the provided Android images and can be conditionally enabled
* A launch activity can now be specified when new sessions are created or existing joined. This allows switching to specific activities within the application.
* Stripped down unnecessary dependencies to speed up deployment time
* Session objects in the gateway now contain information about failed container
* The AMS charm now sets up access to the Anbox Cloud image server via the Ubuntu Advantage subscription the machine is attached to. It’s no longer necessary to supply individual user+password authentication details
* Added API measurements to metrics
* Various fields of an application can now be updated via the AMS HTTP API without providing a new APK file
* The Anbox Stream Gateway has now support for HTTP rate limit which can be configured via a charm configuration option
* AMS can be configured to use pre-existing storage pools and networks
* AMS now exposes the `scheduler.strategy` configuration item to allow choosing between `binpack` and `spread` strategies
* AMS now exposes two configuration items `node.queue_size` and `node.workers_per_queue` to allow fine tuning how AMS processes container launch requests for optimal throughput
* The Google STUN server is no longer used
* Streaming sessions are now ephemeral by default and will be automatically removed when the container it belongs to terminates

### Bug fixes

 * LP #1868945 Android: failed to get memory consumption info
 * LP #1873393 Close of unknown file descriptor in `gralloc` modules causes crash
 * LP #1892693 Provide better error message when web socket connect to gateway fails
 * LP #1897300 Rare ICE errors on iOS Safari when streaming
 * LP #1901035 NVIDIA GPUs cannot host more than 12-13 Anbox containers
 * LP #1903518 Inconsistent Session object returned by the Gateway API
 * LP #1903991 Coturn reports Unauthorised for users when stream was already established
 * LP #1905734 WebRTC streaming fails in Firefox
 * LP #1908240 AMS timing issue when fetching an image before assigning it an alias
 * LP #1908404 Images are not synchronised from `images.anbox-cloud.io`
 * LP #1910203 Dashboard charm crashes with KeyError on certificates relation
 * LP #1911202 Container delete fails with ZFS busy error
 * LP #1912113 WebRTC platform aborts with unhandled exception
 * LP #1912143 Port 3000 will not get opened after exposing `aar` (AMS registry)
 * LP #1912146 when NRPE relation is added to AAR, 'Check AAR HTTPS endpoint' will always fail with 401 Unauthorised
 * LP #1912267 WebRTC platform crashes in `eglReleaseThread` in `libEGL_mesa.so.0` on termination
 * LP #1912302 Container doesn't not terminate correctly
 * LP #1912470 The latest WebRTC platform is broken on NVIDIA based GPU machine
 * LP #1912521 Dashboard charm does not set application version
 * LP #1912588 `anbox-cloud-tests` for gateway, sometime fails to launch container
 * LP #1912732 Anbox cloud dashboard does not show all of the panes correctly
 * LP #1912784 Dashboard register URL is still on `http://`
 * LP #1912785 AMC failed to create container with error, however in LXD it was successfully created
 * LP #1912787 Status message of a session with status error is empty when container crashed
 * LP #1912932 CTS tests claims `EGL_KHR_image` extension is missing
 * LP #1912956 Native SDK example crashes when trying to lock destroyed mutex
 * LP #1913017 SEGV when terminating the streaming on Android client built against native SDK
 * LP #1913020 FORTIFY: `pthread_mutex_lock` called on a destroyed mutex on AudioTrack thread
 * LP #1913058 `gpu-support.sh` script unloads kernel drivers when current driver is already the correct one
 * LP #1913264 Anbox Cloud Dashboard stuck on "waiting for UA" even with UA source configured
 * LP #1913305 Charm stays in blocked when UA attach failed
 * LP #1913364 Meaningless/Invalid resource is listed in the response when deleting an addon version
 * LP #1913391 Coturn uses location as external address when external_address_from_location is set to false
 * LP #1913403 AMS crashed when exporting an application version
 * LP #1913436 Update the command description of `amc config set`
 * LP #1913457 LXD container cgroup metrics are not reported via subordinate Telegraf charm
 * LP #1913462 On ARM64 systems not loaded `nvidia_uvm` kernel module crashes containers
 * LP #1913524 AMS crashed when executing a command within a container by posting a body
 * LP #1913528 The timestamp of event shows `0001-01-01T00:00:00Z`
 * LP #1914008 Juju fails to attach storage to LXD unit
 * LP #1914036 Dashboard sets 5min idle timeout
 * LP #1914188 Opened port is closed when port hasn't changed for gateway
 * LP #1914276 JS SDK reports "Unknown message type error" at times in Firefox
 * LP #1914435 Anbox Stream JS SDK always get `rear` facing mode no matter people switch the camera face mode to "front" or "rear"
 * LP #1914448 Dashboard register command gives private IP instead of public one
 * LP #1914811 NVIDIA kernel modules are not loaded after deployment
 * LP #1914991 Latest gateway API changes break dashboard

[/Details]

[Details=1.8.3]

## 1.8.3 (January 2021)

### New features & improvements

 * Android security fixes from January 2021 (patch level `2021-01-05`, see [here](https://source.android.com/security/bulletin/2021-01-01) for more details)
 * WebView update to upstream release `87.0.4280.141` (see [here](https://chromereleases.googleblog.com/2021/01/chrome-for-android-update.html) for more details)
 * Various improvements to the Coturn charm to allow proper use behind [AWS Elastic Load Balancers](https://aws.amazon.com/elasticloadbalancing/)

### Bug fixes

 * LP #1910583 `anbox-stream-gateway` gets stuck and demands restart after some time of use
 * LP #1912342 Gateway reports database locked errors for various operations

[/Details]

[Details=1.8.2]

## 1.8.2 (December 2020)

### New features & improvements

 * Android security fixes from December 2020 (patch level `2020-12-05`, see [here](https://source.android.com/security/bulletin/2020-12-01) for more details)
 * WebView update to upstream release ` 87.0.4280.86` (see [here](https://chromereleases.googleblog.com/2020/12/chrome-for-android-update.html) for more details)

### Bug fixes

* LP #1907464 NvEnc fails to encode when stream is in portrait mode (720x1280)
* LP #1904078 Garbled image/video generated when taking a picture/recording a video when screen orientation is in portrait mode
* LP #1904417 [REGRESSION] ADB screen record output has incorrect orientation

[/Details]

[Details=1.8.1]

## 1.8.1 (November 2020)

### New features & improvements

 * Android security fixes from November 2020 (patch level `2020-11-05`, see [here](https://source.android.com/security/bulletin/2020-11-01) for more details)
 * WebView update to upstream release ` 86.0.4240.185` (see [here](https://chromereleases.googleblog.com/2020/11/chrome-for-android-update.html) for more details)
* AMS now allows locking image updates to it's own minor version. For example if AMS is at 1.8 it wont pull a 1.9 image but only patch releases for 1.8. This can be configured with the `images.version_lockstep` configuration option

### Bug fixes

*  LP #1903510 `nagios_context` and `nagios_servicegroups` are never used in any charm
*  LP #1885926 One touch point always stays when another touch event was fired
*  LP #1902282 Idle timer in the WebRTC platform is not reinitialised after the first client disconnected
*  LP #1902494 A malformed UA source blocked the Anbox Cloud deployment on AWS
*  LP #1902665 The latest `anbox-stream-sdk.js` broke the keyboard/mouse/touch input events to be propagated to the container
*  LP #1902693 `inhibit-auto-updates` setting never worked
*  LP #1902996 Time doesn't get refreshed in the status bar but the it does in the System settings
*  LP #1903492 charm-upgrade hook implementation is missing apt update call
*  LP #1903525 Invalid service directory permissions for the stream gateway
*  LP #1903559 Gateway service is restarted when new units are added
*  LP #1903676 Failed to remove LXD charm because zpool command is missing
*  LP #1903747 Host composition is causing flickering in Anbox when streaming with LLVMpipe
*  LP #1903672 Application bootstrap fails due to malformed addon name
*  LP #1902650 The error message needs to be simplified when ABI is unmatched

[/Details]

[Details=1.8.0]

## 1.8.0 (October 2020)

### New features & improvements

* Camera can now be provided with video and static images as content via the Anbox HTTP API
* A new `ANBOX_EXIT_CODE` environment variable is provided to the `backup` hook of addons to provide information if Anbox terminate correctly or not
* [Crashpad](https://chromium.googlesource.com/crashpad/crashpad/) is now used for crash dump reporting in Anbox
* Sensors exposed to Android can now be provided with data via the Anbox HTTP API
* Prometheus endpoint of the Anbox Stream Gateway now supports TLS and HTTP basic authentication
* AMS now supports multiple architectures in the connected LXD cluster
* NVIDIA GPU support for ARM (rendering only, encode will come with 1.9)
* Upgrade to etcd 3.4
* Anbox Stream SDK now supports native applications (Linux, Android)
* Anbox provides support for [Perfetto](https://perfetto.dev/) based tracing via its HTTP API
* A custom expiration timeout can now be set for service accounts created for the Anbox Stream Gateway
* HA support in the Anbox Stream Gateway was improved and stabilised
* The Coturn charm now support HA
* Applications in AMS can now provide a free-form version field in their manifest to allow users to identify which application version is based on which APK version


### Bug fixes

 * LP #1898180 AMS fails when related to Anbox registry due to missing certificate
 * LP #1901513 Don't join Dqlite cluster if gateway is not able to start
 * LP #1901573 Coturn charm does not remove Debian package and configuration
 * LP #1900704 HA attach fails if other application was already attached on same machine
 * LP #1901185 Manually pulling an application from registry crashes AMS
 * LP #1901511 UA layer fails in HA
 * LP #1884526 Dqlite shouldn't start in cluster if its certs aren't setup
 * LP #1889923 Stream stops when browser window is resized
 * LP #1895009 UA Token is printed when attach failed
 * LP #1896813 Picture recorded via the camera app is corrupted
 * LP #1896953 Make `getevent` Android tool work with Unix sockets in `/dev/input`
 * LP #1897085 Take a picture from the `uber` driver application causes the application crash
 * LP #1897277 Streaming gives a black screen on iOS Safari
 * LP #1898220 A native crash occurs when doing a video recording from camera applications
 * LP #1898698 Video stream is empty after joining existing session
 * LP #1898740 LXD unit fails to stop when storage pool still has containers
 * LP #1899324 Video recording doesn't work out on `swrast` platform
 * LP #1899658 SensorManager thread run into a busy loop
 * LP #1901021 checksum of dump file is different from the original log file pulled out from the LXD container
 * LP #1901194 Anbox Stream Gateway doesn't register dashboard with Grafana
 * LP #1901197 Android streaming example hangs after adding the audio support
 * LP #1901668 Stream SDK should time out if WebRTC connection is not established in time
 * LP #1901744 Anbox hangs at time when container is terminated
 * LP #1884498 Improve error when application has an APK with unsupported ABIs
 * LP #1888383 Supply `extra-properties` upon Anbox session startup broke the Android container startup
 * LP #1892410 Containers hangs after `anbox-system-update` failed
 * LP #1896789 `uiautomator` crashes in `anbox-shell`
 * LP #1897790 Read UA token from include-file://
 * LP #1898697 `anbox-stream-sdk._unregisterControls` is not working correctly
 * LP #1894978 Sanitise prepare hook upon an addon creation

[/Details]

[Details=1.7.4]

## 1.7.4 (October 2020)

### New features & improvements

 * Android security fixes from October 2020 (patch level `2020-10-05`, see [here](https://source.android.com/security/bulletin/2020-10-01) for more details)
 * WebView update to upstream release ` 86.0.4240.75` (see [here](https://chromereleases.googleblog.com/2020/10/chrome-for-android-update.html) for more details)

### Bug fixes

None

[/Details]

[Details=1.7.3]

## 1.7.3 (September 2020)

### New features & improvements

 * Android security fixes from September 2020 (patch level `2020-09-05`, see [here](https://source.android.com/security/bulletin/2020-09-01) for more details)
 * WebView update to upstream release ` 85.0.4183.101` (see [here](https://chromereleases.googleblog.com/2020/09/chrome-for-android-update.html) for more details)

### Bug fixes

None

[/Details]

[Details=1.7.2]

## 1.7.2 (September 2020)

### New features & improvements

* Various improvements for HA support in the Anbox Stream Gateway and its [Dqlite](https://dqlite.io) integration
 * The Anbox Stream Gateway now exposes a `/1.0/status` endpoint to allow simple health checks
 * The number of registered stream agents is now exported via the Prometheus endpoint of the Anbox Stream Gateway
 * The LXD charm can now use Juju storage (AWS EBS, ..) at deployment time as base for the LXD storage pool
 * Coturn can now be manually configured via the Anbox Stream Agent charm configuration

### Bug fixes

 * Various fixes around interoperability of the various charms in an Anbox Cloud deployment
 * Updated and verified NRPE checks for all service components

[/Details]

[Details=1.7.1]

## 1.7.1 (August 2020)

### New features & improvements

* Switched to [LLVMpipe](https://docs.mesa3d.org/gallium/drivers/llvmpipe.html) based software rendering in favour of [swiftshader](https://swiftshader.googlesource.com/SwiftShader/) to mitigate memory corruption during rendering in the [Android WebView](https://developer.android.com/reference/android/webkit/WebView) on both ARM and x86

### Bug fixes

* LP #1892149: `anbox-shell pm install` fails in the prepare hook of an addon when bootstrapping an application
* LP #1889747: Coturn should not run as root
* LP #1891746: Some ARM applications crash because of failing cache flush syscall

[/Details]

[Details=1.7.0]

## 1.7.0 (August 2020)

### New features & improvements

* Anbox Cloud is now fully integrated with [Ubuntu Advantage](https://ubuntu.com/advantage)
* TLS certificates are now managed through a common CA for all components ([Easy-RSA](https://charmhub.io/containers-easyrsa))
* GPS position updates can now be provided via a new  HTTP API endpoint Anbox exposes within
  the container or via the streaming SDK
* Removed [KSM](https://www.kernel.org/doc/html/latest/admin-guide/mm/ksm.html) support
* Allow streams started via the stream gateway UI to use 1080p as display resolution
* Deprecated the Anbox Cloud Doctor in favour of [Juju crashdump](https://github.com/juju/juju-crashdump)

### Bug fixes

* LP #1890573: Always delete the base container even when an application failed to be bootstrapped
* LP #1847226 Fixed a bug that prevented the Dev UI to be run in fullscreen in some cases
* LP #1890573: Stop the signalling session when a container no longer exists to avoid hanging the client for too long
* LP #1886200: Fixed issues that appeared when displaying web pages on a software rendering backend
(`swrast` and `webrtc` without GPU) after upgrading the system WebView to 84.0.4147.89.
* Reduced resource consumption of the WebRTC platform by avoiding unnecessary screen refresh cycles
* Fixed timing issue which resulted in locked databases in some cases on the Stream Gateway

[/Details]

[Details=1.6.3]

## 1.6.3 (July 2020)

### Bug fixes

* LP #1885726: Fix the mouse and touch displacement issue for Anbox Stream Gateway UI

[/Details]

[Details=1.6.1]

## 1.6.1 (June 2020)

### Bug fixes

* LP #1885257: Fix high CPU usage for Anbox daemon
* LP #1885972: Fix watchdog, services and video encoder settings out of sync when updating an application

[/Details]

[Details=1.6.2]

## 1.6.2 (June 2020)

### New features & improvements

* Applications without an APK can now specify a boot activity in their application manifest

### Bug fixes

* LP #1885107: Automatic application updates were missing configured resources, watchdog
  or service information
* LP #1885257: `anboxd` was using 100% of a single CPU core due to a spinning loop

[/Details]

[Details=1.6.0]

## 1.6.0 (June 2020)

### New features & improvements

* Watchdog can now be disabled via the application manifest or configured to allow
  additional packages to provide a foreground activity
* Service endpoints can now be defined in the application manifest
* Full HA support for the streaming stack
* Rejoining a streaming session when the initial client left is now possible and can
  be configured via the stream gateway API when a new session is created
* GPU acceleration support for Tensorflow Lite via the [GPU delegate](https://www.tensorflow.org/lite/performance/gpu)
  on supported GPUs (requires OpenGL ES >= 3.1)
* GPS support in the Anbox Platform SDK
* GPS position can be statically configured before the Android system boots
* Application resources (CPU, memory, disk, GPUs) can now be declared in the
  application manifest as an alternative to predefined instance types
* Updated Android WebView to 83.0.4103.96
* Latest security updates for Android 10 (patch level [2020-06-05](https://source.android.com/security/bulletin/2020-06-01))
* Manual mode for the Anbox Application Registry (AAR) which allows pushing and pulling
  applications via the REST API or the `amc` command line client to or from the registry
* Improved audio latency for the streaming protocol implementation
* Various fixes for improved Android system stability
* Increased [Android CTS](https://source.android.com/compatibility/cts) test coverage
* The Anbox Streaming SDK now comes with an Android example to demonstrate how to
  utilise streaming within an Android application.

[/Details]

[Details=1.5.2]

## 1.5.2 (June 2020)

### New features & improvements

* Fix infinite loading screen issue when streaming from Anbox Stream Gateway UI
* Fix SDK documentation for Anbox Stream Gateway and all API routes are prefixed with "/1.0"
* Reconfigure Anbox Stream Gateway upon charm upgrade

[/Details]

[Details=1.5.1]

## 1.5.1 (May 2020)

### New features & improvements

* Fix timeout issue when adding or removing LXD nodes from the cluster in AMS
* Containers are now gracefully terminated to ensure the backup hook is executed
* Support to start a container with one specific application version from Anbox Stream Gateway UI
* Support numpad and mouse wheel input for the WebRTC based Streaming Stack
* Collecting basic statistics (FPS, RTT and bandwidth) while streaming and display them in Anbox Stream Gateway UI
* Stream Gateway will not directly be exposed to the public network but only accessible via a reverse proxy
* Dropped the monitoring stack from the default Juju bundle. It is now available via an overlay

[/Details]

[Details=1.5]

## 1.5 (April 2020)

### New features & improvements

* Support for Android 10 including latest security updates
* Updated software rendering to work on Android 10
* Applications can now have encoder requirements (e.g. whether or not they
  require a GPU or are fine on a CPU encoder) and are scheduled accordingly
* Use [Dqlite](https://dqlite.io/) in the Stream Gateway for High Availability
* HTTP/HTTPS proxy support in AMS
* Highly Availability support for Anbox Stream Gateway via [Dqlite](https://dqlite.io/)
* Charms now properly work with DNS names when adding machines
* Updated Android WebView to [80.0.3987.132](https://chromereleases.googleblog.com/2020/03/stable-channel-update-for-desktop.html)
* Preliminary support for Ubuntu 20.04
* Software rendering and video encoding support for the streaming stack
* GPUs are now identified by their PCI address in order for a correct mapping
  inside containers

### Deprecations

* Android 7 images are now deprecated and will be dropped with the next release
  of Anbox Cloud

[/Details]

[Details=1.4]

## 1.4 (March 2020)

### New features & improvements

* Support for Android 10 including latest security updates
* Inclusion of an alpha version of the WebRTC based Streaming Stack
* Updated and improve OpenGL/EGL layer to provide better performance and
  API support up to OpenGL ES 3.2 and EGL 1.4
* Nested Android container is now using a nested user namespace with its own
  user id range to further isolate the Android system from the host system.
* Support for [explicit graphics synchronisation](https://source.android.com/devices/graphics/sync)
* Automatic GPU detection on deployment and at runtime
* Default LXD version changed to 3.21 for shiftfs and extended GPU support
* Container life-cycle events are now reported via `amc monitor` and the corresponding REST API
* Support for VNC was removed as [scrcpy](https://github.com/Genymobile/scrcpy) offers a good alternative

[/Details]

[Details=1.3]

## 1.3 (January 2020)

### New features & improvements

* Generating thumbnails within `libstagefright` in the Android 7 images is now working
  reliable where it was generating single coloured images at times before.
* Error messages are now presented via the AMS REST API for application versions.
* The configuration of a container was created with (platform, boot package, ...)
  was added to the container REST API object which makes it visible with
  `$ amc show <container id>` for later inspection
* Life-cycle events are now returned from the monitor endpoint the AMS REST API provides
* Download of addons is now retried up to three times during the container bootstrap
  to workaround busy network environments
* The addon prepare hook is now correctly executed while the container is running
  and before the bootstrap process finishes

[/Details]

[Details=1.3.2]

## 1.3.2 (October 2019)

### New features & improvements

* Increased maximum allowed startup time for containers to 15 minutes
* Containers can now started with additional disk space added
* Nodes can be marked as unschedulable to allow rebooting them for maintenance
* `amc` supports deleting containers on a specific node (e.g. `$ amc delete --node=lxd0 --all`)
* The default deployment configuration now allows deploying AMS and LXD on the same machine
* Integrated Android security fixes for September and October 2019. See the
  [Android Security Bulletins](https://source.android.com/security/bulletin) for more information.
* Added `prepare` hook to allow customising Android while it's running as part of the bootstrap process
* Updated LXD charm to install latest NVIDIA CUDA drivers

[/Details]

[Details=1.3.1]

## 1.3.1 (September 2019)

### New features & improvements

* Allow underlying image of an application to be changed
* Support for applications without an APK
* An Anbox platform can now specify the display refresh rate
* Integrated Android security fixes for August 2019. See the
  [Android Security Bulletins](https://source.android.com/security/bulletin) for more information.

### Bug fixes

* Refresh the LXD snap on demand when the configuration is changed
* Don't use embedded etcd when a real etcd is available
* Correctly determine the maximum OpenGL ES version the host GL driver supports
* Support for gamepad devices in Anbox and the platform SDK

[/Details]

[Details=1.3.0]

## 1.3.0 (August 2019)

### New features & improvements

* Images are now only distributed via the official image server and no longer available for download
* The application registry received a dedicated CLI command to manage trusted clients
* A dedicated charm now takes care of deploying the Anbox Application Registry
* The disk space available to a container was reduced from 5GB to 3GB for all instance types
* Android ANR and tombstone crash logs are now pulled from a container when it fails at runtime or on
  startup
* Gamepad support was added to Anbox and the Platform SDK
* Sensor support was added to Anbox and the Platform SDK
* AMS now supports marking a single image as the default one which will be used if no other is specified
  for raw container launches or applications
* Initial support for event monitoring of the AMS service via `amc monitor` and the REST API
* The `swrast` platform is now part of the default image and doesn't need to be installed via an addon
* The `binder` and `ashmem` kernel modules are now supported on the HWE 5.0 kernel coming with Ubuntu 18.04.3
* Services a container provides can now be named to help identifying them
* The Android container is now further secured with a more narrow [`seccomp`](https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt)
  profile than the outer Anbox container.
* Addons can now declare that they add support for specific Android ABIs not supported by the hardware
  via software based binary translation
* Integrated Android security fixes until July 2019. See the
  [Android Security Bulletins](https://source.android.com/security/bulletin) for more information.

[/Details]

[Details=1.2.1]

## 1.2.1 (April 2019)

### Bug fixes

  * Telegraf was restarted every five minutes which caused metrics from Anbox
    being lost.
  * Android framework crashed in [`WifiManager.getWifiState()`](https://developer.android.com/reference/android/net/wifi/WifiManager.html#getWifiState())
  * Application updates failed due to limited cluster capacity. Base containers
    are now queued up and processed in order as soon as capacity is available.
  * AMS was not correctly finishing a container timeout on launch when restarted. On
    restart AMS now resumes the timeout.
  * Base containers are now correctly marked as stopped during the bootstrap process
    when the related LXD container is also stopped.
  * Fixed unhandled timeouts in the LXD API client implementation causing API calls
    to stall forever.
  * Added Android security fixes from April 2019. See the
    [Android Security Bulletins](https://source.android.com/security/bulletin) for more information.
  * Installing applications with an architecture not supported by the LXD cluster caused
    the installation process to stall. AMS now checks on APK upload if the APK can be executed
    by the available machines in the LXD cluster. The installation process was updated to not
    stall on unsupported APKs.
  * The Android WebView crashed in specific scenarios with SIGBUS on ARM64. This was caused
    by unaligned memory access in the OpenGL translation layer inside Anbox.

[/Details]

[Details=1.2.0]

## 1.2.0 (April 2019)

### New features & improvements

* Full support for an [Application Registry](installation-registry.md)
* Updated Android 7.x with all [security patches](https://source.android.com/security/bulletin) as of Mar 5 2019
* Support for Intel and AMD GPUs
* If configured, images will now be automatically pulled from a Canonical provided
  image server which will automatically bring updates once published.
* Various performance and stability improvements
* Dynamic management of [KSM](https://www.kernel.org/doc/html/latest/admin-guide/mm/ksm.html)
* Dedicated tool to backup and restore user data of Android applications
* Extended timeouts for addon hook execution
* Tab completion (bash only) for the `amc` command
* Improve startup time for the Android container
* The `amc` command now has `shell` and `exec` subcommands to allow easy access of containers
* Applications can now be tagged
* Filtering of containers and applications via the `amc` command
* `amc wait` allows to wait for a status change of a container or application object
* Reworked APK validator for application packages
* The Android container now uses dnsmasq, as provided by LXD on the host, as DNS server
* Various improvements on the Anbox Cloud charms

[/Details]

[Details=1.1.1]

## 1.1.1 (February 2019)

### Bug fixes

* Anbox was taking an incorrect display size from platform plugins and failed
  to initialise EGL rendering context.
* The Anbox container now always dumps system log files when an error occurred.

[/Details]

[Details=1.1.0]

## 1.1.0 (January 2019)

### New features & improvements

* The Anbox container is now based on Ubuntu 18.04
* Experimental support for an application registry which serves as a central repository
  of applications for multiple Anbox Cloud deployments
* Updated Android 7.x with all [security patches](https://source.android.com/security/bulletin) as of Jan 5 2019
* Added GPU support to allow hardware accelerated rendering and video encoding/decoding
* Various improvements to container startup time and overall performance
* Improved AMS SDK (Go)
* Support for “raw” containers (containers without installed applications)
* The container scheduler now accounts for container disk requirements
* AMS exposes additional metrics (containers per app, ...)
* Anbox Platform SDK ABI version is marked as stable
* Containers logs can be retrieved via the REST API and command line tools
* Extended instance types (a6.3, a8.3, a10.3)
* Binder support is now based on the new binderfs coming with Linux 5.0
* AMS can now run on Arm64 machines
* Example platform plugin with software rendering and VNC support

### Known issues

None

[/Details]

[Details=1.0.1]

## 1.0.1 (December 2018)

### Bug fixes

 * Applications are not freezing anymore when using OpenGL ES >= 2.x extensively
 * AArch32 support is now properly detected on AArch64 only machines

[/Details]

[Details=1.0.0]

## 1.0.0 (November 2018)

### New features & improvements

* First official stable release of the Anbox Cloud stack
* Simple deployment via Juju in a single command on any cloud (public, private or bare metal)
* Dedicated management service for container orchestration, managing the entire life cycle of Android applications in Anbox Cloud
* Rich REST API to talk to the management service
* Automatic container scheduling and cluster resource management
* Optimised containers for performance, scalability and high density
* Based on Android 7.1.2
* Platform SDK to allow development of custom platform plugins to integrate with existing or new streaming solutions
* Golang SDK to allow easy use of the management service REST API
* Support for addons to extend the content of the container images
* Support for hooks inside the container images (e.g. restore/backup of user data)
* Rich online documentation
* Metrics collection support via Telegraf, Prometheus and Grafana
* High availability support for the management service
* Support for x86 and Arm64
* Enabled for binary translation of AArch32 on AArch64 only systems
* OpenGL ES 3.x support

### Bug fixes

None

### Known issues

* A few applications freeze after some time and stop rendering. A reason is not known yet
  and the issue is being investigated.

[/Details]
