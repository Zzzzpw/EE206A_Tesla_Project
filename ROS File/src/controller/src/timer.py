#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Bool

def timer():

    rospy.init_node('Timer', anonymous=True)

    timer_topic = '/video_timer'

    timer_publisher = rospy.Publisher(timer_topic, Bool, queue_size=10)

    rate = rospy.Rate(10)

    print('video start')
    t = 0

    while not rospy.is_shutdown():

        if t < 4:
            val = False
        else:
            val = True

        timer_publisher.publish(val)

        # rospy.loginfo("Is there a pedestrain crossing?")
        print(t)
        print('Is there a pdestrain crossing?', val)
        
        # rate.sleep()
        rospy.sleep(1)
        t += 1


if __name__ == '__main__':
    try:
        timer()
    except rospy.ROSInterruptException:
        pass