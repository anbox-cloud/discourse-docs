.. _howto_container_wait:

====================
Wait for a container
====================

When launching a container, the container should not be considered
started until it reaches the running state. Sometimes if you want to
interact with the container (with the ``amc shell`` command, for
example), you must wait until the container reaches a ``running``
status.

The ``amc wait`` command allows to wait for a container to reach a
specific condition. If the condition is not satisfied within the
specified time (five minutes by default), a timeout error will be
returned by AMS.

The supported conditions for a container are as follows:


.. list-table::
   :header-rows: 1

   * - Name
     - Value
   * - \ ``app``\ 
     - Application name or ID
   * - \ ``type``\ 
     - Container type, possible values: “base”, “regular”
   * - \ ``node``\ 
     - Node on which the container runs
   * - \ ``status``\ 
     - Container status, possible values: “created”, “prepared”, “started”, “stopped”, “running”, “error”, “deleted”, “unknown”


For example, to wait for the container to reach state ``running``:

::

   amc wait -c status=running bdpaqaqhmss611ruq6kg
