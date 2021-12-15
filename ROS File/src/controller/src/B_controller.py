#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

slowdown = False

def Callback(msg):
    
    global slowdown
    slowdown = msg.data
    print('Got message from Car red, is: ', slowdown)


def green_Controller():

    rospy.init_node('Vehicle_green_controller', anonymous=True)

    green_vel_topic = '/green/mobile_base/commands/velocity'

    cmd_green_publisher = rospy.Publisher(green_vel_topic, Twist, queue_size=10)

    rate = rospy.Rate(10)

    rospy.Subscriber('/red2green', Bool, Callback)

    timer = 0

    while not rospy.is_shutdown() and timer <=3.0:

        vel_msg = Twist()

        if slowdown:
            vel_msg.linear.x = 0.1
            timer += 0.1
            print('timer:', timer)
            print('vehicle slowing down')

        else:
            
            vel_msg.linear.x = 0.22
            vel_msg.angular.z = 0.0

        cmd_green_publisher.publish(vel_msg)

        # rospy.loginfo("Publish Vehicle green velocity command[%0.2f m/s, %0.2f rad/s]",
        #     vel_msg.linear.x, vel_msg.angular.z)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        green_Controller()
    except rospy.ROSInterruptException:
        pass