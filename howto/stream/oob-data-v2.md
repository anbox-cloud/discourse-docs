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
