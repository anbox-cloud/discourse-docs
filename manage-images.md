An image is the base for a container running in the Anbox Cloud. It contains all necessary things like Anbox or the Android root filesystem. Each release of Anbox Cloud comes with an update image which has to be uploaded to the AMS service to make it available to be used inside any container.

AMS can manage different types of images which can be individually selected by applications. For that each image needs to be named when it's initially uploaded to AMS. If the same image receives an update with the next release of Anbox Cloud it does not need to be recreated but can be simply updated. This will cause all applications using the image to be updated and rebased on the new image version.

Officially released images are available for each version of Anbox Cloud either on the [Downloads](https://oem-share.canonical.com/partners/indore/share/docs/1.7/en/installation-downloads.html) page or on an image server hosted by Canonical.

> **Note**: Anbox images are regular [Ubuntu cloud images](https://cloud-images.ubuntu.com/) where Anbox and its dependencies are installed. Unnecessary packages are removed to improve images size, boot time and security.

## Supported Images

The official image server has a set of images available. The following table lists all and their corresponding Android and Ubuntu versions. Please note the support status for each of the images.

| Name                        | Android Version | Ubuntu Version | Support Status     | Available since |
|-----------------------------|-----------------|----------------|------------|---------------|
| `bionic:android11:amd64`      | 11              | 18.04          | supported | 1.10 |
| `bionic:android11:arm64`      | 11              | 18.04          | supported | 1.10 |
| `bionic:android10:amd64`      | 10              | 18.04          | supported | 1.0
| `bionic:android10:arm64`      | 10              | 18.04          | supported | 1.0
| `bionic:android7:amd64`       | 7               | 18.04          | unsupported as of 1.10 | 1.0 |
| `bionic:android7:arm64`       | 7               | 18.04          | unsupported as of 1.10 | 1.0 |

The `bionic:android7:arm64` and `bionic:android7:amd64`  images are not receiving Android security updates anymore as Google stopped supporting Android 7 late 2019. They are only provided for legacy reasons and will be dropped with Anbox Cloud 1.10 in April 2021.

## Configure Image Server

Using the image server hosted by Canonical enables automated updates on your Anbox Cloud deployment. AMS will automatically synchronize new image versions in regular intervals and update your applications. Using the image server should be preferred over using manually managed images. Images on the image server are updated for important security updates or bug fixes and with every release of Anbox Cloud.

Starting with Anbox Cloud 1.9 access to the image server is automatically configured as part of your Ubuntu Advantage subscription during the charm deployment and no further manual steps are necessary.

AMS will start automatically to import images available on the image server.
The `images.update_interval` configuration option allows to customize how often AMS looks for new images. You can set it to a desired interval with the following command:

```bash
$ amc config set images.update_interval 5m
```

Synchronized images will become available next to images you manually add:

```bash
$ amc image list
+----------------------+-----------------------------+--------+----------+
|          ID          |            NAME             | STATUS | VERSIONS |
+----------------------+-----------------------------+--------+----------+
| bj03g89hpuo10ed1riog | io.anbox-cloud:nougat:amd64 | active | 1        |
+----------------------+-----------------------------+--------+----------+
| bj003kphpuo2bt5edjtg | default                     | active | 1        |
+----------------------+-----------------------------+--------+----------+
```

In contrast to manually added images synchronized ones are marked as immutable as they can't be manually updated. In case you want to remove an immutable image you need to call the following command:

```bash
$ amc image delete --force io.anbox-cloud:nougat:amd64
```

If you're not using `--force` the command will fail.

## Add a new Image to AMS

Adding an image to AMS can be done with a simple command

```bash
$ amc image add default anbox-lxd-bionic_1.7_amd64.tar.xz
```

`default` is the name assigned to the new image and can be used by applications to reference the image.

Each image gets a unique ID assigned which can be used to retrieve further information about the image.

```bash
$ amc image show bcpm2r2hmss0427lkrn0
id: bcpm2r2hmss0427lkrn0
name: default
status: active
versions:
    0:
        size: 374.69MB
        created-at: 2018-06-27 10:05:32 +0000 UTC
        status: active
```

Similar to applications managed by AMS (see [Application Management](https://discourse.ubuntu.com/t/managing-applications/17760)) images have a list of versions too. A new version is created each time an image is updated.

## Default image
When adding your first image to AMS, it will be marked as the default image.
The default image is used when you create an application without the `image` field or launch a raw container without specifying any ID.

You can set any image as your default with the following command:

```bash
$ amc image switch bcpm2r2hmss0427lkrn0
```

Listing images will now show this image marked as default.

> **Hint:** Note that you cannot delete an image marked as default, you'll need to set a new one first. *(does not apply if you only have one image left)*

## Update an existing image

As each release of Anbox Cloud comes with a new image which includes various updates to the Ubuntu or Android systems AMS allows to easily update an existing image with a new version.

Similar as adding a new image to AMS updating the image is simple as well:

```bash
$ amc image update default anbox-lxd-bionic_1.7_amd64.tar.xz
```

`default` is again the name assigned to the existing image. Uploading the new image to the connected LXD cluster will take a short moment but once the upload has finished the image is marked as `active`.

Now that a new image version is available to AMS it will start to create new versions of all available applications but won't publish them. Creating new versions of each application can take a moment depending on the current load of the cluster. You can see available versions of a specific application with the following command:

```bash
$ amc application show <id>
```

Each version will tell you also which version of an image it is based on.

## Delete an Image

Deleting an image will make it unavailable to the Anbox Cloud. However it will not affect any application based on the image directly as the application keeps a copy of the image internally. As the image is not available to AMS anymore after deleting it, updating the underlying image of applications with a new version is then not possible anymore.

Deleting a specific image can be achieved with the following command:

```bash
$ amc image delete default
```

Where `default` is the name of the image to delete.

Specific image versions can be deleted too, which is useful when all applications were migrated to a newer version and the old version is not needed anymore. Only requirement is that an image as a single version available at all time.

```bash
$ amc image delete default --version=1
```

The command removes version `1` of the image with the name `default`.

## Next Steps

 * [Application Management](https://discourse.ubuntu.com/t/managing-applications/17760)
 
