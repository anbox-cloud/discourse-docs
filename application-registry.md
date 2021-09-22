The Anbox Application Registry, or *AAR*, provides a central repository for applications created on Anbox Cloud. Using an AAR is very useful for larger deployments involving multiple regions, in order to keep applications in sync.

## How does it work

You can configure the AMS service to regularly look at an AAR and import any new application versions found there. When a new application version is found, AMS starts to import it. Once done, AMS makes it available for use.

An imported application is immutable and cannot be changed other than through the AAR itself. If an application is removed from the AAR, it is removed from AMS on the next update as well.

AMS can act in two different roles when working with the AAR:

* `publisher` - should be related to one AMS unit
* `client` - can be related to many units

The `publisher` role allows both read and write access to the AAR. AMS instances registered as publishers act in `push` mode and are meant to push new applications and updates of these to the AAR so that they can be consumed by regular read-only `clients`.

A single AMS instance can act only as a publisher or as a client, but not both. We recommend you have one publishing AMS instance per architecture, for example, one for `amd64` and one for `arm64`. These should not be used to host regular containers but only to manage applications. Regular users should be directed to AMS instances acting in `client` mode.

## Using an AAR

See the following documentation for instructions on how to use the AAR:

* [Deploy an AAR](https://discourse.ubuntu.com/t/installation-application-registry/17749)
* [Configure an AAR](https://discourse.ubuntu.com/t/configure-an-aar/24319)
* [Revoke an AAR client](https://discourse.ubuntu.com/t/revoke-an-aar-client/24320)
