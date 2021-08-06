Applications are one of the main objects AMS manages. A single application encapsulates one Android application and manages it within the cluster. It takes care about installing the supplied application package ([Android Package Kit - APK](https://en.wikipedia.org/wiki/Android_application_package)), to make it available to users. Further AMS manages updates to existing applications which includes allowing the operator to give new uploaded versions a test run before making them available to any users.

## Application Requirements
In order to run on the Anbox Cloud platform applications need to fulfill a set of requirements. These are:

* Application  **SHOULD**  not download any additional resources on regular startup to contribute to short startup times. If additional resources need to be downloaded this can be done during the application bootstrap phase.
* Application  **MUST NOT**  require the **Google Play services** to be available as Anbox Cloud does not include them.

If the application fulfils all of the requirements above it is ready to run on the Anbox Cloud platform. If not, please file a [bug report](https://bugs.launchpad.net/indore-extern/+filebug) so that we can find out what we can do to still support the application.

<h2 id='heading--create-applications'> Create Applications</h2>

Every application which should be available on an Anbox Cloud cluster has to be created first. The internal process will prepare a container based on the currently available image with the application package installed and will use that for any newly launched containers to support fast boot times.

### Preparation

To create an application a Android package (APK) is needed with support for the target architecture. Additionally one of the available instance types has to be selected for the application which defines CPU/RAM constraints put onto the container launch for the application.

> **Note:** See chapter [Available Instance Types](https://discourse.ubuntu.com/t/instances-types-reference/17764) for a list of available instance types.

In order to create a new application a manifest file has to be written first to define the various attributes the new application should have. The manifest is a simple [YAML](http://yaml.org/) file and looks like this:

```yaml
name: candy
instance-type: a2.3
image: default
boot-activity: com.canonical.candy.GameApp
required-permissions:
  - android.permission.WRITE_EXTERNAL_STORAGE
  - android.permission.READ_EXTERNAL_STORAGE
addons:
  - ssh
tags:
  - game
extra-data:
  com.canonical.candy.obb:
    target: /data/app/com.canonical.candy-1/lib
  game-data-folder:
    target: /sdcard/Android/data/com.canonical.candy/
watchdog:
  disabled: false
  allowed-packages:
    - com.android.settings
services:
  - name: adb
    port: 5559
    protocols: [tcp]
    expose: false
resources:
  memory: 4GB
  disk-size: 8GB
```

The available attributes are listed in the following table:

Name          | Value type | Description
--------------|------------|-------------------------
`name`          | string     | Verbose name of the application, A few special characters are not allowed: '< > : " / \ &#124; ? *', as well as space
`version`       | string     | Version to encode with the application. Maximum length is 50 characters
`instance-type` | string     | Container instance type all containers created for the application will use
`required-permissions` | array of strings | List of permissions to automatically grant to the application. See [Android Permissions](https://developer.android.com/guide/topics/permissions/overview) for a list of available permissions. If `[*]` was given, all required runtime permissions for the application will be granted on application installation
`image` (optional) | string     | Name or ID of an image to be use for the application. Default image is used if empty
`addons` (optional) | array      | List of addons to be installed during the application bootstrap process
`tags` (optional) | array      | List of tags to be associated with the application
`boot-package` (optional) | string     | Package to launch once the system has booted (default: package name retrieved from the apk if apk file is present)
`boot-activity` (optional) | string     | Activity of boot package to launch once the system has booted (default: Main activity as defined in the application manifest)
`video-encoder` (optional) | string     | Video encoder to be used by a container launched from the application  (default: gpu-preferred). Possible values are: gpu, gpu-preferred, software
`watchdog` (optional)    | map        | Watchdog settings to be configured on application installation
`services` (optional)    | array      | Services to be provided from the installed application
`resources` (optional)   | map        | Resources to be allocated on application installation
`extra-data` (optional)  | array      | List of additional data to be installed on application installation

#### Video Encoder
A video encoder type can be specified through `video-encoder` field in the manifest file when creating an application so that a container launched from the application can use a GPU or software video encoder according to different scenarios.

Name                     |  Description
-------------------------|-------------------------
`gpu`                      |  a GPU-based video encoder
`gpu-preferred`  |  a GPU-based video encoder if gpu slots are not used up, otherwise it fallbacks to use software-based video encoder
`software`            |  a software-based video encoder

When `gpu` video encoder is specified in the manifest, AMS can fail to create an application if
 - GPU slots are used up by running containers
 - No GPU support across the entire lxd cluster

#### Watchdog Settings

The `watchdog` attribute includes the following field definitions:

Name                     | Value type | Description
-------------------------|------------|-------------------------
`disabled`               | boolean    | Toggle application watchdog on or off (default: false)
`allowed-packages`       | array of strings | Besides boot package, list of packages to be allowed to display in the foreground
When a container is launched, Anbox enables an application watchdog by default for the installed
package unless it's disabled explicitly with:

```yaml
name: candy
instance-type: a2.3
image: default
watchdog:
  disabled: true
```

If one of the following scenarios occurs, the watchdog will be triggered. The container will be terminated and ends up with `error` status.

- The application crashes or an [ANR](https://developer.android.com/topic/performance/vitals/anr) is triggered
- The application is not in the foreground when an application which is not listed in `allowed-packages`
 was brought into the in the foreground and gained the focus
- The boot package or activity is invalid
- One of the `allowed-packages` is invalid

The rules forbid launching another activity, not part of the installed package or listed allowed packages. Launching activities of the same package is allowed.

Supplying `['*']` to the `allowed-packages` when the watchdog is enabled allows any application
can be display in the foreground without triggering a watchdog.

#### Services

A container launched from the installed application can expose `services` you want to make accessible from outside the container. You must define the following properties for each service.

Name           | Value type | Description
---------------|------------|-------------------------
`name`         | string     | Name of service
`port`         | integer    | Port number to be exposed by the service
`protocols`    | array of strings | Protocols to be used by the service (Possible values are: tcp, udp)
`expose`       | boolean    | Expose service to be accessible externally or internally

#### Resources

If the [`instance-type`](https://discourse.ubuntu.com/t/instances-types-reference/17764) that is provided by AMS doesn't meet the criteria that the installed application requires to function, you can make use of `resources` directive to override the predefined resources in instance-type.

Name           | Value type | Minimum value  | Description
---------------|------------|----------------|-------------------------
`cpus`         | integer    |     1          | Number of vcpu cores
`memory`       | string     |     3GB        | Memory to be assigned to the application
`disk-size`    | string     |     3GB        | Disk size to be assigned to the application
`gpu-slots`(optional) | integer |     0      | number of gpu slots to be assigned to the application

In the following application manifest file, the application is created with `a2.3` instance-type, which will be assgined 2 vcpu cores, 3GB memory and 3GB disk size. With the following resources supplied to manifest file:

```yaml
name: candy
instance-type: a2.3
resources:
  memory: 4GB
  disk-size: 8GB
```

The allocated memory and disk size will end up to 4GB and 8GB respectively on application installation and the number of vcpu cores remains the same. If all required fields(`cpus`/`memory`/`disk-size`) of resources are supplied in the application manifest, the `instance-type` field is no longer needed. Even if the `instance-type` field is provided, it will be overridden by `resources` in the end upon application installation.

#### <h4 id='heading--extra-data'>Extra Data </h4>

Some Android applications which contain large program assets such as graphics, media files use so called [OBB](https://developer.android.com/google/play/expansion-files) files to store additional data. These data files are separated from the APK and saved onto the external or internal SD card of an Android device. The `extra-data` field can be used in this case to install an APK with separated OBB files or any other additional data into the Android system.

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
`name`                   | string     | Name of file or directory to be installed into the Android filesystem
`target-path`            | string     | Target location for the file or directory
`owner` (optional)       | string     | Owner assigned to the target file or directory in the Android filesystem
`permissions` (optional) | string     | Permissions assigned to the target file or directory in the Android filesystem

`permissions` represents [Linux file permissions](https://en.wikipedia.org/wiki/File_system_permissions) in octal notation.

It's recommended to let Anbox choose the right values for `owner` and `permissions` instead of manually providing them. If `owner` and `permissions` are not specified, the following default values will be used:

Name          | App Data Installation Directory | Type | Value
--------------|---------------------------------|------|--------
|`owner`       | sdcard      | File | package_uid:sdcard_rw
|              | sdcard      | Dir  | package_uid:sdcard_rw
|              | system data | File | package_uid:package_gid
|             | system data | Dir  | package_uid:package_gid
|`permissions` | sdcard      | File | 0660
|              | sdcard      | Dir  | 0771
|              | system data | File | 0660
|              | system data | Dir  | boot package folder -> 0700, nested folders of boot package folder -> 0770

Each item, e.g. file or folder, declared in the `extra-data` field of the manifest yaml file should be placed in a directory called `extra-data`.

For security reasons, the target location of the files and directories listed in the `extra-data` section is restricted to a few specific locations in the Android file system. These are:

* `/sdcard/Android/obb/<apk-package-name>`
* `/sdcard/Android/data/<apk-package-name>`
* `/data/app/<apk-package-name>`
* `/data/data/<apk-package-name>`

The `image` attribute defines which image the application is based on. If left empty, your application will be based on the default image. See [Image Management](https://discourse.ubuntu.com/t/managing-images/17758) for more details on this. Available images on your installation can be listed with the following command:

```bash
$ amc image list
```

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

### From a Directory

When creating an application from the folder path, the location should contain the required components for the creation.

* `manifest.yaml`
* `app.apk`
* `extra-data` (optional)

With everything in place the application can now be created:

```bash
$ amc application create <path/to/application-content>
applications:
- bcmap7u5nof07arqa2ag
```

When the `create` command returns the application package is uploaded to the AMS service and the bootstrap process was started. The application is not yet ready to be used. You can watch the status of the application with the following command:

```bash
$ amc application show bcmap7u5nof07arqa2ag
id: bcmap7u5nof07arqa2ag
name: candy
status: initializing
published: false
config:
  instance-type: a2.3
  boot-package: com.canonical.candy
versions:
  0:
    image: bf7u4cqkv5sg5jd5b2k0 (version 0)
    published: false
    status: initializing
    addons:
    - ssh
    boot-activity: com.canonical.candy.GameApp
    required-permissions:
    - android.permission.WRITE_EXTERNAL_STORAGE
    - android.permission.READ_EXTERNAL_STORAGE
    extra-data:
      com.canonical.candy.obb:
        target: /data/app/com.canonical.candy-1/lib
      game-data-folder:
        target: /sdcard/Android/data/com.canonical.candy/
    watchdog:
      disabled: false
      allowed-packages:
      - com.android.settings
    services:
    - port: 5559
      protocols:
      - tcp
      expose: false
      name: adb
resources:
  memory: 4GB
  disk-size: 8GB
```

Once the status of the application switches to `ready` the application is ready and can be used.

### From a Tarball

An application can be also created from a tarball file. The tarball file has to be compressed with bzip2 and must follow the format of the application package as described before.

For example, a tarball can be created with:

```bash
$ tar cvjf foo.tar.bz2 -C <package-folder-path> app.apk extra-data manifest.yaml
```

Once the tarball is created you can proceed creating the application:

```bash
$ amc application create foo.tar.bz2
applications:
- bcmap7u5nof07arqa2ag
```

The AMS service now starts the application bootstrap process as described before.

> **Note:** Due to Snap strict confinement, no matter which approach you're going to take,  the folder or tarball file must be located home directory

### Bootstrap process

Whenever creating an application either from a directory or a tarball, AMS will perform a bootstrap process, which builds the application and synchronizes it across all LXD nodes in the cluster. There are major benefits the bootstrap process provides:

  * It enables AMS to launch a container for an application without installing the APK everytime
  * It dramatically speeds up startup time of a regular container

Furthermore an application is synchronized within the LXD cluster, which enables AMS continuing to work when nodes are being remove from the cluster through [Node Management] or lost from the cluster unexpectedly.

A temporary base container will be created and used for the bootstrapping during the application creation:

```bash
$ amc application create foo.tar.bz2
applications:
- bq789q0j1qm02cebmoeg
$ amc ls
+----------------------+-------------+------+----------+------+---------------+-----------+
|          ID          | APPLICATION | TYPE |  STATUS  | NODE |    ADDRESS    | ENDPOINTS |
+----------------------+-------------+------+----------+------+---------------+-----------+
| bq78a3oj1qm02cebmof0 |    candy    | base | prepared | lxd0 | 192.168.100.2 |           |
+----------------------+-------------+------+----------+------+---------------+-----------+
```

In general, the bootstrap process goes through the following steps in order:

![application-bootstrap|690x467](upload://haAJJ8p8ZEQXmsvrVb3HOHhl1io.png)

  * Configure network interface and gateway
  * Apply any pending Ubuntu system security updates
  * Install [addons](https://discourse.ubuntu.com/t/managing-addons/17759) via the `install` hook provided by each addon listed in the application manifest file
  * Launch Android container
  * Install the APK provided by the application
  * Grant the application permissions as requested in the application manifest
  * Install the extra data as listed in the application manifest
  * Execute the `prepare` hook provided by each addon listed in the application manifest

If one of the steps fails, AMS will interrupt the bootstrap process and make the entire process fail. As a result, the status of base container will be marked with `error` and the application's status will end up with `error` as well.

> **Note:** An application crash or ANR upon APK installation will cause the bootstrap process to terminate abnormally and the status of application is set to `error` too.

When a base container runs into an error status, you can see what has gone wrong there by checking the error message with:

```bash
$ amc show bq78a3oj1qm02cebmof0
id: bq78a3oj1qm02cebmof0
name: ams-bq78a3oj1qm02cebmof0
status: error
node: lxd0
created_at: 2019-08-09T02:11:33Z
application:
    id: bq6ktjgj1qm027q585kg
network:
    address: ""
    public_address: ""
    services: []
stored_logs:
- container.log
- system.log
- android.log
error_message: 'Failed to install application: com.foo.bar: Failed to extract native libraries, res=-113'
config: {}
```

Or [show container logs](https://discourse.ubuntu.com/t/managing-containers/17763#heading--show-container-logs) which is useful for troubleshooting problems in a container.

If an application bootstrap succeeds, the base container will be automatically removed and the status of the application changes to `ready` and is ready to be used.

## Wait for Applications

With `amc wait` command, it enables to wait for an application to reach a specific condition. If the condition is not satisfied within the specified time (5 minutes by default), a timeout error will be returned by AMS.

The supported conditions for an application are as follows:

Name            |  Value
----------------|------------
`instance-type` |  Supported instance type. See chapter [Available Instance Types](https://discourse.ubuntu.com/t/instances-types-reference/17764) for a list of available instance types
`addons`        |  Comma separated list of addons
`tag`           |  Application tag name
`publishd`      |  "true" or "false" which indicates if the application is published
`immutable`     |  "true" or "false" which indicates if the application is changeable
`status`        |  Application status, possible values: "error", "unknown", "initializing", "ready", "deleted"

One example of using `amc wait` command is to wait for the application bootstrap to be done since
the application bootstrap is performed asynchronously by the AMS service and takes some time to
process. The application can not be used until the bootstrap is complete and the status is marked
as `ready`.

```bash
$ amc wait -c status=ready bcmap7u5nof07arqa2ag
```


## Update Applications

Updating an existing application works similar as creating a new one. Each time an existing application is updated it is extended with a new version. All versions an application currently has are individually usable but only one can be available to users.

When you want to update an existing application with a new manifest or APK, you have to provide both in the same format as when the application was created. The `amc application update` command accepts both a directory and an absolute file path

From a path:

    amc application update bcmap7u5nof07arqa2ag $PWD/foo

From a file:

    amc application update bcmap7u5nof07arqa2ag foo.tar.bz2

AMS will start the update process internally. You can watch the status of the new version with the following command:

    amc application show bcmap7u5nof07arqa2ag

The output will show you detailed information about the application and all of its versions:

```bash
id: bcmap7u5nof07arqa2ag
name: candy
status: ready
published: false
config:
  instance-type: a2.3
  boot-package: com.canonical.candy
versions:
  0:
    image: bf7u4cqkv5sg5jd5b2k0 (version 0)
    published: false
    status: active
    addons:
    - ssh
    boot-activity: com.canonical.candy.GameApp
    required-permissions:
    - android.permission.WRITE_EXTERNAL_STORAGE
    - android.permission.READ_EXTERNAL_STORAGE
    extra-data:
      com.canonical.candy.obb:
        target: /data/app/com.canonical.candy-1/lib
      game-data-folder:
        target: /sdcard/Android/data/com.canonical.candy/
    watchdog:
      disabled: false
      allowed-packages:
      - com.android.settings
    services:
    - port: 5559
      protocols:
      - tcp
      expose: false
      name: adb
  1:
    image: bf7u4cqkv5sg5jd5b2k0 (version 0)
    published: false
    status: active
    addons:
    - ssh
    boot-activity: com.canonical.candy.GameApp
    required-permissions:
    - android.permission.READ_EXTERNAL_STORAGE
    - android.permission.READ_EXTERNAL_STORAGE
    extra-data:
      com.canonical.candy.obb:
        target: /data/app/com.canonical.candy-1/lib
    watchdog:
      disabled: false
      allowed-packages:
      - com.android.settings
    services:
    - port: 5559
      protocols:
      - tcp
      expose: false
      name: adb
resources:
  memory: 4GB
  disk-size: 8GB
```

Each version gets a monotonically increasing number assigned (here we have version `0` and version `1`).
In addition each version has a status which indicates the status of the bootstrap process AMS is
performing for it. Once an application version is marked as `active` it is ready to be used.

The most important part of an application version is the `published` field. If a version is marked as published it is accessible to users of Anbox Cloud. Generally when launching containers by using the AMS REST API and no specific application version is given the last published version of an application is used to create the container.

Marking an application version as published can be achieved with the following command

    amc application publish bcmap7u5nof07arqa2ag 1

Next to publishing an application version its already possible to revoke it

    amc application revoke bcmap7u5nof07arqa2ag 1

As consequence if an application only has a single published version and that version is revoked the application can't be used by any users anymore. AMS will still list the application but will mark it as not published as it has no published versions.

Each version takes space on the LXD nodes. To free up space and remove old and unneeded version they can be individually removed with the only requirement that an application needs to have at least a single version at all time. Removing a specific application version is possible with the following command:

    amc application delete --version=1 bcmap7u5nof07arqa2ag

The `amc` command will ask for your approval before the version is removed as it may affect your users. If you want to bypass the check you can add the `--yes` flag to the command.

## Disable Automatic Application Updates

**since 1.11.0**

AMS will automatically update applications whenever any of its dependencies (parent image, addons, global configuration) changes. This will produce a new version for the application which gets also automatically published, if the `application.auto_publish` configuration item is enabled.

In some cases an automatic update is not wanted. To support this AMS allows disabling automatic application updates via the `application.auto_update` configuration update.

To disable automatic updates:

    amc config set application.auto_update false

To enable automatic updates:

    amc config set application.auto_update true

When automatic updates are disabled applications need to be manually updated for any changed dependencies. To do this can you use the following command:

    amc application update <application id or name>

This will initiate the update process and create a new application version.

## Change Image an Application is based on

The image an application is based on can be easily changed with the following command:

```bash
$ amc application set com.canonical.candy image <image name or id>
```

Changing the image will cause AMS to generate a new version for the application. Previous versions will continue using the image the application used before.

## Delete Applications

When an application is no longer needed it can be fully removed from Anbox Cloud. Removing an application will cause all of its versions to be removed next to all currently active containers. Please be extra careful as this might affect your users if any are still using containers of the application you want to remove.

Once you're sure you want to remove the application you can do so with the following command:

```bash
$ amc application delete bcmap7u5nof07arqa2ag
```

The `amc` tool will ask for your approval before the application is removed. If you want to bypass the check you can add the `--yes` flag to the command.

## Filter Applications

By default, `amc application ls` shows all applications. If you want to search for specific types of applications, e.g. only show a group of applications with a particular tag, you can use the `--filter` flag to filter and group applications.

The filter flag accepts a key-value pair as input for the filter. The following attributes are valid keys.

Name            |  Value
----------------|------------
`instance-type` |  Supported instance type. See chapter [Available Instance Types](https://discourse.ubuntu.com/t/instance-types-reference/17764) for a list of available instance types
`addons`        |  Comma separated list of addons
`tag`           |  Application tag name (deprecated, use `tags` instead)
`tags`          |  Comma separated list of tags
`publishd`      |  "true" or "false" which indicates if the application is published
`immutable`     |  "true" or "false" which indicates if the application is immutable
`status`        |  Application status, possible values: "error", "unknown", "initializing", "ready", "deleted"


To list all applications with a tag called "game":

```bash
$ amc application ls --filter tag=game
```

If you need to apply multiple filters, you could pass multiple flags:

```bash
$ amc application ls --filter published=true --filter tag=game
```

This will query all published applications that have the tag "game"

## Next Steps

 * [Container Management](https://discourse.ubuntu.com/t/managing-containers/17763)
