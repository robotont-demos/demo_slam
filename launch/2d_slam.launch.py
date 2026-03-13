from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    namespace_arg    = DeclareLaunchArgument('namespace',    default_value='')
    use_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='false')

    namespace    = LaunchConfiguration('namespace')
    use_sim_time = LaunchConfiguration('use_sim_time')

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            FindPackageShare('robotont_navigation'), 'launch', 'nav2_bringup.launch.py'
        ])),
        launch_arguments={
            'namespace':    namespace,
            'use_sim_time': use_sim_time,
            'params_file':  PathJoinSubstitution([
                FindPackageShare('robotont_navigation'), 'config', 'nav', 'nav2_gen3_lite.yaml'
            ]),
        }.items()
    )

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            FindPackageShare('demo_slam'), 'launch', 'slam_toolbox_sync.launch.py'
        ])),
        launch_arguments={
            'namespace':    namespace,
            'use_sim_time': use_sim_time,
            'params_file':  PathJoinSubstitution([
                FindPackageShare('demo_slam'), 'config', 'nodes', 'slam.yaml'
            ]),
        }.items()
    )

    return LaunchDescription([
        namespace_arg,
        use_sim_time_arg,
        nav2,
        slam,
    ])