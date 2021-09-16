Anbox Cloud provides a series of Software Development Kits (SDKs) to facilitate integrating and extending Anbox Cloud for different use cases.

## Anbox Platform SDK

The Anbox Platform SDK provides support for developing custom platform plugins, which allows cloud providers to integrate Anbox with their existing infrastructure. The SDK provides several integration points for things like rendering, audio or input processing.

For more details about custom platform plugins, refer to the [Anbox Platform API documentation](https://anbox-cloud.github.io/1.9/anbox-platform-sdk/index.html).

### Download and installation

The Anbox Platform SDK can be downloaded via Git from GitHub:

    git clone https://github.com/anbox-cloud/anbox-platform-sdk.git

You need the following build dependencies:

    sudo apt install cmake-extras libavcodec-dev libavformat-dev libelf-dev libegl1-mesa-dev

### Examples

The Anbox Platform SDK provides a collection of example platform plugins to help developers get started with plugin development. The following examples are included:

* `minimal` - A platform plugin that provides a dummy implementation of a minimal platform plugin to demonstrate the general plugin layout.
* `audio_streaming` - A platform plugin that provides a more advanced example of how a platform plugin can process audio and input data.

## AMS SDK

The AMS SDK offers a set of [Go](https://golang.org/) packages and utilities for any external [Go](https://golang.org/) code to be able to connect to the AMS service through the exposed REST API.

### Components

The AMS SDK consist of the following Go packages:

* `client`: A REST client object with methods to manage applications, images, nodes, addons or containers. Each method relates to a specific management operation and wraps the REST calls and listening operations.

* `api`: AMS REST API objects.

* `shared`: Helper methods and tools for common tasks like system tasks, certificates, password hashing or websocket dialing.

* `shared/rest/client`: REST client base functionality to wrap common behaviour of the various operations of the REST protocol and websocket management for event listening.

* `shared/rest/api`: REST API basic objects, independent of any specific REST implementation.

* `shared/errors`: A simple wrapper for the most commonly-used error implementation in the return of REST API.

* `examples`: A set of examples to demonstrate how the `client` package can be used.

### Download and installation

The AMS SDK can be downloaded via Git from GitHub:

    git clone https://github.com/anbox-cloud/ams-sdk.git

To start using the SDK, simply add the content of the provided SDK zip file into your projects `vendor/` directory or your `GOPATH`.

### Examples

The AMS SDK comes with a set of examples demonstrating the capabilities of the SDK. You can find them in the `examples` directory of the AMS source.

### Authentication setup

Clients must authenticate to AMS before communicating with it.
See [client management](https://discourse.ubuntu.com/t/managing-ams-access/17774).

### Connecting to AMS

When creating custom code to connect to the service, you must start with the creation of a REST client object. Such an object needs a TLS configuration that includes the client certificate to be sent to AMS and the server certificate the client trusts. There are many ways of creating a TLS configuration in go. The AMS SDK provides an easy solution involving a few lines of code:

```go
import (
    "flag"
    "net/url"
    "os"

    "github.com/CanonicalLtd/ams/client"
    "github.com/CanonicalLtd/ams/shared"
)

func main() {
    flag.Parse()
    if flag.NArg() == 0 {
        fmt.Println("Please provide AMS service URL")
        os.Exit(1)
    }

    serviceURL := flag.Arg(0)
    u, err := url.Parse(serviceURL)
    if err != nil {
        fmt.Println("Failed to parse AMS service URL")
        os.Exit(1)
    }

    serverCert, err := shared.GetRemoteCertificate(serviceURL)
    if err != nil {
        fmt.Println("Failed to get remote certificates")
        os.Exit(1)
    }

    tlsConfig, err := shared.GetTLSConfig(clientCert, clientKey, "", serverCert)
    if err != nil {
        fmt.Println("Failed to get TLS config")
        os.Exit(1)
    }

    ...
}
```

> **Note:** Here, we regard any server certificate as valid. If you want a better compromise on the client side with the server certificate to trust, replace the `shared.GetRemoteCertificate(serviceURL)` method with code to read a server well-known certificate from a remote or local path to an x509 object and pass it to the `shared.GetTLSConfig()` method.

Once the TLS configuration is ready, the next step is to create the REST client object:

```go
amsClient, err := client.New(u, tlsConfig)
if err != nil {
    return err
}
```

Now the client object is ready to be used.

### Asynchronous operations

All operations modifying entities on AMS are executed asynchronously to prevent blocking the client. This means that a call, say, to `c.CreateApplication(...)` won't block and will return immediately, even when the operation is still not finished by the service.

All asynchronous operations return a `github.com/CanonicalLtd/ams/shared/rest/client/Operation` struct object.

If you want your client to wait for an asynchronous operation to complete, you can call the `Operation.Wait()` method, which will block the current thread until the operation finishes or an error occurs:

```go
operation, err := c.CreateApplication(".", nil)
err = operation.Wait(context.Background())
if err != nil {
    return err
}
```

In your code, you can receive the resulting resources and extract the ID of the created application:

```go
resources := operation.Get().Resources
for _, r := range resources {
    for _, id := range r {
        fmt.Printf("id: %s", path.Base(id))
    }
}
```

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
