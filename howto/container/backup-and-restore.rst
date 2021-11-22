.. _howto_container_backup-and-restore:

====================================
Back up and restore application data
====================================

Backup and restoration of application data can be achieved easily with
the ``aam`` (Anbox Application Manager) utility helper installed in the
image. The ``aam`` can bundle any necessary application data together
into a tarball file or uncompress the tarball file to a particular
application folder according to the specified package name.

Back up application data
========================

See the following script for an example for backing up your data:

.. code:: bash

    #!/bin/sh -ex
   aam backup com.canonical.candy
   TARBALL_FILE=$(basename $(find ./ -name *.tar.bz2))
    # Upload the tarball to public or private cloud storage service
   curl -i -X POST --data-binary @"${TARBALL_FILE}" <cloud_storage_upload_url>

Running this script in an :ref:`addon post-stop hook <howto_addons_backup-and-restore>` will
back up the user data of a particular application with ``aam`` and
upload the resulting tarball file to the cloud storage service when a
container is stopped.

If
:ref:`boot-package <ref_application-manifest>`
is specified in the application manifest file, you can also back up the
boot application data simply with the flag ``--boot-package``.

::

   aam backup --boot-package

``aam`` will automatically query the boot package name from the
container and back up the relevant application data. As result ``aam``
will create a tarball file with the name ``<package name>.tar.bz2``.

Restore application data
========================

The application data can be restored with the following :ref:`pre-start hook <howto_addons_backup-and-restore-restore>`
when a container is up and running:

.. code:: bash

   #!/bin/sh -ex
   # Download the tarball from public or private cloud storage service
   if curl -o app-data.tar.bz2 <cloud_storage_download_url> ; then
     aam restore -p app-data.tar.bz2 com.canonical.candy
   fi

Or by relying on the boot package of the container:

::

   aam restore -p app-data.tar.bz2 --boot-package

Filter data to be backed up
===========================

Sometimes, not every piece of data is useful (for example, cache), and
backing up the entire application data takes a long time and occupies
more disk space if the application data is large. ``aam`` supports two
filters to back up files that match wildcard patterns:


.. list-table::
   :header-rows: 1

   * - Filter
     - Description
   * - ``include``
     - Include files in resulting tarball with a wildcard
   * - ``exclude``
     - Exclude files in resulting tarball with a wildcard


Please refer to the pattern syntax
`here <https://golang.org/pkg/path/filepath/#Match>`__.

For example, with the following filters:

.. code:: bash

   aam backup com.canonical.candy \
      --include=/data/data/com.canonical.candy/cache/*.db \
      --include=/data/data/com.canonical.candy/new_level/fixture* \
      --exclude=/sdcard/Android/data/com.canonical.candy/user_data/*.jpeg \
      --exclude=/data/data/com.canonical.candy/new_level/*.cfg

The resulting tarball file will include the following files:

-  Files with *db* suffix below the folder
   /data/data/com.canonical.candy/cache
-  Files with *fixture* prefix below the folder
   /data/data/com.canonical.candy/new_level

And exclude the following files:

-  Files with *jpeg* suffix below the folder
   /sdcard/Android/data/com.canonical.candy/user_data
-  Files with *cfg* suffix below the folder
   /data/data/com.canonical.candy/new_level
