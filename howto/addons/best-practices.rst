.. _howto_addons_best-practices:

=========================
Best practices for addons
=========================

When building addons, consider the following good practices.

Keep addons light
=================

Addons are executed synchronously. This means that an addon that
performs long-running operations (for example, downloading large files,
installing packages on regular containers or querying unresponsive
services) will delay when an application can start.

Use the ``CONTAINER_TYPE`` environment variable to run only the
necessary code in your hooks.

Be careful when using global addons
===================================

Addons that are enabled for all applications can be useful, but they can
add up quickly. Try to attach addons to individual applications unless
you’re absolutely sure that you need a global addon and it won’t slow
down containers.

Clean up your addons
====================

If your addon needs additional tools and dependencies during its
installation, make sure you remove them afterwards. This will make your
addon lighter and all applications using it will start faster.
