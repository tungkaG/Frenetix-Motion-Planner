cmake_minimum_required(VERSION 3.8)
project(trajectory_msgs_custom)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/BoardInputData.msg"
  "msg/CartesianSample.msg"
  "msg/CurvilinearSample.msg"
  "msg/BoardOutputData.msg"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
