#! /usr/bin/env python
import rospy
from robot import Robot
from clase8.srv import Cuadrado

if __name__ == '__main__':
    rospy.init_node('main')
    tortuga = Robot("franco")
    """
    tortuga.mostrar_nombre()
    tortuga.girar(2,90)
    tortuga.mover_derecho(1,3)
    """
    rospy.wait_for_service('cuadrado')
    try:
        cuadrado = rospy.ServiceProxy('cuadrado', Cuadrado)
        resp1 = cuadrado(8)
        lados=resp1.resultado.split(":")
        print(lados)
        tortuga.cuadrado(int(lados[0]), int(lados[1]))
    except rospy.ServiceException, e:
        print("ERROR") 