#! /usr/bin/env python3

import sys
import rclpy
import tf2_ros
import tf2_geometry_msgs
import tf_transformations
import json
from rclpy.node import Node
from tf2_ros import TransformListener, Buffer
from tf2_geometry_msgs import do_transform_pose
from geometry_msgs.msg import PoseStamped, String
from nav2_simple_commander.robot_navigator import BasicNavigator

class Navigation(Node):

    def __init__(self):
        super().__init__('navigation')
        self.nav = BasicNavigator()
        self.waypoints = []
        self.initial_pose = self.create_pose_stamped(self.nav, 0.0, 0.0, 0.0)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.create_initial_pose()

        self.nav.waitUntilNav2Active()
        self.nav.setInitialPose(self.initial_pose)

        self.subscription = self.create_subscription(
            String,
            'move_robot',
            self.listener_callback,
            10)
        self.subscription

    def create_initial_pose(self):
        pass

    def create_pose_stamped(self, navigator, pos_x, pos_y, rot_z):
        q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, rot_z)
        self.pose = PoseStamped()
        self.pose.header.frame_id = 'map'
        self.pose.header.stamp = self.nav.get_clock().now().to_msg()
        self.pose.pose.position.x = pos_x
        self.pose.pose.position.y = pos_y
        self.pose.pose.position.z = pos_x
        self.pose.pose.orientation.x = q_x
        self.pose.pose.orientation.y = q_y
        self.pose.pose.orientation.z = q_z
        self.pose.pose.orientation.w = q_w
        return self.pose

    def map_range(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    def listener_callback(self, msg):
        command = json.load(msg.data)
        
        # Lendo os valores de x e y do comando
        x = command['x']
        y = command['y']

        # Mapeando os valores de x e y para o intervalo desejado
        x_mapped = self.map_range(x, 0, 1000, 0.0, 1.8)  # Supondo que o intervalo original de x seja de 0 a 1000
        y_mapped = self.map_range(y, 0, 1000, 0.0, 1.8)  # Supondo que o intervalo original de y seja de 0 a 1000

        # Criando o ponto dentro dos limites desejados
        new_waypoint = self.create_pose_stamped(self.nav, x_mapped, y_mapped, 0.0)
        self.waypoints.append(new_waypoint)
        self.nav.followWaypoints(self.waypoints)

def main(args=None):

    rclpy.init(args=args)
    waypoint_listener = Navigation()
    rclpy.spin(waypoint_listener)
    waypoint_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()