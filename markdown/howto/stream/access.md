Similarly to [AMS](https://discourse.ubuntu.com/t/about-ams/24321), the Stream Gateway (see [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769) for more information) exposes its API over an HTTP interface. Clients can be anything from the provided Dev UI to any custom client you develop.

## Service accounts

All calls to the Stream Gateway must be authenticated. Authentication takes the form of a single token per client you must embed in your requests.
A token is associated to a *service account*, has a limited lifetime, and can be revoked at any time.

### 1. Creating the token

An internal HTTP API is exposed for managing client tokens. This API is only accessible via a Unix domain socket which resides at `/var/snap/anbox-stream-gateway/common/service/unix.socket` by default.
For convenience, the Stream Gateway has a built-in client designed to communicate to that API.

**Creating a token**

```bash
$ anbox-stream-gateway account create my-client
AgEUYW5ib3gtc3RyZWFtLWdhdGV3YXkCBGFzZGYAAhkyMDIwLTA2LTIzVDA5OjMyOjE5KzAyOjAwAAAGIDcZMdTrdNdJB6kzjoXyx1_T6s8-0C1AQSyzaA_GHLYQ
```

**Deleting a token**

```bash
$ anbox-stream-gateway account delete my-client
Account my-client deleted successfully
```

You can type `anbox-stream-gateway --help` to list all commands

### 2. Using the token in your requests

When making requests to the Stream Gateway API you can either place the token in the request HTTP headers or in the query parameters.

**Request headers**

```bash
$ curl -X GET https://20.234.75.29:4000/1.0/sessions \
    -H 'authorization=macaroon root=AgEUYW5ib3...QSyzaA_GHLYQ'
```

**Query parameters**

```bash
$ curl -X GET https://20.234.75.29:4000/1.0/sessions?api_token=AgEUYW5ib3...QSyzaA_GHLYQ
```

[note type="information" status="Hint"]The Anbox Stream SDK handles the token automatically for all its requests.[/note]
