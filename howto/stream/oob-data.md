
- [Version 1](#oob-v1)
- [Version 2](#oob-v2)

<a name="oob-v1"></a>
## Version 1

[note type="caution" status="Warning"]The v1 of the out-of-band data exchange between an Android application and WebRTC client is deprecated. Currently, there is no plan to remove it soon or discontinue its support, but it's recommended to migrate your integration of v1 of the OOB data exchange to [v2](tbd) for full-duplex data transmission and better performance. [/note]

The exchange of out-of-band data transmission between an Android application and a WebRTC client enables Android application developers to trigger an action from an Android application and forward it to a WebRTC client through Anbox WebRTC platform. Once Anbox receives the action, as one peer of WebRTC platform, the action will be propagated from the Anbox to the remote peer(WebRTC client) through WebRTC data channel so that client can react to the action received from the remote peer and respond accordingly on the UI.

This document will walk you through how to send a message from an Android application
running in the container to the client application developed with the Anbox Streaming
SDK.

### Android Application

#### Add Required Permissions

For the Android application running in the container, you need to add the
following required permission to the `AndroidManifest.xml` to allow the
application to send messages to the Anbox runtime:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="<your_application>">

    …
    <uses-permission android:name="android.permission.ANBOX_SEND_MESSAGE" />
    …
</manifest>
```

Any attempt of an application which lacks the `android.permission.ANBOX_SEND_MESSAGE`
permission to invoke APIs that are provided by the Anbox Platform Library will
be disallowed and a security exception will be raised.

#### Import Java Library

Check out the [Anbox Streaming SDK](https://github.com/anbox-cloud/anbox-streaming-sdk) from GitHub

    git clone https://github.com/anbox-cloud/anbox-streaming-sdk.git

To import the `com.canonical.anbox.platform_api_skeleton.jar` library into your
Android project, please refer to the official [documentation](https://developer.android.com/studio/build/dependencies)
on how to import an external library into an Android application project.

Alternatively, you can follow the steps below:

Copy the `com.canonical.anbox.platform_api_skeleton.jar` to the `project_root/app/libs`
directory (If the folder doesn’t exist, just create it).

Edit the `build.gradle` under the app folder by adding the following line
under the dependencies scope.

```
dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    …
    …
    implementation files('libs/com.canonical.anbox.platform_api_skeleton.jar')
}
```

#### Send Message from Android

The following example demonstrates how to send a message with the Anbox
Platform API to a remote client:

```
import com.canonical.anbox.PlatformAPISkeleton;

public class FakeCameraActivity extends AppCompatActivity {
     ….
     ….
     public void onResume() {
        super.onResume();

        String type = “message-type”;
        String data = ”message-data”;
        PlatformAPISkeleton api_skeleton = new PlatformAPISkeleton();
        if (!api_skeleton.sendMessage(type, data)) {
            Log.e(TAG, "Failed to send a message type " + type + " to Anbox session");
        }
    }
}
```

[note type="information" status="Note"]The length for message type is limited to 256KB and the length of data is limited to 1MB.[/note]

### Receive Message on the Client

A client application that receives a message from the Android application can be written
in JavaScript, C or C++ by using the Anbox Streaming SDK.

#### Web Application

For a web based application you can use the JavaScript SDK which you can find at
[Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#streaming-sdk). To receive the data sent from the Android application
running in the Anbox container you need to implement the `messageReceived` callback
of the `AnboxStream` object:

```
    let stream = new AnboxStream({
      ...
      ...
      callbacks: {
        ….
        messageReceived: (type, data) => {
          console.log("type: ", type, "  data: ", data);
        }
      }
    });
```

<a name="oob-v2"></a>
## Version 2

In the v1 of the out-of-band data exchange between an Android application and a WebRTC client via Anbox WebRTC platform, it only supports half-duplex data transmission and people can only send data from an Android application to a WebRTC platform. Still, they can't receive data from the WebRTC client to an Android application. The v2 of out-of-band data exchange provides a full-duplex bidirectional data transmission mode in which data can flow in both directions at the same time.

This document will walk you through how to setup data channels and perform data transmission in both directions between an Android application and a WebRTC platform.

### Web Application

In a web based application, import the JavaScript SDK which you can find at [Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#streaming-sdk).

Create a data channel `foo` under the  `dataChannels` property of an `AnboxStream` object, register event handlers in responding to the events sent from an Android application:
```
    let stream = new AnboxStream({
      ...
      ...
      dataChannels: {
        "foo": {
          callbacks: {
            close: () => {
              console.log('data channel is closed')
            },
            open: () => {
              console.log('data channel is open')
            },
            error: (err) => {
              console.log(`error: ${err}`)
            },
            message: (data) => {
              console.log(`data received: ${data}`)
            }
          }
        }
      }
    });
```

[note type="information" status="Note"]An `AnboxStream` object can create a maximum of 5 data channels. If the number of data channels exceeds the maximum allowed, an exception will be thrown when instantiating an `AnboxStream` object.[/note]

When a new WebRTC session is launched from a client by calling:
```
        stream.connect();
```

The `AnboxStream` object builds up WebRTC native data channel internally based on the data channels' name declared under its `dataChannels` property for peer to peer communication.

on the other hand, the member function `sendData` of the `AnboxStream` class enables people to send data to an Android application through one specific data channel:

```
        stream.sendData('foo', 'hello world');
```


### Anbox WebRTC Platform

In the Anbox WebRTC platform, during the establishment of a peer connection, a number of data channels will be set up on WebRTC server side upon request by the client. In the meantime, a number of UNIX domain sockets are created as well under the folder `/run/user/1000/anbox/sockets` in the format of `webrtc_data_<channel_name>`  standing for the established communication bridge between a WebRTC client and Anbox WebRTC platform. Those UNIX domain sockets can be used by a service or daemon to
- receive the data sent from a WebRTC client over the data channel and forward it to an Android application.
- receive data sent from an Android application and forward it to a WebRTC client over the data channel.

One trivial example to simulate the data transmission between Anbox container and a WebRTC client is that you can use the [`socat`](https://manpages.ubuntu.com/manpages/bionic/man1/socat.1.html) command to connect the UNIX domain socket and perform bidirectional asynchronous data sending and receiving:

```
    socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo
```

After the UNIX domain socket is connected, when typing a message and hitting the `Enter` key:

```
    socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo
    hello world
```

The data will be sent from Anbox WebRTC platform over the data channel to the WebRTC client. As a result, a message will be displayed in the console of a web browser in responding to the message event:

```
    data received: hello world
```

On other way around, if a WebRTC client sends a message to Anbox WebRTC platform through one specific data channel:

```
    session.sendData('foo', 'anbox cloud')
```

The regarding data will be printed out from a `socat` TCP session too:

```
   socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo
   hello world <--  the sent data
   anbox cloud <--  the received data
```

### Anbox Data Proxy

To build up the communication bridge between an Android application and Anbox WebRTC platform, you have to implement a service or daemon being responsible for
 - socket connection
 - events polling
 - data forwarding between both ends

A system service `anbox-data-proxy` which covers all the above functionalities will be implemented in Anbox Cloud 1.16.0 release. It makes use of [`gbinder`](https://github.com/mer-hybris/libgbinder) to set up a communication bridge and provide reliable and high-efficiency data transmission between Android system and Anbox WebRTC platform.
