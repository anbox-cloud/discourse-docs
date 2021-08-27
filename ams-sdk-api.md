The Anbox Management SDK offers a set of [Go](https://golang.org/) packages and utilities for any external [Go](https://golang.org/) code to be able to connect to the AMS service through the exposed REST API.

The AMS SDK consist of the following Go packages:

* `client`: The main purpose of this package is to provide a REST client object with methods to manage applications, images, nodes, addons or containers. Each method relates to a specific management operation and wraps the REST calls and listening operations.

* `api`: AMS REST API objects

* `shared`: Helper methods and tools for common tasks like system tasks, certificates, password hashing or websocket dialing.

* `shared/rest/client`: REST client base functionality to wrap common behavior of the various operations of the REST protocol and websocket management for event listening.

* `shared/rest/api`: REST API basic objects, independent of any specific REST implementation.

* `shared/errors`: A simple wrapper for the most commonly-used error implementation in the return of REST API.

* `examples`: A set of examples to demonstrate how the `client` package can be used.


## Install

There are no special instructions to install the AMS SDK. You can simply add the content of the provided SDK zip file into your projects `vendor/` directory or your `GOPATH` and start using it.

## Examples

The SDK comes with a set of examples demonstrating the capabilities of the SDK. You can find them in the `examples` directory of the AMS source.

## Authentication Setup

Clients must authenticate to AMS before communicating with it.
See [client management](https://discourse.ubuntu.com/t/managing-ams-access/17774).

## Custom Client Code

### Connecting to AMS

Main steps for custom code to connect to the service start with the creation of a REST client object. Such object needs a TLS configuration including the client certificate to be sent to AMS and the server certificate the client trusts. There are many ways of creating a TLS configuration in go. AMS SDK provides an easy solution involving a few lines of code:

```go
import (
    "flag"
    "net/url"
    "os"

    "github.com/CanonicalLtd/ams/client"
    "github.com/CanonicalLtd/ams/shared"
)

func main() {
    flag.Parse()
    if flag.NArg() == 0 {
        fmt.Println("Please provide AMS service URL")
        os.Exit(1)
    }

    serviceURL := flag.Arg(0)
    u, err := url.Parse(serviceURL)
    if err != nil {
        fmt.Println("Failed to parse AMS service URL")
        os.Exit(1)
    }

    serverCert, err := shared.GetRemoteCertificate(serviceURL)
    if err != nil {
        fmt.Println("Failed to get remote certificates")
        os.Exit(1)
    }

    tlsConfig, err := shared.GetTLSConfig(clientCert, clientKey, "", serverCert)
    if err != nil {
        fmt.Println("Failed to get TLS config")
        os.Exit(1)
    }

    ...
}
```

> **Note:** Here, we take any server certificate as valid. In case you want a better compromise on the client side with the server certificate to trust, you simply have to replace `shared.GetRemoteCertificate(serviceURL)` method with code to read a server well-known certificate from a remote or local path to a x509 object and pass it to the `shared.GetTLSConfig()` method.

Once the TLS configuration is ready, the next step is to create the REST client object:

```go
amsClient, err := client.New(u, tlsConfig)
if err != nil {
    return err
}
```

Now the client object is ready to be used.

## Asynchronous Operations

All operations modifying entities on AMS are executed asynchronously to prevent
blocking the client. This means that a call, say, to `c.CreateApplication(...)`
won't block and will return immediately, even when the operation is still not
finished by the service.

All asynchronous operations return an
`github.com/CanonicalLtd/ams/shared/rest/client/Operation` struct object

If you want your client to wait for an asynchronous operation to complete, you
can call `Operation.Wait()` method, which will block the current thread until
the operation finishes or an error occurs:

```go
operation, err := c.CreateApplication(".", nil)
err = operation.Wait(context.Background())
if err != nil {
    return err
}
```

In your code you can receive the resulting resources and extract the ID of the
created application:

```go
resources := operation.Get().Resources
for _, r := range resources {
    for _, id := range r {
        fmt.Printf("id: %s", path.Base(id))
    }
}
```
