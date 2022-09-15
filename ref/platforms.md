Anbox can make use of different [platforms](https://anbox-cloud.github.io/latest/anbox-platform-sdk/) to customise its behaviour. Anbox Cloud currently supports 3 platforms. Which one to use depends on your needs.

## Supported platforms

| Name     	| Behaviour                                                                                                                                            	|
|----------	|-----------------------------------------------------------------------------------------------------------------------------------------------------	|
| `null`   	|  A headless-GL platform. No rendering is performed. No audio input/output. Useful for functional tests. It's used by default if no platform is specified when launching a container.                                                                       	|
| `webrtc` 	| Full-featured WebRTC based streaming platform. Includes driver and integration for AMD and Nvidia GPUs as well as LLVMpipe based software rendering if no GPU is detected.  Support audio input/output. |
| `swrast` 	| (DEPRECATED) Software Rasterization platform. A LLVMpipe based software rendering platform. Useful for visual tests. No audio input/output.                                                               	|

## Using platforms

Instructing a container to use a platform is done through the `--platform` (or `-p`) flag when launching a container, e.g.

    amc launch -p webrtc <application>

### `swrast` platform
#### Display Settings Configuration

[note type="caution" status="Warning"]The `swrast` platform is deprecated and has been replaced with the `webrtc` platform starting with Anbox Cloud 1.13. You can still explicitly specify `swrast` as platform name, but internally, it is mapped to the `webrtc` platform. The `webrtc` platform provides backward compatibility with the display settings described below.[/note]

Anbox Cloud provides a way of inserting user data to Android container upon its launch which can configure the display settings for `swrast` platform.

By default when launching a container on the `swrast` platform without specifying the display settings through user data, the following display specification will be used:

Display specs   | Value
----------------|-------
Width           | 1280
Height          | 720
FPS             | 60
Density         | 160

If you want to change the display settings of Android container, you need to provide a combination of a numeric formatting string as follows:

    <Display width>,<Display height>,<FPS>,<Display density>

The first two fields which imply display width and display height respectively are required, however the latter two are optional.
And when launching a container, supply the display settings via user data:

    amc launch --userdata="960,720,30,120" -p swrast <application>

Then the supplied display setting will be applied after the container gets started.

### `null` platform
#### Display Settings Configuration

Display settings for the `null` can be configured in the same way as for the `swrast` platform.

Instead of supplying the display settings via `userdata` through the `amc launch` command they can be alternatively written before the start of the Anbox runtime (e.g. in a `pre-start` hook) to `/var/lib/anbox/display_settings`. The format remains the same as when supplied as `userdata`.

### `webrtc` platform

The `webrtc` platform is used by Anbox to provide graphical output. It supports all GPUs supported by Anbox Cloud in addition to software rendering. It is used when a container is launched with `--enable-graphics`, or via the Anbox Stream Gateway.

#### Configuration

The `webrtc` platform can be configured through user data provided to the container in JSON format. AMS puts the configuration data at `/var/lib/anbox/userdata`.

Field name | Type | Default | Description
-----------|------|---------|------------
`display_width` | `int` | `1280` | Width of the display provided to Android.
`display_height` | `int` | `720` | Height of the display provided to Android.
`display_density` | `int` | `240` | Density of the display provided to Android.
`fps` | `int` | `60` | Refresh rate of the display provided to Android.

For example, to configure the platform for a display height of 1080p and 60 FPS, set the user data for a container like this:

    amc launch -p webrtc --userdata '{"display_width":1920, "display_height":1080, "fps": 60}'
