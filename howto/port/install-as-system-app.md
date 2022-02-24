Normally, a user app is signed by the developer and restricted to fewer permissions at runtime while a system app is usually [signed with the platform key](https://source.android.com/devices/tech/ota/sign_builds) when building an Android image, it's pre-installed under the system partition and running a process with some ["signature" protection level permissions](https://developer.android.com/guide/topics/manifest/permission-element.html#plevel) in Android container. An application must be running as a system app if it

- requires to access Android hidden APIs
- gains some signature protection level permissions

Anbox Cloud allows a user app to be installed as a system app in Android container. This can be done by

1. create an addon
2. call the `aam install-system-app` command in the `pre-start` hook of the addon
3. include the addon in an application after adding it to AMS
4. enable `allow_custom_system_signatures` feature in application manifest file
5. create the application

Then you will have the APK installed as system app in Android container after the application is created successfully.

### Make a system app
To be a system app running a process with system privileges, you must add the attribute `android:sharedUserId="android.uid.system"` into the `<manifest>` tag in the AndroidManifest.xml file of your Android application.

```xml
...
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="<package_name>"
    android:sharedUserId="android.uid.system">
...
```

Then build and sign the application alongside with other Android applications when building your Android image or sign it with [Android Studio](https://developer.android.com/studio/publish/app-signing). For the latter, the system platform key is not required and you can use the keys that are generated from Android Studio to sign the application.

### Create an addon

By creating an addon and invoking the `aam install-system-app` command in a `pre-start` hook, the signed APK can be installed as a system app in the Android container.

Following the [tutorial](https://discourse.ubuntu.com/t/creating-an-addon/25284) and create the basic layout of an addon, which has a manifest.yaml file and hooks folder prepared in advance. Assumed that the APK file is named `app.apk`, place the APK into the addon folder and create a `pre-start` hook with the following content.

```bash
#!/bin/bash -ex

# Only install the APK as a system app when bootstrapping an application.
if  [ "$CONTAINER_TYPE" = "regular" ]; then
  exit 0
fi

aam install-system-app \
  --apk="${ADDON_DIR}"/app.apk \
  --permissions=<comma separated permissions list the appliation requires>  \
  --package-name=<package_name>
```

The value to the `package_name` parameter must match the one defined in the AndroidManifest.xml file of the Android project, so must the `permissions` parameter. If the application requires to access Android hidden apis to function, you need to addd `--access-hidden-api` parameter to the above command. Use `aam install-system-app --help` for more details about this command.

And the final layout of this addon is as follows:

```bash
.
├── app.apk
├── hooks
│   └── pre-start
└── manifest.yaml
```

Add this addon to the AMS with the following command:

```bash
amc addon add install-sys-app .
```

### Include this addon to an application

To use this addon in an application, include the addon name under the `addons` in the application manifest file when creating an application. Beside this, you need to enable the feature `allow_custom_system_signatures` as well. This ensures that the command `aam install-sys-app` that is invoked in the `pre-start` hook of this addon works properly.
```yaml
...
addons: [ install-sys-app ]
features: [ allow_custom_system_signatures ]
...
```

Create the application afterward with `amc` command
```bash
amc application create .
```

After the AMS application is created successfully, the APK is installed as a system app properly. The Android app will run as a system app in the Android container when you start it from a container launched from the newly created application.
