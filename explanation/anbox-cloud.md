Anbox Cloud provides a rich software stack to enable you to run Android in the cloud for all kinds of different uses cases. This page intends to give you an overview over the available variants and internal components which make Anbox Cloud.

<a name="variants"></a>
## Variants

Anbox Cloud exists in two different variants which serve different purposes:

**Anbox Cloud Appliance**

The Anbox Cloud Appliance is a self-contained, single-machine deployment variant of Anbox Cloud. It uses a sensible standard configuration to hide the complexity and flexibility of [Juju](https://juju.is/). In this way, the Anbox Cloud Appliance allows simple and fast development and prototyping.

**Anbox Cloud**

The regular Anbox Cloud uses [Juju](https://juju.is/) for deployment and operations. It provides rich features and is ready made for a large scale deployment.

Which of both variants you choose depends on your needs. The appliance is well suited for quick prototyping and development or small scale deployments, whereas the regular Anbox Cloud is best to scale big.

## Components

Anbox Cloud is composed of many pieces interacting with one another. This page gives a summary of what those pieces are and how they interact with each other.

### Core Stack

Anbox Cloud takes care of all management aspects and provides both a fully functional implementation and an integration model to support existing infrastructure and service implementations.

The following figure gives an overview over the different components and their responsibility within the core stack of Anbox Cloud.

![anbox-core-overview|690x398](upload://x0budFKybsbYLhiplNhF4R91Ght.png)

At the heart of Anbox Cloud sits the **[Anbox Management Service (AMS)](https://discourse.ubuntu.com/t/about-ams/24321)**. **AMS** has the job to handle all aspects of the application and container lifecycle (including application and image updates) while ensuring high density, performance and fast container startup times.
A developer or system administrator will manage **AMS** through the **command line interface (AMC)** or through custom-built tools interacting with the [**AMS HTTP API**](https://discourse.ubuntu.com/t/ams-rest-api-reference/17801).

For example, a simple Android application testing service would provide a user-facing interface dealing with things like authentication and user management, and would communicate with the REST API to add applications or start and stop containers when a user asks to.

Anbox Cloud can be heavily customized and extended via [**Platform Plugins**](https://oem-share.canonical.com/partners/indore/share/docs/1.7/en/sdk/anbox/) and [**addons**](https://discourse.ubuntu.com/t/managing-addons/17759). Platform plugins and addons can be built to add specific streaming capabilities, perform operations within Android containers and much more. One example of a platform plugin is the **Anbox WebRTC Platform** used in the Anbox Streaming Stack. Addons are ways to customize the base image by installing additional software and running scripts on different lifecycle hooks.


### Streaming Stack

Starting from 1.4, Anbox Cloud comes with an easy to use streaming solution. The **Anbox Streaming Stack** is a collection of components designed to run containers on GPU equipped machines and stream their visual output to clients via [WebRTC](https://webrtc.org/).

The following picture shows an overview of how the different components work together to enable this.

![streaming-stack-overview|690x440](upload://qXJleBmvwQFi2cc1HuPF7P5S15b.png)

Main components powering the streaming stack in Anbox Cloud:

**Agent**: software running on a server equipped with a GPU connected to Anbox Cloud.
It serves as an entrypoint the gateway can connect to.

**Anbox Stream Gateway**: the central component that connects clients with agents.
Its role is to choose the best possible region depending on the user location and server capacities.

**Client**: the end user application that will display the stream. It can be a desktop application, a website, a mobile application, a TV, a car system, or anything capable of handling a WebRTC stream.
An SDK is provided along the streaming stack to provide easier integration with web-based applications.

**TURN/STUN servers**: they find the most optimal network path between a client and the container running its application. The streaming stack provides secure STUN and TURN servers but you can use public ones as well.

**NATS**: A messaging system the different components use to communicate (see the [project page](https://github.com/nats-io)).
