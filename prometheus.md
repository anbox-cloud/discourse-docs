To see how to deploy a monitoring stack in Anbox Cloud, refer to the instructions for [deploying Grafana](https://discourse.ubuntu.com/t/monitoring-grafana/17787). Those instructions will take you through the installation Prometheus and Grafana.

The base installation provides basic dashboards. You can however update them to fit your needs. Below is the list of all metrics returned to Prometheus by each component of Anbox Cloud.


## AMS
Metrics prefixed with `ams_cluster_` give information about the Anbox management system (AMS). They keep you informed about the status of your cluster.

| Name                                             | Description                                                                                                                                                                             | Available since |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `ams_cluster_nodes_total`                        | Number of nodes in the cluster                                                                                                                                                          | 1.0.0           |
| `ams_cluster_applications_total`                 | Number of applications                                                                                                                                                                  | 1.0.0           |
| `ams_cluster_containers_total`                   | Number of containers currently in the cluster                                                                                                                                           | 1.0.0           |
| `ams_cluster_container_boot_time_seconds_count`  | Number of container boot time measured                                                                                                                                                  | 1.0.0           |
| `ams_cluster_container_boot_time_seconds_sum`    | Sum of all container boot times. Can be used to compute the average boot time                                                                                                           | 1.0.0           |
| `ams_cluster_container_boot_time_seconds_bucket` | Container boot times bucket. Can be used for alerting when above a threshold. See the [Prometheus documentation](https://prometheus.io/docs/practices/histograms/) for more information | 1.0.0           |
| `ams_cluster_containers_per_application_total`   | Number of containers per application                                                                                                                                                    | 1.0.0           |
| `ams_cluster_containers_per_status_total`        | Number of containers per container status                                                                                                                                               | 1.0.0           |
| `ams_cluster_available_cpu_total`                | Total CPUs available in each worker node                                                                                                                                                | 1.0.0           |
| `ams_cluster_used_cpu_total`                     | Used CPUs in each worker node                                                                                                                                                           | 1.0.0           |
| `ams_cluster_available_memory_total`             | Total memory available in each worker node                                                                                                                                              | 1.0.0           |
| `ams_cluster_used_memory_total`                  | Used memory in each worker node                                                                                                                                                         | 1.0.0           |


## Anbox Stream Gateway
Metrics prefixed with `anbox_stream_gateway_` give you information on your cluster related to streaming: number of sessions, agents, etc.

| Name                                             | Description                                                                                                                                                                             | Available since |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `anbox_stream_gateway_sessions_total`            | Total number of sessions, categorized by status                                                                                                                                         | 1.7.2           |
| `anbox_stream_gateway_accounts_total`            | Total number of accounts                                                                                                                                                                | 1.7.2           |
| `anbox_stream_gateway_agents_total`              | Number of active and unresponsive agents                                                                                                                                                | 1.7.2           |


## WebRTC metrics
Metrics prefixed with `webrtc_` give you detailed insight of the WebRTC protocol for every streaming instance.
See the [official W3C reference](https://www.w3.org/TR/webrtc-stats) for more information.

| Name                                | Description                                                                                                                                                                                      | Available since |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `webrtc_frames_encoded`             | Total number of frames successfully encoded                                                                                                                                                      | 1.8.0           |
| `webrtc_key_frames_encoded`         | Total number of key frames, such as key frames in VP8 or IDR-frames in H.264. `webrtc_key_frames_encoded - webrtc_frames_encoded` will give you the number of delta frames                       | 1.8.0           |
| `webrtc_total_encode_time`          | Total number of seconds that has been spent encoding the `webrtc_frames_encoded` frames. The average encode time can be calculated by dividing this value with `webrtc_frames_encoded`           | 1.8.0           |
| `webrtc_target_bitrate`             | Reflects the current encoder target in bits per second                                                                                                                                           | 1.8.0           |
| `webrtc_bytes_sent`                 | Total number of bytes sent for a specific [SSRC](https://tools.ietf.org/html/rfc3550#section-3) (a SSRC represents one resource sent over a WebRTC track. It can be video, audio or binary data) | 1.8.0           |
| `webrtc_retransmitted_bytes_sent`   | The total number of bytes that were retransmitted for a specific SSRC, only including payload bytes                                                                                              | 1.8.0           |
| `webrtc_retransmitted_packets_sent` | The total number of packets that were retransmitted for a specific SSRC                                                                                                                          | 1.8.0           |
| `webrtc_total_packet_send_delay`    | The total number of seconds that packets have spent buffered locally before being transmitted onto the network                                                                                   | 1.8.0           |
| `webrtc_packets_sent`               | Total number of RTP packets sent for this SSRC. This includes retransmissions                                                                                                                    | 1.8.0           |
| `webrtc_nack_count`                 | Count the total number of Negative ACKnowledgement (NACK) packets received by this sender                                                                                                        | 1.8.0           |
| `webrtc_fir_count`                  | Only exists for video. Count the total number of Full Intra Request (FIR) packets received by this sender                                                                                        | 1.8.0           |
| `webrtc_pli_count`                  | Only exists for video. Count the total number of Picture Loss Indication (PLI) packets received by this sender                                                                                   | 1.8.0           |
| `webrtc_sli_count`                  | Only exists for video. Count the total number of Slice Loss Indication (SLI) packets received by this sender                                                                                     | 1.8.0           |

## HTTP Metrics

Anbox Cloud services that include an HTTP API are monitored.

### Anbox Stream Gateway

A few metrics are available to instrument the API. Routes are indicated in the labels, e.g.:
```
anbox_stream_gateway_http_request_duration_seconds_bucket{handler="get_sessions",host="juju-2db13b-1",method="get",le="0.5"} 1
```
The route name would be `get_sessions` in this case.

Here's the list of all routes and their corresponding label

| Method   | Route                             | Label                        |
|----------|-----------------------------------|------------------------------|
| `GET`    | `/1.0/status`                      | `get_service_status`         |
| `POST`   |` /1.0/sessions`                     | `create_new_session`         |
| `GET`    | `/1.0/sessions`                     | `get_sessions`               |
| `GET`    | `/1.0/sessions/<id>`                | `get_session`                |
| `DELETE` | `/1.0/sessions/<id>`                | `delete_session`             |
| `DELETE` | `/1.0/sessions`                     | `delete_sessions`            |
| `POST`   | `/1.0/sessions/<id>/join`           | `join_session`               |
| `GET`    | `/1.0/sessions/<id>/sockets/master` | `streaming_websocket_master` |
| `GET`    | `/1.0/sessions/<id>/sockets/slave`  | `streaming_websocket_slave`  |
| `GET`    | `/1.0/applications`                 | `get_applications`           |
| `GET`    | `/1.0/regions`                      | `get_regions`                |

The different metrics available are as follow:

| Name                                                        | Description                                           | Available since |
|-------------------------------------------------------------|-------------------------------------------------------|-----------------|
| `anbox_stream_gateway_http_in_flight_requests`              | Number of HTTP requests being processed at the moment | 1.9.0           |
| `anbox_stream_gateway_http_request_duration_seconds_bucket` | The HTTP request latencies in seconds                 | 1.9.0           |
| `anbox_stream_gateway_http_request_size_bytes_bucket`       | The HTTP request size in bytes                        | 1.9.0           |
| `anbox_stream_gateway_http_requests_total`                  | Total number of HTTP requests made                    | 1.9.0           |
| `anbox_stream_gateway_http_response_size_bytes_bucket`      | The HTTP response sizes in bytes                      | 1.9.0           |

### AMS

AMS can either be reached via HTTP/S or via a Unix domain socket. The API metrics are separate between `http`, `https` and `unix`:
```
ams_http_request_duration_seconds_bucket{handler="http_applications_GET",host="juju-2db13b-1",method="get",le="0.5"} 1
ams_http_request_duration_seconds_bucket{handler="https_applications_GET",host="juju-2db13b-1",method="get",le="0.5"} 1
ams_http_request_duration_seconds_bucket{handler="unix_applications_GET",host="juju-2db13b-1",method="get",le="0.5"} 1
```
This distinction gives a more granular approach to monitoring.

All handler names adopt the following convention `<transport method>_<object>_<http method>`. E.g.: `unix_containers_POST`
Here's the list of all routes and their corresponding label (ignoring the communication method prefix)

| Method   | Route                             | Label                        |
|---------------|-----------------------------------|------------------------------|
| `GET`       | `/1.0`                      | `service_GET`         |
| `GET`       |` /1.0/addons`                     | `addons_GET`         |
| `POST`    | `/1.0/addons`                     | `addons_POST`               |
| `GET`       |` /1.0/addons/<id>`                     | `addon_GET`         |
| `PATCH`  |` /1.0/addons/<id>`                     | `addon_PATCH`         |
| `DELETE`| `/1.0/addons/<id>`                     | `addon_DELETE`               |
| `DELETE`| `/1.0/addons/<id>/<version>`| `addon_version_DELETE`                |
| `GET`       | `/1.0/applications`                | `applications_GET`             |
| `POST`    | `/1.0/applications`                     | `applications_POST`            |
| `GET`       |` /1.0/applications/<id>`                     | `application_GET`         |
| `PATCH`  | `/1.0/applications/<id>`                     | `application_PATCH`               |
| `DELETE`| `/1.0/applications/<id>`| `application_DELETE`                |
| `GET`       |` /1.0/applications/<id>/<version>`                     | `application_version_GET`         |
| `PATCH`  | `/1.0/applications/<id>/<version>`                     | `application_version_PATCH`               |
| `DELETE`| `/1.0/applications/<id>/<version>`| `application_version_DELETE`                |
| `GET`       |` /1.0/applications/<id>/manifest`                     | `application_manifest_GET`         |
| `GET`       |` /1.0/applications/<id>/<version>/manifest`  | `application_version_manifest_GET`         |
| `GET`       | `/1.0/containers`                | `containers_GET`             |
| `POST`    | `/1.0/containers`                | `containers_POST`             |
| `GET`       | `/1.0/containers/<id>`                | `container_GET`             |
| `DELETE`| `/1.0/containers/<id>`                | `container_DELETE`             |
| `POST`    | `/1.0/containers/<id>/exec`                | `container_exec_POST`             |
| `GET`       | `/1.0/containers/<id>/logs`                | `container_logs_GET`             |
| `GET`       | `/1.0/containers/<id>/logs/<name>`                | `container_log_GET`             |
| `GET`       | `/1.0/version`                | `version_GET`             |
| `GET`       | `/1.0/nodes`                | `nodes_GET`             |
| `POST`    | `/1.0/nodes`                | `nodes_POST`             |
| `GET`       | `/1.0/nodes/<id>`                | `node_GET`             |
| `PATCH`  | `/1.0/nodes/<id>`                | `node_PATCH`             |
| `DELETE`| `/1.0/nodes/<id>`                | `node_DELETE`             |
| `GET`| `/1.0/images`                | `images_GET`             |
| `POST`| `/1.0/images`                | `images_POST`             |
| `GET`| `/1.0/images/<id>`                | `image_GET`             |
| `PATCH`| `/1.0/images/<id>`                | `image_PATCH`             |
| `DELETE`| `/1.0/images/<id>`                | `image_DELETE`             |
| `DELETE`| `/1.0/images/<id>/<version>`                | `image_version_DELETE`             |
| `GET`| `/1.0/config`                | `config_GET`             |
| `PATCH`| `/1.0/config`                | `config_PATCH`             |
| `GET`| `/1.0/tasks`                | `tasks_GET`             |
| `GET`| `/1.0/registry/applications`                | `registry_applications_GET`             |
| `DELETE`| `/1.0/registry/applications/<id>`                | `registry_application_DELETE`             |
| `POST`| `/1.0/registry/applications/<id>/push`                | `registry_application_push_POST`             |
| `POST`| `/1.0/registry/applications/<id>/pull`                | `registry_application_pull_POST`             |
| `GET`| `/1.0/artifacts/<id>`                | `internal_artifacts_GET`             |
| `PATCH`| `/1.0/containers/<id>`                | `internal_containers_PATCH`             |




The different metrics available are as follow:

| Name                                                        | Description                                           | Available since |
|-------------------------------------------------------------|-------------------------------------------------------|-----------------|
| `ams_http_in_flight_requests`              | Number of HTTP requests being processed at the moment | 1.10.0           |
| `ams_http_request_duration_seconds_bucket` | The HTTP request latencies in seconds                 | 1.10.0           |
| `ams_http_request_size_bytes_bucket`       | The HTTP request size in bytes                        | 1.10.0           |
| `ams_http_requests_total`                  | Total number of HTTP requests made                    | 1.10.0           |
| `ams_http_response_size_bytes_bucket`      | The HTTP response sizes in bytes                      | 1.10.0           |
