.. _explanation_benchmarking:

==================
About benchmarking
==================

Anbox Cloud provides different tools to allow benchmarking different
aspects of a deployment. This pages describes the available tools and
how to use them.

Container Benchmarking
======================

The ``amc`` command line utility comes with a subcommand to allow easy
benchmarking of an Anbox Cloud deployment. It can be used to measure the
time containers take to start up but also for measuring their frames per
second. The benchmark enables you to put Anbox Cloud under load. The
results can be used to evaluate the performance of Anbox Cloud for a
well defined workload.

.. warning::
   If your application is not
   constantly refreshing the screen by itself, like regular Android
   applications providing a simple user interface do, you will get a low
   FPS number. The benchmark can only provide useful information if you
   know your workload and how it should perform in an ideal
   scenario.

Run the Benchmark
-----------------

Have a look at the output of

.. code:: bash

   $ amc benchmark -h

to learn more about the different arguments and their purpose.

.. hint::
   Keep in mind that the success of
   container startup and the times you will get depend on the underlying
   resources used on the machines hosting the containers. Latency between
   the different nodes and the AMS services also play their role.

An example benchmark session looks like this:

.. code:: bash

   $ amc benchmark --fps --network-address=172.31.4.11 --num-containers=15 --containers-per-second=0.1 bh2q90vo3v1lt1ft4mlg
   2019/01/21 11:11:49 Test environment:
   2019/01/21 11:11:49   AMS version: 1.7
   2019/01/21 11:11:49   Available nodes:
   2019/01/21 11:11:49     lxd0 (CPU: 48, Memory: 185GB)
   2019/01/21 11:11:49
   2019/01/21 11:11:49 Launching 15 containers for application bh2q90vo3v1lt1ft4mlg with 0.1 containers per second
   2019/01/21 11:11:49
   2019/01/21 11:11:59 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:12:05 Started container bh2qhvvo3v1lt1ft4ndg
   2019/01/21 11:12:09 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:12:15 Started container bh2qi2fo3v1lt1ft4neg
   2019/01/21 11:12:19 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:12:25 Started container bh2qi4vo3v1lt1ft4nfg
   2019/01/21 11:12:29 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:12:35 Started container bh2qi7fo3v1lt1ft4ngg
   2019/01/21 11:12:39 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:12:45 Started container bh2qi9vo3v1lt1ft4nhg
   2019/01/21 11:12:49 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:12:55 Started container bh2qicfo3v1lt1ft4nig
   2019/01/21 11:12:59 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:13:05 Started container bh2qievo3v1lt1ft4njg
   2019/01/21 11:13:09 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:13:15 Started container bh2qihfo3v1lt1ft4nkg
   2019/01/21 11:13:19 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:13:25 Started container bh2qijvo3v1lt1ft4nlg
   2019/01/21 11:13:29 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:13:35 Started container bh2qimfo3v1lt1ft4nmg
   2019/01/21 11:13:39 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:13:45 Started container bh2qiovo3v1lt1ft4nng
   2019/01/21 11:13:49 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:13:55 Started container bh2qirfo3v1lt1ft4nog
   2019/01/21 11:13:59 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:14:05 Started container bh2qitvo3v1lt1ft4npg
   2019/01/21 11:14:09 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:14:15 Started container bh2qj0fo3v1lt1ft4nqg
   2019/01/21 11:14:19 Launching container for application bh2q90vo3v1lt1ft4mlg ...
   2019/01/21 11:14:25 Started container bh2qj2vo3v1lt1ft4nrg
   2019/01/21 11:14:25 Done starting all containers. Measuring container statistics for 1m0s ...
   2019/01/21 11:15:25 Removing all containers ...
   2019/01/21 11:15:25 Removing container bh2qi2fo3v1lt1ft4neg ...
   2019/01/21 11:15:25 Removing container bh2qi7fo3v1lt1ft4ngg ...
   2019/01/21 11:15:25 Removing container bh2qitvo3v1lt1ft4npg ...
   2019/01/21 11:15:25 Removing container bh2qievo3v1lt1ft4njg ...
   2019/01/21 11:15:25 Removing container bh2qj2vo3v1lt1ft4nrg ...
   2019/01/21 11:15:25 Removing container bh2qj0fo3v1lt1ft4nqg ...
   2019/01/21 11:15:25 Removing container bh2qicfo3v1lt1ft4nig ...
   2019/01/21 11:15:25 Removing container bh2qihfo3v1lt1ft4nkg ...
   2019/01/21 11:15:25 Removing container bh2qijvo3v1lt1ft4nlg ...
   2019/01/21 11:15:25 Removing container bh2qimfo3v1lt1ft4nmg ...
   2019/01/21 11:15:25 Removing container bh2qiovo3v1lt1ft4nng ...
   2019/01/21 11:15:25 Removing container bh2qi4vo3v1lt1ft4nfg ...
   2019/01/21 11:15:25 Removing container bh2qirfo3v1lt1ft4nog ...
   2019/01/21 11:15:25 Removing container bh2qhvvo3v1lt1ft4ndg ...
   2019/01/21 11:15:25 Removing container bh2qi9vo3v1lt1ft4nhg ...
   2019/01/21 11:15:39 Containers boot time measurement:
   2019/01/21 11:15:39   Launching all 15 containers took 2m36.560310342s
   2019/01/21 11:15:39   Out of 15 containers 0 failed to launch
   2019/01/21 11:15:39   Average container launch time: 6.149119411s
   2019/01/21 11:15:39   Max container launch time: 6.576302043s
   2019/01/21 11:15:39   Min container launch time: 5.911184959s
   2019/01/21 11:15:39   Android system failed to boot in the following containers:
   2019/01/21 11:15:39     None
   2019/01/21 11:15:39 Containers statistics:
   2019/01/21 11:15:39   FPS avg 58 min 52 max 64 for 15 containers
   2019/01/21 11:15:39   Containers below run at low FPS(<30):
   2019/01/21 11:15:39     None

The benchmark command launches 15 containers on the Anbox :ref:`null platform <reference_platforms>` with
the following default display specification:

=============== =====
Display Spec    Value
=============== =====
Display width   1280
Display height  720
FPS             60
Display density 160
=============== =====

You can configure a different display specification through the
``--user-data`` parameter when running the benchmark. The required
format for the parameter varies based on the different platforms:

+------------+---------------------+----------------------------------+
| Platform   | Required format of  | Example                          |
|            | user data           |                                  |
+============+=====================+==================================+
| Null       | Comma-separated     | ,,,                              |
|            | values              |                                  |
+------------+---------------------+----------------------------------+
| Swrast     | Comma-separated     | ,,,                              |
|            | values              |                                  |
+------------+---------------------+----------------------------------+
| WebRTC     | Json-based          | {“display_width”:                |
|            |                     | ,“display_height”:               |
|            |                     | ,“display_density”: ,“fps”:      |
|            |                     | ,“render_only”: true }           |
+------------+---------------------+----------------------------------+

.. note::
   If you’re running a benchmark
   against the ``webrtc`` platform, make sure to specify
   ``"render_only": true`` to launch the containers in render-only mode.
   Otherwise, the container creation will fail, because the
   ``amc benchmark`` command doesn’t interact with the stream gateway for
   the benchmark execution.

Stream Benchmarking
===================

As streaming involves more things to automate for a proper benchmark
Anbox Cloud provides a dedicated benchmark tool which allows creating a
streaming session, receiving the video/audio stream and collecting
various statistics and optional also dumping the received stream to a
local file.

.. warning::
   Right now the benchmark tool is
   only supported on a Linux system supporting snaps and on 64 bit x86
   systems. Support for 64 bit ARM systems will be added at a later
   point.

The benchmark tool comes with the ``anbox-cloud-tests`` snap which you
can install with

.. code:: bash

   $ snap install anbox-cloud-tests

Once the snap is installed you can have a look at the supported command
line options of the benchmark tool:

.. code:: bash

   $ anbox-cloud-tests.benchmark -h

To run the benchmark against an existing Anbox Cloud deployment, use the
following as an example but check the other available options the
benchmark offers too:

.. code:: bash

   $ anbox-cloud-tests.benchmark \
     --screen-width=1280 \
     --screen-height=720 \
     --screen-fps=60 \
     --stream-dump-path=/path/to/stream/dump/output \
     --application=my-application \
     --url=<https:// URL of the Anbox Stream Gateway> \
     --auth-token=<valid auth token for the Anbox Stream Gateway> \

.. hint::
   Check :ref:`howto_stream_access`
   if you haven’t already created an authentication token.

If your Anbox Stream Gateway is behind a self-signed TLS certificate you
also need to specify the ``--insecure-tls`` option.

The benchmark will emit various statistics once it finished:

.. code:: bash

   I0104 13:03:09.860428 556511 benchmark.cpp:165] Created new session bvpg7vbmend4td6moir0 in region cloud-0 for application bombsquad-stress-nvc
   I0104 13:03:10.188585 556626 websocket_client.cpp:32] Successfully connected to websocket
   I0104 13:03:10.228832 556626 benchmark.cpp:273] Established connection with stream gateway at https://10.229.100.14
   I0104 13:03:10.247896 556626 fake_video_decoder_factory.cpp:149] Adding decoding support for H264
   I0104 13:03:10.247918 556626 fake_video_decoder_factory.cpp:161] Adding decoding support for VP8
   I0104 13:03:10.309556 556626 peer_connection.cpp:233] Using the following STUN/TURN servers:
   I0104 13:03:10.309569 556626 peer_connection.cpp:236] stun:stun.l.google.com:19302
   I0104 13:03:10.309572 556626 peer_connection.cpp:236] turn:10.229.100.15:5349
   I0104 13:03:10.362562 556626 benchmark.cpp:319] Creating offer to establish connection with the other peer
   I0104 13:03:10.378496 556637 peer_connection.cpp:866] Adjusted bitrate for all video and audio encodings on our RTP senders
   I0104 13:03:10.378552 556637 benchmark.cpp:370] Offer was created, sharing with the other side
   I0104 13:03:38.232844 556637 peer_connection.cpp:746] New stream stream_id added
   I0104 13:03:38.820360 556637 benchmark.cpp:396] Connection with other peer is established (took 29s)
   I0104 13:03:38.820413 556637 benchmark.cpp:181] Using 10s as sample interval
   I0104 13:03:38.820453 556637 main.cpp:165] Connected, starting execution timeout of 1min
   I0104 13:03:38.925285 556626 websocket_client.cpp:67] Websocket connection was closed
   I0104 13:03:39.048584 556637 peer_connection.cpp:759] New data channel control added
   E0104 13:03:40.437090 557770 fake_video_decoder_factory.cpp:63] Failed to create video dumper
   I0104 13:03:40.437153 557770 fake_video_decoder_factory.cpp:65] Initialized video decoder for codec H264
   I0104 13:04:39.508816 556511 main.cpp:200] Finished benchmark, generating report ...
   +-----------------------------------------------------------------------------------------------------------------------------------------------------+
   |             Connection |                Average |                    Min |                    Max |                 Stddev |                  Count |
   +-----------------------------------------------------------------------------------------------------------------------------------------------------+
   |   Round trip time (ms) |                 103.40 |                 101.00 |                 107.00 |                   2.94 |                   5.00 |
   |     Bandwidth (Mbit/s) |                   0.00 |                   0.00 |                   0.00 |                   0.00 |                   5.00 |
   +-----------------------------------------------------------------------------------------------------------------------------------------------------+
   |                  Video |                Average |                    Min |                    Max |                 Stddev |                  Count |
   +-----------------------------------------------------------------------------------------------------------------------------------------------------+
   |    Bandwidth (Mbit/s)  |                  10.55 |                   9.08 |                  11.88 |                   0.95 |                   5.00 |
   |      Frames per second |                  66.00 |                  62.00 |                  69.00 |                   3.29 |                   5.00 |
   |        Frames received |                 621.20 |                 619.00 |                 623.00 |                   1.47 |                   5.00 |
   |         Frames decoded |                 621.40 |                 617.00 |                 623.00 |                   2.24 |                   5.00 |
   |         Frames dropped |                   0.00 |                   0.00 |                   0.00 |                   0.00 |                   5.00 |
   |           Freeze count |                   0.00 |                   0.00 |                   0.00 |                   0.00 |                   5.00 |
   |            Pause count |                   0.00 |                   0.00 |                   0.00 |                   0.00 |                   5.00 |
   |     Key frames decoded |                   4.80 |                   4.00 |                   5.00 |                   0.40 |                   5.00 |
   +-----------------------------------------------------------------------------------------------------------------------------------------------------+
   Sample interval is 10 seconds
   Benchmark ran for 1 minutes

The results can also be saved in a file with the
``--report-path=/path/to/report.json`` option and the format changed to
JSON with ``--format=json`` for easier automated processing.
