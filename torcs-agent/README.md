# Python client for TORCS with network plugin for the 2012 SCRC

This is a copy of the reimplementation in Python 3 by @moltob of the original SCRC TORCS client pySrcrcClient from @lanquarden. It is used to teach ideas of computational intelligence. The file `my_driver.py` contains a shell to start writing your own driver.

## `Client`

* top level class
* handles _all_ aspects of networking (connection management, encoding)
* decodes class `State` from message from server, `state = self.decode(msg)`
* encodes class `Command` for message to server, `msg = self.encode(command)`
* internal state connection properties only and driver instance
* use `Client(driver=your_driver, <other options>)` to use your own driver

## `Driver`

* encapsulates driving logic only
* main entry point: `drive(state: State) -> Command`

## `State`

* represents the incoming car state

## `Command`

* holds the outgoing driving command


python run.py -p 3001


-----------------Car State:-----------------
angle: 4.950452752755485
current_lap_time: 4.888
damage: 0
distance_from_start: 45.0354
distance_raced: 49.0354
fuel: 93.9606
gear: 1
last_lap_time: 0.0
opponents: (200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0)
race_position: 1
rpm: 5683.0
speed_x: 13.780611111111112
speed_y: 0.01092636111111111
speed_z: 0.00012334972222222224
distances_from_edge: (10.829, 11.4774, 13.1625, 16.7668, 25.4807, 41.5498, 61.8257, 122.574, 200.0, 14.0383, 7.01071, 4.69575, 3.55041, 2.8718, 2.11467, 1.58255, 1.3372, 1.2303, 1.21596)
distance_from_center: -0.798096
wheel_velocities: (2392.2706820097264, 2384.3753235928234, 2448.95912625997, 2374.755362212577)
z: 0.344067
focused_distances_from_edge: (-1.0, -1.0, -1.0, -1.0, -1.0)



-----------------Command:-----------------
accelerator: 0.0
brake: 0.0
gear: 0
steering: 0.0
focus: 0.0


angle: TORCS angle [-180 , 180] in graden. In csv in radian
    TORCS: 
current_lap_time: 4.888

| TORCS | CSV   | Description                                          |
| ----- | ----- | ---------------------------------------------------- |
| angle | angle | TORCS angle [-180 , 180] in graden. In csv in radian |