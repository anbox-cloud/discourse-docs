:hide-toc:

.. _howto_addons_customise-android:

=================================
Example: How to customise Android
=================================

If you need to do any customisation to the Android system that runs your
application, you can use the ``anbox-shell`` tool within a hook. This
tool is useful to interact with the Android system directly.

The following hook configures the Android system to use an HTTP proxy:

.. code:: bash

   #!/bin/sh -ex

   # The settings we change are persistent, so we only need to set them once
   if [ "$CONTAINER_TYPE" = "regular" ]; then
     exit 0
   fi

   anbox-shell settings put global http_proxy myproxy:8080
