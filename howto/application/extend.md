You can extend an application by adding an [addon](https://discourse.ubuntu.com/t/addons/25293) or [hooks](https://discourse.ubuntu.com/t/hooks/28555).

If your extension contains common functionality that you want to share among multiple applications, you should create an addon. You can then add the addon to all applications that should use the functionality.

If you want to extend one application only, use application hooks instead. They are easier to create and do not require creating an addon.

## Extend an application with addons

See [Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284) for detailed instructions.

## Extend an application with hooks

The following example shows how to use application hooks to change the Android system locale.

1. In a new `app` directory, create a `manifest.yaml` file with the following content:

   ```
   name: custom-locale
   instance-type: a2.3
   ```

1. Build the [CustomLocale](https://android.googlesource.com/platform/development/+/master/apps/CustomLocale) application from the AOSP project and move the compiled APK to the `app` folder.

1. Create the `hooks` directory next to the application manifest file:

        mkdir -p hooks

1. Create a `post-start` script file in the `hooks` directory with the following content:

   ```
   #!/bin/sh -ex
   if  [ "$CONTAINER_TYPE" = "regular" ]; then
     exit 0
   fi
   cp "$APP_DIR"/*.apk $ANDROID_ROOTFS/data
   anbox-shell pm install -t -g /data/CustomLocale.apk && sleep 5
   # Start CustomLocale2 application after installation, this aims to
   # initialize all available locales in the app, otherwise the following
   # system language broadcast won't work
   anbox-shell am start -n com.android.customlocale2/.CustomLocaleActivity && sleep 5
   # Change the system language by sending the broadcast to CustomLocale2
   anbox-shell am broadcast \
     -a com.android.intent.action.SET_LOCALE \
     --es com.android.intent.extra.LOCALE "ko_KR" \
     com.android.customlocale2
   sleep 5
   ```

1. Make the hooks executable:

        chmod +x hooks/*

   [note type="information" status="Tip"]Supported hooks are `pre-start`, `post-start` and `post-stop`. Read more about them [here](https://discourse.ubuntu.com/t/hooks/28555).[/note]


1. Then create the application in AMS:

        amc application create app

After the application is created successfully, launch a container, and you can see the system locale is changed to Korean.

[note type="information" status="Tip"]By default, the `CustomLocale` APK file is removed automatically from the application image after the [application bootstrap](https://anbox-cloud.io/docs/exp/applications#bootstrap) is completed. According to your application requirements, consider using the [`bootstrap.keep`](https://discourse.ubuntu.com/t/application-manifest/24197#bootstrap) attribute in the application manifest file if you want to keep any content needed by the application running in a regular container. [/note]
