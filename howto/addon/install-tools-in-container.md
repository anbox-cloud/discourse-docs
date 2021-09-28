Application images are designed to be as lightweight as possible, and as such, common tools
you might expect to see in a regular cloud image might not be available.

You can use hooks to install packages that you might require for your workload. In this example
we'll install `curl` and `python3`.

Create a new addon with a `pre-start` hook.

```bash
#!/bin/bash -e

# We only need to install things once, when the image is being created, so we
# don't need to execute the hook when users are running the application
if  [ "$CONTAINER_TYPE" = "regular" ]; then
  exit 0
fi

apt update -q
apt install -y curl python3
```

When an application is first created or updated with this addon, both `curl` and `python3` will
be installed and made available for other hooks to use.
