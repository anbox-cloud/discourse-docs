Anbox Cloud has support to manage GPUs and can provide them to individual containers for rendering and video encoding functionality.

In case that no GPU is available Anbox Cloud automatically falls back to software rendering and video encoding. This makes it possible to run entirely without a GPU.

## Supported GPUs

Anbox Clouds allows access to GPUs from Intel, AMD and Nvidia inside the Anbox container. Concrete support for the individual GPU depends on the platform being using for Anbox. The included `webrtc` platform currently supports the following GPUs:

| Vendor | Model          | Render | Hardware Video Encode |
|--------|----------------|--------|-----------------------|
| AMD    | WX5100, WX4100 | Yes    | No                    |
| Nvidia | Quadro, Tesla  | Yes    | Yes                   |

For those GPUs which Anbox Cloud doesn't support hardware video encoding, a software based video encoding fallback is available.

## Enable Support for GPUs in Anbox Cloud

Anbox Cloud will automatically detect GPU devices on deployment and configure the cluster for these. **You can't mix GPUs from different vendors in a single deployment.**

## GPU Slots

GPUs have limited capacity that can be shared amongst multiple containers and `gpu-slots` are a way to fine-tune how many containers can run on a given node.

In short, each LXD node has a certain amount of `gpu-slots` available, and each application can define a number of `gpu-slots` it needs. Both are configurable.

### GPU Slots for LXD nodes

Each GPU equipped [LXD node](https://discourse.ubuntu.com/t/managing-lxd-nodes/17757) has its own number of GPU slots configured. You can see that number with the following command:

```bash
$ amc node show lxd0
...
config:
    ...
    gpu-slots: 0
```

You can change the number of GPU slots of each node with the following command:

```bash
$ amc node set lxd0 gpu-slots 10
```
> **NOTE**: Determining the correct number of GPU slots for a specific GPU model depends on various things. The following just gives an idea of what should drive the decision for the right number of GPU slots:
> * Memory a GPU provides
> * Memory a container uses
> * Number of parallel encoding pipelines a GPU offers
>
> Finding the right number of GPU slots requires benchmarking and testing of the intended workload.

Launching a container on that node will reserve some of those `gpu-slots` and mark them as unavailable until the container is terminated. If your node has no `gpu-slot` available, containers requiring a GPU will not be launched on it. Containers not requiring a GPU can still be launched.

### GPU Slots for application

Applications can declare how many `gpu-slots` they require. This number is set by default when specifying the [Instance Type](https://discourse.ubuntu.com/t/instance-types/17764) but can be overridden using [resources](https://discourse.ubuntu.com/t/managing-applications/17760).

```bash
name: android
instance-type: g4.3
resources:
  gpu-slots: 3 
```
In this case the application will use 3 `gpu-slots` instead of 1 as defined in the instance type.

Increasing the number of `gpu-slots` does **NOT** guarantee that more GPU resources are allocated to that application container.
*e.g.: An intensive game configured with 1 `gpu-slot` will still consume more resources than a photo gallery app configured with 5 `gpu-slots`*

However, it means that less containers will be launched on that node, reducing contention for GPU resources.



Containers can be configured to use a hardware or software video encoder for video encoding
This can be done through `video-encoder` field declared in the manifest file when creating an application as well. See [ Managing applications](https://discourse.ubuntu.com/t/managing-applications/17760) for more details.

## Using GPUs inside a Container

AMS configures a LXD container to passthrough a GPU device from the host. As of right now all GPUs available to a machine are passed to every container owning a GPU slot. For Nvidia GPUs LXD uses the [Nvidia container runtime](https://github.com/NVIDIA/nvidia-container-runtime) to make the GPU driver of the host available to a container. When GPUs from Intel or AMD are being used no GPU driver is made available automatically. It has to be provided by an [addon](https://discourse.ubuntu.com/t/managing-addons/17759).

If a GPU driver is available inside the container there are no further differences of how to use it in comparison to a regular environment.

If you want to let an application use the GPU but are not interested in streaming its visual output, you can simply launch a container with the `webrtc` platform. The platform will automatically detect the underlying GPU and make use of it.

```bash
$ amc launch -p webrtc my-application
```

## Force Software Rendering and Video Encoding

> **Note:** Software rendering and video encoding will utilize the CPU. This will mean you can run less containers on a system than you can, when you have a GPU.

It is possible to force a container to run with software rendering. For that simply launch a container with

```bash
$ amc launch -p swrast my-application
```

This will start the container with the `swrast` platform which forces software based rendering.

If you want to force an application to use software rendering and video encoding when streaming via the Anbox Stream Gateway you can simply set a an [instance type](https://discourse.ubuntu.com/t/instance-types/17764) which doesn't require a GPU slot. For example

```bash
$ amc application set my-app instance-type a4.3
```
