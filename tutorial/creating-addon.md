This tutorial will guide you through the creation of a simple addon that enables SSH access on a container.

### 1. Write the addon metadata
In a new `ssh-addon` directory, create a `manifest.yaml` file with the following content
```yaml
name: ssh
description: |  
  Enable SSH access when starting a container
```

### 2. Add a hook
Next to your `manifest.yaml` file, create a `hooks` directory. This is where we'll put the hooks we want to implement.
Hooks can be implemented in any language, but we are using a bash script here.

Create a new `pre-start` file under the `hooks` directory with the following content
```bash
#!/bin/bash

mkdir -p ~/.ssh
cat "$ADDON_DIR"/ssh-addon-key.pub >> ~/.ssh/authorized_keys
```

And make it executable
```bash
chmod +x hooks/pre-start
```

> INFO: supported hooks are: `pre-start`, `post-start` and `post-stop`. Read more about them [here](TODO: INSERT LINK TO ADDON REFERENCE)

Create a new SSH key (you can use an existing key) in your addon directory.
```bash
ssh-keygen -f ssh-addon-key -t ecdsa -b 521
mv ssh-addon-key.pub ssh-addon/
```


### 3. Create the addon
Your addon structure currently looks like this:
```bash
ssh-addon
├── hooks
│   └── pre-start
├── manifest.yaml
└── ssh-addon-key.pub
```  

Create the addon with `amc`:
```bash
amc addon add ssh ./ssh-addon
```

When your addon is created, you can view it with
```bash
amc addon list
```

### 4. Use the addon in an application
Create an application manifest to include the addon name under `addons`

```yaml
name: my-application
instance-type: a2.3
addons:
  - ssh
```

Then create your application
```bash
application_id=$(amc application create ./my-application)
amc wait "$application_id" -c status=ready
```

The `amc wait` command returns when your application is ready to launch.  
You can now launch an instance of your application.
```bash
amc launch my-application --service +ssh 
```
> NOTE: port 22 (ssh) is closed by default. We open it via services. Read more about services [here](https://anbox-cloud.io/docs/howto/container/expose-services)

You can now access your container via ssh.
```bash
ssh -i ssh-addon-key root@<container_ip> -p <exposed port>
```

[note type="information" status="Note"] The exposed port can be found be running `amc ls`, under the `ENDPOINTS` column. Exposed ports usually start around port 10000.[/note]

## More information about addons

* [Addon reference](link to addon reference)
* [Updating addons](link to updating addons)