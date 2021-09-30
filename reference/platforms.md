Anbox can make use of different [platforms](https://oem-share.canonical.com/partners/indore/share/docs/1.7/en/sdk/anbox/) to customize its behavior. Anbox Cloud currently supports 3 platforms. Which one to use depends on your needs.

## Supported platforms

| Name     	| Behavior                                                                                                                                            	|
|----------	|-----------------------------------------------------------------------------------------------------------------------------------------------------	|
| `null`   	|  A headless-gl platform. No rendering is performed. No audio input/output. Useful for functional tests. It's used by default if no platform is specified when launching a container.                                                                       	|
| `webrtc` 	| Full-featured WebRTC based streaming platform. Includes driver and integration for AMD and NVidia GPUs as well as LLVMPipe based software rendering if no GPU is detected.  Support audio input/output.	|
| `swrast` 	| **S**oft**w**are **Rast**erization platform. A LLVMPipe based software rendering platform. Useful for visual tests. No audio input/output.                                                               	|

## Using platforms

Instructing a container to use a platform is done through the `--platform` (or `-p`) flag when launching a container, e.g.

```bash
$ amc launch -p swrast <application>
```

### `swrast` platform
#### Display Settings Configuration

Anbox Cloud provides a way of inserting user data to Android container upon its launch which can configure the display settings for swrast platform.

By default when launching a container on the swrast platform without specifying the display settings through user data, the following display specification will be used:

Display specs   | Value
----------------|-------
Width           | 1280
Height          | 720
FPS             | 60
Density         | 160

If you want to change the display settings of Android container, you need to provide a combination of a numeric formatting string as follows:

```
<Display width>,<Display height>,<FPS>,<Display Density>
```

The first two fields which imply display width and display height respectively are required, however the latter two are optional.
And when launching a container, supply the display settings via user data:

```bash
$ amc launch --userdata="960,720,30,120" -p swrast <application>
```

Then the supplied display setting will be applied after the container gets started.

### `null` platform
#### Display Settings Configuration

Display settings for the `null` can be configured in the same way as for the `swrast` platform.

Instead of supplying the display settings via userdata through the `amc launch` command they can be alternatively written before the start of the Anbox runtime (e.g. in a restore or install hook) to `/var/lib/anbox/display_settings`. The format remains the same as when supplied as userdata.

### `webrtc` platform

When using the [Stream Gateway](https://discourse.ubuntu.com/t/streaming-android-applications/17769), the `webrtc` platform is automatically used when launching containers. You don't need to perform additional steps. Launching a container with the webrtc platform can be done via the [web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871).
