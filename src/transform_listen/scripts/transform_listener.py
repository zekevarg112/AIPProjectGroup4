#!/usr/bin/env python
import yaml
import tf
import rospy


rospy.init_node("tf_listener")

listener = tf.TransformListener()

print("Node initialized, looking for tag positions")
while not rospy.is_shutdown():
	try:
		(trans,rot) = listener.lookupTransform('/map', '/tag_5', rospy.Time(0))
		output = yaml.dump(trans, sort_keys=False)
		rospy.Rate(2).sleep()
                        
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		#continuerospa
		continue
