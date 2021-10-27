An application manifest defines the various attributes of an application.

The available attributes are listed in the following table:

Name          | Value type | Description
--------------|------------|-------------------------
`name`          | string     | Verbose name of the application. The following special characters are not allowed: `< > : " / \ &#124; ? *`, as well as space
`version`       | string     | Version to encode with the application. Maximum length is 50 characters.
`instance-type` | string     | Container instance type that all containers created for the application will use.
`required-permissions` | array of strings | List of permissions to automatically grant to the application. See [Android Permissions](https://developer.android.com/guide/topics/permissions/overview) for a list of available permissions. If `[*]` was given, all required runtime permissions for the application will be granted on application installation.
`image` (optional) | string     | Name or ID of an image to be used for the application. The default image is used if empty.
`addons` (optional) | array      | List of addons to be installed during the application bootstrap process.
`tags` (optional) | array      | List of tags to be associated with the application.
`boot-package` (optional) | string     | Package to launch once the system has booted (default: package name retrieved from the APK if APK file is present).
`boot-activity` (optional) | string     | Activity of boot package to launch once the system has booted (default: main activity as defined in the application manifest).
`video-encoder` (optional) | string     | Video encoder to be used by a container launched from the application  (default: gpu-preferred). Possible values are: gpu, gpu-preferred, software
`watchdog` (optional)    | map        | Watchdog settings to be configured on application installation.
`services` (optional)    | array      | Services to be provided from the installed application.
`resources` (optional)   | map        | Resources to be allocated on application installation.
`extra-data` (optional)  | array      | List of additional data to be installed on application installation.

## Image

The `image` attribute defines which image the application is based on. If left empty, your application is based on the default image. See [Manage images](https://discourse.ubuntu.com/t/managing-images/17758) for more details on this. Available images on your installation can be listed with the following command:

    amc image list

<a name="video-encoder"></a>
## Video encoder
A video encoder type can be specified through the `video-encoder` field in the manifest file when creating an application, so that a container launched from the application can use a GPU or software video encoder according to different scenarios.

Name                     |  Description
-------------------------|-------------------------
`gpu`                      |  A GPU-based video encoder
`gpu-preferred`  |  A GPU-based video encoder if GPU slots are not used up, otherwise, fall back to use a software-based video encoder
`software`            |  A software-based video encoder

When `gpu` video encoder is specified in the manifest, AMS can fail to create an application if:
 - All GPU slots are used up by running containers.
 - There is no GPU support across the entire LXD cluster.

<a name="watchdog"></a>
## Watchdog settings

The `watchdog` attribute includes the following field definitions:

Name                     | Value type | Description
-------------------------|------------|-------------------------
`disabled`               | Boolean    | Toggle application watchdog on or off (default: false)
`allowed-packages`       | array of strings | Besides the boot package, list of packages to be allowed to display in the foreground

When a container is launched, Anbox enables an application watchdog by default for the installed package unless it's disabled explicitly with:

```yaml
name: candy
instance-type: a2.3
image: default
watchdog:
  disabled: true
```

If one of the following scenarios occurs, the watchdog will be triggered. The container will be terminated and ends up with `error` status.

- The application crashes or an [ANR](https://developer.android.com/topic/performance/vitals/anr) is triggered.
- The application is not in the foreground when an application which is not listed in `allowed-packages` was brought to the foreground and gained the focus.
- The boot package or activity is invalid.
- One of the `allowed-packages` is invalid.

The rules forbid launching another activity, not part of the installed package or listed allowed packages. Launching activities of the same package is allowed.

Supplying `['*']` to the `allowed-packages` when the watchdog is enabled allows any application to be displayed in the foreground without triggering a watchdog.

## Services

A container launched from the installed application can expose `services` you want to make accessible from outside the container. You must define the following properties for each service:

Name           | Value type | Description
---------------|------------|-------------------------
`name`         | string     | Name of service
`port`         | integer    | Port number to be exposed by the service
`protocols`    | array of strings | Protocols to be used by the service (Possible values are: tcp, udp)
`expose`       | Boolean    | Expose service to be accessible externally or internally

<a name="resources"></a>
## Resources

If the [`instance-type`](https://discourse.ubuntu.com/t/instances-types-reference/17764) that is provided by AMS doesn't meet the criteria that the installed application requires to function, you can use the `resources` directive to override the predefined resources.

Name           | Value type | Minimum value  | Description
---------------|------------|----------------|-------------------------
`cpus`         | integer    |     1          | Number of vCPU cores
`memory`       | string     |     3 GB       | Memory to be assigned to the application
`disk-size`    | string     |     3 GB       | Disk size to be assigned to the application
`gpu-slots`(optional) | integer |     0      | Number of GPU slots to be assigned to the application

In the following application manifest file, the application is created with `a2.3` instance type, which will be assigned 2 vCPU cores, 3 GB of memory and a disk size of 3 GB. With the following resources defined in the manifest file, the allocated memory and disk size will end up at 4 GB and 8 GB, respectively, on application installation, and the number of vCPU cores remains the same:

```yaml
name: candy
instance-type: a2.3
resources:
  memory: 4GB
  disk-size: 8GB
```

If all required fields (`cpus`/`memory`/`disk-size`) of `resources` are supplied in the application manifest, the `instance-type` field is no longer needed. Even if the `instance-type` field is provided, it will be overridden by the requirements in the `resources` fields upon application installation.

## Extra data

Some Android applications which contain large program assets such as graphics or media files use so-called [OBB](https://developer.android.com/google/play/expansion-files) files to store additional data. These data files are separated from the APK and saved onto the external or internal SD card of an Android device. The `extra-data` field can be used in this case to install an APK with separated OBB files or any other additional data into the Android system.

Each item of `extra-data` should be declared as follows:

```yaml
<name>:
    target: <target-path>
    owner:  <uid>:<gid> # optional
    permissions: <file-permission> # optional
```

The fields have the following purpose:

Name                     | Value type | Description
-------------------------|------------|-------------------------
`name`                   | string     | Name of file or directory to be installed into the Android file system
`target-path`            | string     | Target location for the file or directory
`owner` (optional)       | string     | Owner assigned to the target file or directory in the Android file system
`permissions` (optional) | string     | Permissions assigned to the target file or directory in the Android file system

`permissions` represents [Linux file permissions](https://en.wikipedia.org/wiki/File_system_permissions) in octal notation.

It's recommended to let Anbox choose the right values for `owner` and `permissions` instead of manually providing them. If `owner` and `permissions` are not specified, the following default values will be used:

Name          | App data installation directory | Type | Value
--------------|---------------------------------|------|--------
|`owner`       | sdcard      | File | package_uid:sdcard_rw
|              | sdcard      | Dir  | package_uid:sdcard_rw
|              | system data | File | package_uid:package_gid
|             | system data | Dir  | package_uid:package_gid
|`permissions` | sdcard      | File | 0660
|              | sdcard      | Dir  | 0771
|              | system data | File | 0660
|              | system data | Dir  | boot package folder -> 0700, nested folders of boot package folder -> 0770

Each item (file or folder) declared in the `extra-data` field of the manifest yaml file should be placed in a directory called `extra-data`.

For security reasons, the target location of the files and directories listed in the `extra-data` section is restricted to a few specific locations in the Android file system. These are:

* `/sdcard/Android/obb/<apk-package-name>`
* `/sdcard/Android/data/<apk-package-name>`
* `/data/app/<apk-package-name>`
* `/data/data/<apk-package-name>`

The manifest and extra data in our example are placed next to the application package, which must be named **app.apk**:

```bash
$ tree
.
├── app.apk
├── extra-data
│   ├── com.canonical.candy.obb
│   └── game-data-folder
│       └── data.bin
└── manifest.yaml
```
