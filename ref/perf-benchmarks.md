The following benchmarks give an overview of the performance that you can achieve with Anbox Cloud.

The benchmarks were performed using the `amc benchmark` utility as described in [How to run benchmarks](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770). The results describe the maximum number of parallel running containers (column "# Containers") delivering a stable frame rate (column "Avg. FPS"). Running more containers either gives too high variation in the provided frame rate or is not possible due to other hardware limitations (system memory, GPU memory, ...).

All benchmarks include rendering and video encoding. On machines/VMs without a GPU, rendering and video encoding are performed in software on the CPU.

For most of the benchmarks below, a special version of the [BombSquad](https://www.froemling.net/apps/bombsquad) application was used. This version runs in a demo mode in which the game provides random and automated simulated gameplay. This allows the benchmark to simulate a real-world scenario where actual users would play the game, instead of sitting on a static game scene without much variation across the Android instances.

All benchmarks are done with a variation of the following `amc benchmark` command:

    amc benchmark --network-address 192.168.100.1 -n <number of containers> \
        -p webrtc -f -s 0.1 --measure-time 5m \
        --userdata '{"display_width":1280,"display_height":720,"fps":30,"benchmark":{"enabled":true}}' \
        <app name>

## Bare metal

| Hardware                            | Anbox Cloud version | Rendering / encoding | Resolution | Application         | # Containers | Avg. FPS |
|-------------------------------------|---------------------|----------------------|------------|---------------------|--------------|---------|
| Ampere Altra + 1x NVIDIA Tesla T4   | 1.11.2 (appliance)  | hardware / hardware  | 720p       | [BombSquad](https://www.froemling.net/apps/bombsquad)    | 30           | 29      |
| Ampere Altra + 2x NVIDIA Tesla T4   | 1.11.2 (appliance)  | hardware / hardware  | 720p       | [BombSquad](https://www.froemling.net/apps/bombsquad)    | 55           | 29      |
| Ampere Altra + 1x NVIDIA Tesla T4   | 1.11.2 (appliance)  | hardware / hardware  | 1080p      | [BombSquad](https://www.froemling.net/apps/bombsquad)    | 20           | 28      |
| Ampere Altra + 2x NVIDIA Tesla T4   | 1.11.2 (appliance)  | hardware / hardware  | 1080p      | [BombSquad](https://www.froemling.net/apps/bombsquad)    | 50           | 26      |

## AWS

| Instance type | Anbox Cloud version | Rendering / encoding | Resolution | Application         | # Containers | Avg. FPS |
|---------------|---------------------|----------------------|------------|---------------------|--------------|---------|
| `m6g.2xlarge` | 1.11.2 (appliance)  | software / software  | 720p       | Android 10 Launcher | 3            | 20      |
| `m5a.2xlarge` | 1.11.2 (appliance)  | software / software  | 720p       | Android 10 Launcher | 3            | 13      |
| `g5g.metal`   | 1.12.1 (appliance)  | hardware / hardware  | 720p       | [BombSquad](https://www.froemling.net/apps/bombsquad) | 55 | 28 |
| `g5g.metal`   | 1.12.1 (appliance)  | hardware / hardware  | 720p       | [BombSquad](https://www.froemling.net/apps/bombsquad) | 40 | 55 |
| `g5g.metal`   | 1.12.1 (appliance)  | hardware / hardware  | 1080p      | [BombSquad](https://www.froemling.net/apps/bombsquad) | 40 | 27 |
| `g5g.metal`   | 1.12.1 (appliance)  | hardware / hardware  | 1080p      | [BombSquad](https://www.froemling.net/apps/bombsquad) | 20 | 57 |
