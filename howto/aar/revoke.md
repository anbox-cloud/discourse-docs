If a client gets compromised, it's important to block its access to the [Anbox Application Registry (AAR)](https://discourse.ubuntu.com/t/application-registry/17761) by revoking its certificate.

Revoked clients are blocked from accessing the AAR. You'll need to create a new certificate and add it manually for the client to be trusted again.

Use the following command to revoke a certificate:

    aar trust revoke <fingerprint>

[note type="caution" status="Warning"]This operation is irreversible. You cannot reverse a revocation or add the certificate again.[/note]
