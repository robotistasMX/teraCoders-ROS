#!/usr/bin/env python
from clase5.srv import Ejemplo
import rospy

def cliente_ejemplo(x,y):
    rospy.wait_for_service('ejemplo')
    try:
        ejemplo = rospy.ServiceProxy('ejemplo', Ejemplo)
	resp1 = ejemplo(10, 9)
	return resp1.status
    except rospy.ServiceException, e:
	print("ERROR")
        
if __name__ == "__main__":
    x=9
    y=10
    print("Requesting: {} & {}".format(x,y))
    print("resultado: {}".format(cliente_ejemplo(x, y)))
