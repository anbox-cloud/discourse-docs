The AMS service can be configured to regularly look at an application registry and import any new application versions found there. When a new application version is found AMS starts to import it and once done, makes it available for use. An imported application is immutable and cannot be changed other than through the registry itself. If an application is removed from the registry it is removed from AMS on the next update as well.

AMS can act in two different roles when working with the registry:

* `publisher`
* `client`

The `publisher` role allows both read and write access to the registry. AMS instances registered as clients act in `push` mode and are meant to push new applications and updates of these to the registry so that they can be consumed by regular read-only `clients`.

It is important to note that a single AMS instance can only act as a publisher or as a client, but not both. We recommend you have one publishing AMS instance per architecture, e.g. one for `amd64` and one for `arm64`. These should not be used to host regular containers but only to manage applications. Regular users should be directed to AMS instances acting in `client` mode.

## Register AMS with the Registry
The registry uses a certificate based authentication system which uses TLS server and client certificates to establish a trusted connection between registry and AMS.

Certificates from both the Registry and AMS must be exchanged to setup a trust relation.
This can done easily with Juju (recommanded), or manually.


### Register clients using Juju (recommanded)

Registering a client to the Registry is done via [Juju relations](https://jaas.ai/docs/relations)

```bash
$ juju add-relation aar:client ams:registry-client
```

or to register a publisher

```bash
$ juju add-relation aar:publisher ams:registry-publisher
```

> **Hint:** You can check `amc config show` to see that registry configuration items were changed.


### Register clients manually

Adding clients manually requires access to the machines hosting AMS and the Registry 

#### Configure AMS

The first step is to import the registry certificate into every AMS instance which should have access to the registry. You can find the registry certificate at `/var/snap/aar/common/certs/server.crt` on the machine hosting the registry. Copy the certificate to the AMS machine and import it with the following command:

```bash
$ amc config trust add server.crt
```

You can verify the new certificate is listed in the AMS trust store:

```bash
$ amc config trust list
```

##### Configure AMS to use the Registry

To configure AMS to pull or push applications and new version of these to or from the registry you have to tell AMS about the registry endpoint first:

```bash
$ amc config set registry.url https://192.168.178.45:3000
```

As next step you have to tell the registry client in AMS which certificate it should exepct from the registry to ensure trust between both. For this we need the fingerprint of the certificate you imported into AMS before. You can find it via

```bash
$ amc config trust list
```

Set the certificate fingerprint with the following command:

```bash
$ amc config set registry.fingerprint <fingerprint>
```

As last thing you can set the interval in which AMS will check for new applications to push or pull to or from the registry. By default it is set to one hour. You can set it to a smaller interval of five minutes with the following command:

```bash
$ amc config set registry.update_interval 5m
```

AMS will now check every five minutes if any updates need to be pushed or pulled to or from the registry.

#### Configure AMS to push Applications to the Registry

To tell AMS to push any local applications to the registry you have to set the `registry.mode` configuration item to `push`.

```bash
$ amc config set registry.mode push
```

From now on all existing and future added applications and updates are automatically pushed to the registry.

Please keep in min that only published application versions are pushed to the registry. If you don't publish a version it will not be pushed.

#### Configure AMS to pull Applications from the Registry

To tell AMS to pull applications from the registry you have to set the `registry.mode` configuration item to `pull`.

```bash
$ amc config set registry.mode pull
```

From now on all existing and future added applications and updates are automatically pulled from the registry.

#### Configure the Registry

The Registry provides a CLI called `aar`. You can manage client trust with `aar trust` subcommand.

```bash
$ aar trust --help
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

Every AMS instance has a registry specific client certificate which is stored at `/var/snap/ams/common/registry/client.crt`.
To manually register an AMS client, you'll need to copy this certificate to the machine hosting AAR, and use the CLI to trust it.

```bash
$ cat client.crt | sudo aar trust add
```

or

```bash
$ sudo aar trust add client.crt
```

> **Note:** Due to Snap strict confinement and the Registry sudo requirement, the second method requires certificates to be located in the root user home directory `/root`.

Finally, reboot the registry.

```bash
$ snap restart aar
```

## Revoke clients

In the event a client get compromised, it's important to block its access by revoking its certificate.
Revoked clients are blocked from accessing the registry. You'll need to create a new certificate and add it manually for the client to be trusted again.

```bash
$ aar trust revoke <fingerprint>
```

> **Warning:** This operation is irreversible, you cannot reverse a revocation or add the certificate again
