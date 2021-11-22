.. _ref_ams-configuration:

=================
AMS configuration
=================

AMS provides various configuration items to customize its behavior. The
following lists the available ones and their meaning.


.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - \ ``application.addons``\ 
     - string
     - -
     - Comma separate listed of addons every application managed by AMS should use.
   * - \ ``application.auto_publish``\ 
     - boolean
     - true
     - If set to ``true`` AMS will automatically publish new applications versions when they finished the bootstrap process. ``false`` disables this.
   * - \ ``application.auto_update``\ 
     - boolean
     - true
     - If set to ``true`` AMS will automatically update applications whenever any dependencies (parent image, addons, global configuration) change. ``false`` disables this.
   * - \ ``application.default_abi``\ 
     - string
     - -
     - Default Android ABI applications should use. See https://developer.android.com/ndk/guides/abis for a list of available ABIs
   * - \ ``application.max_published_versions``\ 
     - integer
     - 3
     - Maximum number of published versions per application. If the number of versions of an application is higher, AMS will automatically clean up older versions.
   * - \ ``container.default_platform``\ 
     - string
     - -
     - Set to the platform name Anbox should use by default
   * - \ ``container.features``\ 
     - string
     - -
     - Comma separate list of features to enable (see list below)
   * - \ ``container.security_updates``\ 
     - boolean
     - true
     - If set to ``true`` automatic Ubuntu security updates are applied during the application bootstrap process. ``false`` will disable this.
   * - \ ``core.proxy_http``\ 
     - string
     - -
     - HTTP proxy to use for HTTP requests AMS performs
   * - \ ``core.proxy_https``\ 
     - string
     - -
     - HTTPS proxy to use for HTTPS requests AMS performs
   * - \ ``gpu.allocation_mode``\ 
     - string
     - all
     - \ ``all`` tells AMS to allocate all available GPUs on a system to a container and ``single`` will only allocate a single GPU.
   * - \ ``images.allow_insecure``\ 
     - boolean
     - false
     - If set to true this allow accepting untrusted certificates provides by the configure image server
   * - \ ``images.auth``\ 
     - string
     - -
     - Authentication details for AMS to access the image server. A boolean value will be presented when the item is read indicated if the item is set or not to not expose credentials.
   * - \ ``images.url``\ 
     - string
     - https://images.anbox-cloud.io/stable/
     - URL of the image server to use
   * - \ ``images.version_lockstep``\ 
     - boolean
     - true
     - Put the version of the latest pulled image and the AMS version in a lockstep. This ensures a deployment is not automatically updated to newer image versions if AMS is still at an older version. This only applies for new major and minor but not patch version updates.
   * - \ ``node.queue_size``\ 
     - integer
     - 100
     - Maximum size of the queue containing requests to start and stop container per LXD node. Changing the value requires a restart of AMS
   * - \ ``node.workers_per_queue``\ 
     - integer
     - 4
     - Number of workers processing container start and stop requests. Changing the value requires a restart of AMS
   * - \ ``register.filter``\ 
     - string
     - -
     - Comma separate list of tags to filter for when applications are fetched from the application registry. If empty no filter is applied
   * - \ ``registry.fingerprint``\ 
     - string
     - -
     - Fingerprint of the certificate the registry uses to TLS secure its HTTPS endpoint. Is used by AMS for mutual TLS authentication with the registry
   * - \ ``registry.mode``\ 
     - string
     - pull
     - Mode the registry client in AMS operates in. Possible values are: manual, pull, push
   * - \ ``registry.url``\ 
     - string
     - -
     - URL of the application registry to use
   * - \ ``scheduler.strategy``\ 
     - string
     - spread
     - Strategy the internal container scheduler in AMS is using to distribute container across available LXD nodes. Possible values are: binpack, spread


Features
========

Anbox Cloud includes some features which are not enabled by default but
can be conditionally enabled. The features are enabled by flags which
are configured through AMS. You can configure the feature flags either
globally for all containers or per application.

To configure a feature globally for all containers, use a command
similar to the following:

::

   amc config set container.feature foo,bar

To configure a feature for one application in the manifest, use a syntax
similar to the following:

::

   name: my-app
   instance-type: a4.3
   features: ["foo", "bar"]

System UI
---------

*since 1.10.2*

By default, Anbox hides the Android system UI when an application is
running in foreground mode. In some use cases, however, it’s required to
have the system UI available for navigation purposes. This can be
enabled with the ``enable_system_ui`` feature flag.

The feature flag will be considered by all new launched containers once
set.

Virtual Keyboard
----------------

*since 1.9.0*

The Android virtual keyboard is disabled by default but can be enabled
with the ``enable_virtual_keyboard`` feature flag.

For the feature to be considered, applications must be manually updated,
because changes to allow the feature to work are only applied during the
:ref:`application bootstrap process <exp_applications-bootstrap>`.

Wi-Fi
-----

*since 1.12.0*

Wi-Fi support can be optionally enabled. Anbox will then set up a
virtual Wi-Fi device, which sits on top of an ethernet connection and
simulates a real Wi-Fi connection.

The feature flag will be considered by all newly launched containers
once set.

Android reboot
--------------

*since 1.12.0*

By default, Android is not allowed to reboot. With the
``allow_android_reboot`` feature flag, this can be allowed.

Note that you must disable the
:ref:`watchdog <ref_application-manifest-watchdog>`
if reboots are allowed.

The feature flag will be considered by all newly launched containers
once set.
