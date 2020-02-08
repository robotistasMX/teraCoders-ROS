#! /usr/bin/env python
import rospy
import math
import sys
from clase4.msg import Ejercicio
from geometry_msgs.msg import Twist
import time 

def circle(radio,w):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    speed = w*radio 
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = w
    vel_msg.linear.x = speed

    t0 = rospy.Time.now().to_sec()
    S=2*math.pi*radio
    current_distance = 0
    while(current_distance < S):
        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance= speed*(t1-t0)
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def rotate(speed,angle):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    angular_speed = math.radians(speed) 
    relative_angle = math.radians(angle) 
    vel_msg.linear.x = 0 
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angular_speed
 
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_angle= angular_speed*(t1-t0)
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    
def straight_line(speed,distance):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = speed 
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    while(current_distance < distance):
        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance= speed*(t1-t0)
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    
def run_shape(id_fig,area):
    rospy.init_node('ejercicio_node')
    pub = rospy.Publisher('tortuga', Ejercicio, queue_size=10)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0 
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    time.sleep(2)
    
    """
    id_fig  1-> cuadrado, 2-> rectangulo, 
            3->triangulo, 4->circulo
    """

    if id_fig == 1: #cuadrado
        lado=math.sqrt(area)
        contador=0
        while not rospy.is_shutdown():
            for x in range(4):
                rotate(20,90)
                time.sleep(1)
                straight_line(1,lado)
                time.sleep(1)
            contador=contador+1
            pub.publish("franco","cuadrado",contador)
    
    if id_fig == 2: #rectangulo
        base=area*0.20
        altura=area/base
        contador=0
        while not rospy.is_shutdown():
            for x in range(2):
                rotate(15,90)
                time.sleep(1.5)
                straight_line(1,base)
                time.sleep(1.5)
                rotate(15,90)
                time.sleep(1.5)
                straight_line(1,altura)
                time.sleep(1)
            contador=contador+1
            pub.publish("franco","rectangulo",contador)
            
    if id_fig == 3: #triangulo
        contador=0
        while not rospy.is_shutdown():
            cateto1=float(math.sqrt(area))
            cateto2=float((area*2)/cateto1 )
            hipotenusa=math.sqrt((cateto1*cateto1)+(cateto2*cateto2))
            straight_line(1,cateto1)
            time.sleep(1.5)
            rotate(15,90)
            time.sleep(1.5)
            straight_line(1,cateto2)
            time.sleep(1.5)
            angulo_alpha=math.atan(cateto1/cateto2)
            angulo_alpha=math.degrees(angulo_alpha)
            rotate(5,180-angulo_alpha)
            time.sleep(1.5)
            straight_line(1,hipotenusa)
            time.sleep(1.5)
            angulo_alpha=90+angulo_alpha
            time.sleep(1.5)
            rotate(5,angulo_alpha)
            straight_line(1,cateto1)
            time.sleep(1.5)
            contador=contador+1
            pub.publish("franco","triangulo",contador)

    if id_fig == 4: #circulo
        contador=0
        #https://www.areaciencias.com/fisica/velocidad-lineal.html
        #https://www.areaciencias.com/fisica/desplazamiento-angular.html
        #http://recursostic.educacion.es/newton/web/materiales_didacticos/EDAD_4eso_movimiento_circular/impresos/quincena2.pdf
        while not rospy.is_shutdown():
            radio=math.sqrt(area/math.pi)
            circle(radio,1)
            time.sleep(1.5)
            contador=contador+1
            pub.publish("franco","circulo",contador)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            run_shape(int(sys.argv[1]), int(sys.argv[2]))
        except rospy.ServiceException, e:
            print("ERROR")
    else:
        print("ERROR EN ARGUMENTOS")
        sys.exit(1)
    

        