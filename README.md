# Demo Slam
This repository is a ROS package that contains the base for supporting 2D mapping demo showing the capabilities of the Robotont platform create a 2D map of the surrounding using different methods.

## Besides this package, you need to clone one of the following mapping packages for different mapping methods
 * [gmapping](https://github.com/robotont-demos/demo_slam_gmapping)
 * [cartographer](https://github.com/robotont-demos/demo_slam_cartographer)
 * [Hector slam](https://github.com/robotont-demos/demo_slam_hector)

**On PC**, visualize the result in RViz with:<br/>
```bash
roslaunch demo_slam slam_2d_display.launch
```
