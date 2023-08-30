Anbox Cloud has support for managing GPUs and can provide them to individual containers for rendering and video encoding functionality.

Anbox Cloud automatically detects GPU devices during the deployment and configures the cluster to use them. If no GPU is available, Anbox Cloud automatically falls back to the [`null` platform](https://discourse.ubuntu.com/t/anbox-platforms/18733) that does not perform any rendering. However, you can enable software rendering and video encoding by launching your application with the `--enable-graphics` flag. This makes it possible to run entirely without a GPU and still use rendering.

## Required GPU slots

GPUs have limited capacity that can be shared amongst multiple containers. To fine-tune how many containers can run on a given node, configure the number of available GPU slots on the node.

See [GPU slots](https://discourse.ubuntu.com/t/about-capacity-planning/28717#gpu-slots) for detailed information.

## Using GPUs inside a container

AMS configures each LXD container to pass through a GPU device from the host. Currently, all GPUs that are available to a machine are passed to every container that owns a GPU slot. For NVIDIA GPUs, LXD uses the [NVIDIA container runtime](https://github.com/NVIDIA/nvidia-container-runtime) to make the GPU driver of the host available to the container.

Check the [list of supported GPUs](https://discourse.ubuntu.com/t/37322#supported-gpus) to see if Anbox Cloud includes a driver for your GPU device. If a GPU driver is available inside the container, there are no further differences in how to use it in comparison to a regular environment. If no GPU driver is available, you must provide it through an [addon](https://discourse.ubuntu.com/t/managing-addons/17759).

If you want to let an application use the GPU (even if you are not interested in streaming the visual output), launch it with the `--enable-graphics` flag. With this flag, the command will launch the container using the `webrtc` platform, which will automatically detect the underlying GPU and make use of it.

    amc launch --enable-graphics my-application

<a name="software-rendering"></name>
## Force software rendering and video encoding

It is possible to instruct a container to run with software rendering. To do so, change the [instance type](https://discourse.ubuntu.com/t/application-manifest/24197#instance-type) or [resources](https://discourse.ubuntu.com/t/application-manifest/24197#resources) of the application to not require a GPU. Anbox Cloud will then automatically determine that no GPU is available and use software rendering instead if a container is launched with graphics enabled.

Since software rendering and video encoding will utilise the CPU, you won't be able to run as many containers on a system when compared to running containers when you have a GPU.

## Related information
* [Supported rendering resources](https://discourse.ubuntu.com/t/37322)

