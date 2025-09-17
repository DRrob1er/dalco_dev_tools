import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    stage_launch = os.path.join(
        get_package_share_directory('stage_ros2'),
        'launch',
        'stage.launch.py'
    )

    world_file = os.path.join(
        get_package_share_directory('dalco_simulation'),
        'worlds',
        'dalco_horeca'
    )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(stage_launch),
            launch_arguments={
                'world': world_file,
                'enforce_prefixes': 'false',
                'one_tf_tree': 'true'
            }.items()
        )
    ])
