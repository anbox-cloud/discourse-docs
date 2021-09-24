The AMS services provides with addons a way to customize the images used as base for the containers. An addon is basically a tarball providing several hooks and additional metadata. A very good example for an addon is one which enables the SSH service inside a container to provide access from the outside for any kind of automation of the container.

An addon can be installed into a container by adding it to a registered application in AMS.

> **Note:**  Addons provide can be very powerful feature. Be careful with how you customize the container as it may prevent it from running properly or impact its performance.

In the next sections you will learn how to manage addons in AMS.

<h2 id='heading--build-your-own-addon'>Build your own Addon</h2>

Any addon has the following structure:

```text
manifest.yaml
hooks/install
```

The hooks directory contains a set of executable files where each corresponds to a single hook. Any other files are ignored.

At the moment the following hooks are supported:

Name                 |  Description
---------------------|-----------------------------------------------------------------------------------
`install`            | Invoked on the installation of the addon during the application bootstrap process.
`prepare` (optional) | Invoked during the bootstrap process when the Android container is running
`restore` (optional) | Invoked before the Android system gets started.
`backup` (optional)  | Invoked right after the Android system shuts down.

The `manifest.yaml` file describes the addon:

```yaml
name: nil
description: |
  A very simple addon doing nothing but showing how an addon is build
```

Name          | Value type | Description
--------------|------------|-------------------------
`name`          | string     | Verbose name of the addon, A few special characters are not allowed: '< > : " / \ &#124; ? *', as well as space
`description`       | string     | A short description to the  addon

 The hook itself can be written in any programming language but the most common way is to use a shell script. An `install` hook that instructs how to install the addon must be included in the addon package. The two other hooks `restore` and `backup` are optional and are only executed if they exist in the package. Because of the execution sequence of `restore` and `backup` hooks and to avoid hangups on system startup or termination, you should not perform long time operations on these two hooks, the `restore` and `backup` processes will be killed if they take more than 5 minutes to complete. All hooks need to marked as executable, otherwise containers will fail to start.

### Install Hook
An example `install` hook can look like this:

```bash
#!/bin/sh -ex
echo "I am the install hook!"
echo "ANBOX_DIR: $ANBOX_DIR"
echo "ADDON_DIR: $ADDON_DIR"
echo "ANDROID_ROOTFS: $ANDROID_ROOTFS"
exit 0
```

As you can see, the script is invoked with a few special environment variables set which let the addon know where certains things like the Android root filesystem inside the container are.
The following environment variables are available:

Name             |  Description
-----------------|-------------------------------------------------------------------------------------------------
`ANBOX_DIR` | Directory the configurations, logs, data, and Android rootfs are placed in. Used to install additional data under Anbox directory.
`ADDON_DIR`      | Directory the addon itself is placed in. Used to access additional data shipped with the addon.
`ANDROID_ROOTFS` | Path to the writable Android root filesystem inside the Android container.
`BOOT_PACKAGE`   | Application package to be installed and launched inside the Android container.

Packaging the addon itself is as simple as creating a tarball given that the following files exist in the current directory:

```bash
$ find -type f
./manifest.yaml
./hooks/install
```

Creating the addon now goes as

```bash
$ tar cvjf ../foo-addon.tar.bz2 *
```

The tarball now contains everything necessary and is ready to be registered as an addon in AMS.

 ```bash
$ amc addon add foo ../foo-addon.tar.bz2
```

### Prepare Hook

The `prepare` hooks allows customization of the Android container while it's running when the bootstrap process is performed. This enables the addon to install Android applications (APKs)
into the Android container or perform other customizations which are only possible at runtime.

An example `prepare` hook looks like this:

```bash
#!/bin/sh -ex
anbox-shell settings put global http_proxy myproxy:8080
```

The hook implementation above uses the `anbox-shell` command to invoke commands within the Android container. In this case it's adjusting the global HTTP proxy Android should use.

The `prepare` hook needs to be placed as `hook/prepare` within the addon package.

<h3 id='heading--backup-and-restore'>Backup and Restore Hooks</h3>

Backup and restore hooks are scripts that run automatically whenever a container is terminated or get started. These two hooks let you trigger customizable actions at key points in the container life cycle.

Common use cases for these two hooks are to [back up and restore application data](https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183). Whenever Android container is terminating, all application data, logs that are produced during the container runtime would go away. In most cases, rather than losing those data, you want to backup them by store those data to public or private cloud storage service and restore the data next time when a container was launched from the same application.

Meanwhile, there is an `ANBOX_EXIT_CODE`  environment variable that can be used in the  `backup` hook to detect if Anbox terminates correctly or not.

For example, if you want to collect container logs and backup them to a public or private storage service for further investigation when a container doesn't terminate properly.

```bash
#!/bin/sh -ex
if [ "$ANBOX_EXIT_CODE" = 0 ]; then
  exit 0
fi

FILE_NAME=container-logs.tar.bz2
(cd /var/lib/anbox/logs; tar cvjf ../"${FILE_NAME}" *)
# Upload the tarball to public or private cloud storage service
curl -i -X POST --data-binary @"${FILE_NAME}" <cloud_storage_upload_url>
```

For the use of restore hook, let's consider that you want to restore an application user data which was yielded out from the last container session.

```bash
#!/bin/sh -ex
# Download the tarball from a public or private cloud storage service
if curl -o app-data.tar.bz2 <cloud_storage_download_url> ; then
  tar xvjf app-data.tar.bz2 -C /var/lib/anbox/data/data/com.foo.bar
fi
```

The use of `aam` is recommended to [back up and restore application data](https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183) on container start and stop. The process involves various operations to assign correct permissions to files and directories Android expects.

## Add Addon to AMS

Adding an addon to AMS works similar as adding images to AMS (see [Manage images](https://discourse.ubuntu.com/t/managing-images/17758)).
The `amc` command line utility has a subcommand which only deals with addons.

Adding the addon can be done with the following command

```bash
$ amc addon add foo foo-addon.tar.bz2
```

The command expects you to define a name of the addon (`foo` in this case) which should be the same
as in the addon manifest.

> **Note:** Due to Snap strict confinement,  the tarball file must be located home directory.

## Update an existing Addon

Updating an existing addon with a new version is possible with the following command:

```bash
$ amc addon update foo foo-addon.tar.bz2
```

AMS will take care of updating all existing applications which use the addon in the background.

## Create Application with an Addon

Adding an addon to a newly created application can be easily done by extending the application manifest (see [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)). An example application manifest with the `foo` addon added looks like this:

```bash
$ cat manifest.yaml
name: candy
instance-type: a2.3
boot-activity: com.canonical.candy.GameApp
image: default
addons:
- foo
```

An application can take any number of addons. If a not existing addon is specified the application creation process will fail.

Creating the application with the modified manifest goes as usual:

```bash
$ amc application create .
```

## Set Default Addons used by all Applications

AMS provides a configuration item which allows defining a set of addons which should be used by all newly added applications. They will extend the list of addons defined in the application manifest.

You can set a default list of addons with the following command:

```bash
$ amc config set application.addons foo,bar
```

The list of addons is comma separated.

## Addons providing support for additional CPU architectures

You might want to have addons that perform translation on platforms that are not natively supported by your application (running x86_64 applications on ARM for example).

You can add the top-level key `provides` to your addon manifest and list the architecture it supports:

```bash
$ cat my-addon/manifest.yaml
name: my-addon
description: provides support for x86_64 architecture
provides:
    abi-support:
        - arm64-v8a
        - armeabi-v7a
```
