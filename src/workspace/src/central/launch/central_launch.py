from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition

def generate_launch_description():
    return LaunchDescription([
       
        ExecuteProcess(
          cmd=['ros2', 'run', 'central', 'telegram'],
        output='screen',
        ),

        ExecuteProcess(
          cmd=['ros2', 'run', 'central', 'llm'],
        output='screen',
        ),
        
        ExecuteProcess(
          cmd=['ros2', 'run', 'central', 'voice_processing'],
        output='screen',
        ),

        ExecuteProcess(
          cmd=['ros2', 'run', 'central', 'regex'],
        output='screen',
        )
       
    ])