This tutorial guides you through the first steps of using Anbox Cloud. You will learn how to create and access a virtual Android device or an application using the [web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871).

The web dashboard provides an easy-to use interface to Anbox Cloud. However, it currently supports a limited set of functionality, which means that it might not be sufficient for all use cases. If you want to learn how to manage Anbox Cloud from the command line, see the [Get started with Anbox Cloud (CLI)](https://discourse.ubuntu.com/t/getting-started/17756) tutorial.

[note type="information" status="Important"]
If you haven't installed Anbox Cloud or the Anbox Cloud Appliance yet, you must do so before you can continue with this tutorial. See the following documentation for installation instructions:

- [How to install the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702)
- [How to install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336) (note that you must install the streaming stack for the web dashboard to be available)
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
4. Keep the preselected instance type.
5. Select the Android image that you want to use, for example, `jammy:android13:arm64`.
6. Do not upload an APK file.
7. Click **Add Application**.

   ![Add a virtual device](https://assets.ubuntu.com/v1/8560991b-gs_dashboard_add_virtual_device.png)
8. You are redirected to the application view. Wait until the application status changes to `ready`.

## 2. Launch and test the virtual device

When the application has been initialised and its status changes to `ready`, complete the following steps to launch and test the virtual device:

1. In the list of applications, click the play button (labelled **New session**) in the **Actions** column for the application to start a new session.

   ![Start a new session](https://assets.ubuntu.com/v1/d6380c07-gs_dashboard_new_session.png)
2. Accept the default settings and click **New Session**.

   ![Start with default settings](https://assets.ubuntu.com/v1/b27e8be8-gs_dashboard_start_session.png)
3. When the stream has loaded, you can interact with your virtual device.

   ![Stream the virtual device](https://assets.ubuntu.com/v1/1d1fc6ef-gs_dashboard_streaming.png)

## 3. Create an application from an APK

To create an application for a specific Android app, follow the steps in [1. Create a virtual device](#virtual-device), but upload the APK of the Android app.

[note type="information" status="Important"]Not all Android apps are compatible with Anbox Cloud. See [How to port Android apps](https://discourse.ubuntu.com/t/port-android-apps/17776) for more information.[/note]

Choose an [instance type](https://discourse.ubuntu.com/t/instances-types-reference/17764) that is suitable for your application. If your instance is equipped with a GPU and your application requires the use of the GPU for rendering and video encoding, select an instance type with GPU support like `g4.3`. For other instance types, the container will use a GPU if available or software encoding otherwise.

![Add an application](https://assets.ubuntu.com/v1/2ccd2c00-gs_dashboard_add_application.png)

You can launch and test the application in the same way as you did for the virtual device.

## 4. Update an application

You can have several versions of an application. See [How to update an application](https://discourse.ubuntu.com/t/update-an-application/24201) for detailed information.

Complete the following steps to add a new version to your application:

1. Open `https://<your-machine-address>/applications` in your browser.
2. Click the **Edit application** button  in the **Actions** column next to the application for which you want to add a new version.

   ![Update an application](https://assets.ubuntu.com/v1/7365d305-gs_dashboard_edit_application.png)
3. Upload a new APK, or do other changes to the configuration.
4. Click **Update application**.

## 5. Delete an application

While following this tutorial, you created several applications. You can see them in the application view at `https://<your-machine-address>/applications`.

To delete an application, click the **Delete application** button in the **Actions** column and confirm the deletion.

![Delete an application](https://assets.ubuntu.com/v1/584a5f70-gs_dashboard_delete_application.png)

[note type="information" status="Tip"]
To skip the confirmation window, hold **Shift** when clicking the **Delete application** button.
[/note]

## 6. Inspect containers

Every time you start a session for an application, Anbox Cloud creates a container. The container keeps running even if you exit the stream, until you either stop the session by clicking **Stop session** or delete the container.

You can see all containers in the container view at `https://<your-machine-address>/containers`.

![Container view](https://assets.ubuntu.com/v1/55b5f36f-gs_dashboard_containers.png)

Complete the following steps to inspect a container:

1. Click on the ID of one of the running containers to see detailed information for the container.

   ![Container information](https://assets.ubuntu.com/v1/60de9b54-gs_dashboard_container_overview.png)
1. Switch to the **Terminal** tab. You will see a terminal for the Linux container that runs the Android container.

   You can run commands in the Linux container, or you can enter `anbox-shell` to access the nested Android container (enter `exit` to go back to the Linux container).

   ![Use the container terminal](https://assets.ubuntu.com/v1/286a95da-gs_dashboard_container_terminal.png)
1. Switch to the **Logs** tab. You will not see any logs, because log files are available only for containers that are in an error state, not for running containers.

   To simulate a failure for the container, switch to the **Terminal** tab and enter the following command:

        amsctl notify-status error --message="My error message"

   Go back to the container overview, and when the container status changes to **error**, click on the container ID and switch to the **Logs** tab. You can now see the error logs for the container.

   ![Container logs](https://assets.ubuntu.com/v1/5ee5624c-gs_dashboard_container_logs.png)

## Done!

You now know how to use the web dashboard to create, launch and test applications in Anbox Cloud.

If you are interested in more advanced use cases, check out the [Get started with Anbox Cloud (CLI)](https://discourse.ubuntu.com/t/getting-started/17756) tutorial to learn how to use Anbox Cloud from the command line.

Also see the documentation about [How to manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) and [How to work with containers](https://discourse.ubuntu.com/t/work-with-containers/24335).
