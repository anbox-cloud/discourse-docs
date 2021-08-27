AMS exposes an HTTP interface. Clients can be anything, whether it's the CLI (amc), the registry (aar) or any client you developed yourself.
However, talking with AMS **requires** a secure and trusted setup for communications with **TLS** and [certificates](https://en.wikipedia.org/wiki/X.509).

## Managing certificates

Through AMS eyes, every client is similar. To establish communication, AMS needs the client certificates, and the client needs AMS certificate.

You can generate certificates using a Certificate Authority or via openssl and self signing it. The former is better suited for multiple clients while the latter is more straight forward.

### Option 1: Certificate Authority (CA)

Certificates authorities are useful for larger teams as you only need to trust a single certificate. 

```text
                         +-----+
                         | CA  |
           +-------------+--+--+-------------+
           |                |                |
    +------v------+  +------v------+  +------v------+
    | Certificate |  | Certificate |  | Certificate |
    +-------------+  +-------------+  +-------------+

    Trusting a CA trusts all its signed certificates as well
```

To setup you own Certificate Authority, you need to generate its own certificate and key

```bash
$ openssl genrsa -out ca.key 2048
$ openssl req -new -x509 -key ca.key -out ca.crt -days 1024
```

and tell AMS to trust it and verify all subsequents certificates.

```bash
$ amc config trust add ca.crt
```


### Option 2: Self signed certificate

Every new self signed certificates you create has to be manually added to AMS.

You can use the following command to generate a simple key pair:

> **NOTE:** Don't set a password for the key as `amc` wont be able to make use of it otherwise.

```bash
$ openssl req -nodes -x509 -newkey rsa:4096 -keyout anbox-cloud.key -out anbox-cloud.crt -days 365
```

And tell `ams` to trust it:

```bash
$ amc config trust add anbox-cloud.crt
```


## Using the certificate on clients

To finalize the setup, you have to tell your client to use the newly trusted certificate.

For `amc`, place the certificate in `$HOME/snap/ams/current/client/client.crt` and the key in `$HOME/snap/ams/current/client/client.key`.

For your client, it depends on the language and framework used.  

## Installing the AMC client on a separate machine

If you want to access AMS from a separate machine you have to install the AMC command line client.

You can install the AMC client with the following command:

```bash
$ snap install amc
```

You'll have to generate a certificate as indicated above, register it with `ams`, and point `amc` to it:

```bash
$ amc remote add <your remote name> https://<IP adddress of the AMS machine>:8444
```

> **Hint:** If you haven't changed the port AMS is listening on, it's 8444 by default.

The command will now connect to AMS and show you the fingerprint of the server certificate. If it matches what you expect, acknowledge the fingerprint by typing "yes" and the new remote is successfully added.

To switch to the new remote you can now run

```bash
$ amc remote set-default <your remote name>
```

All invocations of the `amc` command will from now on use the new remote.

## Custom clients

While `amc` provides full use of `ams` features, you can take further advantage of `ams` capabilities by developing a client built around your needs using `ams` [REST API](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801).

`ams` can be access either by IP or unix socket.
The IP depends on your network, but the unix socket will always be located at `/var/snap/ams/common/server/unix.socket` on the machine hosting `ams`.

> **Hint:** If your client requires it, you can find the certificate for AMS in `/var/snap/ams/common/server/ams.crt`.

