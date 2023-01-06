Anbox Cloud provides images based on different Android versions and different architectures (amd64, arm64). AMS manages these images, which can be individually selected by applications. When an image is updated, all applications using the image are automatically updated and rebased on the new image version.

Officially released images are available from the [official image server](https://images.anbox-cloud.io) hosted by Canonical. It is currently not possible to build custom images for Anbox Cloud.

[note type="information" status="Note"]Anbox images are regular [Ubuntu cloud images](https://cloud-images.ubuntu.com/) where Anbox and its dependencies are installed. Unnecessary packages are removed to improve images size, boot time and security.[/note]

## Official images

The following table lists all images that are available on the official image server, along with their corresponding Android and Ubuntu versions. Please note the support status for each of the images.

| Name                        | Android Version | Ubuntu Version | Support Status     | Available since |
|-----------------------------|-----------------|----------------|------------|---------------|
| `jammy:android13:amd64`     | 13              | 22.04          | supported | 1.16 |
| `jammy:android13:arm64`     | 13              | 22.04          | supported | 1.16 |
| `jammy:android12:amd64`     | 12              | 22.04          | supported | 1.14 |
| `jammy:android12:arm64`     | 12              | 22.04          | supported | 1.14 |
| `jammy:android11:amd64`     | 11              | 22.04          | supported | 1.14 |
| `jammy:android11:arm64`     | 11              | 22.04          | supported | 1.14 |
| `jammy:android10:amd64`     | 10              | 22.04          | supported | 1.14 |
| `jammy:android10:arm64`     | 10              | 22.04          | supported | 1.14 |
| `bionic:android12:amd64`    | 12              | 18.04          | deprecated as of 1.16 | 1.12 |
| `bionic:android12:arm64`    | 12              | 18.04          | deprecated as of 1.16 | 1.12 |
| `bionic:android11:amd64`    | 11              | 18.04          | deprecated as of 1.16 | 1.10 |
| `bionic:android11:arm64`    | 11              | 18.04          | deprecated as of 1.16 | 1.10 |
| `bionic:android10:amd64`    | 10              | 18.04          | deprecated as of 1.16 | 1.0  |
| `bionic:android10:arm64`    | 10              | 18.04          | deprecated as of 1.16  | 1.0  |
| `bionic:android7:amd64`     | 7               | 18.04          | unsupported as of 1.10 | 1.0 |
| `bionic:android7:arm64`     | 7               | 18.04          | unsupported as of 1.10 | 1.0 |

## Image support

Anbox Cloud provides images based on two different Ubuntu versions, currently 18.04 (bionic) and 22.04 (jammy). The bionic images are deprecated and will receive their last update with the Anbox Cloud 1.18 release.

Android versions are supported as long as Google provides security updates for the respective version. This means that the Android 10 images will be deprecated in Anbox Cloud 1.17 and will be dropped with Anbox Cloud 1.19. The `bionic:android7:arm64` and `bionic:android7:amd64` images are not receiving Android security updates anymore as Google stopped supporting Android 7 in 2019. They are listed only for legacy reasons and have been dropped with Anbox Cloud 1.10 in April 2021.

Deprecations are announced at least two releases in advance.
