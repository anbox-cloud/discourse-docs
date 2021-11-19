.. _explanation_application-streaming:

===========================
About application streaming
===========================

The Streaming Stack is based on `WebRTC <https://webrtc.org/>`_ and
integrates with GPUs from different vendors to enable low latency video
encoding mandatory for any kind of real time streaming use case.

This section covers usage of the Streaming Stack, for installation
instructions please refer to :ref:`the installation page <howto_install_deploy-juju>`.
We also assume you know :ref:`how to get access to the Stream Gateway API <howto_stream_access>`.

Streaming Stack Overview
========================

The Streaming Stack is highly customizable but requires some knowledge
about how it works. Each component of the stack fills a specific role:


.. list-table::
   :header-rows: 1

   * - Gateway
     - Agent
     - NATS
     - Coturn
   * - Provides the initial place where a client and a container go to start a peer to peer discussion. Those ‘chatrooms’ are called sessions and are central to the rest.
     - A middleware between the Gateway and AMS. It secures access to AMS, launches containers, relays status information, and more.
     - A messaging queue to allow components to communicate.
     - A STUN/TURN server needed for WebRTC to work behind NATs and firewalls.


You can see how each component interact when creating a new streaming
session

.. figure:: /images/streaming-stack-sequence.png
   :alt: Streaming stack sequence

   Streaming stack sequence

Streaming an Application
========================

As mentioned above, ``sessions`` are an important concept for the
Streaming Stack. They contain userdata, application information and
more, but most importantly, they provide an entrypoint for both the
client and the container to start the `signaling process <https://www.html5rocks.com/en/tutorials/webrtc/infrastructure/>`_.
Signaling is a process by which both peers establish optimal codecs,
network routes and content types.

1. Creating the session
-----------------------

WebRTC is a peer to peer protocol, but clients have to find each other
through a central server first. This is the primary purpose of the
Stream Gateway. ``Sessions`` are equivalent to *chatrooms* that allow
two peers to discover each other.

The session is created by calling the Gateway API at
``POST /1.0/sessions``. The returned object contains information about
the created session as well as a websocket ``url`` you have to use to
start the signaling process.

2. The signaling process
------------------------

When they can contact each other, both peers have to agree on a number
of parameters. This process of exchanging messages is called the
``signaling process``. Details about exchanged messages aren’t covered
in this page, but you can find more information
`here <https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Signaling_and_video_calling>`__.
The following provides an overview of the process:

1. The container creates an offer containing the desired streams (video,
   audio, binary) as well as codec information.
2. The client replies to that offer by accepting or refusing it.
3. At that point, both peers agreed on the media type, but don’t know
   how to send data directly to each other (keep in mind that, so far,
   all communication is done through a websocket on the Gateway).
4. They start going through the `ICE protocol <https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Signaling_and_video_calling>`_
   and interact with STUN servers to establish an optimal path.
5. Each network path is bundled in an ``ICE candidate``. There are
   usually multiple ICE candidates per peer and both sides negotiate the
   best candidate pair.
6. Both peer agree on the best network path (``ICE candidate``) and
   start the actual streaming. At this point, they stop communicating
   through the Gateway websocket and talk directly to each other.

.. hint::
   The server itself does not need
   to know about the messages content, it just has to forward messages from
   one peer to the other.

3. Establishing the stream
--------------------------

When optimal ICE candidates have been selected and codecs capabilities
have been agreed upon, the actual tracks are being sent. These tracks
can be either video, audio or binary. The binary data channel can be
useful to send arbitrary data like controls. The streams can then be
consumed to display the final content.

Supported Video Codecs
======================

In order to support low latency encoding the list of supported video
codecs is limited as not all codecs are either supported by any of the
supported GPU models or are not performing well enough for low latency
purposes.

Currently supported video codecs are:

-  H.264
-  VP8

.. important::
   The use of H.264 requires a
   license from the `MPEG LA <https://www.mpegla.com/>`_. It’s your
   obligation to ensure you have the rights to streaming H.264 encoded
   video content to your users.

In the future we plan to add support for:

-  VP9
-  AV1

When additional codecs become available depends on when they are
supported by the GPU vendors in their hardware encoding solutions or if
a viable software encoding solution exists.

Anbox Cloud combines both software and hardware video encoding in order
to utilize available resources in the best possible way. Hardware video
encoders usually have limited capacity of how many simulatenous video
streams they can encode for low latency scenarios. The Nvidia T4 can for
example encode 37 video streams at 720p and 30 frames per second (see
“`Turing H.264 Video Encoding Speed and Quality <https://devblogs.nvidia.com/turing-h264-video-encoding-speed-and-quality/>`_”
for more details). Depending on the used CPU platform additional compute
capacity might be available to support additional session via software
encoding.
