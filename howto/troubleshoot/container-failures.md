The following information should help you in determining why your container failed.

## More information on container failures

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> A container failed to start. Where can I find more information why it failed to start?

If a container fails to start, its status is set to `error`. Anbox Management Service (AMS) automatically fetches several log files from the container and makes them available for further inspection. The log files can provide information on why the container failed to start. The reason for container failure may not always be simple and easy to resolve because of a number of variable factors, for example, the application that the container is hosting or any installed addons.

See [How to view the container logs](https://discourse.ubuntu.com/t/view-the-container-logs/24329) for instructions on how to access the container log files.

## Published application version not found

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> When launching a container for an application, I get an error that mentions "published application version not found". Why?

If you launch a container by only specifying the application ID and the application has no published version yet, you must explicitly specify the version that you want to launch or publish a version of the application. See [How to launch application containers](https://discourse.ubuntu.com/t/launch-a-container/24327#application-containers) and [How to publish application versions](https://discourse.ubuntu.com/t/update-an-application/24201#publish-application-versions) for more information.