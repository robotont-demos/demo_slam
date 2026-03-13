# demo_slam

![ROS 2](https://img.shields.io/badge/ROS2%20-Jazzy-blue.svg) ![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)

## **Overview**
SLAM demo for Robotont (ROS 2).
## **Table of Contents**
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Building the Package](#building-the-package)
- [Launch Files](#launch-files)
- [License](#license)

---

## **Installation**

### **1. Clone the Repository**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>/src
git clone https://github.com/robotont-demos/demo_slam.git
```

## **Dependencies**
### **1. List of dependencies**
1.1. robotont_navigation<br>
1.2. depthimage_to_laserscan<br>
1.3. slam_toolbox

### **2. Install dependencies**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>
rosdep install --from-paths src --ignore-src -r -y
```

## **Building the package**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>
colcon build --packages-select demo_slam
```

## **Launch files**
### **1. Source workspace**
```bash
source ~/<YOUR_WORKSPACE_NAME_HERE>/install/setup.bash
```
## 2. Available Launch Files

### 2.1. `2d_slam.launch.py`
Launch navigation (Nav2) together with SLAM (slam_toolbox).

**Usage:**
```bash
ros2 launch demo_slam 2d_slam.launch.py
```

### 2.2. `rviz2_visualize_costmaps.launch.py`
Launches RViz2 with a preconfigured layout for visualizing the robot's costmaps and state.

**Usage:**
```bash
ros2 launch demo_slam 2d_slam_display.launch.py
```

## **License**
This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for more information.
