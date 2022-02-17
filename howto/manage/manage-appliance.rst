:hide-toc:

.. _howto_manage_appliance:

=======================================
How to manage the Anbox Cloud Appliance
=======================================

The Anbox Cloud Appliance comes with a command line tool that you can use to manage the appliance and its components.

Run ``anbox-cloud-appliance --help`` or ``anbox-cloud-appliance <command> --help`` to display usage information for the tool and its commands.

The available commands for the ``anbox-cloud-appliance`` tool are:

``ams``
  Expose the AMS HTTPS service on the public endpoint of the machine on which the appliance is running. If you do this, you can :ref:`control AMS remotely <howto_manage_ams-access>`.

``crashdump``
  Generate a tarball that contains debug information.

``dashboard``
  Manage the web dashboard and access to it. By default, the dashboard is enabled and exposed, but you can disable it. You can also register new users for the web dashboard. See :ref:`howto_manage_web-dashboard_register` for more information.

``destroy``
  If you want to uninstall the Anbox Cloud Appliance, you must first destroy the deployment. Run this command before you uninstall the snap.

  .. warning::
     This command resets the Anbox Cloud Appliance and destroys all data. Execution of the command cannot be undone.

``gateway``
  Expose the HTTP API of the stream gateway and manage access to it. If the HTTP API is exposed, authenticated clients can connect to it. Authentication requires an access token that you can create with the ``account create`` subcommand. See :ref:`howto_stream_access` for more information.

``help``
  Display detailed information about a command.

``init``
  Configure and initialise the Anbox Cloud Appliance. See :ref:`tut_install_app_initialise` for more information.

``monitor``
  Expose the monitoring dashboard. See :ref:`howto_monitor_landing`.

``status``
  Display status information for the Anbox Cloud Appliance.

``upgrade``
  Upgrade the Anbox Cloud Appliance to the latest version. See :ref:`howto_update_upgrade-appliance` for more information.
