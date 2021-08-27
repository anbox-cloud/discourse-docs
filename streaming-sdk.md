The Streaming Stack comes with 
- a Javascript SDK designed to help you get started with the development of a web based client. It handles all aspects of streaming, from the WebRTC protocol to handling controls, gamepads, speakers and screen resolutions.
- a Native SDK offers a C API to provide full-featured video streaming that Javascript SDK provides but aims for a low latency to your application based on Anbox Cloud. The Native SDK is intended for C and C++ based application and currently supports Android and Linux.

You can find the SDK in the [download page](https://anbox-cloud.io/docs/sdks). The SDK comes bundled with examples to help you get started. They are located in the `examples` directory.

| Feature                                          | Javascript SDK | C++ SDK |
|--------------------------------------------------|:--------------:|:-------:|
| Video streaming                                  |        ✓       |    ✓    |
| Audio streaming                                  |        ✓       |    ✓    |
| Microphone support                               |        ✓       |    ✓    |
| Dynamically changing Android foreground activity |        ✓       |    ✓    |
| Send commands to the Android container           |        ✓       |    ✓    |
| Gamepad support                                  |        ✓       |    ✓    |
| Camera support                                   |        ✓       |         |
| Sensor support | | |
| Location support | ✓ | |
| Supported platforms | All | Linux, Android |
| Zero Copy rendering and decoding | ✓ | |
| Supported codecs | VP8, H.264 | VP8, H.264 (Android only) |

### Requirements

This guide assumes you have [deployed the Anbox Streaming Stack](https://discourse.ubuntu.com/t/installation-quickstart/17744).

### Working with the Anbox Stream Stack

* [Implement Android native streaming client](https://discourse.ubuntu.com/t/implement-android-native-streaming-client/21833)
* [Implement web based streaming client](https://discourse.ubuntu.com/t/implement-web-based-streaming-client/21835)
* [Exchange out-of-band data](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)
* [Integrate a client-side virtual keyboard](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643)
