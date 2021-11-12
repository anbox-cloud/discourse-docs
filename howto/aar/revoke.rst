.. _howto_aar_revoke:

====================
Revoke an AAR client
====================

If a client gets compromised, it’s important to block its access to the
:ref:`Anbox Application Registry (AAR) <explanation_aar>` by
revoking its certificate.

Revoked clients are blocked from accessing the AAR. You’ll need to
create a new certificate and add it manually for the client to be
trusted again.

Use the following command to revoke a certificate:

::

   aar trust revoke <fingerprint>

.. warning::
   This operation is irreversible.
   You cannot reverse a revocation or add the certificate again.
