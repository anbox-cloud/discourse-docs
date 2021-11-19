This tutorial guides you through the first steps of using Anbox Cloud. You will learn how to create and access a virtual Android device or an application using the [web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871).

The web dashboard provides an easy-to use interface to Anbox Cloud. However, it currently supports a limited set of functionality, which means that it might not be sufficient for all use cases. If you want to learn how to manage Anbox Cloud from the command line, see the [Getting started with Anbox Cloud (CLI)](https://discourse.ubuntu.com/t/getting-started/17756) tutorial.

[note type="information" status="Important"]
If you haven't installed Anbox Cloud or the Anbox Cloud Appliance yet, you must do so before you can continue with this tutorial. See the following documentation for installation instructions:

- [Installing the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681)
- [Install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336) (note that you must install the streaming stack for the web dashboard to be available)
[/note]

<a name="virtual-device"></a>
## 1. Create a virtual device

Let's start exploring what Anbox Cloud can do by launching a virtual device that runs a specific Android version.

[note type="information" status="Note"]With "virtual device" we mean a simulated device that runs a plain Android operating system without any special apps installed. Technically speaking, Anbox Cloud treats such a virtual device as an "empty" application, thus an application that is not running a specific APK.[/note]

Complete the following steps to create a virtual device:

1. Open `https://<your-machine-address>/applications` in your browser.

   [note type="information" status="Note"]By default, the Anbox Cloud Appliance uses self-signed certificates, which might cause a security warning in your browser. Use the mechanism provided by your browser to proceed to the web page.[/note]
2. Click **Add Application**.
3. Enter a name for the application, for example, `virtual-device-web`.
4. Keep the pre-selected instance type.
5. Select the Android image that you want to use, for example, `bionic:android11:arm64`.
6. Do not upload an APK file.
7. Click **Add Application**.

   ![Add a virtual device|690x312](upload://oXj59uQULQySK2fPjlKCAdIPl3K.png)
8. Wait until the application status changes to `ready`.

## 2. Launch and test the virtual device

When the application has been initialised and its status changes to `ready`, complete the following steps to launch and test the virtual device:

1. In the list of applications, click the play button (labelled **New session**) for the application to start a new session.

   ![Start a new session|690x222](upload://erAnVEmlucBTrnc6GHFsSjkriuN.png)
2. Accept the default settings and click **New Session**.

   ![Start with default settings|690x322](upload://7mRukJHoTPoQ04Mrvj1FuXC5Tcc.png)
3. When the stream has loaded, you can interact with your virtual device.

## 3. Create an application from an APK

To create an application for a specific Android app, follow the steps in [1. Create a virtual device](#virtual-device), but upload the APK of the Android app.

[note type="information" status="Important"]Not all Android apps are compatible with Anbox Cloud. See [Issues when porting Android apps](https://discourse.ubuntu.com/t/usecase-port-android-application-to-anbox-cloud/17776) for more information.[/note]

Choose an [instance type](https://discourse.ubuntu.com/t/instances-types-reference/17764) that is suitable for your application. If your instance is equipped with a GPU and your application requires the use of the GPU for rendering and video encoding, select an instance type with GPU support like `g2.3`. For other instance types, the container will use a GPU if available or software encoding otherwise.

![Add an application|690x316](upload://3Q3izbrav4LBEcxEx9ahhmRyy0l.png)

You can launch and test the application in the same way as you did for the virtual device.

## 4. Update an application

You can have several versions of an application. See [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201) for detailed information.

Complete the following steps to add a new version to your application:

1. Open `https://<your-machine-address>/applications` in your browser.
2. Click the **Edit application** button next to the application for which you want to add a new version.

   ![Update an application|690x227](upload://qAXQo0sDFYQupEEHoZ70UqDu1Xh.png)
3. Upload a new APK, or do other changes to the configuration.
4. Click **Update application**.

## Done!

You now know how to use the web dashboard to create, launch and test applications in Anbox Cloud.

If you are interested in more advanced use cases, check out the [Getting started with Anbox Cloud (CLI)](https://discourse.ubuntu.com/t/getting-started/17756) tutorial to learn how to use Anbox Cloud from the command line.

Also see the documentation about [how to manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) and [how to work with containers](https://discourse.ubuntu.com/t/work-with-containers/24335).
