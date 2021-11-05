Anbox Cloud provides images based on different Android versions and different architectures (amd64, arm64). AMS manages these images, which can be individually selected by applications. When an image is updated, all applications using the image are automatically updated and rebased on the new image version.

Officially released images are available from the [official image server](https://images.anbox-cloud.io) hosted by Canonical.

[note type="information" status="Note"]Anbox images are regular [Ubuntu cloud images](https://cloud-images.ubuntu.com/) where Anbox and its dependencies are installed. Unnecessary packages are removed to improve images size, boot time and security.[/note]

## Official images

The official image server has a set of images available. The following table lists all images and their corresponding Android and Ubuntu versions. Please note the support status for each of the images.

| Name                        | Android Version | Ubuntu Version | Support Status     | Available since |
|-----------------------------|-----------------|----------------|------------|---------------|
| `bionic:android11:amd64`      | 11              | 18.04          | supported | 1.10 |
| `bionic:android11:arm64`      | 11              | 18.04          | supported | 1.10 |
| `bionic:android10:amd64`      | 10              | 18.04          | supported | 1.0
| `bionic:android10:arm64`      | 10              | 18.04          | supported | 1.0
| `bionic:android7:amd64`       | 7               | 18.04          | unsupported as of 1.10 | 1.0 |
| `bionic:android7:arm64`       | 7               | 18.04          | unsupported as of 1.10 | 1.0 |

The `bionic:android7:arm64` and `bionic:android7:amd64` images are not receiving Android security updates anymore as Google stopped supporting Android 7 in 2019. They are only provided for legacy reasons and have been dropped with Anbox Cloud 1.10 in April 2021.
