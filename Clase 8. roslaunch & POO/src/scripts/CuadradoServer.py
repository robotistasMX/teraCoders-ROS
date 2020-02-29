#!/usr/bin/env python
from clase8.srv import Cuadrado,CuadradoResponse
import rospy
import math

def handle_cuadrado(req):
    lado=int(math.sqrt(req.area))
    base=int(math.sqrt(req.area))
    resultado=str(lado)+":"+str(base)
    return CuadradoResponse(resultado)

if __name__ == "__main__":
    rospy.init_node('cuadrado_servidor')
    s = rospy.Service('cuadrado', Cuadrado, handle_cuadrado)
    rospy.spin()