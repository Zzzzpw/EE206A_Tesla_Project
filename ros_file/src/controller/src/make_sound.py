#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from kobuki_msgs.msg import Led
from kobuki_msgs.msg import Sound
from std_msgs.msg import Bool


blink = False

def Callback(msg):
    
    global blink
    blink = msg.data

# blink = True

def main():
   
    rospy.init_node('green_sound', anonymous=True)

    led1_topic = '/green/mobile_base/commands/led1'
    led2_topic = '/green/mobile_base/commands/led2'
    sound_topic = '/green/mobile_base/commands/sound'

    led1_publisher = rospy.Publisher(led1_topic, Led, queue_size=10)
    led2_publisher = rospy.Publisher(led2_topic, Led, queue_size=10)
    sound_publisher = rospy.Publisher(sound_topic, Sound, queue_size=10)

    rospy.Subscriber('/red2green', Bool, Callback)

    rate = rospy.Rate(5)
    
    timer = 0
   
    while not rospy.is_shutdown():
        if blink:

            led1_msg = Led()
            led2_msg = Led()
            sound_msg = Sound()
            print('/---------------------------------------------------------------------------------------------------------------------------')

            if timer % 2 == 0:

                led1_msg = 3
                led2_msg = 0
                sound_msg = 0
                #print('green')   

            else:
                led1_msg = 0
                led2_msg = 3
                sound_msg = 0

            if timer >= 15:
                led1_msg = 0
                led2_msg = 0
                sound_msg = 7
            
            #print(timer)

            led1_publisher.publish(led1_msg)
            led2_publisher.publish(led2_msg)
            sound_publisher.publish(sound_msg)


            timer += 1

            #rospy.loginfo("Publish Vehicle A velocity command[%0.2f m/s, %0.2f rad/s]",
            #   vel_msg.linear.x, vel_msg.angular.z)
            
            rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
