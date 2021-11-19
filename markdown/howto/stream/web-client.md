The following HTML document should give you the minimum to get started.
Detailed explanations can be found below.

```html
<!DOCTYPE html>
<html>
<head>
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
    <meta content="utf-8" http-equiv="encoding">
    <title>Anbox Streaming SDK Example</title>
</head>
<body>
    <script type="module">
    import {AnboxStream, AnboxStreamGatewayConnector} from './anbox-stream-sdk.js';

    const connector = new AnboxStreamGatewayConnector({
        url: 'https://gateway.url.net',
        authToken: 'YOUR_AUTH_TOKEN',
        session: {
            app: "com.foo.bar",
        },
    });

    let stream = new AnboxStream({
        connector: connector,
        targetElement: "anbox-stream",
        screen: {
            width: 1280,
            height: 720,
            fps: 25,
        },
        controls: {
            keyboard: true
        },
        callbacks: {
            error: error => {
                console.log("AnboxStream failed: ", error);
            }
        }
    });
    stream.connect();
    </script>

    <div id="anbox-stream"></div>
</body>
```

Let's go through each step here:

```javascript
const connector = new AnboxStreamGatewayConnector({
    url: 'https://gateway.url.net',
    authToken: 'YOUR_AUTH_TOKEN',
    session: {
        app: "com.foo.bar",
    },
});
```

Behind the scenes, the SDK is actually comprised of two parts. The `connector` takes care of talking to the stream backend (in this case the Stream Gateway, but this could be replaced with your own middleware) and initiating the WebRTC setup.
The `Anbox Stream` takes care of displaying the video and audio feed and handle controls, lifecycle events, and more.

The distinction between the two is made to make it easier to plug your own software in the SDK rather than having to re-write everything again.

In this case, the connector is made to talk directly to the Stream Gateway and thus needs its location and an access token. It also needs to know which Android application to start.

`gateway.url.net` should be replaced with the Stream Gateway IP/Domain name. You can get this information by running `juju status`.
`YOUR_AUTH_TOKEN` is a token [generated with the Stream Gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784).
`com.foo.bar` is the name of an application added via `ams`. You can list all applications by running `amc list`.

```javascript
let stream = new AnboxStream({
    connector: connector,
    targetElement: "anbox-stream",
    screen: {
        width: 1280,
        height: 720,
        fps: 25,
    },
    controls: {
        keyboard: true
    },
    callbacks: {
        error: error => {
            console.log("AnboxStream failed: ", error);
        }
    }
});
```

This is the *main* class. It takes the previously created connector and prepares the browser to handle the stream properly.

```javascript
targetElement: "anbox-stream",
```

The SDK needs an HTML element where it can attach the video, `targetElement` is the ID of that element.
In this case you'd need to add the following to your HTML body:

```html
<div id="anbox-stream"></div>
```

[note type="information" status="Note"]Make sure events can reach this element, otherwise controls will not work.[/note]

The default behavior of the video is to fill the maximum space given by this element while keeping aspect ratio intact.

```javascript
screen: {
    width: 1280,
    height: 720,
    fps: 25,
},
controls: {
    keyboard: true
},
callbacks: {
    error: error => {
        console.log("AnboxStream failed: ", error);
    }
}
```

The rest is mostly optional and is made to customize the stream. You can find a complete inline documentation in the SDK.
Note that you can register callbacks to be notified at specific points in the stream lifecycle.

```javascript
stream.connect();
```

Once everything is ready, you can start the connection and start the stream.
