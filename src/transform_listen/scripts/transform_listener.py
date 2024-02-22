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
		write_yaml_to_file(trans)
		rospy.Rate(2).sleep()
                        
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		#continuerospa
		continue
		
def write_yaml_to_file(py_obj):
    with open('output.yaml', 'w',) as f :
        yaml.dump(py_obj,f,sort_keys=False) 
    print('Written to file successfully')
    
    

