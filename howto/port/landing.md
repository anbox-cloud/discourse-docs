When porting an Android app to Anbox Cloud (usually in the form of an APK), there are a few issues that might cause your app to not function properly:

* Missing dependencies, most importantly to Google Play services. Google Play services are not supported by Anbox Cloud, and apps that require Google Play services can therefore not be ported to Anbox Cloud.
* Missing runtime permissions. See [Grant runtime permissions](tbd) for instructions on how to grant the required permissions.
* Mismatched architecture. See [Choose APK architecture](tbd) for information on which architecture you should choose.
* App size. See [Port APKs with OBB files](tbd) for instructions on how to port large APKs.
* Strict watchdog restrictions. See [Configure the watchdog](tbd) if you want to turn the watchdog off for debugging or configure it to not trigger for specific apps.
