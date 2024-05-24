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
*csv naming convention: `trackname_laps_version.csv` (e.g. `aalborg_3_0.csv`)*
| Track name             | Laps | Tester | csv_name            | Collected             |
| ---------------------- | ---- | ------ | ------------------- | --------------------- |
| `Aalborg`              |      | Sam    | `aalborg`           | :black_square_button: |
| `Alpine 1`             |      | Sam    | `alpine1`           | :black_square_button: |
| `Alpine 2`             |      | Sam    | `alpine2`           | :black_square_button: |
| `Brondehach`           |      | Sam    | `brondehach`        | :black_square_button: |
| `Corkscrew`            |      | Sam    | `corkscrew`         | :black_square_button: |
| `E-Track 1`            |      | Sam    | `etrack1`           | :black_square_button: |
| `E-Track 2`            |      | Sam    | `etrack2`           | :black_square_button: |
| `E-Track 3`            |      | Jaouad | `etrack3`           | :black_square_button: |
| `E-Track 4`            |      | Jaouad | `etrack4`           | :black_square_button: |
| `E-Track 6`            |      | Jaouad | `etrack6`           | :black_square_button: |
| `E-Road`               |      | Jaouad | `eroad`             | :black_square_button: |
| `Forza`                |      | Jaouad | `forza`             | :black_square_button: |
| `CG Speedway number 1` |      | Jaouad | `cgspeedwaynumber1` | :black_square_button: |
| `CG track 2`           |      | Sabri  | `cgtrack2`          | :black_square_button: |
| `CG track 3`           |      | Sabri  | `cgtrack3`          | :black_square_button: |
| `Olethros Road 1`      |      | Sabri  | `olethrosroad1`     | :black_square_button: |
| `Ruudskogen`           |      | Sabri  | `ruudskogen`        | :black_square_button: |
| `Spring`               | 1    | Sabri  | `spring`            | :black_square_button: |
| `Street 1`             |      | Sabri  | `street1`           | :black_square_button: |
| `Wheel 1`              |      | Sabri  | `wheel1`            | :black_square_button: |
| `Wheel 2`              |      | Sabri  | `wheel2`            | :black_square_button: |
| `Dirt 1`               |      | Sam    | `dirt1`             | :black_square_button: |
| `Dirt 2`               |      | Sam    | `dirt2`             | :black_square_button: |
| `Dirt 3`               |      | Sam    | `dirt3`             | :black_square_button: |
| `Dirt 4`               |      | Jaouad | `dirt4`             | :black_square_button: |
| `Dirt 5`               |      | Jaouad | `dirt5`             | :black_square_button: |
| `Dirt 6`               |      | Jaouad | `dirt6`             | :black_square_button: |
| `Mixed 1`              |      | Sabri  | `mixed1`            | :black_square_button: |
| `Mixed 2`              |      | Sabri  | `mixed2`            | :black_square_button: |
| `A-Speedway`           |      | Sam    | `aspeedway`         | :black_square_button: |
| `B-Speedway`           |      | Sam    | `bspeedway`         | :black_square_button: |
| `C-Speedway`           |      | Sam    | `cspeedway`         | :black_square_button: |
| `D-Speedway`           |      | Jaouad | `dspeedway`         | :black_square_button: |
| `E-Speedway`           |      | Jaouad | `espeedway`         | :black_square_button: |
| `E-Track 5`            |      | Jaouad | `etrack5`           | :black_square_button: |
| `F-Speedway`           |      | Sabri  | `fspeedway`         | :black_square_button: |
| `G-Speedway`           |      | Sabri  | `gspeedway`         | :black_square_button: |
| `Michigan Speedway`    |      | Sabri  | `michiganspeedway`  | :black_square_button: |