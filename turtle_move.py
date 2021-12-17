import rospy
from geometry_msgs.msg import Twist
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


distance = 5.54
value = 0.6
class move:
    
    def foward(message):

        pub_twist = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        message.linear.x = value
        message.linear.y=message.linear.z=message.angular.z=0
        current_distance = 0.00

        while distance > current_distance:
            pub_twist.publish(msg)
            # rate=rospy.Rate(10)
            current_distance+=0.1
            # rate.sleep()

    def backward(message):
        pub_twist = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        message.linear.x=-value
        message.linear.y=message.linear.z=0
        current_distance = 0.00

        while distance > current_distance:
            pub_twist.publish(msg)
            # rate=rospy.Rate(10)
            current_distance+=0.1
            # rate.sleep()

    def left(message):
        pub_twist = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        message.angular.z=value
        # message.linear.x=value
        message.linear.x=message.linear.y=message.linear.z=0
        current_distance = 0.00

        while distance > current_distance:
            pub_twist.publish(msg)
            # rate=rospy.Rate(10)
            current_distance+=0.1
            # rate.sleep()

    def right(message):
        pub_twist = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        message.angular.z=-value
        # message.linear.y=-value
        message.linear.x=message.linear.z=message.linear.y=0
        current_distance = 0.00

        while distance > current_distance:
            pub_twist.publish(msg)
            # rate=rospy.Rate(10)
            current_distance+=0.1
            # rate.sleep()

    def stop(message):
        pub_twist = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        message.linear.x=message.linear.z=message.linear.y=0

def main():
    rospy.init_node('turtle_move')
    rospy.Subscriber('/cv_camera/image_raw', Image, callback)
    rospy.spin()


def callback(data):
    key=cv2.waitKey(1)
    cap = brige.imgmsg_to_cv2(data,'bgr8')
    cv2.resize(cap,(320,240))
    cv2.imshow('turtle_cam',cap)
    # cv2.imshow(" ","../images/center.png")
    
    key=cv2.waitKey()
    # if key==ord('q'):
    #     cv2.destroyAllWindows()
    if key==ord('w'):
        move.foward(msg)
    if key==ord('s'):
        move.stop(msg)
    if key==ord('a'):
        move.left(msg)
    if key==ord('d'):
        move.right(msg)
    if key==ord('x'):
        move.backward(msg)

msg = Twist()
brige = CvBridge()

if __name__=='__main__':

    main()
    pass

