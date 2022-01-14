#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter") 


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
