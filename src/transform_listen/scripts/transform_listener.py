#!/usr/bin/env python
import yaml
import tf
import rospy


def write_yaml_to_file(py_obj):
    with open('output.yaml', 'w',) as f :
        yaml.dump(py_obj,f,sort_keys=False) 
    print('Written to file successfully')




rospy.init_node("tf_listener")

listener = tf.TransformListener()

    

print("Node initialized, looking for tag positions")
while not rospy.is_shutdown():
	try:
		(trans,rot) = listener.lookupTransform('/map', '/tag_5', rospy.Time(0))
		trans_dict={
			"X":trans[0],
			"Y":trans[1],
			"Z":trans[2]
		}
			
		write_yaml_to_file(trans_dict)
		rospy.Rate(2).sleep()
                        
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		#continuerospa
		continue
		

    

