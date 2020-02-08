#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def mensaje():
    pub = rospy.Publisher('saludar', String)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "Que onda %s" % rospy.get_time()
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('nodo_saludar', anonymous=True)
    try:
        mensaje()
    except rospy.ROSInterruptException:
        pass
