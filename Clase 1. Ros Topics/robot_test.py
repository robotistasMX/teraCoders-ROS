#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

sensor1=0
sensor2=0
sensor3=0

def callback(msg):
    global sensor1
    global sensor2
    global sensor3
    sensor1=msg.ranges[300]
    sensor2=msg.ranges[350]
    sensor3=msg.ranges[400]
    print(sensor1)
    print(sensor2)
    print(sensor3)
    print()

if __name__ == '__main__':
    rospy.init_node('topics_node')
    sub = rospy.Subscriber('/hokuyo_base/scan', LaserScan, callback)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    rate = rospy.Rate(10)
    move = Twist()

    while not rospy.is_shutdown():
        if sensor1 > 1 and sensor2 > 1 and sensor3 > 1:
            move.linear.x = 0.5
            move.angular.z = 0.0
        else:
            move.linear.x = 0.0
            move.angular.z = 0.5

        pub.publish(move)
        rate.sleep()
