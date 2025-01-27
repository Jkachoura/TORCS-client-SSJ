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
| `Aalborg`              | 85   | 01 & 04 & 07      | `aalborg`           | :white_check_mark: |
| `Alpine 1`             | 77   | 10 & 07 & 06      | `alpine1`           | :white_check_mark: |
| `Alpine 2`             | 78   | 10 & 05 & 08      | `alpine2`           | :white_check_mark: |
| `Brondehach`           | 80   | 06 & 08 & 06      | `brondehach`        | :white_check_mark: |
| `Corkscrew`            | 120  | 10 & 05 & 06      | `corkscrew`         | :white_check_mark: |
| `E-Track 3`            | 80   | 10 & 06 & 06      | `etrack3`           | :white_check_mark: |
| `E-Track 4`            | 73   | 10 & 04 & 06      | `etrack4`           | :white_check_mark: |
| `E-Track 6`            | 89   | 10 & 04 & 06      | `etrack6`           | :white_check_mark: |
| `E-Road`               | 90   | 10 & 07 & 04      | `eroad`             | :white_check_mark: |
| `Forza`                | 85   | 10 & 04 & 06      | `forza`             | :white_check_mark: |
| `CG Speedway number 1` | 90   | 10 & 08 & 04      | `cgspeedwaynumber1` | :white_check_mark: |
| `CG track 2`           | 85   | 10 & 04 & 06      | `cgtrack2`          | :white_check_mark: |
| `CG track 3`           | 90   | 10 & 05 & 08      | `cgtrack3`          | :white_check_mark: |
| `Olethros Road 1`      | 70   | 10 & 04 & 06      | `olethrosroad1`     | :white_check_mark: |
| `Ruudskogen`           | 85   | 10 & 07 & 03      | `ruudskogen`        | :white_check_mark: |
| `Spring`               | 20   | 10 & 04 & 07      | `spring`            | :white_check_mark: |
| `Street 1`             | 90   | 07 & 04 & 09      | `street1`           | :white_check_mark: |
| `Wheel 1`              | 90   | 10 & 04 & 07      | `wheel1`            | :white_check_mark: |
| `Wheel 2`              | 90   | 08 & 04 & 02      | `wheel2`            | :white_check_mark: |