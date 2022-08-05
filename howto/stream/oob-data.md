Enabling out-of-band (OOB) data transmission between an Android application and a WebRTC client makes it possible to exchange data and trigger actions between an Android application and a WebRTC client.

Anbox Cloud provides two versions of this OOB data exchange:

- [Version 2](#oob-v2) provides a full-duplex bidirectional data transmission mode in which data can flow in both directions at the same time.

  Use this version if you start your implementation now. If you already have an existing implementation, you should plan to update it to use version 2.
- [Version 1](#oob-v1) enables Android application developers to trigger an action from an Android application running in a container and forward it to a WebRTC client through the Anbox WebRTC platform. When Anbox receives the action, as one peer of the WebRTC platform, the action is propagated from Anbox to the remote peer (the WebRTC client) through a WebRTC data channel. The client can then react to the action received from the remote peer and respond accordingly on the UI.

  This version supports only half-duplex data transmission. It allows sending data from an Android application to a WebRTC client through the Anbox WebRTC platform, but it is not possible to receive data from the WebRTC client to an Android application.

[note type="caution" status="Warning"]
[Version 1](#oob-v1) of the out-of-band data exchange between an Android application and a WebRTC client is deprecated. Support for it will be discontinued in a future release. Therefore, you should migrate your integration of version 1 of the OOB data exchange to [version 2](#oob-v2) for full-duplex data transmission and better performance.
[/note]

See the instructions for exchanging OOB data using a specific implementation version below:
- [Version 2](#oob-v2)
- [Version 1](#oob-v1)

<a name="oob-v2"></a>
## Version 2

The following instructions will walk you through how to set up data channels and perform data transmission in both directions between an Android application and a WebRTC platform.

### Web application

In your web-based client application, import the [Anbox Streaming SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#streaming-sdk).

Create a data channel (named `foo` in the following example) under the `dataChannels` property of an `AnboxStream` object and register event handlers that respond to the events sent from an Android application:

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

[note type="information" status="Note"]
An `AnboxStream` object can create a maximum of five data channels. If the number of data channels exceeds the allowed maximum, an exception is thrown when instantiating the `AnboxStream` object.
[/note]

To launch a new WebRTC session, the client must call `stream.connect()`. The `AnboxStream` object then builds up a WebRTC native data channel internally, based on the name declared under its `dataChannels` property for peer-to-peer communication (`foo` in the example).

To send data to an Android application through the channel, the client must use the member function `sendData` of the `AnboxStream` class:

```
        stream.sendData('foo', 'hello world');
```


### Anbox WebRTC platform

When establishing a peer connection, a number of data channels are set up in the Anbox WebRTC platform on the server side, upon request by the client.

At the same time, a number of Unix domain sockets are created under the `/run/user/1000/anbox/sockets` folder. They use the format `webrtc_data_<channel_name>` and represent the established communication bridge between a WebRTC client and the Anbox WebRTC platform. Those Unix domain sockets can be used by a service or daemon to:

- Receive data sent from a WebRTC client over the data channel and forward it to an Android application.
- Receive data sent from an Android application and forward it to a WebRTC client over the data channel.

A trivial example to simulate the data transmission between an Anbox container and a WebRTC client is using the [`socat`](https://manpages.ubuntu.com/manpages/bionic/man1/socat.1.html) command to connect the Unix domain socket and perform bidirectional asynchronous data sending and receiving:

1. Connect the Unix domain socket:

        socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo

1. After the Unix domain socket is connected, type a message and hit the `Enter` key:

        hello world

   The data is now sent from the Anbox WebRTC platform over the data channel to the WebRTC client.
1. Observe that the message is displayed in the console of a web browser, responding to the message event:

        data received: hello world

1. To test the other direction of the communication, send a message from a WebRTC client to the Anbox WebRTC platform through the data channel:

        session.sendData('foo', 'anbox cloud')

1. Observe that the received data is printed out in the `socat` TCP session:

   ```
      socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo
      hello world <--  the sent data
      anbox cloud <--  the received data
   ```

### Anbox data proxy

To build up the communication bridge between an Android application and the Anbox WebRTC platform, you must implement a service or daemon that is responsible for:

 - The socket connection
 - Polling events
 - Forwarding data between both ends

A system service named `anbox-data-proxy`, which covers all the above functionalities, will be implemented in the 1.16.0 release of Anbox Cloud. It makes use of [`gbinder`](https://github.com/mer-hybris/libgbinder) to set up a communication bridge and provide reliable and high-efficiency data transmission between the Android system and the Anbox WebRTC platform.

<a name="oob-v1"></a>
## Version 1

The following instructions will walk you through how to send a message from an Android application
running in a container to the client application developed with the Anbox Streaming
SDK.

### Android application

#### Add required permissions

For the Android application running in the container, add the
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

Any attempt of an application that lacks the `android.permission.ANBOX_SEND_MESSAGE`
permission to invoke APIs that are provided by the Anbox platform library will
be disallowed, and a security exception will be raised.

#### Import Java library

Check out the [Anbox Streaming SDK](https://github.com/anbox-cloud/anbox-streaming-sdk) from GitHub:

    git clone https://github.com/anbox-cloud/anbox-streaming-sdk.git

To import the `com.canonical.anbox.platform_api_skeleton.jar` library into your
Android project, refer to the official [documentation](https://developer.android.com/studio/build/dependencies)
on how to import an external library into an Android application project.

Alternatively, you can follow the steps below:

1. Copy `com.canonical.anbox.platform_api_skeleton.jar` to the `project_root/app/libs`
   directory (if the folder doesn’t exist, just create it).

2. Edit `build.gradle` under the app folder by adding the following line
   under the dependencies scope.

   ```
   dependencies {
       implementation fileTree(dir: 'libs', include: ['*.jar'])
       …
       …
       implementation files('libs/com.canonical.anbox.platform_api_skeleton.jar')
   }
   ```

#### Send message from Android

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

[note type="information" status="Note"]The length for the message type is limited to 256 KB, and the length of the data is limited to 1 MB.[/note]

### Receive message on the client

A client application that receives a message from the Android application can be written
in JavaScript, C or C++ by using the Anbox Streaming SDK.

#### Web application

For a web-based application, you can use the JavaScript SDK which you can find under
[Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#streaming-sdk). To receive the data sent from the Android application
running in the Anbox container, implement the `messageReceived` callback
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
