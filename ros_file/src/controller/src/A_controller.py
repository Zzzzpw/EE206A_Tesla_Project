#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from visualization_msgs.msg import Marker

crossing = False

def Callback(msg):
   
    global crossing

    if msg is not None:
        crossing = True
    
    print(crossing)
    #without AR tag
    # crossing = msg.data
    
    # print("callback: ",crossing)

def A_Controller():
   
    rospy.init_node('Vehicle_red_controller', anonymous=True)

    red_vel_topic = '/red/mobile_base/commands/velocity'

    cmd_red_publisher = rospy.Publisher(red_vel_topic, Twist, queue_size=10)

    red2green_publisher = rospy.Publisher('/red2green', Bool, queue_size=10)

    rate = rospy.Rate(10)
    #without ARtag
    # rospy.Subscriber('/video_timer', Bool, Callback)

    #with ARtag
    rospy.Subscriber('/visualization_marker', Marker, Callback)

    while not rospy.is_shutdown():

        vel_msg = Twist()

        if crossing:

            vel_msg.linear.x = 0.0
            print('vehicle stop')

            rospy.sleep(2)
            red2green_msg = True   

        else:
            
            vel_msg.linear.x = 0.2
            vel_msg.angular.z = 0.0
            red2green_msg = False

        cmd_red_publisher.publish(vel_msg)
        red2green_publisher.publish(red2green_msg)

        # rospy.loginfo("Publish Vehicle red velocity command[%0.2f m/s, %0.2f rad/s]",
            # vel_msg.linear.x, vel_msg.angular.z)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        A_Controller()
    except rospy.ROSInterruptException:
        pass