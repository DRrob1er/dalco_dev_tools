#!/usr/bin/env python3
import rospy

from geometry_msgs.msg 			import Twist

rospy.init_node('Remap_joy', anonymous=True)

def callback_cmd_vel_joy(data):
    pub_cmd_vel.publish(data)

pub_cmd_vel			= rospy.Publisher('cmd_vel', Twist, queue_size=10)
rospy.Subscriber('cmd_vel_joy', 			Twist, callback_cmd_vel_joy)


if __name__ == '__main__':
	while not rospy.is_shutdown():
		rate = rospy.Rate(20) 
		try:
			rate.sleep()
		except rospy.ROSInterruptException:
			print("noworky HLC")
			rate.sleep()
			pass