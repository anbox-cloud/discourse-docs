Anbox Cloud provides a set of instance types that define the resources available to a container. Often your application may require resources that do not correspond to any of the provided instance types. In such cases, you can override some or all of the resource requirements in your application manifest.

Define the required `cpus`, `memory`, `disk size` values for the `resources` attribute in the application manifest. 

For example, the following application manifest results in allotting 6 vCPU cores, 4 GB memory and 8 GB disk size instead of the standard 4 vCPU cores, 3 GB memory and 3 GB disk size for an `a4.3` instance type.

```yaml
name: my-application
instance-type: a4.3
resources:
  cpus: 6
  memory: 4GB
  disk-size: 8GB
```
If you require a custom number of GPU slots to be assigned to the application, change the `gpu-slots` value for the `resources` attribute in the application manifest.

If you are using the instance type `g6.3` but require 3 GPU slots, use the following application manifest:

```yaml
name: my-GPU-applicaton
instance-type: g6.3
resources:
  gpu-slots: 3
```
## Related information
* [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)
* [Instance types](https://discourse.ubuntu.com/t/application-manifest/24197#instance-type)
