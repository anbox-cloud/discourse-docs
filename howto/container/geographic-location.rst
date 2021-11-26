.. _howto_container_geographic-location:

=============================
Configure geographic location
=============================

Anbox Cloud allows specifying a geographic location for an Android
container. This location can either be specified statically through a
configuration file or dynamically through the HTTP API.

Set a static location
=====================

To specify a static location for an Android container, configure it in
the ``/var/lib/anbox/static_gps_position`` file within the container.

The location data is constructed in the following format:

::

   <Latitude>,<Latitude in hemisphere>,<Longitude>,<Longitude in hemisphere>

For example:

::

   4807.038,N,1131.001,E

You can find details about the different parts of the location in the
following table.


.. list-table::
   :header-rows: 1

   * - Field
     - Value type
     - Description
   * - Latitude
     - float
     - In the format of ddmm.mm (d refers to degrees, m refers to minutes). For example: 4807.038 = 48 degrees 7.038 minutes
   * - Latitude in hemisphere
     - char
     - Latitude hemisphere ``N`` (northern hemisphere) or ``S`` (southern hemisphere)
   * - Longitude
     - float
     - In the format of ddmm.mm (d refers to degrees, m refers to minutes). For example: 1131.001 = 11 degrees 31.001 minutes
   * - Longitude in hemisphere
     - char
     - hemisphere ``E`` (east longitude) or ``W`` (west longitude)


To make the file ``/var/lib/anbox/static_gps_position`` available to the
Android container, create a file that contains GPS data in the above
format and move that file from ``ADDON_DIR`` to
``/var/lib/anbox/static_gps_position`` via an :ref:`addon pre-start hook <howto_addons_landing>` during
the installation. When an Android container gets started and an
application requests the current location information through the
Android framework, the GPS data is then forwarded from the Anbox session
to the application.

Set the location dynamically
============================

To update the geographic location of an Android container dynamically
while the container is running, use the location endpoint of the Anbox
HTTP API.

See the documentation of the :ref:`PATCH method <ref_anbox-http-api-location-patch>`
for more information and the specification of the data format.
