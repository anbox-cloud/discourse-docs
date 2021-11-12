.. _howto_update_control:

===============
Control updates
===============

For security reasons, you should keep your systems up-to-date at all
times. To ensure this, `snaps <https://snapcraft.io/about>`_ update
automatically, and the snap daemon is by default configured to check for
updates four times a day.

In a production environment, this update behaviour might cause problems
in some cases. For example:

-  snapd might automatically update the Anbox Cloud Appliance to a
   version that is not backward compatible.
-  snapd might automatically update the snap of a prerequisite that is
   not compatible with the current version of Anbox Cloud.
-  Different nodes of an Anbox Cloud or LXD cluster might end up running
   different snap versions.

To prevent such problems, you should define maintenance windows in which
your systems can be updated without interrupting operations. See
`Managing updates <https://snapcraft.io/docs/keeping-snaps-up-to-date>`_ in the
snap documentation for information on how to control snap updates on
your systems.
