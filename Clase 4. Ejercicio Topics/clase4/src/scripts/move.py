#! /usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('topics_node')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist)

    rate = rospy.Rate(10)
    move = Twist()

    while not rospy.is_shutdown():
        move.linear.x = 4
        move.angular.z = 1

        pub.publish(move)
        rate.sleep()

        