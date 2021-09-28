You can access the `anbox-shell` tool within addons. This tool is useful to
interact with the Android system directly. This example configures the Android system to use an HTTP proxy.

```bash
#!/bin/sh -ex

# The settings we change are persistent, so we only need to set them once
if [ "$CONTAINER_TYPE" = "regular" ]; then
  exit 0
fi

anbox-shell settings put global http_proxy myproxy:8080
```