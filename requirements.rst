.. _requirements:

============
Requirements
============

To run Anbox Cloud you need to fulfil a few minimum requirements which
are a bit different depending on which kind of deployment you choose.

The following two different deployment variants and their minimum
requirements will be covered below:

1. The Anbox Cloud Appliance
2. Juju based deployments

See the
:ref:`Variants <explanation_anbox-cloud-variants>`
for a explanation of the differences between both variants.

General requirements
====================

The following requirements apply to all variants of Anbox Cloud

Ubuntu Advantage Token
----------------------

After registering to Anbox Cloud, you should have received an `Ubuntu Advantage for Applications <https://ubuntu.com/advantage>`_ token. If
you haven’t received one, please contact
`support <https://support.canonical.com/>`_ or your Canonical account
representative as you’ll need it to deploy Anbox Cloud.

Ubuntu OS
---------

Anbox Cloud is supported only on the `Ubuntu <https://ubuntu.com/>`_
operating system. Other Linux-based operating systems are not supported.

You must run either the `server <https://ubuntu.com/download/server>`_
or the `cloud <https://ubuntu.com/download/cloud>`_ variant of Ubuntu.
Running Anbox Cloud on a Ubuntu Desktop installation is not supported.

Supported Ubuntu versions:

-  18.04 (bionic) - see :ref:`Linux kernel <requirements-linux-kernel>` below for
   limitations
-  20.04 (focal)

For new deployments, Ubuntu 20.04 (focal) is preferred.

.. _requirements-linux-kernel:

Linux kernel
------------

Anbox Cloud is only supported on the Ubuntu variant of the Linux kernel
starting with version 5.4. The GA kernel for Ubuntu 18.04 (based on
4.15) is not supported.

AppArmor support must be enabled in the kernel as it’s mandatory for the
Anbox containers to run.

The following table gives an overview of the available kernel versions
for the different supported clouds:

======= ============== ========================================
CLOUD   KERNEL VERSION UBUNTU PACKAGES                         
======= ============== ========================================
AWS     >= 5.4         linux-aws, linux-modules-extra-aws      
GCE     >= 5.4         linux-gcp, linux-modules-extra-gcp      
Azure   >= 5.4         linux-azure, linux-modules-extra-azure  
OCI     >= 5.4         linux-oracle, linux-modules-extra-oracle
Private >= 5.4         linux-generic                           
======= ============== ========================================

.. _requirements-appliance:

Anbox Cloud Appliance
=====================

The Anbox Cloud Appliance has the following minimum hardware
requirements:

-  64 bit x86 or Arm CPU with >= 4 CPU cores
-  8 GB of memory
-  40 GB of disk space for the OS
-  optional, but strongly recommended: >= 50GB block volume to host
   container storage

The above defines a minimum of what is necessary to run the Anbox Cloud
Appliance. As Anbox Cloud is dependent on available resources to launch
its Android containers, the available resources dictate the maximum
number of possible containers. See :ref:`explanation_clustering`
for an explanation on how to plan for a specific capacity on your
appliance.

On public clouds it’s recommended to always allocate an additional
storage volume for the container storage. If no additional storage
volume is available, the appliance will create an on-disk image it will
use for the container storage. This is sufficient for very simple cases
but does not provide optimal performance and will slow down operations
and container startup time.

For external access to the Anbox Cloud Appliance, a couple of network
ports must be exposed on the machine it’s running on. The following
table lists all ports.


.. list-table::
   :header-rows: 1

   * - Port(s)
     - Protocol
     - Necessity
     - Description
   * - 80
     - tcp
     - mandatory
     - HTTP (redirects to HTTPS on port 443)
   * - 443
     - tcp
     - mandatory
     - HTTPS
   * - 5349
     - udp
     - mandatory
     - STUN/TURN
   * - 60000-60100
     - udp
     - mandatory
     - TURN relay ports
   * - 10000-11000
     - udp
     - optional
     - Service endpoints exposed by AMS
   * - 10000-11000
     - tcp
     - optional
     - Service endpoints exposed by AMS


How to allow incoming traffic on the listed ports is different depending
on the cloud used. Please consult the documentation of the cloud for
further information on how to change the firewall.

Juju based deployments
======================

Anbox Cloud deployments are managed by Juju. They can be created on all
the `supported clouds <https://juju.is/docs/clouds>`_ as well as
manually provided machines as long as they follow the required minimums.

Juju setup
----------

Anbox Cloud requires `Juju <https://juju.is/>`_ to be installed to
manage the different components and their dependencies. Follow the
official `documentation <https://juju.is/docs/installing>`_ to get it
installed on your machine.

Minimum hardware
----------------

While you can run Anbox Cloud on a single machine, we strongly recommend
the following setup for a production environment:


.. list-table::
   :header-rows: 1

   * - ID
     - Architecture
     - CPU cores
     - RAM
     - Disk
     - GPUs
     - FUNCTION
   * - 0
     - amd64
     - 4
     - 4GB
     - 50GB SSD
     - no
     - Hosts the `Juju controller <https://discourse.juju.is/t/controllers/1111>`__\ 
   * - 1
     - amd64
     - 4
     - 8GB
     - 100GB SSD
     - no
     - Host the management layer of Anbox Cloud
   * - 2
     - amd64 or arm64
     - 8
     - 16GB
     - 200GB NVMe
     - optional
     - LXD worker node. Hosts the actual Anbox containers


The specified number of cores and RAM is only the minimum required to
run Anbox Cloud at a sensible performance.

More CPU cores and more RAM on the machine hosting LXD will allow to run
a higher number of containers. See :ref:`explanation_clustering`
for an introduction of how many resources are necessary to host a
specific number of containers.

If you require GPU support, see :ref:`explanation_gpu-support` for a list
of supported GPUs.

Applications not maintained by Anbox Cloud may have different hardware
recommendations:

-  **etcd**: https://etcd.io/docs/v3.4.0/op-guide/hardware/
-  **HAProxy** (load balancer for the Stream Gateway and the dashboard):
   https://www.haproxy.com/documentation/hapee/latest/installation/getting-started/os-hardware/#hardware-requirements

Please note that these are just baselines and should be adapted to your
workload. No matter the application, :ref:`measuring performances <howto_monitor_install>`
is always important.
