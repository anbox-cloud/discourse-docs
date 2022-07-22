The WebRTC streamer implementation in Anbox Cloud can be fine tuned to provide better results in certain situations. The default configuration is optimized to provide a good balance between low latency and high quality and usually does not need to be adjusted.

The WebRTC streamer configuration has to be placed within an Anbox container at `/var/lib/anbox/streamer.json` before the Anbox runtime starts and can be shipped as part of an [application](https://discourse.ubuntu.com/t/managing-applications/17760) or an [addon](https://discourse.ubuntu.com/t/managing-addons/17759).

JSON is being used as the format of the configuration file and has the following structure:

| Name | Value type | Default | Description |
|------|------------|---------|-------------|
| `video.bitrate_limits` | array of objects | `[]` | [Bitrate limits](#video-bitrate-limits) to apply to the video encoder. |
| `nvidia_h264.multipass` | boolean | `false` | If set to true multipass encoding is enabled. |
| `nvidia_h264.aq` | boolean | `false` | If set to true, adaptive quantization is enabled. |
| `nvidia_h264.aq_strength` | integer | `0` | Strength of adaptive quantization. `0` means the encoder will automatically decide, otherwise a value from `1` (least aggressive) to `15` (most aggressive) |

See the [NVENC Video Encoder API](https://docs.nvidia.com/video-technologies/video-codec-sdk/nvenc-video-encoder-api-prog-guide/) documentation for more details on the `nvidia_h264` options.

<a href="#video-bitrate-limits"/>
## Video bitrate limits

Bitrate limits allow to fine tune which minimum and maximum bitrate the WebRTC streamer will use to dynamically decide the target bitrate for the encoded video stream. As network conditions are constantly changing, WebRTC automatically tries to adapt the video bitrate to find a configuration with best throughput,  quality and latency. The bitrate limits allow changing the default values the WebRTC will use a lower and upper bound for its decision.

As different resolutions require different bitrates, the bitrate limits allow defining a minimum and maximum bitrate for frames having up to the specified number of pixels. This puts aside the actual geometry of the frame and solely concentrates on the amount of pixels the frame has.

The WebRTC streamer will pick the closest limit for the configured resolution by comparing the number of pixels. If more than one limit is specified, the nearest limit with a number of pixels higher than the number of pixels, a frame of the given resolution has, is selected.

The JSON object defining a bitrate limit has the following possible fields:

| Name | Value type | Default | Description |
|------|------------|---------|-------------|
| `num_pixels` | integer | 0 | Number of pixels up to which the limit is considered |
| `min_kbps` | integer | 0 | Minimum bitrate in kb/s |
| `max_kbps` | integer | 0 | Maximum bitrate in kb/s |

## Example configuration

The following shows an example configuration for the WebRTC streamer:

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

The `num_pixels` value here is calculated based on a 720p resolution, e.g. `1280 * 720 = 921600`.