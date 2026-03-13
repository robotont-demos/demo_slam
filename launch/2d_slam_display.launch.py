from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os
import yaml
import tempfile

def launch_setup(context, *args, **kwargs):
    namespace = LaunchConfiguration('namespace').perform(context)
    
    rviz_config_path = os.path.join(
        get_package_share_directory('2d_slam'),
        'config',
        'rviz2',
        'costmaps_visualization_robotont.rviz'
    )

    # Load and patch the rviz config
    with open(rviz_config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Override fixed frame if namespace is provided
    if namespace:
        config['Visualization Manager']['Global Options']['Fixed Frame'] = f'{namespace}/map'
    
    # Write to a temp file
    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.rviz', delete=False)
    yaml.dump(config, tmp)
    tmp.flush()

    return [
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            namespace=namespace,
            output='screen',
            arguments=['-d', tmp.name],
        )
    ]

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='Robot namespace'
        ),
        OpaqueFunction(function=launch_setup)
    ])