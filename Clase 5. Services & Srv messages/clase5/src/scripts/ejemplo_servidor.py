#!/usr/bin/env python
from clase5.srv import Ejemplo,EjemploResponse
import rospy

def handle_ejemplo(req):
    if req.ultra1 < 8 or req.ultra2 <8:
        return EjemploResponse("veo algo")
    else:
        return EjemploResponse("NO VEO NADA")

if __name__ == "__main__":
    rospy.init_node('ejemplo_servidor')
    s = rospy.Service('ejemplo', Ejemplo, handle_ejemplo)
    print("esperando...")
    rospy.spin()
