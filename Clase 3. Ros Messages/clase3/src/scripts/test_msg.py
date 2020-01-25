#!/usr/bin/env python


import rospy
import sys
from clase3.msg import Example

def talker(x,y):
    pub = rospy.Publisher('test', Example, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(x,y)
        rate.sleep()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            talker(int(sys.argv[1]),int(sys.argv[2]))
        except rospy.ServiceException, e:
            print("ERROR")
    else:
        print("eror en argumentos")
        sys.exit(1)
	

