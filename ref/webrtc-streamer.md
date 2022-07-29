You can fine-tune the WebRTC streamer implementation in Anbox Cloud to provide better results in certain situations.

[note type="information" status="Note"]
The default configuration is optimised to provide a good balance between low latency and high quality, and usually, you don't need to adjust it.
[/note]

Place the WebRTC streamer configuration at `/var/lib/anbox/streamer.json` within the Anbox container before the Anbox runtime starts. The configuration can be shipped as part of an [application](https://discourse.ubuntu.com/t/managing-applications/17760) or an [addon](https://discourse.ubuntu.com/t/managing-addons/17759).

The configuration file uses the JSON format. It has the following structure:

| Name | Value type | Default | Description |
|------|------------|---------|-------------|
| `video.bitrate_limits` | array of objects | `[]` | [Bitrate limits](#video-bitrate-limits) to apply to the video encoder. |
| `nvidia_h264.multipass` | bool | `false` | If set to true, multi-pass encoding is enabled. |
| `nvidia_h264.aq` | bool | `false` | If set to true, adaptive quantisation is enabled. |
| `nvidia_h264.aq_strength` | integer | `0` | Strength of adaptive quantisation: a value from `1` (least aggressive) to `15` (most aggressive). `0` means the encoder will automatically decide. |

See the [NVENC Video Encoder API](https://docs.nvidia.com/video-technologies/video-codec-sdk/nvenc-video-encoder-api-prog-guide/) documentation for more details on the `nvidia_h264` options.

<a name="#video-bitrate-limits"/></a>
## Video bitrate limits

Bitrate limits allow to fine-tune which minimum and maximum bitrate the WebRTC streamer will use to dynamically decide the target bitrate for the encoded video stream. As network conditions are constantly changing, WebRTC automatically tries to adapt the video bitrate to find a configuration with best throughput, quality and latency. The bitrate limits allow changing the default values that WebRTC will use as the lower and upper bound for its decision.

As different resolutions require different bitrates, the bitrate limits allow defining a minimum and maximum bitrate for frames having up to the specified number of pixels. This puts aside the actual geometry of the frame and solely concentrates on the amount of pixels the frame has.

The WebRTC streamer will pick the closest limit for the configured resolution by comparing the number of pixels. If more than one limit is specified, it selects the nearest limit with a number of pixels higher than the number of pixels that a frame of the given resolution has.

The JSON object defining a bitrate limit has the following possible fields:

| Name | Value type | Default | Description |
|------|------------|---------|-------------|
| `num_pixels` | integer | 0 | Number of pixels up to which the limit is considered. |
| `min_kbps` | integer | 0 | Minimum bitrate in kb/s. |
| `max_kbps` | integer | 0 | Maximum bitrate in kb/s. |

## Example configuration

The following example shows a configuration for the WebRTC streamer:

    {
        "video": {
            "bitrate_limits": [
                { "num_pixels": 921600, "min_kbps": 1000, "max_kbps": 4500 },
            ],
            "nvidia_h264": {
                "multipass": true,
                "aq": true,
                "aq_strength": 5
            }
        }
    }

The `num_pixels` value here is calculated based on a 720p resolution, thus `1280 * 720 = 921600`.
