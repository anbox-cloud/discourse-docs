Anbox Cloud enables you to run automated tests for Android applications at scale. In the following example, we make use of [Appium](http://appium.io/) to interact with a container running on Anbox Cloud and automate UI testing for Android applications.

## Setup Anbox Cloud for Appium

As most deployments don't include GPUs we're going to use the `swrast` software rendering platform for Anbox which provides a graphics driver based on [swiftshader](https://swiftshader.googlesource.com/SwiftShader).

If you want to automate the UI tests against an APK which is externally provided, you can launch a raw container:

```bash
$ amc launch -s adb -p swrast -r default
```

This will create a container which exposes the TCP port `5559` on its private address from the default image `default`. If you want to expose ADB on the public address of a node, you can add the `+` from the service endpoint specification. With that the command looks as follows:

```bash
$ amc launch -s +adb -p swrast -r
```

[note type="information" status="Hint"]If you're wondering about the syntax of the command used to launch a container, see [Launch a container](https://discourse.ubuntu.com/t/launch-a-container/24327).[/note]

If you want to run the Appium tests against an Android application managed by AMS (see [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)) you can start a regular container instead:

```bash
$ amc launch -s adb -p swrast --disable-watchdog app
```

[note type="information" status="Hint"]The `--disable-watchdog` argument is important as by default Anbox prevents Android from switching its foreground application and terminates when the application is stopped. To prevent this we need to disable the watchdog which is responsible for this.[/note]

Once the container is up and running, you can get its private IP address and the exposed port for the ADB service endpoint with the following command:

```bash
$ amc ls
+----------------------+-------------+---------+---------+------+---------------+------------------------+
|          ID          | APPLICATION |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
+----------------------+-------------+---------+---------+------+---------------+------------------------+
| bj0mpv0j1qm60tfotdrg | default     | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:5559/tcp |
|                      |             |         |         |      |               | 10.226.4.168:10000/tcp |
+----------------------+-------------+---------+---------+------+---------------+------------------------+
```

In the above output, the IP address and the exposed port of the running container is `10.226.4.168:10000/tcp`

## Connect Appium with Android Instance

As the endpoint `10.226.4.168:10000/tcp` shown above is not exposed to the public internet, the Android instance is not accessible from outside of the subnet the LXD instance is on. To connect to the exposed ADB port you have to setup a secure and encrypted SSH tunnel to the LXD machine the container is running on. For that you should have an SSH client available you can use to setup the tunnel.

On a Linux system you can setup a tunnel with the following command:

```bash
$ ssh -NL 10000:10.226.4.168:10000 ubuntu@10.180.45.183
```

This will forward any connection to port `10000` on your localhost to port `10000` on the remote machine with the address `10.226.4.168` via the AMS machine with the address `10.180.45.183`. The AMS machine here is used as relay server to establish the connection with the Android container.

Now you can connect to the remote machine via ADB with the following command:

```bash
$ $ANDROID_HOME/platform-tools/adb connect localhost:10000
* daemon not running; starting now at tcp:5037
* daemon started successfully
connected to localhost:10000
```

[note type="caution" status="Warning"]Appium uses ADB as located in the Android SDK to establish a connection between the remote Android instance and the ADB daemon running on your machine. As mixing different versions of ADB is not supported you need to use ADB from the Android SDK in all cases. If you have the `adb` client installed from other sources, like the Ubuntu package archive, remove it first (`$ sudo apt purge -y adb`).[/note]

## Execute Tests with Appium

Once the connection is established between the Anbox Container and your development machine through ADB, you can launch the Appium desktop application to execute test cases.

### Manually provided APK

If the APK file that you want to test is located in local folder or hosted on a web server, add the following capabilities and save it as a preset:

```json
{
  "platformName": "Android",
  "platformVersion": "7.1",
  "app": "<apk_path>",
  "appActivity": "<activity_name>",
  "deviceName": "Android Emulator",
}
```

The above preset accepts either an absolute path to an APK or a URL.

Finally you can start a new test session and run your test cases.
For more details about Appium, please refer to the [official documentation](http://appium.io/docs/en/about-appium/getting-started/)

### APK managed by AMS

If you want to run test cases without installing the APK every time when starting a new test session in Appium, you can let AMS manage the application for you. See [About applications](https://discourse.ubuntu.com/t/managing-applications/17760) for more details.

In this example we use the following application `manifest.yaml`:

```bash
$ cat << EOF > manifest.yaml
name: app
instance-type: a2.3
EOF
```

Once the application is fully bootstrapped by AMS, you can launch a container for it with the following command:

```bash
$ amc launch -s +adb -p swrast --disable-watchdog app
```

After the container is up and running, you need to specify the proper `appPackage` and `appActivity` in the Appium preset, the installed Android application will be launched automatically in the container when a new session is created by Appium.

```json
{
  "platformName": "Android",
  "platformVersion": "7.1",
  "deviceName": "Android Emulator",
  "noReset": true,
  "appPackage": "com.canonical.anboxtestapp",
  "appActivity": ".MainActivity"
}
```
