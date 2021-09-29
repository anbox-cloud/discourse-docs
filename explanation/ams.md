The Anbox Management Service (AMS) sits at the heart of Anbox Cloud and handles all aspects of the application and container life cycle. It is responsible for managing containers, applications, addons, updates and more, ensuring high density, performance and fast container startup times.

AMS is usually managed through the command line interface (the Anbox Management Client - AMC), which can run either on the same machine as AMS or on a remote machine.

Since AMS exposes an HTTP interface, any tool can use the [AMS HTTP API](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801) to interact with AMS. Both the AMC (when running remotely) and the [Anbox Application Registry (AAR)](https://discourse.ubuntu.com/t/application-registry/17761) use this mechanism. You can also develop your own client by using the [AMS SDK](https://discourse.ubuntu.com/t/ams-sdk-api-reference/17845).

<a name="security-certificates"></a>
## Security certificates for remote clients

Talking with AMS through HTTP requires a secure and trusted setup for communications, using TLS and [certificates](https://en.wikipedia.org/wiki/X.509).

> **NOTE:** The AMC running on the same machine as AMS communicates with AMS through a socket, not through HTTP. Therefore, you do not need to worry about security certificates for local clients.

You can generate self-signed certificates or use certificates signed by a Certificate Authority.

### Self-signed certificates

This option is more straightforward to set up than CA certificates, but it requires every new self-signed client certificate to be added to AMS manually.

AMC automatically generates a self-signed certificate the first time it is invoked. You must add this certificate to AMS before you can use AMC to access AMS remotely.

### Certificate Authority (CA)

This option is best suited if you have multiple clients connecting to AMS, because you only need to configure AMS to trust a single certificate.

After adding the CA certificate to AMS, any client certificates that are generated off the CA certificate are trusted as well.

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

## Custom clients

As an alternative to using AMC, you can develop a custom client built around your own needs using the [AMS HTTP API](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801).

You can access AMS either by IP or through a UNIX socket. The IP depends on your network, but the UNIX socket will always be located at `/var/snap/ams/common/server/unix.socket` on the machine that hosts AMS.

> **Hint:** If your client requires the AMS certificate, you can find it in `/var/snap/ams/common/server/ams.crt`.

## Remote access to AMS

See [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774) for instructions on how to set up an Anbox Management Client on a separate machine and configure it to remotely connect to AMS.
