The topics in this guide describe some commonly encountered problems with Anbox Cloud and provide instructions for resolving them. If you encounter an issue with Anbox Cloud, check if any of the following scenarios help in resolving your issue.

* [Troubleshooting issues during initial setup](tbd)
* [Troubleshooting container failures](tbd)
* [Troubleshooting issues when creating an application](tbd)
* [Troubleshooting LXD clustering](tbd)

If you still need help, use the following instructions to collect troubleshooting information from the container and report an issue.

*Applies to: Anbox Cloud, Anbox Cloud Appliance since 1.16.0*

Anbox containers come preinstalled with the `anbox-bug-report` utility, which
collects the log files and other relevant information for a specific container.
To generate the report and save it to a local file, use `amc exec` on a running
container:

```
amc exec <container_id> -- bash -c 'cat "$(anbox-bug-report)"' > "<target_file>"
```

This command builds a zip archive that contains the container report. It then
saves it to the local `<target_file>`. This process might take a few seconds.