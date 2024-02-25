#!/usr/bin/env python
import yaml
import tf
import tf2_ros
import rospy


def write_yaml_to_file(tag_list):
    with open('./src/navi_goals/config/waypoints.yaml', 'w',) as f:
	f.write("waypoints:\n")
	for tag in tag_list:
		if tag != None:
			f.write("  - point:\n")
			f.write("      x: "+ str(tag[0])+ "\n")
			f.write("      y: "+ str(tag[1])+ "\n")
			f.write("      th: 0\n")
        #yaml.dump(py_obj,f) 
    print('Written to file successfully')

rospy.init_node("tf_listener")

#tf_buffer = tf2_ros.Buffer()
listener = tf.TransformListener()

#number_of_decimals = 2

tag_list = [None]*20
  
print("Node initialized, looking for tag positions")
while not rospy.is_shutdown():
	for i in range(0,19):	
		try:	
		
			if listener.waitForTransform('/map','/tag_'+str(i), rospy.Time(0), rospy.Duration(0.2)) == None:
				(trans,rot) = listener.lookupTransform('/map','/tag_'+str(i), rospy.Time(0))
				tag_list[i]=trans

				print(tag_list)
			
			#rospy.Rate(2).sleep()
	                
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException, tf2_ros.TransformException):
			#continuerospa
			print("We be catching them exceptions")
			#rospy.Rate(2).sleep()
			continue
		
	write_yaml_to_file(tag_list)
    

