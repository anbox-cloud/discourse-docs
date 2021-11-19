.. _howto_monitor_grafana:

===========
Use Grafana
===========

If you added metrics collection support to your Anbox Cloud installation
you can access the `Grafana <https://grafana.com/>`_ service to get
your first insight into the active cluster.

Grafana is a tool for analytics and monitoring that allows to query,
visualize or alert based on the metrics of the cluster or individual
containers.

Every cluster LXD node contains a running Telegraf instance gathering
machine metrics. Besides, Anbox containers existing in that node also
report their metrics to that same Telegraf instance.

Grafana takes its data by considering the Telegraf instances as metrics
targets and polls for new content

.. figure:: /images/grafana.png
   :alt: Grafana

   Grafana

Access Grafana
==============

Open your favourite browser and type:

::

   https://[Apache_IP]/grafana

where *Apache_IP* is the IP of the machine the ``grafana-proxy``
application is deployed to.

You can check the Apache IP in a juju status output executed from
command line:

.. code:: bash

   $ juju status

Once entered the above URL, You are now redirected to the login page
requiring to enter user and password. In order to obtain the
administrator credential open a console and type:

.. code:: bash

   $ juju run-action --wait grafana/0 get-admin-password

.. note::
   You have to replace the ``0`` in
   ``grafana/0`` with the unit version of the installed grafana juju
   unit.

You should obtain a response like:

.. code:: yaml

   unit-grafana-0:
     id: 29f07367-556b-41d0-8318-b9fa13a78b63
     results:
       password: jd673zyYWkR7kyPW
     status: completed
     timing:
       completed: 2018-06-29 13:29:38 +0000 UTC
       enqueued: 2018-06-29 13:29:36 +0000 UTC
       started: 2018-06-29 13:29:38 +0000 UTC
     unit: grafana/0

From that response we get the password to login. In the browser on the
Grafana website you can now type in the credentials:

.. code:: yaml

   User: admin
   Password: jd673zyYWkR7kyPW

.. note::
   The value ``jd673zyYWkR7kyPW`` is
   illustrative. Replace it by the one received as response to the juju
   run-action command.
