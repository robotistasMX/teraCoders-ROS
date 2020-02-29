#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
import math

class Robot:
    def __init__(self, name):
        self.name=name

    def mostrar_nombre(self):
        print(self.name)    

    def mover_derecho(self, speed, distance):
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
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
    
    def girar(self, speed,angle):
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
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

    def cuadrado(self,base,altura):
        for _ in range(4):
            self.girar(2,90)
            time.sleep(1)
            self.mover_derecho(1,base)
            time.sleep(1)
