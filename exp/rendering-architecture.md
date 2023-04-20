The rendering pipeline of Anbox Cloud can vary depending on the GPU used. The aim of this topic is to list various supported GPU vendors, drivers, platforms, APIs and discuss the rendering pipelines used for different GPUs.

# Supported GPU vendors

Being a cloud solution, Anbox Cloud is optimised for GPUs that are designed for a data centre. We currently support the following GPU vendors:

* NVIDIA
* Intel
* AMD

Anbox Cloud is extensively tested using NVIDIA GPUs and occasionally, on Intel and AMD GPUs. However, if you want to use a different GPU vendor, you can customise and configure Anbox Cloud for the GPU vendor of your choice using the [Anbox Platform SDK](https://anbox-cloud.io/docs/ref/sdks#anbox-platform-sdk).

# Supported GPU drivers

For NVIDIA GPUs, Anbox Cloud uses the [Enterprise Ready Driver (ERD) from NVIDIA](https://help.ubuntu.com/community/NvidiaDriversInstallation) for Linux as available in Ubuntu. 
For AMD and Intel GPUs, Anbox Cloud uses the [Mesa driver](https://www.mesa3d.org/).

See [Component versions](https://anbox-cloud.io/docs/component-versions) to refer to the actual version supported for any particular Anbox Cloud release.

# Supported platforms

For rendering, you can use the `swrast` or the `null` platforms depending on your requirements.

`swrast` is a software rasterization platform, which is a rendering implementation of the Mesa driver with support for LLVMpipe. It can be utilised for use cases that require a visual output without a GPU. The rendering pipe for the `swrast` or `null` platform is not different than the one for the `webrtc` platform with NVIDIA GPU support except that it is irrespective of any available GPUs. To know more about this implementation, see [LLVMpipe](https://docs.mesa3d.org/drivers/llvmpipe.html).

`null` is an OpenGL headless platform that makes use of the rendering backend of the [Almost Native Graphics Layer Engine (ANGLE)](https://chromium.googlesource.com/angle/angle) and can be used when you do not need a graphic output, such as, automation testing. It does not perform software rendering and does not produce any graphic output. Hence, the overhead on the CPU when using `null` platform is significantly low which makes it a good candidate for all use cases where a graphic output is not necessary.

For more information on the platforms supported by Anbox Cloud and how to configure them, see [Anbox platforms](https://anbox-cloud.io/docs/ref/platforms).

# Supported APIs

For NVIDIA GPUs Anbox Cloud uses [OpenGL ES 3.2](https://www.khronos.org/opengles/) and [EGL 1.5](https://www.khronos.org/egl/) graphical interfaces. For Intel and AMD GPUs, Anbox Cloud uses [Vulkan 1.3](https://vulkan.org/).

# Rendering architecture

For NVIDIA GPUs, Anbox Cloud driver stacks currently have a native OpenGL ES driver. For AMD and Intel GPUs, an OpenGL ES or EGL driver is layered on top of the Vulkan API. Since Vulkan API provides better GPU management at a lower level than OpenGL ES or EGL, this approach is beneficial and preferred by many users.

To have a better understanding of the rendering architecture of Anbox Cloud, it is important to understand what the Android framework offers in terms of rendering. In Android, applications interact with the SurfaceFlinger which is the system compositor that is responsible for composing a frame together from all the outputs rendered by different applications. The frame is then submitted to the hardware composer which renders the frames on a screen. For more information on Android graphics components and how they work, see https://source.android.com/docs/core/graphics. 

# Rendering pipeline

Anbox Cloud has two rendering pipeline models - one for NVIDIA and the other for Intel and AMD. However, irrespective of the GPU that you use, the path of a frame typically looks like this: Android application > SurfaceFlinger > Hardware composer > Anbox Cloud > Display on screen or send it to streaming component.

For communication between the hardware composer module on the Android side and Anbox runtime, we use [Wayland](https://wayland.freedesktop.org/). So Anbox Cloud really functions as a compositor for Android i.e., the hardware composer module receives frames from the SurfaceFlinger and notifies Anbox runtime using Wayland. The Anbox runtime then submits the frame towards its output, which is either the screen or the streaming component.

## For NVIDIA

![Anbox Cloud NVIDIA pipeline|690x440](https://assets.ubuntu.com/v1/3ba1fddd-NVIDIA_pipeline.png)

For NVIDIA, as we cannot use the NVIDIA driver inside the Android container because of compatibility issues, we use the Enterprise Ready NVIDIA driver that is available on every Ubuntu installation. Instead, we have an Anbox Cloud GPU driver which is a standard OpenGL ES or EGL driver that receives the API calls and converts them to remote procedure calls to the NVIDIA driver. The actual rendering and actions on the NVIDIA driver happens on the Anbox runtime side inside the Ubuntu container and not in the Android space.

In terms of performance, this could be perceived to have some transmission overhead when compared to the rendering on Intel and AMD GPUs. However, Anbox Cloud is optimised to keep this overhead minimal and the additional overhead due to the transmission of OpenGL ES calls from the Android space to Anbox runtime is not significant enough to affect most use cases.

## For Intel and AMD

![Anbox Cloud Intel and AMD pipeline|690x440](https://assets.ubuntu.com/v1/7aa9aff1-Intel_AMD_pipeline.png)

For AMD and Intel GPUs, Anbox Cloud uses Vulkan as API in the Android space and we use ANGLE on top of Vulkan to circumvent OpenGL ES and EGL. Since the Mesa driver (vendor GPU driver) is available directly in the Android space, we do not have the overhead of the remote procedure call implementation as in the pipeline for NVIDIA. 






