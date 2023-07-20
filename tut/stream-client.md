This tutorial guides you through the process of setting up a web-based streaming client using the Anbox Cloud streaming stack.

## Preparation

### Install the Anbox Cloud Appliance
We need the Anbox Cloud streaming stack to be deployed already to set up a streaming client. So let's get the streaming stack ready by installing the Anbox Cloud Appliance. Follow the instructions in the [appliance installation tutorial](https://discourse.ubuntu.com/t/22681) until you finish initialising the Appliance.

### Create an access token

To access the HTTP API of the Anbox Stream Gateway, an access token is required. Each access token is associated with a service account.

On the machine where Anbox Cloud Appliance is installed, create the service account by running the following command:

    anbox-cloud-appliance gateway account create test

The output of this command provides the access token. Make a note of this token to use when you make a request to the stream gateway API.

### Create an application

Follow the instructions in [How to create an application](https://discourse.ubuntu.com/t/24198) and create an application.

## Set up the stream client
Create a directory to set up the stream client:

    sudo mkdir -p /srv/stream-client

Create a `demo.html` file inside `/srv/stream-client` with the following content:

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
        // Run `juju status` to get the stream gateway IP/domain name
        // Replace 'https://gateway.url.net' with the stream gateway IP/domain name
        url: 'https://gateway.url.net',
        //Use the access token created earlier as 'YOUR_AUTH_TOKEN'
        authToken: 'YOUR_AUTH_TOKEN',
        session: {
            // Run `amc list` to see a list of all applications
            // Replace `com.foo.bar` with your application name
            app: "com.foo.bar",
        },
        // Set the display resolution and frame rate for the Android container
        screen: {
            width: 1280,
            height: 720,
            fps: 25,
        }
    });
    // The AnboxStream class takes care of the WebRTC signaling process as well as the web browser integration
    let stream = new AnboxStream({
        connector: connector,
        // targetElement is the ID of the HTML element where the SDK can attach the video
        targetElement: "anbox-stream",
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
    <!--To display the video element correctly, always specify both the height and the width attributes-->
    <div id="anbox-stream" style="width: 100vw; height: 100vh;"></div>
</body>
```
If you experience any streaming issues, you can turn on debug information by adding the following option to the `AnboxStream` which is the `main` class:

    experimental: {
       debug: true,
       }

## Create and enable the stream UI service

Create a `stream-ui.service` with the following content:
```
[Unit]
Description=Simple Anbox Cloud Stream Client

[Service]
WorkingDirectory=/srv/stream-client
ExecStart=/usr/bin/python3 -m http.server -b 127.0.0.1 8080

[Install]
WantedBy=multi-user.target
```

Run the following commands to install and start the service:
```bash
#Install the service file
sudo cp stream-ui.service /etc/systemd/system/
#Reload systemd
sudo systemctl daemon-reload
#Enable and start the service
sudo systemctl enable --now stream-ui.service
```

## Add a middleware definition

Add a middleware definition (see [Adding Basic Authentication](https://doc.traefik.io/traefik/v2.0/middlewares/basicauth/) for more details) to the [`traefik`](https://traefik.io/) configuration.

Create `stream-ui.yaml` under `/var/snap/anbox-cloud-appliance/common/traefik/conf/` with the following content for `traefik` to redirect requests to the service. 

```yaml
http:
  routers:
    to-stream-ui-demo:
      entryPoints: ["websecure"]
      rule: "PathPrefix(`/demo/`)"
      service: stream-ui-demo
      priority: 110
      tls: {}deployed
        forceSlash: false
    demo-auth:
      basicAuth:
        users:
        # demo is the user name and
        # foobar is the password for HTTP basic authentication
        - "demo:foobar"
  services:
    stream-ui-demo:
      loadBalancer:
        servers:
          - url: http://127.0.0.1:8080
```

Set the right permissions for the `stream-ui.yaml`:

    chmod 0600  /var/snap/anbox-cloud-appliance/common/traefik/conf/stream-ui.yaml

## Generate the HTTP basic authentication credentials

Use the `htpasswd` tool to generate a user/password combination:
```
apt install -y apache2-utils
httpasswd -n <your user name>
```

Enter your desired password when prompted.

Insert the generated credentials to the `traefik` configuration by editing `/var/snap/anbox-cloud-appliance/common/traefik/conf/stream-ui.yaml` to look like:
```
http:
routers:
    ...
    middlewares: ["ratelimiter", "strip-demo-prefix", "demo-auth"]
middlewares:
    ...
    demo-auth:
        basicAuth:
            users:
            - "<user name>:<hashed password>"
...
```

With this configured, users will be asked to enter the basic authentication credentials to access the site.

Restart `traefik`:

    sudo snap restart anbox-cloud-appliance.traefik

Now you can go to `https://<ip>/demo/`, enter the HTTP basic authentication credentials and view the web-based streaming client.
