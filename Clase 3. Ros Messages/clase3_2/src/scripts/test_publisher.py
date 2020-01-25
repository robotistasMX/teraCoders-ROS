#!/usr/bin/env python

import rospy
import sys
from clase3_2.msg import Pines

def talker(x,y):
    pub = rospy.Publisher('test', Pines)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(x,y)
        rate.sleep()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            talker(str(sys.argv[1]),int(sys.argv[2]))
        except rospy.ServiceException, e:
            print("ERROR")
    else:
        print("eror en argumentos")
        sys.exit(1)
	
