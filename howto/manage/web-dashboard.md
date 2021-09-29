The Anbox Cloud Dashboard offers a web GUI from where developers can create, manage, and even stream applications from their web browser.
The dashboard is useful if you are new to Anbox Cloud or want a simple management interface.

Starting in 1.9.0, the dashboard replaces the old Dev UI.

> **Note**: The web dashboard is more oriented toward developers than end-users. However, it only uses available APIs and SDKs, and can be a good example to build your own web-based platform.

![Screenshot 2021-02-10 at 14.33.52|690x322](upload://azCr6HYSx9mJZ82K2CPdTb3IS34.png)

## Installation

The dashboard comes pre-installed when you deploy [Anbox Cloud with the streaming stack](https://discourse.ubuntu.com/t/install-anbox-cloud/17744) or the [Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681). It sits behind a reverse proxy for performance and security reasons.

## Usage

To access the dashboard, go to `https://<your-machine-address>/`.

> **Hint**: The dashboard uses self-signed certificates. You might see a warning from your browser and have to accept the certificates manually.

### Granting access

Instead of implementing its own user management, the dashboard relies on OAuth for user authentication. The only OAuth provider supported right now is [Ubuntu One](https://login.ubuntu.com/). Future versions of Anbox Cloud will allow using other OAuth providers.

If you haven't registered an Ubuntu One account yet, you can do that at https://login.ubuntu.com/.

Before you can log into the dashboard, you must register your Ubuntu One account with the dashboard to grant it access.

#### Register a Ubuntu One account in Anbox Cloud

On a regular Anbox Cloud deployment, use the following Juju action to register a Ubuntu One account:

    juju run-action anbox-cloud-dashboard/0 --wait register-account email=<Ubuntu One email address>

You will see output similar to the following:

```sh
unit-anbox-cloud-dashboard-0:
  UnitId: anbox-cloud-dashboard/0
  id: "157"
  results:
    Stdout: |
      Visit https://10.10.10.10/register?token=eyJ0...-Td7A to create the new user
  status: completed
  timing:
    completed: 2021-02-10 14:04:46 +0000 UTC
    enqueued: 2021-02-10 14:04:44 +0000 UTC
    started: 2021-02-10 14:04:44 +0000 UTC
```

#### Register a Ubuntu One account in Anbox Cloud Appliance

If you followed the instructions in [Installing the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) to install the Anbox Cloud Appliance, you already registered your Ubuntu One account.

To add more accounts, use the following command:

    $ anbox-cloud-appliance dashboard register <Ubuntu One email address>

Accessing the resulting link will create the account and ask you to login via Ubuntu One. You only need to do this step once per user you want to grant access to the dashboard.

The generated link is valid for one hour.

### Creating applications

Creating applications through the dashboard is done the same way as you would do with `amc` (see [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)).
Note that more advanced scenarios might not yet be possible via the dashboard and require going through `amc`.

![image|690x438](upload://9fPqr5DXciTsKy8bw90FzBxguZH.png)

### Streaming applications

The dashboard comes with in-browser streaming capabilities through WebRTC.

> **Note**: The dashboard uses the [Streaming SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#streaming-sdk) under the hood.

You can select any application you previously created and start a streaming session.

![image|690x352](upload://l2azfsITC0bCjN9D0Xe2IRIEQOI.png)

For more information about the Streaming Stack, visit [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769).
