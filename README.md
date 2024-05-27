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
| Track name             | Laps | Starting Position | Tester | csv_name            | Collected             |
| ---------------------- | ---- | ----------------- | ------ | ------------------- | --------------------- |
| `Aalborg`              | 3    | 3                 | Sam    | `aalborg`           | :white_check_mark:    |
| `Alpine 1`             | 3    | 8                 | Sam    | `alpine1`           | :white_check_mark:    |
| `Alpine 2`             | 3    | 10                | Sam    | `alpine2`           | :white_check_mark:    |
| `Brondehach`           | 3    | 10                | Sam    | `brondehach`        | :white_check_mark:    |
| `Corkscrew`            | 3    | 10                | Sam    | `corkscrew`         | :white_check_mark:    |
| `E-Track 1`            | X    | X                 | Sam    | `etrack1`           | :black_square_button: |
| `E-Track 2`            | X    | X                 | Sam    | `etrack2`           | :black_square_button: |
| `E-Track 3`            | 3    | 9                 | Jaouad | `etrack3`           | :white_check_mark:    |
| `E-Track 4`            | 3    | 5                 | Jaouad | `etrack4`           | :white_check_mark:    |
| `E-Track 6`            | 3    | 8                 | Jaouad | `etrack6`           | :white_check_mark:    |
| `E-Road`               | 3    | 5                 | Jaouad | `eroad`             | :white_check_mark:    |
| `Forza`                | 3    | 7                 | Jaouad | `forza`             | :white_check_mark:    |
| `CG Speedway number 1` | 3    | 10                | Jaouad | `cgspeedwaynumber1` | :white_check_mark:    |
| `CG track 2`           | 3    | 10                | Sabri  | `cgtrack2`          | :white_check_mark:    |
| `CG track 3`           | 3    | 3                 | Sabri  | `cgtrack3`          | :white_check_mark:    |
| `Olethros Road 1`      | 3    | 3                 | Sabri  | `olethrosroad1`     | :white_check_mark:    |
| `Ruudskogen`           | 3    | 7                 | Sabri  | `ruudskogen`        | :white_check_mark:    |
| `Spring`               | 1    | 4                 | Sabri  | `spring`            | :white_check_mark:    |
| `Street 1`             | 3    | 5                 | Sabri  | `street1`           | :white_check_mark:    |
| `Wheel 1`              | 3    | 6                 | Sabri  | `wheel1`            | :white_check_mark:    |
| `Wheel 2`              | 3    | 7                 | Sabri  | `wheel2`            | :white_check_mark:    |
| `A-Speedway`           | 3    | 3                 | Sabri  | `aspeedway`         | :white_check_mark:    |
| `B-Speedway`           | 3    | 8                 | Jaouad | `bspeedway`         | :white_check_mark:    |
| `C-Speedway`           | 3    | 5                 | Jaouad | `cspeedway`         | :white_check_mark:    |
| `D-Speedway`           | 3    | 10                | Jaouad | `dspeedway`         | :white_check_mark:    |
| `E-Speedway`           | 3    | 2                 | Jaouad | `espeedway`         | :white_check_mark:    |
| `E-Track 5`            | 3    | 6                 | Jaouad | `etrack5`           | :white_check_mark:    |
| `F-Speedway`           | 3    | 2                 | Sabri  | `fspeedway`         | :white_check_mark:    |
| `G-Speedway`           | 3    | 5                 | Sabri  | `gspeedway`         | :white_check_mark:    |
| `Michigan Speedway`    | 3    | 9                 | Sabri  | `michiganspeedway`  | :white_check_mark:    |



### New Bigger Dataset
*csv naming convention: `trackname_laps_startingPosition_version.csv` (e.g. `aalborg_3_6_0.csv`)*
| Track name             | Laps | Starting Position | csv_name            | Collected             |
| ---------------------- | ---- | ----------------- | ------------------- | --------------------- |
| `Aalborg`              | 35   | 1                 | `aalborg`           | :white_check_mark:    |
| `Alpine 1`             | 27   | 10                | `alpine1`           | :white_check_mark:    |
| `Alpine 2`             | 28   | 10                | `alpine2`           | :white_check_mark:    |
| `Brondehach`           | 30   | 10                | `brondehach`        | :white_check_mark:    |
| `Corkscrew`            | 30   | 10                | `corkscrew`         | :white_check_mark:    |
| `E-Track 3`            | 20   | 10                | `etrack3`           | :white_check_mark:    |
| `E-Track 4`            | 20   | 10                | `etrack4`           | :white_check_mark:    |
| `E-Track 6`            | 30   | 10                | `etrack6`           | :white_check_mark:    |
| `E-Road`               | 30   | 10                | `eroad`             | :white_check_mark:    |
| `Forza`                | 25   | 10                | `forza`             | :white_check_mark:    |
| `CG Speedway number 1` | 30   | 10                | `cgspeedwaynumber1` | :white_check_mark:    |
| `CG track 2`           | 25   | 10                | `cgtrack2`          | :white_check_mark:    |
| `CG track 3`           | 30   | 10                | `cgtrack3`          | :white_check_mark:    |
| `Olethros Road 1`      | 25   | 10                | `olethrosroad1`     | :white_check_mark:    |
| `Ruudskogen`           | 30   | 10                | `ruudskogen`        | :white_check_mark:    |
| `Spring`               | 7    | 10                | `spring`            | :white_check_mark:    |
| `Street 1`             | 30   | 7                 | `street1`           | :white_check_mark:    |
| `Wheel 1`              | 30   | 10                | `wheel1`            | :white_check_mark:    |
| `Wheel 2`              | 30   | 8                 | `wheel2`            | :white_check_mark:    |
| `A-Speedway`           |      |                   | `aspeedway`         | :black_square_button: |
| `B-Speedway`           |      |                   | `bspeedway`         | :black_square_button: |
| `C-Speedway`           |      |                   | `cspeedway`         | :black_square_button: |
| `D-Speedway`           |      |                   | `dspeedway`         | :black_square_button: |
| `E-Speedway`           |      |                   | `espeedway`         | :black_square_button: |
| `E-Track 5`            |      |                   | `etrack5`           | :black_square_button: |
| `F-Speedway`           |      |                   | `fspeedway`         | :black_square_button: |
| `G-Speedway`           |      |                   | `gspeedway`         | :black_square_button: |
| `Michigan Speedway`    |      |                   | `michiganspeedway`  | :black_square_button: |
