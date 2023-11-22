#! /usr/bin/env python3 
import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped, String
from tf2_ros import TransformListener, Buffer
from tf2_geometry_msgs import do_transform_pose
import tf_transformations
import tf2_ros
import tf2_geometry_msgs
import sys

class WaypointListener(Node):
    def __init__(self):
        super().__init__('waypoint_listener')
        self.nav = BasicNavigator()
        self.waypoints = []
        self.initial_pose = self.create_pose_stamped(nav, 0.0, 0.0, 0.0)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.create_initial_pose()
        self.create_default_waypoints()

        self.nav.waitUntilNav2Active()
        self.nav.setInitialPose(self.initial_pose)

        self.cmd_subscription = self.create_subscription(
            String, 'command_topic', self.command_callback, 10)
        self.cmd_subscription

    def create_initial_pose(self):
        pass
        # Define a função create_pose_stamped aqui

    def create_pose_stamped(self, navigator, pos_x, pos_y, rot_z):
        q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, rot_z)
        self.pose = PoseStamped()
        self.pose.header.frame_id = 'map'
        self.pose.header.stamp = nav.get_clock().now().to_msg()
        self.pose.pose.position.x = pos_x
        self.pose.pose.position.y = pos_y
        self.pose.pose.position.z = pos_x
        self.pose.pose.orientation.x = q_x
        self.pose.pose.orientation.y = q_y
        self.pose.pose.orientation.z = q_z
        self.pose.pose.orientation.w = q_w
        return self.pose
        # Define os goal_poses aqui

    def command_callback(self, msg):
        command = msg.data
        if command == 'adicionar_waypoint':
            # Adiciona um novo waypoint à lista
            new_waypoint = self.create_pose_stamped(self.nav, 2.0, 3.0, 1.57)  # Exemplo de novo waypoint
            self.waypoints.append(new_waypoint)
            self.nav.followWaypoints(self.waypoints)

nav = BasicNavigator()
def main(args=None):
    rclpy.init(args=args)
    waypoint_listener = WaypointListener()
    rclpy.spin(waypoint_listener)
    waypoint_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
