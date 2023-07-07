Developing and testing addons using the Anbox Management Service (AMS) may be time-consuming. Instead, a container with `--devmode` enabled can provide a safe environment to develop and test addons and their hooks without having to upload the addon to the AMS.

This guide explains how to use a container in development mode to develop and test an addon using Anbox runtime. See [development mode](https://discourse.ubuntu.com/t/17763#dev-mode) to learn more about development mode enabled containers.

## Launch a container in development mode

Start a raw container with `--devmode` enabled:

```
amc launch --devmode --raw
```

The command prints out the ID of the container. Note down the container ID for next steps.

Use the `amc shell <container_id>` command to open a shell inside the container. `container_id` is the container ID from the previous step.

Alternatively, you can use `amc exec <container_id> <command_options>` to directly execute commands inside the container.

## Create an addon within the container

Use the container as a remote environment to develop your addon. To make your addon source available within the container, either copy the addon manifest and hooks using the [`lxc file push`](https://documentation.ubuntu.com/lxd/en/latest/howto/instances_access_files/#push-files-from-the-local-machine-to-the-instance) command or clone a git repository using SSH.

You can test your addon hooks by running it inside the container shell. For example, `ADDON_DIR=$PWD ./hooks/install` can help test if the install hook of the addon works. See [environment variables](https://discourse.ubuntu.com/t/28555#env-variables) for a list of available variables.

To troubleshoot issues within the container, try either of the following options:
* Run `amc logs <container-id>` on the host to see the Anbox runtime logs.
* Run `journalctl --no-pager` within the container to view container logs.
* Restart the container using `amc stop <container_id>` and then `amc start <container_id>`.

## Example: Launch an SSH-enabled container for remote development

```bash
# Launch and obtain the container id
id="$(amc launch --devmode -s ssh --raw)"
# Install the ssh-import-id package
amc exec $id -- apt install -y ssh-import-id
# Import SSH keys for GitHub; Use lp:<user_name> for Launchpad
amc exec $id -- ssh-import-id gh:<user_name>
# Get the <public_address> and <node_port> values of the container
amc show $id --format=json | json_pp
# Connect to the container using SSH
ssh -p <node_port> root@<public_address>
```
Once you are logged in to the container, you can remotely develop and test your addon within the container. For example, see how to [set up VS Code for remote development using SSH](https://code.visualstudio.com/docs/remote/ssh).
