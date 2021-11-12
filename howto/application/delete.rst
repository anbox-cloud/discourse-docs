.. _howto_application_delete:

=====================
Delete an application
=====================

When an application is no longer needed, it can be fully removed from
Anbox Cloud. Removing an application will cause all of its versions to
be removed, including all of its currently active containers. Be extra
careful as this might affect your users if any are still using
containers of the application you want to remove.

Once you’re sure you want to remove the application, you can do so with
the following command:

::

   amc application delete bcmap7u5nof07arqa2ag

The command will ask for your approval before the application is
removed. If you want to bypass the check, you can add the ``--yes`` flag
to the command.
