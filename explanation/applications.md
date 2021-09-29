Applications are one of the main objects AMS manages. A single application encapsulates one Android application and manages it within the cluster. It takes care of installing the supplied application package ([Android Package Kit - APK](https://en.wikipedia.org/wiki/Android_application_package)), to make it available to users. Further, AMS manages updates to existing applications, which includes allowing the operator to test new uploaded versions before making them available to any users.

## Application requirements
To run on the Anbox Cloud platform, applications must fulfil a set of requirements. These are:

* The application  **SHOULD**  not download any additional resources on regular startup to contribute to short startup times. If additional resources need to be downloaded, this can be done during the application bootstrap phase.
* The application  **MUST NOT**  require the **Google Play services** to be available as Anbox Cloud does not include them.

If the application fulfils all of the requirements above, it is ready to run on the Anbox Cloud platform. If not, please file a [bug report](https://bugs.launchpad.net/indore-extern/+filebug) so that we can find out what we can do to still support the application.

<a name="bootstrap"></a>
### Bootstrap process

Whenever [creating an application](https://discourse.ubuntu.com/t/create-an-application/24198) either from a directory or a tarball, AMS will perform a bootstrap process, which builds the application and synchronises it across all LXD nodes in the cluster. There are major benefits the bootstrap process provides:

  * It enables AMS to launch a container for an application without installing the APK every time.
  * It dramatically speeds up the startup time of a regular container.

Furthermore, an application is synchronised within the LXD cluster, which enables AMS to continue to work when nodes are being removed from the cluster through [scaling down](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323) or lost from the cluster unexpectedly.

A temporary base container will be created and used for the bootstrapping during the application creation. For example, you might see the following output for `amc ls` right after creating an application:

```bash
+----------------------+-------------+------+----------+------+---------------+-----------+
|          ID          | APPLICATION | TYPE |  STATUS  | NODE |    ADDRESS    | ENDPOINTS |
+----------------------+-------------+------+----------+------+---------------+-----------+
| bq78a3oj1qm02cebmof0 |    candy    | base | prepared | lxd0 | 192.168.100.2 |           |
+----------------------+-------------+------+----------+------+---------------+-----------+
```

In general, the bootstrap process goes through the following steps in order:

![application-bootstrap|690x467](upload://haAJJ8p8ZEQXmsvrVb3HOHhl1io.png)

  * Configure network interface and gateway.
  * Apply any pending Ubuntu system security updates.
  * Install [addons](https://discourse.ubuntu.com/t/managing-addons/17759) via the `install` hook provided by each addon listed in the application manifest file.
  * Launch Android container.
  * Install the APK provided by the application.
  * Grant the application permissions as requested in the application manifest.
  * Install the extra data as listed in the application manifest.
  * Execute the `prepare` hook provided by each addon listed in the application manifest.

If one of the steps fails, AMS will interrupt the bootstrap process and make the entire process fail. As a result, the status of the base container will be marked with `error` and the application's status will end up with `error` as well.

> **Note:** An application crash or ANR upon APK installation will cause the bootstrap process to terminate abnormally and the status of application is set to `error` too.

When a base container runs into an error status, you can see what has gone wrong there by checking the error message with `amc show <application ID>`:

```bash
id: bq78a3oj1qm02cebmof0
name: ams-bq78a3oj1qm02cebmof0
status: error
node: lxd0
created_at: 2019-08-09T02:11:33Z
application:
    id: bq6ktjgj1qm027q585kg
network:
    address: ""
    public_address: ""
    services: []
stored_logs:
- container.log
- system.log
- android.log
error_message: 'Failed to install application: com.foo.bar: Failed to extract native libraries, res=-113'
config: {}
```

Alternatively, [check the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329) to troubleshoot problems in the container.

When the application bootstrap succeeds, the base container is automatically removed and the status of the application changes to `ready`. The application is then ready to be used.

## Managing applications

See the following documentation for instructions on how to manage your applications:

 * [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)
 * [Wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202)
 * [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201)
 * [Delete an application](https://discourse.ubuntu.com/t/delete-an-application/24199)
 * [List applications](https://discourse.ubuntu.com/t/list-applications/24200)
 * [Test your application](https://discourse.ubuntu.com/t/usecase-application-testing/17775)
 * [Create a virtual device](https://discourse.ubuntu.com/t/virtual-devices/19069)
