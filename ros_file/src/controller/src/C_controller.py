#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

GO = False

def Callback(msg):
    
    global GO
    GO = msg.data
    print('Got message from Car red, is: ', GO)


def Blue_Controller():

    rospy.init_node('Vehicle_blue_controller', anonymous=True)

    blue_vel_topic = '/blue/mobile_base/commands/velocity'

    cmd_blue_publisher = rospy.Publisher(blue_vel_topic, Twist, queue_size=10)

    rate = rospy.Rate(10)

    rospy.Subscriber('/red2green', Bool, Callback)

    timer = 0

    rospy.sleep(3)
    
    while (not rospy.is_shutdown()) and (timer < 2.0):

        vel_msg = Twist()
            
        vel_msg.linear.x = 0.15
        vel_msg.angular.z = 0.0
        timer += 0.1
        print('timer:', timer)

    
        cmd_blue_publisher.publish(vel_msg)
        
        rate.sleep()

    while (not rospy.is_shutdown()) and (2.0<= timer <= 15.0):

        vel_msg = Twist()
        
        if GO:
            vel_msg.linear.x = 0.15
            vel_msg.angular.z = 0.0
            timer += 0.1
            print('timer:', timer)

        else:
            
            vel_msg.linear.x = 0.0
            print('vehicle slowing down')

        cmd_blue_publisher.publish(vel_msg)
        # rospy.loginfo("Publish Vehicle blue velocity command[%0.2f m/s, %0.2f rad/s]",
        #     vel_msg.linear.x, vel_msg.angular.z)
        
        rate.sleep()
        

if __name__ == '__main__':
    try:
        Blue_Controller()
    except rospy.ROSInterruptException:
        pass