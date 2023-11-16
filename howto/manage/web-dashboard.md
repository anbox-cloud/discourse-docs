The Anbox Cloud Dashboard offers a web GUI from where developers can create, manage, and even stream applications from their web browser.
The dashboard is useful if you are new to Anbox Cloud or want a simple management interface.

[note type="information" status="Note"]The web dashboard is more oriented toward developers than end-users. However, it only uses available APIs and SDKs, and can be a good example to build your own web-based platform.[/note]

![Anbox Cloud web dashboard|690x322](https://assets.ubuntu.com/v1/4a1c8531-manage_dashboard-applications.png)

## Installation

The dashboard comes pre-installed when you deploy [Anbox Cloud with the streaming stack](https://discourse.ubuntu.com/t/install-anbox-cloud/17744) or the [Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681). It sits behind a reverse proxy for performance and security reasons.

## Usage

To access the dashboard, go to `https://<your-machine-address>/`.

The dashboard uses self-signed certificates. You might see a warning from your browser and have to accept the certificates manually.

### Granting access

Instead of implementing its own user management, the dashboard relies on OAuth for user authentication. The only OAuth provider supported right now is [Ubuntu One](https://login.ubuntu.com/). Future versions of Anbox Cloud will allow using other OAuth providers.

If you haven't registered an Ubuntu One account yet, you can do that at https://login.ubuntu.com/.

Before you can log into the dashboard, you must register your Ubuntu One account with the dashboard to grant it access.

#### Register an Ubuntu One account in Anbox Cloud

On a regular Anbox Cloud deployment, use the following Juju action to register an Ubuntu One account:

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

<a name="dashboard-access-appliance"></a>
#### Register an Ubuntu One account in Anbox Cloud Appliance

If you followed the instructions in the [Install the Anbox Cloud Appliance on a dedicated machine](https://discourse.ubuntu.com/t/install-appliance/22681) tutorial or in [How to install the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702), you already registered your Ubuntu One account.

To add more accounts, use the following command:

    anbox-cloud-appliance dashboard register <Ubuntu One email address>

Accessing the resulting link will create the account and ask you to login via Ubuntu One. You only need to do this step once per user you want to grant access to the dashboard.

The generated link is valid for one hour.

### Creating applications

Creating applications through the dashboard is done the same way as you would do with `amc` (see [How to create an application](https://discourse.ubuntu.com/t/create-an-application/24198)).
Note that more advanced scenarios might not yet be possible via the dashboard and require going through `amc`.

![Create an application|690x438](https://assets.ubuntu.com/v1/40dda4a6-manage_dashboard-add-application.png)

### Streaming applications

The dashboard comes with in-browser streaming capabilities through WebRTC. It uses the [Streaming SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#streaming-sdk) under the hood.

You can select any application you previously created and start a streaming session.

![Start a streaming session|690x352](https://assets.ubuntu.com/v1/6087fbd9-gs_dashboard_start_session.png)

For more information about the Streaming Stack, visit [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769).

#### Streaming statistics

View the streaming statistics for your running sessions by selecting the **Statistics** button on the session. The statistics display on the right pane and also have a download option to download the statistics in a `.csv` format for further analysis.

The downloaded `.csv` file has the following statistics:

| Statistic | Description |
| --------- |------------ |
| `date` | Date and time in ISO 8601 format |
| `network-currentrtt` | Current round-trip time of the network |
| `video-bandwidth` | The amount of video data that the session can handle per second |
| `video-totalreceived` | Total video data received |
| `video-fps` | Video frames per second |
| `video-decodetime` | Time taken to extract video |
| `video-jitter` | Loss of transmitted video data during streaming |
| `video-averagejitterbufferdelay` | Average jitter buffer delay in video transmission  |
| `video-packetsreceived` | Number of video packets received |
| `video-packetslost` | Number of video packets lost |
| `audio-bandwidth` | The amount of audio data that the session can handle per second |
| `audio-totalreceived` | Total audio data received during streaming |
| `audio-totalsamplesreceived` | Total number of audio samples received |
| `audio-jitter` | Loss of transmitted audio data during streaming |
| `audio-averagejitterbufferdelay` | Average jitter buffer delay in audio transmission |
| `audio-packetsreceived` | Number of audio packets received |
| `audio-packetslost` | Number of audio packets lost |

#### Sharing a streaming session

Use the **Sharing** button on the session page to share a streaming session with users without an account. The button generates a link using which users without an account can join your session.

### Managing Applications and their versions

If you have configured the [Anbox Application Registry (AAR)](https://discourse.ubuntu.com/t/application-registry/17761), you can view and manage applications and their versions in the registry using the **Registry** button on the main menu. If you have configured AAR in manual mode, you can also manually push and delete apps from the registry.
