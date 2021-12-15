#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def Callback(msg):
    rospy.loginfo("Vehicle A velocity is x: %0.2f, y: %0.2f", msg.linear.x, msg.angular.z)

def A_subscriber():

    rospy.init_node('A_subscriber', anonymous=True)

    rospy.Subscriber("/A_vel", Twist, Callback)

    rospy.spin()

if __name__ == '__main__':
    A_subscriber()