# Dalco Dev Tools
Dalco development tools is used as the name suggested. Simulation and testing
---

## Simulation with Stage (ROS 2)

We use [stage_ros2](https://github.com/tuw-robotics/stage_ros2) as the simulator backend, together with the original [Stage](https://github.com/tuw-robotics/Stage) library.

### Folder Structure

```
dalco_dev_tools/
  dalco_simulation/        # our own package (launch, worlds, robots, configs)
    launch/                # wrapper launch files
    worlds/                # Stage world definitions (.world)
    robots/                # robot model definitions (.inc)
    scripts/               # helper scripts, image conversion
    maps/                  # maps used in AMCL
  Stage/                   # external Stage simulator (cloned)
  stage_ros2/              # ROS 2 wrapper for Stage (cloned)
```

### Setup
Clone submodules:

```bash
cd ~/dalco_ws/src/dalco_dev_tools
git clone https://github.com/tuw-robotics/Stage.git
git clone https://github.com/tuw-robotics/stage_ros2.git
```

Install dependencies:

```bash
cd ~/dalco_ws
rosdep install --from-paths src --ignore-src -r -y
```

Build:

```bash
cd ~/dalco_ws
colcon build --symlink-install
source install/setup.bash
```

### Running the Simulator

Run Stage directly with the default launch file from `stage_ros2`:

```bash
ros2 launch stage_ros2 stage.launch.py world:=cave enforce_prefixes:=false one_tf_tree:=true
```

Or use the wrappers in `dalco_simulation`:

```bash
ros2 launch dalco_simulation sim_horeca.launch.py
ros2 launch dalco_simulation csd_shuttle.launch.py
```
