Similarly to [AMS](https://discourse.ubuntu.com/t/about-ams/24321), the Stream Gateway (see [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769) for more information) exposes its API over an HTTP interface. Clients can be anything from the provided web dashboard to any custom client you develop.

[note type="information" status="Note"]To access the Stream Gateway, make sure that its HTTP API is exposed. This is the default configuration.[/note]

## Service accounts

All calls to the Stream Gateway must be authenticated. Authentication takes the form of a single token per client you must embed in your requests.
A token is associated to a *service account*, has a limited lifetime, and can be revoked at any time.

### 1. Creating the token

An internal HTTP API is exposed for managing client tokens. This API is only accessible via a Unix domain socket which resides at `/var/snap/anbox-stream-gateway/common/service/unix.socket` by default.
For convenience, the Stream Gateway has a built-in client designed to communicate to that API.

**Creating a token**

If you are running a full Anbox Cloud deployment, use the following command to create a token:

    anbox-stream-gateway account create my-client

If you are running the Anbox Cloud Appliance, use the following command:

    anbox-cloud-appliance gateway account create my-client

**Deleting a token**

If you are running a full Anbox Cloud deployment, use the following command to delete a token:

    anbox-stream-gateway account delete my-client

Type `anbox-stream-gateway --help` to list all commands

### 2. Using the token in your requests

When making requests to the Stream Gateway API you can either place the token in the request HTTP headers or in the query parameters.

**Request headers**

```bash
curl -X GET https://20.234.75.29:4000/1.0/sessions \
    -H 'authorization=macaroon root=AgEUYW5ib3...QSyzaA_GHLYQ'
```

**Query parameters**

```bash
curl -X GET https://20.234.75.29:4000/1.0/sessions?api_token=AgEUYW5ib3...QSyzaA_GHLYQ
```

[note type="information" status="Note"]The Anbox Stream SDK handles the token automatically for all its requests.[/note]
