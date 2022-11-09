The guides in this section describe how to collect troubleshooting information
from various parts of the Anbox Cloud stack. These guides should be used to
analyse or report issues with Anbox Cloud.

Before you follow the steps outlined in this section, check the instructions for
commonly encountered problems at [How to troubleshoot Anbox
Cloud](https://discourse.ubuntu.com/t/how-to-troubleshoot-anbox-cloud/17837).

## How to collect troubleshooting information from a container

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
