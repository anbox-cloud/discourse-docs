Anbox Cloud allows you to stream the whole Android experience next to just individual applications. The following sections will show how to setup such a virtual Android device experience on top of an existing Anbox Cloud deployment.

## Create an Application for the Virtual Device

In order to create a virtual device experience we first have to create an application with AMS. This application will not contain any APK and with that will start directly into the Android system launcher and provide the full Android experience.

A very simple application manifest for such an application looks like this:

```
name: vdev
instance-type: a4.3
```

[note type="information" status="Note"]If you want to use a GPU for containers created for you new `vdev` application, use an [instance type](https://discourse.ubuntu.com/t/instances-types-reference/17764) with GPU support like `g4.3`.[/note]

## Extend the Application with Addons

You can also extend the application with [addons](https://discourse.ubuntu.com/t/addons/25293) which install additional applications you want to offer as part of your default experience. You can for example replace the standard Android launcher with a custom one like [Lawnchair](https://lawnchair.app/).

1. Create the addon directory:

        mkdir -p vdev-support/hooks
        cd vdev-support

1. Download Lawnchair:

        curl -o lawnchair.apk https://f-droid.org/repo/ch.deletescape.lawnchair.plah_2001.apk

1. Create a `manifest.yaml` file in the `vdev-support` directory with the following content:

   ```
   name: vdev-support
   description: |
     Addon installing and configuring the Lawnchair launcher as the systems default one
   ```

1. Create a `pre-start` script file in the `hooks` directory with the following content:

   ```
   #!/bin/sh -ex
   exit 0
   ```

1. Create a `post-start` script file in the `hooks` directory with the following content:

   ```
   #!/bin/sh -ex
   if  [ "$CONTAINER_TYPE" = "regular" ]; then
     exit 0
   fi
   cp "$ADDON_DIR"/lawnchair.apk /var/lib/anbox/data/
   anbox-shell pm install -g -t /data/lawnchair.apk
   #
   # We need to wait until the system has settled after the package installation
   sleep 10
   #
   # Setup lawnchair as our default launcher
   LAUNCHER_ACTIVITY="ch.deletescape.lawnchair.plah/ch.deletescape.lawnchair.Launcher"
   anbox-shell cmd package set-home-activity "$LAUNCHER_ACTIVITY"
   #
   # Once we applied all of our changes we give Android a moment. If we directly
   # return here the Android container will be immediately shutdown.
   sleep 20
   ```

1. Make the script files executable:

        chmod +x hooks/*

1. Add the addon:

        amc addon add vdev-support .

Once the addon is uploaded to AMS, you can reference it from your application manifest:

```
name: vdev
instance-type: a4.3
addons: [vdev-support]
```

The application will now include the [Lawnchair](https://lawnchair.app/) and has it configured as the default system launcher.

## Launching the new Application

Now that we have the application created in AMS we can go ahead and stream it through the UI of the Anbox Stream Gateway (see [Getting started with Anbox Cloud (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958) for more details) or your own custom client application built with the [Anbox Streaming SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#streaming-sdk).

![Virtual device|690x662,100%](https://assets.ubuntu.com/v1/4cc5a115-application_virtual-device.png)
