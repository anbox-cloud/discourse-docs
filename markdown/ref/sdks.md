Anbox Cloud provides a series of Software Development Kits (SDKs) to facilitate integrating and extending Anbox Cloud for different use cases:

- [Anbox Platform SDK](#anbox-platform-sdk)
- [AMS SDK](#ams-sdk)
- [Anbox Streaming SDK](#streaming-sdk)

<a name="anbox-platform-sdk"></a>
## Anbox Platform SDK

The Anbox Platform SDK provides support for developing custom platform plugins, which allows cloud providers to integrate Anbox with their existing infrastructure. The SDK provides several integration points for things like rendering, audio or input processing.

For more details about custom platform plugins, refer to the [Anbox Platform SDK API documentation](https://anbox-cloud.github.io/1.10/anbox-platform-sdk/index.html).

### Download and installation

The Anbox Platform SDK can be downloaded via Git from GitHub:

    git clone https://github.com/anbox-cloud/anbox-platform-sdk.git

You need the following build dependencies:

    sudo apt install cmake-extras libavcodec-dev libavformat-dev libelf-dev libegl1-mesa-dev

### Examples

The Anbox Platform SDK provides a collection of example platform plugins to help developers get started with plugin development. The following examples are included:

* `minimal` - A platform plugin that provides a dummy implementation of a minimal platform plugin to demonstrate the general plugin layout.
* `audio_streaming` - A platform plugin that provides a more advanced example of how a platform plugin can process audio and input data.

<a name="ams-sdk"></a>
## AMS SDK

The AMS SDK offers a set of [Go](https://golang.org/) packages and utilities for any external [Go](https://golang.org/) code to be able to connect to the AMS service through the exposed REST API.

See the [AMS SDK documentation](https://github.com/anbox-cloud/ams-sdk) on GitHub for more information.

### Download and installation

The AMS SDK can be downloaded via Git from GitHub:

    git clone https://github.com/anbox-cloud/ams-sdk.git

To start using the SDK, simply add the content of the provided SDK zip file into your projects `vendor/` directory or your `GOPATH`.

### Examples

The AMS SDK comes with a set of examples demonstrating the capabilities of the SDK. You can find them in the `examples` directory of the AMS source.

### Authentication setup

Clients must authenticate to AMS before communicating with it. For more information, see [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774) and the [AMS SDK documentation](https://github.com/anbox-cloud/ams-sdk) on GitHub.

<a name="streaming-sdk"></a>
## Anbox Streaming SDK

The Anbox Streaming SDK allows the development of custom streaming clients, using JavaScript or C/C++.

### Components

The Anbox Streaming SDK provides the following alternative SDKs:

- A JavaScript SDK designed to help you get started with the development of a web-based client. This SDK handles all aspects of streaming, from the WebRTC protocol to handling controls, game pads, speakers and screen resolutions.
- A native SDK offering a C API that provides the same full-featured video streaming as the JavaScript SDK, but aims for a low latency for your application based on Anbox Cloud. The native SDK is intended for C and C++ based applications. It currently supports Android and Linux.

#### Features

| Feature                                          | JavaScript SDK | Native SDK |
|--------------------------------------------------|:--------------:|:----------:|
| Video streaming                                  |        ✓       |      ✓     |
| Audio streaming                                  |        ✓       |      ✓     |
| Microphone support                               |        ✓       |      ✓     |
| Dynamically change Android foreground activity   |        ✓       |      ✓     |
| Send commands to the Android container           |        ✓       |      ✓     |
| Game pad support                                 |        ✓       |      ✓     |
| Camera support                                   |        ✓       |            |
| Sensor support                                   |                |            |
| Location support                                 |        ✓       |            |
| Supported platforms                              |       All  | Linux, Android |
| Zero Copy rendering and decoding                 |        ✓       |            |
| Supported codecs                      | VP8, H.264 | VP8, H.264 (Android only) |

### Download and installation

To use the Anbox Streaming SDK, you must have [deployed the Anbox Streaming Stack](https://discourse.ubuntu.com/t/installation-quickstart/17744).

You can download the Anbox Streaming SDK via Git from GitHub:

    git clone https://github.com/anbox-cloud/anbox-streaming-sdk.git

### Examples

The Anbox Streaming SDK comes bundled with examples to help you get started. They are located in the `examples` directory.
