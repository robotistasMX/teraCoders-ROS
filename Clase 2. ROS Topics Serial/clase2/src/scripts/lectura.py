#!/usr/bin/env python
import rospy 
import time 
import serial 
from std_msgs.msg import Int32 


def callback(data):
    print("el numeor es: {}".format(data.data))

if __name__ == "__main__":
    rospy.init_node("lectura", anonymous=False)
    rospy.Subscriber("ultra/data", Int32, callback)
    rospy.spin()