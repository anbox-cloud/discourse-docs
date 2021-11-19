.. _howto_addon_landing:

==========
Use addons
==========

Addons can be used to customise the images used for the containers. An
addon has :ref:`hooks <reference_addons-hooks>`
that are invoked at various points in the life cycle of a container.
Addons are created independently and can be attached to individual
applications.

See :ref:`reference_addons` for more
information and a complete reference on addons. Follow the :ref:`tutorial_creating-addon`
tutorial to learn how to write a simple addon.

You can use addons to, for example: - Enable SSH access for automation
tools (see :ref:`tutorial_creating-addon`) - Set
up user-specific data when starting an application (see :ref:`Restore data <howto_addon_backup-and-restore-restore>`)
- Install additional tools in the container (see :ref:`howto_addon_install-tools-in-container`) -
Back up data when the container is stopping (see :ref:`howto_addon_backup-and-restore`) -
Configure the Android system before running the application (see
:ref:`howto_addon_customize-android`)
- Provide support for other platforms (see :ref:`howto_addon_additional-architecture`)

If you have used addons before Anbox Cloud 1.12, see the :ref:`migration guide <howto_addon_migrate-from-old-addons>`
to update your addons to use the new hooks.


.. toctree::
   :titlesonly:

   Enable globally <apply-to-all-applications>
   update
   Migrate from previous versions <migrate-from-old-addons>
   install-tools-in-container
   backup-and-restore
   customize-android
   additional-architecture
   Best practices <best-practices>
