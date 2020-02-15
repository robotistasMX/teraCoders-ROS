#! /usr/bin/env python
import rospy
import math
import sys
from clase4.msg import Ejercicio
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time 

sensor = []

def callback(msg):
    del sensor[:]
    sensor.append(msg.ranges[300])
    sensor.append(msg.ranges[350])
    sensor.append(msg.ranges[400])

def rotate(speed,angle):
    velocity_publisher = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
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
    velocity_publisher = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
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

if __name__ == '__main__':
    rospy.init_node('ejercicio_node')
    velocity_publisher = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/front/scan', LaserScan, callback)
    vel_msg = Twist()
    vel_msg.linear.x = 0 
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    time.sleep(2)
    rate = rospy.Rate(10) 
    
    while not rospy.is_shutdown():
        if sensor[0] > 1 and sensor[1] > 1 and sensor[2] > 1:
            vel_msg.linear.x = 0.5
            vel_msg.angular.z = 0.0
        else:
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.5

        velocity_publisher.publish(vel_msg)
        rate.sleep()