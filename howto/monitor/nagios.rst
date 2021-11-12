.. _howto_monitor_nagios:

==========
Use Nagios
==========

`Nagios <https://www.nagios.org/>`_ is widely used for monitoring
networks, servers and applications. Using the Nagios Remote Plugin
Executor (NRPE) on each node, it can monitor your cluster with
machine-level detail.

Anbox Cloud integrates Nagios and allows you to monitor the status of
its services to be alerted when something goes wrong. The following
services support Nagios:

-  AMS
-  LXD
-  AMS Node Controller
-  Anbox Stream Gateway
-  Anbox Stream Agent
-  Coturn

Deployment
==========

To add Nagios support for either a fresh Anbox Cloud or an existing
deployment, you need to deploy Anbox Cloud along with a Juju overlay
bundle. You can learn more about Juju overlays
`here <https://juju.is/docs/charm-bundles#heading--overlay-bundles>`__.

For Anbox Cloud Core deployment, the overlay bundle used for Nagios
integration is the following:

.. code:: yaml

   applications:
     nagios:
       charm: 'cs:nagios-35'
       expose: true
       num_units: 1
       to:
         - '2'
     nrpe:
      charm: 'cs:nrpe-62'

   relations:
     - ['ams', 'nrpe:nrpe-external-master']
     - ['lxd', 'nrpe:nrpe-external-master']
     - ['ams-node-controller', 'nrpe:nrpe-external-master']
     - ['nrpe', 'nagios']

   machines:
     '0':
       series: bionic
       constraints: "cpu-cores=4 mem=4G root-disk=40G"
     '1':
       series: bionic
       constraints: "cpu-cores=8 mem=16G root-disk=50G"
     '2':
       series: bionic
       constraints: "cpu-cores=2 mem=8G root-disk=10G"

Copy the above code snippet into a ``nagios.yaml`` file, then deploy the
Anbox Cloud Core bundle with the overlay file:

.. code:: bash

   $ juju deploy cs:~anbox-charmers/anbox-cloud-core --overlay nagios.yaml

This will deploy Anbox Cloud Core integrated with Nagios support.

For Anbox Cloud Streaming Stack deployment, the overlay bundle for
Nagios integration is pretty much the same as when you deploy Anbox
Cloud Core with Nagios integration, but with a few more relations added
in the overlay file:

.. code:: yaml

   applications:
     nagios:
       charm: 'cs:nagios-35'
       expose: true
       num_units: 1
       to:
         - '2'
     nrpe:
      charm: 'cs:nrpe-62'

   relations:
     - ['ams', 'nrpe:nrpe-external-master']
     - ['lxd', 'nrpe:nrpe-external-master']
     - ['ams-node-controller', 'nrpe:nrpe-external-master']
     - ['nrpe', 'nagios']
     - ['anbox-stream-gateway', 'nrpe:nrpe-external-master']
     - ['anbox-stream-agent', 'nrpe:nrpe-external-master']
     - ['coturn', 'nrpe:nrpe-external-master']

   machines:
     '0':
       series: bionic
       constraints: "cpu-cores=4 mem=4G root-disk=40G"
     '1':
       series: bionic
       constraints: "cpu-cores=8 mem=16G root-disk=50G"
     '2':
       series: bionic
       constraints: "cpu-cores=2 mem=8G root-disk=10G"

Copy the above code snippet into a ``nagios.yaml`` file, then deploythe
Anbox Cloud Streaming Stack bundle with the overlay file:

.. code:: bash

   $ juju deploy cs:~anbox-charmers/anbox-cloud --overlay nagios.yaml

This will deploy Anbox Cloud Streaming Stack integrated with the Nagios
support.

Access from Web UI
==================

You can now visit the Nagios web interface (port 80 by default) by
getting its IP address:

.. code:: bash

   $ juju status --format yaml nagios/0 | grep public-address

The default username is ``nagiosadmin``. The password is randomly
generated at install time, and can be retrieved by running:

.. code:: bash

   $ juju ssh nagios/0 sudo cat /var/lib/juju/nagios.passwd

Using an existing Nagios service
================================

If you already have an existing Nagios installation, the nrpe charm can
be configured to work with it.

.. code:: bash

   $ juju config nrpe export_nagios_definitions=true
   $ juju config nrpe nagios_master=<ip-address-of-nagios>

See the `External Nagios <https://jaas.ai/nrpe>`_ section of the NRPE
charm readme for more information.
