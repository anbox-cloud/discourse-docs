Anbox Cloud is built using multiple open source software components. This guide lists those components and where to find their license information.

| Software components | Where to find their licenses |
|--|--|
| LXD images | Within the LXD image, <br/>`/usr/share/licenses` and `/opt/mesa/share/licenses`<br/> The copyright information of Anbox Cloud is available at `/usr/share/doc/*/copyright`. |
| Android | In the Android container, <br/> **Settings** > **About emulated device** > **Legal information** |
| Snaps | On the host system,<br/>`/snap/$snap-name/current/` </br>Replace $snap-name with the name of the Snap.|
| Charms | In the container where the charm is deployed,<br/>`/$path-to-charm/COPYRIGHT` <br/> Replace $path-to-charm with the path where the charm is deployed. Usually the charm is deployed in `/var/lib/juju/agents/unit-*/charm`. |
