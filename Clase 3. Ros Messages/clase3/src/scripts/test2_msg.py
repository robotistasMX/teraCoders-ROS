#!/usr/bin/env python
import rospy
import sys
from clase3.msg import Example

def callback(data):
    print(data.n)

def listener():
    rospy.init_node('listener')
    rospy.Subscriber('test', Example, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()