.. _howto_update_upgrade-appliance:

=====================
Upgrade the appliance
=====================

Before you upgrade the Anbox Cloud Appliance, you should make sure all
packages on the machines that are part of the deployment are up-to-date.
To do so, run the following commands on each machine:

::

   sudo apt update
   sudo apt upgrade

The Anbox Cloud Appliance includes an ``upgrade`` command which will
perform all relevant upgrade steps to a newer version of the appliance.
First, run ``anbox-cloud-appliance status`` to check if an update is
available:

::

   status: ready
   update-available: true
   reboot-needed: false

.. important::
   While the upgrade process is
   active API endpoints and the dashboard will not be available. Anbox
   containers will stay active and existing streams will also not be
   interrupted.

In the command output above the ``update-available`` field indicates an
update is available. The upgrade process can now be initiated by running
the ``upgrade`` command:

::

   anbox-cloud-appliance upgrade

The appliance will perform now all necessary steps to upgrade to the
newer available version. You can watch for progress on the web interface

.. figure:: /images/upgrade_appliance_deploy.png
   :alt: Upgrade the appliance

   Upgrade the appliance

or with the ``anbox-cloud-appliance status`` command you used above:

::

   status: maintenance
   progress: 40
   update-available: false
   reboot-needed: true

When the upgrade has finished the appliance is again available for
regular use.
