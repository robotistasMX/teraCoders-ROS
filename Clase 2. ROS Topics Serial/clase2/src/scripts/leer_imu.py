#!/usr/bin/env python
import rospy 
import time 
import serial 
from std_msgs.msg import Int32 


if __name__ == "__main__":
    rospy.init_node("ultra", anonymous=False)
    pub_ultra = rospy.Publisher("ultra/data",Int32)
    rate = rospy.Rate(20)

    arduino = serial.Serial("/dev/ttyACM0", baudrate=9600,timeout=0.5)
    
    while not rospy.is_shutdown():
        line = arduino.readline()
        line = line.rstrip('/r/n')
        try:
            pub_ultra.publish(int(line))
            print("estoy mandando info")
        except:
            print("ERROR SERIAL")
        rate.sleep() 