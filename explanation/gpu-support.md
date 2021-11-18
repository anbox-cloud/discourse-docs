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

## Required GPU slots

GPUs have limited capacity that can be shared amongst multiple containers. To fine-tune how many containers can run on a given node, configure the number of available GPU slots on the node.

See [GPU slots](https://discourse.ubuntu.com/t/capacity-planning/17765#gpu-slots) for detailed information.

## Using GPUs inside a Container

AMS configures a LXD container to passthrough a GPU device from the host. As of right now all GPUs available to a machine are passed to every container owning a GPU slot. For Nvidia GPUs LXD uses the [Nvidia container runtime](https://github.com/NVIDIA/nvidia-container-runtime) to make the GPU driver of the host available to a container. When GPUs from Intel or AMD are being used no GPU driver is made available automatically. It has to be provided by an [addon](https://discourse.ubuntu.com/t/managing-addons/17759).

If a GPU driver is available inside the container there are no further differences of how to use it in comparison to a regular environment.

If you want to let an application use the GPU but are not interested in streaming its visual output, you can simply launch a container with the `webrtc` platform. The platform will automatically detect the underlying GPU and make use of it.

```bash
$ amc launch -p webrtc my-application
```

## Force Software Rendering and Video Encoding

[note type="information" status="Note"]Software rendering and video encoding will utilize the CPU. This will mean you can run less containers on a system than you can, when you have a GPU.[/note]

It is possible to force a container to run with software rendering. For that simply launch a container with

```bash
$ amc launch -p swrast my-application
```

This will start the container with the `swrast` platform which forces software based rendering.

If you want to force an application to use software rendering and video encoding when streaming via the Anbox Stream Gateway you can simply set a an [instance type](https://discourse.ubuntu.com/t/instance-types/17764) which doesn't require a GPU slot. For example

```bash
$ amc application set my-app instance-type a4.3
```
