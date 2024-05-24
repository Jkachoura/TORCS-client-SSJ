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
*csv naming convention: `trackname_laps_startingPosition_version.csv` (e.g. `aalborg_3_0.csv`)*
| Track name             | Laps | Starting Position | Tester | csv_name            | Collected             |
| ---------------------- | ---- | ----------------- | ------ | ------------------- | --------------------- |
| `Aalborg`              | 3    | 3                 | Sam    | `aalborg`           | :white_check_mark:    |
| `Alpine 1`             | 3    | 8                 | Sam    | `alpine1`           | :white_check_mark:    |
| `Alpine 2`             | 3    | 10                | Sam    | `alpine2`           | :white_check_mark:    |
| `Brondehach`           | 3    | 4                 | Sam    | `brondehach`        | :black_square_button: |
| `Corkscrew`            |      |                   | Sam    | `corkscrew`         | :black_square_button: |
| `E-Track 1`            |      |                   | Sam    | `etrack1`           | :black_square_button: |
| `E-Track 2`            |      |                   | Sam    | `etrack2`           | :black_square_button: |
| `E-Track 3`            | 3    | 9                 | Jaouad | `etrack3`           | :white_check_mark:    |
| `E-Track 4`            | 3    | 5                 | Jaouad | `etrack4`           | :white_check_mark:    |
| `E-Track 6`            | 3    | 8                 | Jaouad | `etrack6`           | :white_check_mark:    |
| `E-Road`               | 3    | 5                 | Jaouad | `eroad`             | :white_check_mark:    |
| `Forza`                | 3    | 7                 | Jaouad | `forza`             | :white_check_mark:    |
| `CG Speedway number 1` |      |                   | Jaouad | `cgspeedwaynumber1` | :black_square_button: |
| `CG track 2`           | 3    | 10                | Sabri  | `cgtrack2`          | :white_check_mark:    |
| `CG track 3`           | 3    | 3                 | Sabri  | `cgtrack3`          | :white_check_mark:    |
| `Olethros Road 1`      | 3    | 3                 | Sabri  | `olethrosroad1`     | :white_check_mark:    |
| `Ruudskogen`           | 3    | 7                 | Sabri  | `ruudskogen`        | :white_check_mark:    |
| `Spring`               | 1    | 4                 | Sabri  | `spring`            | :white_check_mark:    |
| `Street 1`             |      |                   | Sabri  | `street1`           | :black_square_button: |
| `Wheel 1`              |      |                   | Sabri  | `wheel1`            | :black_square_button: |
| `Wheel 2`              |      |                   | Sabri  | `wheel2`            | :black_square_button: |
| `A-Speedway`           |      |                   | Sam    | `aspeedway`         | :black_square_button: |
| `B-Speedway`           |      |                   | Sam    | `bspeedway`         | :black_square_button: |
| `C-Speedway`           |      |                   | Sam    | `cspeedway`         | :black_square_button: |
| `D-Speedway`           |      |                   | Jaouad | `dspeedway`         | :black_square_button: |
| `E-Speedway`           |      |                   | Jaouad | `espeedway`         | :black_square_button: |
| `E-Track 5`            |      |                   | Jaouad | `etrack5`           | :black_square_button: |
| `F-Speedway`           |      |                   | Sabri  | `fspeedway`         | :black_square_button: |
| `G-Speedway`           |      |                   | Sabri  | `gspeedway`         | :black_square_button: |
| `Michigan Speedway`    |      |                   | Sabri  | `michiganspeedway`  | :black_square_button: |