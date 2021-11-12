.. _howto_container_delete:

==================
Delete a container
==================

A container can be deleted, which will cause any connected user to be
disconnected immediately. The following command deletes a single
container:

::

   amc delete bcqbicqhmss0448iie2g

The ID given is the one of the container you want to delete.

In some cases, it is helpful to delete all containers currently
available. The ``amc`` command provides a ``--all`` flag for this, but
be careful with this!

::

   amc delete --all
