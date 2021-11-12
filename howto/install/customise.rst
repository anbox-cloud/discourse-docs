.. _howto_install_customise:

==========================
Customise the installation
==========================

The :ref:`Deploy Anbox Cloud with Juju <howto_install_deploy-juju>`
documentation explains how to perform a quick and easy general install
of Anbox Cloud. However, in some cases it may be useful to customise the
installation:

-  Deploying on bare metal
-  Adding additional components
-  Configuring storage or networking
-  Copying an existing configuration
-  Testing a pre-release version

…and many more. This part of the documentation will help you with this.

What You Will Need
==================

The rest of this page assumes you already have Juju installed and have
added credentials for a cloud and bootstrapped a controller. If you
still need to do this, please take a look at the :ref:`Deploy Anbox Cloud with Juju <howto_install_deploy-juju>`,
or, for custom clouds (OpenStack, MAAS), please consult the `Juju documentation <https://jaas.ai/docs>`__. In case that you want to deploy
on bare metal, please have a look below.

Before you start, please make sure you read about the
:ref:`requirements <requirements>`
Anbox Cloud has.

.. _howto_install_customise-available-juju-bundles:

Available Juju Bundles
======================

To deploy Anbox Cloud, two different Juju bundles exist:

-  **anbox-cloud**: This provides the full Anbox Cloud stack, including
   support for streaming
   (`bundle.yaml <https://api.jujucharms.com/charmstore/v5/~anbox-charmers/bundle/anbox-cloud/archive/bundle.yaml>`__)
-  **anbox-cloud-core**: This provides just the core elements of Anbox
   Cloud.
   (`bundle.yaml <https://api.jujucharms.com/charmstore/v5/~anbox-charmers/bundle/anbox-cloud-core/archive/bundle.yaml>`__)

Each bundle as different requirements you can learn about
:ref:`here <requirements>`.

If you don’t have any need for streaming the visual output of the
Android containers you can use the **anbox-cloud-core** bundle,
otherwise you’ll need the **anbox-cloud** bundle. However, even without
the streaming stack there are still ways to get visual access for
inspection purposes. See :ref:`howto_container_access` for
more details.

Manual Deployment
=================

If you don’t want to use any public cloud, MAAS or OpenStack you can
also use the `manual cloud provider <https://jaas.ai/docs/manual-cloud>`_ Juju offers. This allows
you to deploy Anbox Cloud with Juju on a set of SSH connected machines.

As preparation you need to dedicate one machine as the Juju controller.
You can bootstrap the controller onto that machine via

.. code:: bash

   $ juju bootstrap manual/<user>@<controller IP address> anbox-cloud

Juju will connect to the machine via SSH as the specified user and
install all necessary things.

Once the controller is setup we need to create a model we can deploy
Anbox Cloud into:

.. code:: bash

   $ juju add-model main

Before we can deploy Anbox Cloud, we have to add all necessary machines.
Please have a look at the :ref:`installation requirements <requirements>`
for the different machines you need.

To make things easier later on, please add the machines in the exact
same order as mentioned in the :ref:`installation requirements <requirements>`.
For the ``anbox-cloud-core`` bundle this looks like this:

.. code:: bash

   $ juju add-machine ssh:ubuntu@192.168.1.9
   $ juju add-machine ssh:ubuntu@192.168.1.10

And for the ``anbox-cloud`` bundle:

.. code:: bash

   $ juju add-machine ssh:ubuntu@192.168.1.9
   $ juju add-machine ssh:ubuntu@192.168.1.10
   $ juju add-machine ssh:ubuntu@192.168.1.11
   $ juju add-machine ssh:ubuntu@192.168.1.12

.. hint::
   \ ``ubuntu`` is the user that can
   ssh to these machines, it can be another depending on how the operating
   system on the machines is setup. The user needs to have administrator
   rights on the machine.

.. warning::
   Please make sure that you add the
   machine by their IP address rather than a DNS name. Adding a machine by
   its DNS name does currently not working and will be fixed with a future
   version of Anbox Cloud.

Juju now starts to add the machines to its list of usable machines. Take
care that all are in the ``started`` state before you proceed. If any of
them is still in ``down`` state, please wait until they switch to
``started``. You can retrieve the list of machines registered with the
Juju controller with the following command:

.. code:: bash

   $ juju list-machines
   Machine  State    DNS            Inst id              Series AZ Message
   0         started  192.168.1.9   manual:192.168.1.9   bionic  Manually provisioned machine
   1         started  192.168.1.10  manual:192.168.1.10  bionic  Manually provisioned machine

Now that the machines are registered with the Juju controller you can
deploy Anbox Cloud. The deployment is entirely handled by Juju and does
not need any further manual involvement other than running the actual
deploy command.

For **anbox-cloud-core**:

.. code:: bash

   $ juju deploy cs:~anbox-charmers/anbox-cloud-core --overlay ua.yaml --map-machines existing,0=0,1=1

For **anbox-cloud**:

.. code:: bash

   $ juju deploy cs:~anbox-charmers/anbox-cloud --overlay ua.yaml --map-machines existing,0=0,1=1,2=2,3=3

To understand the ``map-machines`` parameters, please take a look at
:ref:`Machine mapping <howto_install_customise-machinemapping>` section. If you strictly followed
the instructions above you should have the machines registered correctly
to match the command above.

You can watch the status of the deployment with a command like:

.. code:: bash

   $ watch -c juju status --color --relations=true

.. _howto_install_customise-machinemapping:

Machine Mapping
===============

When executing the deployment instructions you have to map the existing
machines with the ones described in the ``anbox-cloud-core`` or
``anbox-cloud-core`` bundles.

If you don’t remember the existing machines in your model, just type the
command:

.. code:: bash

   $ juju list-machines
   Machine  State    DNS            Inst id              Series  AZ             Message
   0        started  192.168.0.9   i-09a2fdb5e7a2e8385   bionic  localhost-1a   running
   1        started  192.168.0.10  i-00a05065e2768be5d   bionic  localhost-1b   running

The deployment bundle ``anbox-cloud-core`` requires two machines ``0``
and ``1``. ``0`` is supposed to host the AMS service and ``1`` is meant
for LXD. For the ``anbox-cloud`` bundle you need two additional machines
to host the extra services required for streaming. Please see the
:ref:`bundle.yaml <howto_install_customise-available-juju-bundles>` of each bundle for more
details.

The ``--map-machine`` argument for the ``juju deploy`` command maps the
machines defined inside the bundle to those your Juju controller has
registered in the model. See the `Juju documentation <https://jaas.ai/docs/charm-bundles>`__ for more details.

Customising the Deployment
==========================

A number of the scenarios outlined at the start of this document
involved customising the Anbox Cloud install. There are two main ways to
do this:

1. Using overlays in conjunction with the published Anbox Cloud bundle.
2. Editing the bundle file itself.

Using an overlay means you can easily apply your customisation to
different versions of the bundle, with the possible downside that
changes in the structure of new versions of Anbox Cloud may render your
overlay obsolete or non-functional (depending on what exactly your
overlay does).

Saving a copy of the bundle file and editing that means that your
customisation will always work, but of course, requires that you create
a new file for each version of Anbox Cloud.

Both methods are described below.

Using Overlays
--------------

A *bundle overlay* is a fragment of valid YAML which is dynamically
merged on top of a bundle before deployment, rather like a patch file.
The fragment can contain any additional or alternative YAML which is
intelligible to Juju. For example, to specify custom instance types for
the machines used in your cloud of choice, the following fragment could
be used:

.. code:: bash

   $ cat overlay.yaml
   machines:
   '0':
     series: bionic
     constraints: "instance-type=m4.xlarge root-disk=40G"
   '1':
     series: bionic
     constraints: "instance-type=m4.xlarge root-disk=40G"
   '2':
     series: bionic
     constraints: "instance-type=g3s.xlarge root-disk=50G"
   '3':
     series: bionic
     constraints: "instance-type=m4.xlarge root-disk=40G"

Juju’s bundle format, and valid YAML are discussed more fully in the
Juju documentation. In this example it merely selects a specific
instance-types for the different machines.

To use this overlay with the Anbox Cloud bundle, it is specified during
deploy like this:

.. code:: bash

   $ juju deploy anbox-cloud --overlay ua.yaml --overlay ~/path/overlay.yaml

Substitute in the local path and filename to point to your YAML
fragment.

Changing Configuration Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration settings are mapped to “options” under the charm entries
in the bundle YAML. Usually these are only expressed when they differ
from the default value in the charm. For example, if you look at the
fragment for *anbox-stream-gateway* in the *anbox-cloud* bundle:

.. code:: yaml

   anbox-stream-gateway:
     charm: cs:~anbox-charmers/anbox-stream-gateway-23
     expose: true
     num_units: 1
     options:
       enable_dev_ui: true
       prometheus_port: 10001
       use_insecure_tls: true
     to: ['0']

There are a few entries under ``options``, in this case to enable the
development UI and point Prometheus at a specific port. There are
however, a number of configuration options available (more details are
in `the charm documentation <https://jaas.ai/u/anbox-charmers/anbox-stream-gateway/64>`_).
We can add additional configuration by supplying the desired settings
under options. So, for example, where we might do the following through
Juju to set some proxy values:

.. code:: bash

   $ juju config anbox-stream-gateway https_proxy=https://proxy.example.com
   $ juju config anbox-stream-gateway snap_proxy=https://snap-proxy.example.com

… we can instead use the following YAML fragment as an overlay:

.. code:: yaml

   anbox-stream-gateway:
     options:
       https_proxy: https://proxy.example.com
       snap_proxy: https://snap-proxy.example.com

If we save the overlay as ``proxy.yaml`` we can now use it for the
deployment:

.. code:: bash

   $ juju deploy anbox-cloud --overlay ~/path/proxy.yaml

Editing a Bundle
----------------

Another way to change or customise an install is to store the YAML
bundle file locally and edit it with a standard text editor.

The latest version of the Anbox Cloud bundles can always be retrieved by
fetching the current stable version from the Juju Charm Store. See
:ref:`Available Juju Bundles <howto_install_customise-available-juju-bundles>` for more details.

Care should be taken when editing the YAML file as the format is very
strict. For more details on the format used by Juju, see the `Juju bundle documentation <https://docs.jujucharms.com/stable/en/charms-bundles>`_.

Retrieving a bundle from a running model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes a more convenient way of getting a local bundle file which
matches exactly the deployment you want is simply to save a running
model as a bundle. This will preserve configuration, relations and the
charms used in the deployment so a structural replica can be recreated.

This can be done simply by running the command:

.. code:: bash

   $ juju export-bundle --filename mybundle.yaml

The resulting YAML file will be downloaded to the current working
directory.

It is also possible to view, edit and export bundles from the Juju GUI:

.. code:: bash

   $ juju gui

Running this command will output some login information and a URL for
the GUI interface (the GUI actually runs on the Juju controller
instance). On visiting the URL given and logging in, a graphical
representation of the current model will be shown. To export the model
as a YAML bundle, click on the **Export** button near the top left of
the screen.

.. figure:: upload://bXqb0LwD7EBZDwL18CsZSBZqL5r.png
   :alt: Anbox Cloud - Juju GUI|690x444

   Anbox Cloud - Juju GUI|690x444

For more information on the Juju GUI, see the `Juju documentation <https://juju.is/docs/olm/accessing-the-dashboard>`__.
