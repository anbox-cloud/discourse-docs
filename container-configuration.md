Anbox Cloud enables you to configure a container in a variety of ways.

## Geographical Location

Anbox Cloud allows specifying a static geographical location which is provided to the Android container.  The location is configured in the file `/var/lib/anbox/static_gps_position` within the Anbox container.

The location data is constructed in the following format:

```
<Latitude>,<Latitude in hemisphere>,<Longitude>,<Longitude in hemisphere>
```

For example:

    4807.038,N,1131.001,E

You can find details about the different parts of the location in the following table.

Field                   | Value type | Description
------------------------|------------|-------------------------------------------------------------------
Latitude                | float      | In the format of ddmm.mm (d refers to degrees, m refers to minutes). For example: 4807.038 = 48 degrees 7.038 minutes
Latitude in hemisphere  | char       | Latitude hemisphere `N` (northern hemisphere) or `S` (southern hemisphere)
Longitude               | float      | In the format of ddmm.mm (d refers to degrees, m refers to minutes). For example: 1131.001 = 11 degrees 31.001 minutes
Longitude in hemisphere | char       | hemisphere `E` (east longitude) or `W` (west longitude)

To make the file `/var/lib/anbox/static_gps_position` available to Android container, you can create a file that contains GPS data with the above format and move that file from `ADDON_DIR` to `/var/lib/anbox/static_gps_position` via an [addon install hook](https://discourse.ubuntu.com/t/managing-addons/17759#heading--build-your-own-addon) during its installation time. Then when Android container gets started and an application requests the current location information through Android framework, the GPS data will be forwarded from Anbox session to the application.


<h2 id='heading--backup-and-restore'>Backup and Restore Application Data</h2>

Backup and restoration of application data can be achieved easily with the `aam`  (Anbox Application Manager) utility helper installed in the image. The `aam` can bundle any necessary application data together into a tarball file or uncompress the tarball file to a particular application folder according to the specified package name.

For example, if you want to backup user data of a particular application with `aam` and upload the resulting tarball file to the cloud storage service when a container is stopped, in an [addon backup hook](https://discourse.ubuntu.com/t/managing-addons/17759#heading--backup-and-restore), you can:

```bash
 #!/bin/sh -ex
aam backup com.canonical.candy
TARBALL_FILE=$(basename $(find ./ -name *.tar.bz2))
 # Upload the tarball to public or private cloud storage service
curl -i -X POST --data-binary @"${TARBALL_FILE}" <cloud_storage_upload_url>
```

If [`boot-package`](https://discourse.ubuntu.com/t/managing-applications/17760#heading--create-applications) can be retrieved from apk file or specified in the application manifest file, you can also backup the boot application data simply with the flag `--boot-package`.

```bash
$ aam backup --boot-package
```

`aam` will automatically query the boot package name from the container and backup the relevant application data. As result `aam` will create a tarball file with the name `<package name>.tar.bz2`.

The application data can be restored with the following [restore hook](https://discourse.ubuntu.com/t/managing-addons/17759#heading--backup-and-restore) when a container is up and running:

```bash
#!/bin/sh -ex
# Download the tarball from public or private cloud storage service
if curl -o app-data.tar.bz2 <cloud_storage_download_url> ; then
  aam restore -p app-data.tar.bz2 com.canonical.candy
fi
```

or by relying on the boot package of the container:

```bash
$ aam restore -p app-data.tar.bz2 --boot-package
```

Sometimes, not every piece of data is useful (E.g. cache) and backing up the entire application data takes long time and occupies more disk space if the application data is large. `aam` supports two filters to backup files that match wildcards patterns:

 Filter      |  Description
-------------|--------------------------------------------------------------------
`include`    | Include files in resulting tarball with a wildcard
`exclude`    | Exclude files in resulting tarball with a wildcard

Please refer to the pattern syntax [here](https://golang.org/pkg/path/filepath/#Match)

For example, with the following filters:

```bash
$ aam backup com.canonical.candy \
     --include=/data/data/com.canonical.candy/cache/*.db \
     --include=/data/data/com.canonical.candy/new_level/fixture* \
     --exclude=/sdcard/Android/data/com.canonical.candy/user_data/*.jpeg \
     --exclude=/data/data/com.canonical.candy/new_level/*.cfg"
```

The resulting tarball file will include the following files:

- Files with *db* suffix below the folder /data/data/com.canonical.candy/cache
- Files with *fixture* prefix below the folder /data/data/com.canonical.candy/new_level

And exclude the following files:

* Files with *jpeg* suffix below the folder /sdcard/Android/data/com.canonical.candy/user_data
* Files with *cfg* suffix below the folder /data/data/com.canonical.candy/new_level
