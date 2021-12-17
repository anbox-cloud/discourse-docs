:sequential_nav: prev

.. _tut_creating-addon:

===============
Create an addon
===============

This tutorial guides you through the creation of a simple
:ref:`addon <howto_addons_landing>`. The
addon that we create in this tutorial is an example for enabling SSH
access on a container.

1. Write the addon metadata
===========================

In a new ``ssh-addon`` directory, create a ``manifest.yaml`` file with
the following content:

.. code:: yaml

   name: ssh
   description: |
     Enable SSH access when starting a container

2. Add a hook
=============

Next to your ``manifest.yaml`` file in the ``ssh-addon`` directory,
create a ``hooks`` directory. This is where we’ll put the hooks we want
to implement.

Hooks can be implemented in any language, but we are using a bash script
here.

In the ``hooks`` directory, create a ``pre-start`` file with the
following content:

.. code:: bash

   #!/bin/bash

   mkdir -p ~/.ssh
   cat "$ADDON_DIR"/ssh-addon-key.pub >> ~/.ssh/authorized_keys

Make the file executable. To do so, enter the following command (in the
``ssh-addon`` directory):

.. code:: bash

   chmod +x hooks/pre-start

.. tip::
   Supported hooks are ``pre-start``,
   ``post-start`` and post-stop. Read more about them
   :ref:`here <ref_addons-hooks>`.

Create an SSH key in your addon directory and move the private key to a
location outside of the addon directory (for example, your home
directory):

.. code:: bash

   ssh-keygen -f ssh-addon-key -t ecdsa -b 521
   mv ssh-addon-key ~/

Alternatively, you can use an existing key and move the public key into
the addon directory.

3. Create the addon
===================

Your addon structure currently looks like this:

.. code:: bash

   ssh-addon
   ├── hooks
   │   └── pre-start
   ├── manifest.yaml
   └── ssh-addon-key.pub

Create the addon with ``amc`` by entering the following command (in the
directory that contains the ``ssh-addon`` directory):

.. code:: bash

   amc addon add ssh ./ssh-addon

When your addon is created, you can view it with:

.. code:: bash

   amc addon list

4. Use the addon in an application
==================================

Create an application manifest file (``my-application/manifest.yaml``)
and include the addon name under ``addons``:

.. code:: yaml

   name: my-application
   instance-type: a2.3
   addons:
     - ssh

Then create your application:

.. code:: bash

   application_id=$(amc application create ./my-application)
   amc wait "$application_id" -c status=ready

The ``amc wait`` command returns when your application is ready to
launch. You can now launch an instance of your application:

.. code:: bash

   amc launch my-application --service +ssh

.. note::
   The SSH port 22 is closed by
   default. Therefore, we open it by `exposing its service <https://anbox-cloud.io/docs/howto/container/expose-services>`_.

You can now access your container via SSH:

.. code:: bash

   ssh -i ~/ssh-addon-key root@<container_ip> -p <exposed port>

.. note::
   The exposed port can be found be
   running ``amc ls``, under the ``ENDPOINTS`` column. Exposed ports
   usually start around port 10000.

More information about addons
=============================

-  :ref:`ref_addons`
-  :ref:`howto_addons_update`
