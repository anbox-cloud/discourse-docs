This page collects performance benchmarks collected from various virtual and bare metal hardware in order to provide an overview of what can be achieved with Anbox Cloud.

## Bare Metal

| Instance Type                       | Anbox Cloud version | Rendering / encoding | Resolution | Application         | # containers | avg FPS |
|-------------------------------------|---------------------|----------------------|------------|---------------------|--------------|---------|
| Ampere Altra + 1x Nvidia Tesla T4   | 1.11.2 (appliance)  | hardware / hardware  | 720p       | BombSquad Stress    | 30           | 29      |
| Ampere Altra + 2x Nvidia Tesla T4   | 1.11.2 (appliance)  | hardware / hardware  | 720p       | BombSquad Stress    | 55           | 29      |
| Ampere Altra + 1x Nvidia Tesla T4   | 1.11.2 (appliance)  | hardware / hardware  | 1080p      | BombSquad Stress    | 20           | 28      |
| Ampere Altra + 2x Nvidia Tesla T4   | 1.11.2 (appliance)  | hardware / hardware  | 1080p      | BombSquad Stress    | 50           | 26      |

## AWS

| Instance Type | Anbox Cloud version | Rendering / encoding | Resolution | Application         | # containers | avg FPS |
|---------------|---------------------|----------------------|------------|---------------------|--------------|---------|
| m6g.2xlarge   | 1.11.2 (appliance)  | software / software  | 720p       | Android 10 Launcher | 3            | 20      |
| m5a.2xlarge   | 1.11.2 (appliance)  | software / software  | 720p       | Android 10 Launcher | 3            | 13      |
