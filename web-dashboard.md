The Anbox Cloud Dashboard offers a web GUI from where developers can create, manage, and even stream applications from their web browser.
The dashboard is useful if you are new to Anbox Cloud or want a simple management interface.

Starting in 1.9.0, the dashboard replaces the old Dev UI.

> **Note**: The Web Dashboard is more oriented toward developers than end-users. However, it only uses available APIs and SDKs, and can be a good example to build your own web-based platform.

![Screenshot 2021-02-10 at 14.33.52|690x322](upload://azCr6HYSx9mJZ82K2CPdTb3IS34.png) 

# Installation

The dashboard comes pre-installed when you deploy the [Streaming Stack](https://discourse.ubuntu.com/t/install-anbox-cloud/17744) or the [Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681). It sits behind a reverse proxy for performance and security reasons.

# Usage

## Granting access

No user is configured by default, you will need to register a new user before you can use the dashboard. Instead of implementing it's own user management. the dashboard relies on OAuth for user authentication. The only OAuth provider supported right now is [Ubuntu One](https://login.ubuntu.com/).  Future versions of Anbox Cloud will allow using other OAuth providers.

If you haven't registered an Ubuntu One account yet, you can do that [here](https://login.ubuntu.com/).

Before you can log into the dashboard you need to actually register your [Ubuntu One](https://login.ubuntu.com/) account with the dashboard to grant it access. 

On a regular Anbox Cloud deployment there is a Juju action you can use to do that:

```sh
ubuntu@anbox-cloud:~$ juju run-action anbox-cloud-dashboard/0 --wait register-account email=<your ubuntu one email>
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

When you're using the Anbox Cloud Appliance you can use the following command to register a new Ubuntu SSO user account:

    $ anbox-cloud-appliance dashboard register <your Ubuntu SSO email address>

Accessing the resulting link will create your account and ask you to login via Ubuntu One. You only need to do this step once per user you want to grant access to the dashboard to.

The generated link is valid for one hour.

> **Hint**: The dashboard uses self-signed certificates. You may see a warning from your browser and have to accept the certificates manually.

## Creating applications

Creating applications through the dashboard is done the same way as you would do with [`amc`](https://anbox-cloud.io/docs/manage/managing-applications).
Note that more advanced scenarios may not yet be possible via the dashboard and require going through `amc`.

![image|690x438](upload://9fPqr5DXciTsKy8bw90FzBxguZH.png)

## Streaming Applications

The dashboard comes with in-browser streaming capabilities through WebRTC.

> **Note**: The dashboard uses the [Streaming SDK](https://anbox-cloud.io/docs/usage/usecase-streaming-sdk) under the hood.

You can select any application you previously created and start a streaming session.

![image|690x352](upload://l2azfsITC0bCjN9D0Xe2IRIEQOI.png) 

For more information about the Streaming Stack, visit https://anbox-cloud.io/docs/manage/streaming-android-applications
