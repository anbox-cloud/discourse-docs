.. _howto_container_logs:

=======================
View the container logs
=======================

If a container fails to start or a runtime error occurs, AMS collects
relevant log files from the container and makes them available for
inspection.

Available logs can be listed with the ``amc show <container_id>``
command:

.. code:: bash

   id: bh03th0j1qm6416q0v30
   name: ams-bh03th0j1qm6416q0v30
   status: error
   node: lxd0
   created_at: 1970-01-01T00:00:00Z
   application:
     id: bh03tgoj1qm6416q0v2g
   network:
     address: 192.168.100.2
     public_address: 10.226.4.63
     services: []
   stored_logs:
   - container.log
   - system.log
   - android.log
   error_message: 'Failed to install application com.canonical.candy: exit status 1'

The container in this example failed to install the application as
indicated by the ``error_message`` field. There are three log files
being stored which can be shown with the ``amc show-log`` command (for
example, ``amc show-log bh03th0j1qm6416q0v30 system.log``):

.. code:: bash

   -- Logs begin at Thu 2019-01-17 08:37:56 UTC, end at Thu 2019-01-17 08:38:58 UTC. --
   Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd-journald[38]: Journal started
   Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd-journald[38]: Runtime journal (/run/log/journal/2c8dee797148423b8f8987009ee28eab) is 8.0M, max 99.6M, 91.6M free.
   Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd[1]: Starting Flush Journal to Persistent Storage...
   ....
   Jan 17 08:38:57 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:57 Extracting application package ...
   Jan 17 08:38:58 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:58 Waiting for Android container
   Jan 17 08:38:58 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:58 Installing application com.canonical.candy from app.apk ...

.. note::
   AMS does not support runtime log
   collection. Logs are currently only being collected from a container
   which failed to start or had an error at runtime.
