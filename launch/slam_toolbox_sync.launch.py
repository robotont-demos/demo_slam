from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, EmitEvent, LogInfo, RegisterEventHandler
from launch.conditions import IfCondition
from launch.events import matches_action
from launch.substitutions import AndSubstitution, LaunchConfiguration, NotSubstitution, PathJoinSubstitution
from launch_ros.actions import LifecycleNode
from launch_ros.event_handlers import OnStateTransition
from launch_ros.events.lifecycle import ChangeState
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterFile
from lifecycle_msgs.msg import Transition


def generate_launch_description():

    namespace_arg     = DeclareLaunchArgument('namespace',             default_value='')
    use_sim_time_arg  = DeclareLaunchArgument('use_sim_time',          default_value='false')
    autostart_arg     = DeclareLaunchArgument('autostart',             default_value='true')
    lifecycle_arg     = DeclareLaunchArgument('use_lifecycle_manager', default_value='false')
    params_file_arg   = DeclareLaunchArgument(
        'params_file',
        default_value=PathJoinSubstitution([
            FindPackageShare('2d_slam'), 'config', 'nodes', 'slam.yaml'
        ])
    )

    namespace             = LaunchConfiguration('namespace')
    use_sim_time          = LaunchConfiguration('use_sim_time')
    autostart             = LaunchConfiguration('autostart')
    use_lifecycle_manager = LaunchConfiguration('use_lifecycle_manager')

    params = ParameterFile(
        param_file=LaunchConfiguration('params_file'),
        allow_substs=True
    )

    slam_node = LifecycleNode(
        package='slam_toolbox',
        executable='sync_slam_toolbox_node',
        name='slam_toolbox',
        namespace=namespace,
        output='screen',
        remappings=[
            ('/map', ['/', namespace, '/map']),
            ('/map_updates', ['/', namespace, '/map_updates']),
            ('/map_metadata', ['/', namespace, '/map_metadata']),
        ],
        parameters=[
            params,
            {
                'use_lifecycle_manager': use_lifecycle_manager,
                'use_sim_time': use_sim_time,
            }
        ],
    )

    configure_event = EmitEvent(
        event=ChangeState(
            lifecycle_node_matcher=matches_action(slam_node),
            transition_id=Transition.TRANSITION_CONFIGURE
        ),
        condition=IfCondition(AndSubstitution(autostart, NotSubstitution(use_lifecycle_manager)))
    )

    activate_event = RegisterEventHandler(
        OnStateTransition(
            target_lifecycle_node=slam_node,
            start_state='configuring',
            goal_state='inactive',
            entities=[
                LogInfo(msg='[LifecycleLaunch] slam_toolbox node is activating.'),
                EmitEvent(event=ChangeState(
                    lifecycle_node_matcher=matches_action(slam_node),
                    transition_id=Transition.TRANSITION_ACTIVATE
                ))
            ]
        ),
        condition=IfCondition(AndSubstitution(autostart, NotSubstitution(use_lifecycle_manager)))
    )

    return LaunchDescription([
        namespace_arg,
        use_sim_time_arg,
        autostart_arg,
        lifecycle_arg,
        params_file_arg,
        slam_node,
        configure_event,
        activate_event,
    ])