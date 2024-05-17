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