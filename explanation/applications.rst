.. _explanation_applications:

==================
About applications
==================

Applications are one of the main objects AMS manages. A single
application encapsulates one Android APK (`Android Package Kit <https://en.wikipedia.org/wiki/Android_application_package>`_) and
manages it within the cluster. It takes care of installing the supplied
APK, to make it available to users. Further, AMS manages updates to
existing applications, which includes allowing the operator to test new
uploaded versions before making them available to any users.

Application requirements
========================

To run on the Anbox Cloud platform, applications must fulfil a set of
requirements. These are:

-  The application **SHOULD** not download any additional resources on
   regular startup to contribute to short startup times. If additional
   resources need to be downloaded, this can be done during the
   application bootstrap phase.
-  The application **MUST NOT** require the **Google Play services** to
   be available as Anbox Cloud does not include them.

If the application fulfils all of the requirements above, it is ready to
run on the Anbox Cloud platform. If not, please file a `bug report <https://bugs.launchpad.net/indore-extern/+filebug>`_ so that we
can find out what we can do to still support the application.

.. _explanation_applications-bootstrap:

Bootstrap process
-----------------

When :ref:`creating an application <howto_application_create>`
either from a directory or a tarball, AMS will perform a bootstrap
process, which builds the application and synchronises it across all LXD
nodes in the cluster. There are major benefits the bootstrap process
provides:

-  It enables AMS to launch a container for an application without
   installing the APK every time.
-  It dramatically speeds up the startup time of a regular container.

Furthermore, an application is synchronised within the LXD cluster,
which enables AMS to continue to work when nodes are being removed from
the cluster through :ref:`scaling down <howto_cluster_scale-down>`
or lost from the cluster unexpectedly.

A temporary base container is created and used for the bootstrapping
during the application creation. For example, you might see the
following output for ``amc ls`` right after creating an application:

.. code:: bash

   +----------------------+-------------+------+----------+------+---------------+-----------+
   |          ID          | APPLICATION | TYPE |  STATUS  | NODE |    ADDRESS    | ENDPOINTS |
   +----------------------+-------------+------+----------+------+---------------+-----------+
   | bq78a3oj1qm02cebmof0 |    candy    | base | prepared | lxd0 | 192.168.100.2 |           |
   +----------------------+-------------+------+----------+------+---------------+-----------+

In general, the bootstrap process goes through the following steps in
order:

1. Configure the network interface and gateway.
2. Apply any pending Ubuntu system security updates.
3. Install :ref:`addons <reference_addons>`
   listed in the application manifest file.
4. Run the ``pre-start`` hook provided by each addon listed in the
   application manifest.
5. Launch the Android container.
6. Install the APK provided by the application.
7. Grant the application permissions as requested in the application
   manifest.
8. Install the extra data as listed in the application manifest.
9. Execute the ``post-start`` hook provided by each addon listed in the
   application manifest.

.. figure:: upload://bZZCt9U0YVBYD4le9S9TInMSvE9.png
   :alt: Application bootstrap process|571x653

   Application bootstrap process|571x653

If one of the steps fails, AMS will interrupt the bootstrap process and
make the entire process fail. As a result, the status of the base
container will be marked with ``error`` and the application’s status
will end up with ``error`` as well.

.. note::
   An application crash or ANR upon
   APK installation will cause the bootstrap process to terminate
   abnormally and the status of application is set to ``error`` too.

When a base container runs into an error status, you can see what has
gone wrong there by checking the error message with
``amc show <application ID>``:

.. code:: bash

   id: bq78a3oj1qm02cebmof0
   name: ams-bq78a3oj1qm02cebmof0
   status: error
   node: lxd0
   created_at: 2019-08-09T02:11:33Z
   application:
       id: bq6ktjgj1qm027q585kg
   network:
       address: ""
       public_address: ""
       services: []
   stored_logs:
   - container.log
   - system.log
   - android.log
   error_message: 'Failed to install application: com.foo.bar: Failed to extract native libraries, res=-113'
   config: {}

Alternatively, :ref:`check the container logs <howto_container_logs>`
to troubleshoot problems in the container.

When the application bootstrap succeeds, the base container is
automatically removed and the status of the application changes to
``ready``. The application is then ready to be used.

Managing applications
=====================

See the following documentation for instructions on how to manage your
applications:

-  :ref:`howto_application_create`
-  :ref:`howto_application_wait`
-  :ref:`howto_application_update`
-  :ref:`howto_application_resources`
-  :ref:`howto_application_delete`
-  :ref:`howto_application_list`
-  :ref:`howto_application_test`
-  :ref:`howto_application_virtual-devices`
