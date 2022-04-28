When porting an Android app to Anbox Cloud (usually in the form of an APK), there are a few issues that might cause your app to not function properly:

* Missing dependencies, most importantly to Google Play services. Google Play services are not supported by Anbox Cloud, and apps that require Google Play services can therefore not be ported to Anbox Cloud.
* Missing runtime permissions. See [How to grant runtime permissions](https://discourse.ubuntu.com/t/grant-runtime-permissions/26054) for instructions on how to grant the required permissions.
* Mismatched architecture. See [How to choose APK architecture](https://discourse.ubuntu.com/t/choose-apk-architecture/26055) for information on which architecture you should choose.
* App size. See [How to port APKs with OBB files](https://discourse.ubuntu.com/t/port-apks-with-obb-files/26056) for instructions on how to port large APKs.
* Strict watchdog restrictions. See [How to configure the watchdog](https://discourse.ubuntu.com/t/configure-the-watchdog/26057) if you want to turn the watchdog off for debugging or configure it to not trigger for specific apps.
* Install an APK as a system app. See [How to install an APK as a system app](https://discourse.ubuntu.com/t/install-an-apk-as-a-system-app/27086) if you want to install a user app as a system app running in an Android container.
