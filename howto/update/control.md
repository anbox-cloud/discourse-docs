For security reasons, you should keep your systems up-to-date at all times. To ensure this, [snaps](https://snapcraft.io/about) update automatically, and the snap daemon is by default configured to check for updates four times a day.

In a production environment, this update behaviour might cause problems in some cases. For example:

- snapd might automatically update the Anbox Cloud Appliance to a version that is not backward compatible.
- snapd might automatically update the snap of a prerequisite that is not compatible with the current version of Anbox Cloud.
- Different nodes of an Anbox Cloud or LXD cluster might end up running different snap versions.

To prevent such problems, use either of the following methods:
* Define maintenance windows in which your systems can be updated without interrupting operations. See [Managing updates](https://snapcraft.io/docs/keeping-snaps-up-to-date) in the snap documentation for information on how to control snap updates on your systems.
* Configure a [Snap Store Proxy](https://docs.ubuntu.com/snap-store-proxy/) to control which snaps are served to the machines that use the proxy. In particular, you can use the proxy to [override snap revisions](https://docs.ubuntu.com/snap-store-proxy/en/overrides). In this method, you have full control over when snaps are updated.
