#!/usr/bin/env python

from pcl_helper import *

def get_cloud(ros_msg):
    # convert cloud
    raw_cloud = ros_to_pcl(ros_msg)

    filename = 'raw_cloud.pcd'
    pcl.save(raw_cloud, filename)
    global cloud_captured
    cloud_captured = True
    quit()

if __name__ == '__main__':
    
    # TODO: ROS node initialization
    rospy.init_node('clustering', anonymous=True)
    # Subscriber to topic
    pcl_sub = rospy.Subscriber('/pr2/world/points', pc2.PointCloud2, get_cloud, queue_size=1)
    cloud_captured = False
    while not cloud_captured:
        rospy.spin()

