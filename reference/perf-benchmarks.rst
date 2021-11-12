.. _reference_perf-benchmarks:

======================
Performance benchmarks
======================

The following benchmarks give an overview of the performance that you
can achieve with Anbox Cloud. The numbers were collected on various
virtual and bare metal hardware.

Bare metal
==========


.. list-table::
   :header-rows: 1

   * - Instance type
     - Anbox Cloud version
     - Rendering / encoding
     - Resolution
     - Application
     - # Containers
     - Avg. FPS
   * - Ampere Altra + 1x Nvidia Tesla T4
     - 1.11.2 (appliance)
     - hardware / hardware
     - 720p
     - BombSquad Stress
     - 30
     - 29
   * - Ampere Altra + 2x Nvidia Tesla T4
     - 1.11.2 (appliance)
     - hardware / hardware
     - 720p
     - BombSquad Stress
     - 55
     - 29
   * - Ampere Altra + 1x Nvidia Tesla T4
     - 1.11.2 (appliance)
     - hardware / hardware
     - 1080p
     - BombSquad Stress
     - 20
     - 28
   * - Ampere Altra + 2x Nvidia Tesla T4
     - 1.11.2 (appliance)
     - hardware / hardware
     - 1080p
     - BombSquad Stress
     - 50
     - 26


AWS
===
