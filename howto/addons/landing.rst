.. _howto_addons_landing:

==========
Use addons
==========

Addons can be used to customise the images used for the containers. An
addon has :ref:`hooks <ref_addons-hooks>`
that are invoked at various points in the life cycle of a container.
Addons are created independently and can be attached to individual
applications.

See :ref:`ref_addons` for more
information and a complete reference on addons. Follow the :ref:`tut_creating-addon`
tutorial to learn how to write a simple addon.

You can use addons to, for example: - Enable SSH access for automation
tools (see :ref:`tut_creating-addon`) - Set
up user-specific data when starting an application (see :ref:`Restore data <howto_addons_backup-and-restore-restore>`)
- Install additional tools in the container (see :ref:`howto_addons_install-tools`) -
Back up data when the container is stopping (see :ref:`howto_addons_backup-and-restore`) -
Configure the Android system before running the application (see
:ref:`howto_addons_customise-android`)
- Provide support for other platforms (see :ref:`howto_addons_emulate-platforms`)

If you have used addons before Anbox Cloud 1.12, see the :ref:`migration guide <howto_addons_migrate>`
to update your addons to use the new hooks.


.. toctree::
   :titlesonly:

   Enable globally <enable-globally>
   update
   Migrate from previous versions <migrate>
   install-tools
   backup-and-restore
   customise-android
   emulate-platforms
   Best practices <best-practices>
