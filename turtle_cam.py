import cv2 as cv
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge

def main():
    rospy.init_node('capture_node')
    rospy.Subscriber('/cv_camera/image_raw', Image, callback)
    rospy.spin()

brige = CvBridge()
def callback(data):
    key=cv.waitKey(1)
    cap = brige.imgmsg_to_cv2(data,'bgr8')
    cv.resize(cap,(320,240))
    cv.imshow('turtle_cam',cv.rotate(cap,cv.ROTATE_180))
  
    # cv.imshow('turtle_cam',cv_image)


if __name__=='__main__':
    main()
    pass