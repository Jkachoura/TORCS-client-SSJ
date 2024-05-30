# TORCS-client-SSJ

## Sensors
| Carstate label         | TORCS                             | CSV              |
| ---------------------- | --------------------------------- | ---------------- |
| `angle`                | [-180, 180] (degrees)             | [-π, π] (rad)    |
| `opponents`            | ?                                 | ?                |
| `rpm`                  | [0, 10000]                        | [0, 10000]       |
| `speed_x`              | [-50, 300]                        | []               |
| `speed_y`              | [-50, 50]                         | []               |
| `distance_from_edge`   | ?                                 | ?                |
| `distance_from_center` | [-1, 1] (right edge to left edge) | `track_position` |

## Actions
| Action label   | TORCS   | CSV     |
| -------------- | ------- | ------- |
| `acceleration` | [0, 1]  | [0, 1]  |
| `brake`        | [0, 1]  | [0, 1]  |
| `steering`     | [-1, 1] | [-1, 1] |

## Gathering Training Data
### Used drivers settings
- `berniw 1`
- `berniw two 1`
- `scr_server_1`
- `berniw hist 1`
- `bt 1`
- `damned 1`
- `olethros 1`
- `berniw 2`
- `berniw 3`
- `berniw 4`

### Data Collection Progress
*csv naming convention: `trackname_laps_startingPosition_version.csv` (e.g. `aalborg_3_6_0.csv`)*
| Track name             | Laps | Starting Position | csv_name            | Collected          |
| ---------------------- | ---- | ----------------- | ------------------- | ------------------ |
| `Aalborg`              | 55   | 01 & 04           | `aalborg`           | :white_check_mark: |
| `Alpine 1`             | 47   | 10 & 07           | `alpine1`           | :white_check_mark: |
| `Alpine 2`             | 48   | 10 & 05           | `alpine2`           | :white_check_mark: |
| `Brondehach`           | 50   | 06 & 08           | `brondehach`        | :white_check_mark: |
| `Corkscrew`            | 90   | 10 & 05           | `corkscrew`         | :white_check_mark: |
| `E-Track 3`            | 50   | 10 & 06           | `etrack3`           | :white_check_mark: |
| `E-Track 4`            | 43   | 10 & 04           | `etrack4`           | :white_check_mark: |
| `E-Track 6`            | 59   | 10 & 04           | `etrack6`           | :white_check_mark: |
| `E-Road`               | 60   | 10 & 07           | `eroad`             | :white_check_mark: |
| `Forza`                | 25   | 10 & 04           | `forza`             | :white_check_mark: |
| `CG Speedway number 1` | 60   | 10 & 08           | `cgspeedwaynumber1` | :white_check_mark: |
| `CG track 2`           | 25   | 10 & 04           | `cgtrack2`          | :white_check_mark: |
| `CG track 3`           | 60   | 10 & 05           | `cgtrack3`          | :white_check_mark: |
| `Olethros Road 1`      | 40   | 10 & 04           | `olethrosroad1`     | :white_check_mark: |
| `Ruudskogen`           | 55   | 10 & 07           | `ruudskogen`        | :white_check_mark: |
| `Spring`               | 7    | 10                | `spring`            | :white_check_mark: |
| `Street 1`             | 30   | 07                | `street1`           | :white_check_mark: |
| `Wheel 1`              | 30   | 10                | `wheel1`            | :white_check_mark: |
| `Wheel 2`              | 30   | 08                | `wheel2`            | :white_check_mark: |