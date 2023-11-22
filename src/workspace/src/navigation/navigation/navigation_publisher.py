#! /usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import String

class NavigationPublisher(Node):

    def __init__(self):
        super().__init__('command_publisher')
        self.publisher = self.create_publisher(String, 'command_topic', 10)

    def publish_command(self, command):
        msg = String()
        msg.data = command
        self.publisher.publish(msg)

def main(args=None):

    rclpy.init(args=args)
    command_publisher = NavigationPublisher()

    while True:
        command = input("Enter a command: ")
        command_publisher.publish_command(command)

    rclpy.spin(command_publisher)
    command_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
