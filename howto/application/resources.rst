.. _howto_application_resources:

=============================
Configure available resources
=============================

Anbox Cloud provides a set of :ref:`instance types <reference_instance-types>`
that define the resources available to a container. For example, if you
start a container for an application that uses the instance type
``a4.3``, the container is assigned 4 vCPU cores, 3 GB of RAM and 3 GB
of disk space.

If your application requires resources that do not correspond to any of
the provided instance types, you can override some or all of the
resource requirements in your :ref:`application manifest <reference_application-manifest>`.

For example, if you are using the instance type ``a4.3`` but require 5
GB of disk space, use the following application manifest:

::

   name: my-application
   instance-type: a4.3
   resources:
     disk-size: 5GB

See
:ref:`Resources <reference_application-manifest-resources>`
for more information about how to use the ``resources`` directive to
override the resources defined by the instance type in the application
manifest.
