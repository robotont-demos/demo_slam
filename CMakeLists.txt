cmake_minimum_required(VERSION 3.16)
project(demo_slam)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY config launch
  DESTINATION share/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.yaml" PATTERN "*.py" PATTERN "*.xml" PATTERN "*.rviz"
)

ament_package()
