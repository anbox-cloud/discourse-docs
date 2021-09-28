This page list a few good practices when building addons

### Keep addons light
Addons are executed synchronously, meaning that an addon that performs long-running operations
(e.g.: downloading large files, installing packages on regular containers, query unresponsive services), will
delay when an application can start.

Make use of the `CONTAINER_TYPE` environment variable to only run the necessary code in your hooks.

### Be careful when using global addons
Addons that apply on all applications can be useful, but they can add up quickly.
Try to attach addons to individual applications unless you're absolutely certain you need a global addon and
you're sure it won't slow down containers.

### Cleanup your addons
If your addon needs additional tools and dependencies during its installation, make sure you remove them afterwards.
This will make your addon lighter and all applications using it will start faster.
