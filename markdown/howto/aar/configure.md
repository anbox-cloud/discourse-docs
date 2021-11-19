The [Anbox Application Registry (AAR)](https://discourse.ubuntu.com/t/application-registry/17761) uses a certificate-based authentication system that uses TLS server and client certificates to establish a trusted connection between the AAR and AMS.

AAR and AMS must exchange certificates to set up a trust relation. The recommended way to do this is with Juju, but it is also possible to do it manually.

## Register an instance using Juju (recommended)

Use [Juju relations](https://jaas.ai/docs/relations) to register an instance with the AAR.

To register an instance as client, use the following command:

    juju add-relation aar:client ams:registry-client

To register an instance as publisher, use the following command:

    juju add-relation aar:publisher ams:registry-publisher

[note type="information" status="Hint"]Run `amc config show` to check that the AAR configuration items were changed.[/note]

### Register units deployed in another model

For `ams` units deployed in another model, you can make use of [Juju cross model relations](https://juju.is/docs/cross-model-relations).

Enter the following commands:

    juju switch <model containing aar>
    juju offer aar:client

The second command returns the name of the generated offer, for example, `my-controller/my-model.aar`. Continue with the following commands:

    juju switch <model containing ams>
    juju relate ams <offer name>

## Register clients manually

Adding clients manually requires access to the machines hosting AMS and the AAR.

### Configure AMS

The first step is to import the AAR certificate into every AMS instance that should have access to the AAR. You can find the AAR certificate at `/var/snap/aar/common/certs/server.crt` on the machine hosting the AAR. Copy the certificate to the AMS machine and import it with the following command:

    amc config trust add server.crt

Use the following command to verify that the new certificate is listed in the AMS trust store:

    amc config trust list

### Configure AMS to use the AAR

To configure AMS to pull or push applications and new application versions to or from the AAR, you must tell AMS about the registry endpoint first:

    amc config set registry.url https://192.168.178.45:3000

Next, you must tell the AAR client in AMS which certificate it should expect from the AAR to ensure trust between both. For this, we need the fingerprint of the certificate you imported into AMS before. You can find it with the following command:

    amc config trust list

Set the certificate fingerprint with the following command:

    amc config set registry.fingerprint <fingerprint>

Finally, set the interval in which AMS will check for new applications to push or pull to or from the AAR. By default, the interval is set to one hour. You can set it to a smaller interval of five minutes with the following command:

    amc config set registry.update_interval 5m

AMS will now check every five minutes if any updates need to be pushed or pulled to or from the AAR.

### Configure AMS to push applications to the AAR

To tell AMS to push any local applications to the AAR, set the `registry.mode` configuration item to `push`:

    amc config set registry.mode push

All existing and future applications and updates are now automatically pushed to the AAR.

Keep in mind that only published application versions are pushed to the AAR. If you don't publish a version, it will not be pushed.

### Configure AMS to pull applications from the AAR

To tell AMS to pull applications from the AAR, set the `registry.mode` configuration item to `pull`:

    amc config set registry.mode pull

All existing and future applications and updates are now automatically pulled from the AAR.

### Configure the AAR

The AAR provides a CLI called `aar`. You can manage client trust with the `aar trust` subcommand:

```bash
Manage trusted clients

Usage:
  aar trust [command]

Available Commands:
  add         Register a client certificate
  list        List currently trusted clients
  remove      Remove a trusted certificate
  revoke      Revoke a certificate

Flags:
  -h, --help   help for trust

Use "aar trust [command] --help" for more information about a command.
```

Every AMS instance has a registry-specific client certificate that is stored at `/var/snap/ams/common/registry/client.crt`. To manually register an AMS client, you'll need to copy this certificate to the machine hosting AAR and use the CLI to trust it.

Use any of the following commands to do that:

    cat client.crt | sudo aar trust add

    sudo aar trust add client.crt

[note type="information" status="Note"]Due to Snap strict confinement and the AAR sudo requirement, the second method requires certificates to be located in the root user home directory `/root`.[/note]

Finally, reboot the AAR:

    snap restart aar
