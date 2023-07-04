Developing and testing addons using AMS may take a lot of time. Instead, a container with `--devmode` enabled can provide a safe environment to test addons and their scripts without having to upload the addon to the AMS.

This guide explains how to use a container in development mode to develop and test an addon using Anbox runtime. See [development mode](https://discourse.ubuntu.com/t/17763#dev-mode) to learn more about development mode enabled containers.

## Launch a container with `--devmode` enabled

Start a raw container with `--devmode` enabled:

 `amc launch --devmode --raw`

 The command prints out the ID of the container. Note down the container ID for next steps.

 Use the `amc shell <container_id>` command to open a shell inside the container. `container_id` is the container ID from the previous step.

 Alternatively, you can use `amc exec <container_id> <command_options>` to directly execute commands inside the container.

## Develop and test an addon

Use the container as a remote environment to develop your addon. To make your addon source available within the container, either copy the addon manifest and hooks using the [`lxc file push`](https://linuxcontainers.org/lxd/docs/latest/howto/instances_access_files/#push-files-from-the-local-machine-to-the-instance) command or clone a git repository using SSH.

You can test your addon scripts by running it inside the container shell. For example,  `ADDON_DIR=$PWD ./hooks/install` can help test if the install addon works.

To troubleshoot issues within the container, use `amc logs <container-id>` or restart the container using `amc stop <container_id>` and then `amc start <container_id>`.

## Example
The following example launches an SSH enabled raw container in development mode.
```
# Launch and obtain the container id
id=$(amc launch --devmode -s ssh --raw)
# Install the ssh-import-id package
amc exec $id -- apt install -y ssh-import-id
# Import SSH keys for github
amc exec $id -- ssh-import-id gh:<ssh-key>
# Get the <ssh-port>
amc ls
# Connect to the container using SSH
ssh -p <ssh-port> root@<host ip>
# Clone your GitHub repository
git clone <repository-url>
```
Once you are logged in to the container, you can remotely develop and test your addon within the container. For example, see how to [set up VS Code for remote development using SSH](https://code.visualstudio.com/docs/remote/ssh).
