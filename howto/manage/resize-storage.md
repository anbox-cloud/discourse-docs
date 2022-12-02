# How to resize LXD storage

Resizing the LXD storage pool that Anbox Cloud uses is not recommended. Before you deploy Anbox Cloud, you should analyse and plan the capacity you need, so that you can size the storage that you need correctly right from the start. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for detailed information.

However, if you run into a situation where you need to grow the LXD storage pool, it depends on your setup if this is actually possible.

- **Loop-backed storage pool**

  If you use a loop file for your LXD storage, you can increase its size by following the instructions for ZFS in [Resize a storage pool](https://linuxcontainers.org/lxd/docs/latest/howto/storage_pools/#resize-a-storage-pool) in the LXD documentation.

  After resizing the storage pool, you must restart AMS.
- **Dedicated block device**

  You cannot resize a dedicated block device. In this case, you must replace the block device with a bigger one (which requires re-deploying the cluster node).
- **EBS volume**

  While it is generally possible to resize an EBS volume, it is usually easier to replace the cluster node with a new one that has a bigger EBS volume.
