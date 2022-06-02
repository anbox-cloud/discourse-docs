When planning your Anbox Cloud deployment, you should start by estimating how much capacity you need to be able to provide your application to your users and how many users (thus what number of Android containers) you expect. Based on this estimate, you can then size your deployment and figure out how many cluster nodes you need and what resources they should have.

In your calculation, you should consider the following aspects:

- Application resources - How much CPU, memory and disk space does your application need? Will the application use hardware- or software-based video encoding, and if it uses hardware-based encoding, how much GPU capacity is needed?
- Over-commitment - Does every container need dedicated access to the CPU and memory, or can the capacity be shared between several containers?
- Application requirements - What type of application are you running? What frame rate and what resolution does your application need? How many containers will be running simultaneously? What would be the impact of not being able to serve all users?

See the following sections for detailed information on these aspects.

## Application resources

Depending on the resources that your application requires, choose a suitable [instance type](https://discourse.ubuntu.com/t/instance-types/17764).

The instance type specifies the resources that are available to the application:

- The number of vCPU cores
- The amount of RAM
- The amount of disk space
- The number of GPU slots

If none of the provided instance types fits for your application, you can also manually [configure the resources](https://discourse.ubuntu.com/t/how-to-configure-available-resources/24960) according to your requirements.

When a container for an application is launched, it takes the specified amount of resources. For example, if an application uses the `a2.3` instance type, it requires 2 vCPU cores, 3 GB of memory, 3 GB of disk space and no GPU slot. AMS internally summarises the amount of resources used by containers on a single machine and disallows launching additional containers when all resources are used (see [Over-committing resources](#overcommitting) for how to allow a higher resource usage). In this case, you will see the following error message when trying to launch a new container:

    No suitable node to satisfy container requirement available

[note type="information" status="Note"]
If a container stops with an error, its disk space is preserved for inspection. Other resources are released. Therefore, if you have many containers in `error` status, you might run out of disk space.
[/note]

<a name="gpu-slots"></a>
### GPU slots

An additional aspect to take into account when planning your resources is the number of required GPU slots (see [About GPU support](https://discourse.ubuntu.com/t/gpu-support/17768) for more information).

GPUs have limited capacity that can be shared amongst multiple containers, and GPU slots are a way to fine-tune how many containers can run on a given node. In a cluster setup, you define the number of available GPU slots for each node (see [Configure GPU slots](tbd#configure-gpu-slots) for instructions).

To determine the best number of GPU slots for a specific GPU model, consider the following aspects:

- The memory that the GPU provides
- The memory that a container uses
- The number of parallel encoding pipelines that the GPU offers

When you launch a container for an application, AMS reserves the number of GPU slots defined for the application on the node where it is launched. These GPU slots are marked as unavailable until the container is terminated. If no GPU slots are available on the node, containers that require a GPU ([video encoder type](https://discourse.ubuntu.com/t/application-manifest/24197#video-encoder) `gpu`) will not be launched on it. Containers that don't require a GPU ([video encoder type](https://discourse.ubuntu.com/t/application-manifest/24197#video-encoder) `software` or `gpu-preferred`) can still be launched.

[note type="information" status="Important"]
GPU slots are used to share GPUs amongst containers, but they do not impose limits on GPU usage. Therefore, increasing the number of required GPU slots for an application does not guarantee that more GPU resources are allocated to the corresponding application containers. For example, an intensive game that is configured to use one GPU slot might consume more GPU resources than a simple photo gallery app that is configured to use five GPU slots.

The main purpose of GPU slots is to control the number of containers that are launched on a node that has a GPU installed, which reduces contention for GPU resources.
[/note]

<a name="overcommitting"></a>
## Over-committing resources

If the unused resources on a cluster node don't suffice to launch a container for an application with its defined resource requirements, the container cannot be launched. This behaviour is very restrictive, and in many cases unnecessary.

Usually, a container doesn't use its dedicated vCPU cores and memory at 100% all the time. Therefore, AMS allows over-committing available resources. By default, AMS uses a CPU allocation rate of `4` and a memory allocation rate of `2`, which means that it allows four times the number of vCPU cores and twice the amount of RAM per node. See [Configure allocation rates](tbd#configure-allocation-rates) for instructions on how to define the allocation rates for a node.

For example, consider an application that uses the `a2.3` instance type, which requires 2 vCPU cores and 3 GB of memory, and you have a node with 8 CPU cores and 16 GB of memory. Without over-commitment, you could only launch four containers before you run out of resources on the node. However, with a CPU allocation rate of `4` and a memory allocation rate of `2` (the default), the available resources on the node change to `4 * 8 physical CPU cores = 32 vCPU cores` and `2 * 16 GB memory = 32 GB memory`, which will allow up to ten containers on the node.

Which CPU allocation rate makes sense depends on the type of application that you are running and what amount of CPU it needs. For low CPU-intensive applications a higher and for high CPU-intensive applications a lower allocation rate makes sense.

## Application requirements

To realistically estimate the required capacity for your deployment, you must consider the type of application that you're running and the expected usage behaviour.

You should [run benchmarks](https://discourse.ubuntu.com/t/how-to-run-benchmarks/17770) to test your application performance and fine-tune the best node and application configuration. Also consider whether your containers use a hardware or software [video encoder](https://discourse.ubuntu.com/t/application-manifest/24197#video-encoder) for video encoding, and what frame rate and resolution they require.

Another aspect is, of course, how many users you expect and how many containers will be running simultaneously. If you expect the usage to be rather consistent, you might not need to plan for huge peeks in load. On the other hand, you must also consider the impact if your cluster runs out of resources and it is not possible anymore to start more containers.

## An example calculation

Let's consider an application that uses the `g4.3` instance type with 4 vCPU cores, 3 GB of RAM, 3 GB of disk space and 1 GPU slot. The application is quite CPU-intensive, which means you should not over-commit resources too much. You expect an average of 100 containers running at the same time, with peeks up to 200.

We now want to determine the capacity that is needed for the overall deployment. This capacity can be either for a single machine (which is rather unlikely for the given requirements) or for a cluster with multiple nodes.

Without over-commitment, you would require the following resources to fulfil the average demand of 100 containers:

- vCPU cores: `100 * 4 = 400`
- RAM: `100 * 3 GB = 300 GB`
- Disk space: `100 * 3 GB = 300 GB`
- GPU slots: `100 * 1 = 100`

With a CPU allocation rate of 2, you can bring the requirement of 400 vCPU cores down to 200 cores. With a CPU allocation rate of 4, the requirement would be reduced to 100. With a memory allocation rate of 2, you can bring the memory requirement down to 150 GB:

- vCPU cores: `100 * 4 = 400` - with CPU allocation rate 2: `200`
- RAM: `100 * 3 GB = 300 GB` - with memory allocation rate 2: `150 GB`
- Disk space: `100 * 3 GB = 300 GB`
- GPU slots: `100 * 1 = 100`

The current calculation does not take into account that there might be peeks of up to 200 simultaneous containers. To cover all peeks, you would require the following resources:

- vCPU cores: `200 * 4 = 800` - with CPU allocation rate 2: `400`
- RAM: `200 * 3 GB = 600 GB` - with memory allocation rate 2: `300 GB`
- Disk space: `200 * 3 GB = 600 GB`
- GPU slots: `200 * 1 = 200`

To avoid your cluster running out of resources even at peek loads, you must size it accordingly (or dynamically scale it up and down, see [About clustering](https://discourse.ubuntu.com/t/about-clustering/17765)). If the impact of not being able to provide additional containers at peek loads is rather low, you could compromise on the following factors:

- Use a higher CPU and/or memory allocation rate, which might decrease performance at peek loads.
- Configure your cluster nodes to use more GPU slots per GPU, which might decrease video quality.
- Tweak the instance type or the resource specification for your application to give less resources to each container. The impact of doing this depends very much on your application.
- Base your estimate on a lower maximum number of containers (for example, 150), which will lead to your cluster running out of resources before the peek load is reached.
