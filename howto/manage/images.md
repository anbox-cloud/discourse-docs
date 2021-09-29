An image is the base for a container running in the Anbox Cloud. It contains all necessary components, like Anbox or the Android root file system. Each release of Anbox Cloud comes with an updated image.

See [Provided images](https://discourse.ubuntu.com/t/provided-images/24185) for information about which images Anbox Cloud provides.

## Configure image server

Using the image server hosted by Canonical enables automated updates on your Anbox Cloud deployment. AMS will automatically synchronise new image versions in regular intervals and update your applications. Using the image server should be preferred over using manually managed images. Images on the image server are updated for important security updates or bug fixes, and with every release of Anbox Cloud.

Starting with Anbox Cloud 1.9, access to the image server is automatically configured as part of your Ubuntu Advantage subscription during the charm deployment. No further manual steps are necessary.

AMS will start automatically to import images available on the image server. The `images.update_interval` configuration option allows to customise how often AMS looks for new images. You can set it to a desired interval with the following command:

    amc config set images.update_interval 5m

Synchronised images will become available next to images you manually add:

```bash
+----------------------+-----------------------------+--------+----------+
|          ID          |            NAME             | STATUS | VERSIONS |
+----------------------+-----------------------------+--------+----------+
| bj03g89hpuo10ed1riog | io.anbox-cloud:nougat:amd64 | active | 1        |
+----------------------+-----------------------------+--------+----------+
| bj003kphpuo2bt5edjtg | default                     | active | 1        |
+----------------------+-----------------------------+--------+----------+
```

## Default image
When adding your first image to AMS, it is marked as the default image.
The default image is used when you create an application without the `image` field or launch a raw container without specifying any ID.

You can set any image as your default with the following command:

    amc image switch bcpm2r2hmss0427lkrn0

Running `amc image list` will now show this image marked as default.

> **Hint:** Note that you cannot delete an image marked as default. You'll need to set a new default image first. *(does not apply if you only have one image left)*

## Delete an image

Deleting an image will make it unavailable to Anbox Cloud. However, it will not affect any application based on the image directly, as the application keeps a copy of the image internally. As the image is not available to AMS anymore after deleting it, updating the underlying image of applications with a new version is not possible anymore.

Deleting a specific image can be achieved with the following command, where `default` is the name of the image to delete:

    amc image delete default

Images that are synchronised from the image server are marked as immutable. To delete such images, add the `--force` flag:

    amc image delete --force io.anbox-cloud:nougat:amd64

If you're not using `--force`, the command will fail.

### Delete an image version

Specific image versions can be deleted too, which is useful when all applications were migrated to a newer version and the old version is not needed anymore. The only requirement is that a single version of the image is available at all times.

The following command removes version `1` of the image with the name `default`:

    amc image delete default --version=1

## Manual upload of images

In addition to the images provided through Canonical's image server, you can manually upload your own images to be used by AMS.

You must choose a name for the image when uploading it. If you update the image later, use the same name so that the image is not re-created but simply updated.

### Add an image to AMS

Adding an image to AMS can be done with the following command:

    amc image add default anbox-lxd-bionic_1.7_amd64.tar.xz

`default` is the name assigned to the new image. The name can be used by applications to reference the image.

Each image gets a unique ID assigned which can be used to retrieve further information about the image with `amc image show <ID>`:

```bash
id: bcpm2r2hmss0427lkrn0
name: default
status: active
versions:
    0:
        size: 374.69MB
        created-at: 2018-06-27 10:05:32 +0000 UTC
        status: active
```

Similar to applications managed by AMS (see [About applications](https://discourse.ubuntu.com/t/managing-applications/17760)), images have a list of versions too. A new version is created each time an image is updated.

### Update an existing image

Use the following command to update a manually uploaded image in AMS:

    amc image update default anbox-lxd-bionic_1.7_amd64.tar.xz

`default` is the name assigned to the existing image. Uploading the new image to the connected LXD cluster will take a moment. Once the upload has finished, the image is marked as `active`.

Now that a new image version is available to AMS, it will start to create new versions of all available applications but won't publish them. Creating new versions of each application can take a moment depending on the current load of the cluster. You can see available versions of a specific application with the following command:

    amc application show <id>

Each version will give information about which version of an image it is based on.
