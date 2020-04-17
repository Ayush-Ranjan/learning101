#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import cv2
import numpy as np 
import matplotlib.pyplot as plt

def move():
    # Starts a new node
    cap = cv2.VideoCapture(0)
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    min_HSV = np.array([0, 58, 30], dtype = "uint8")
    max_HSV = np.array([33, 255, 255], dtype = "uint8")    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Display the resulting frame
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        imageHSV = cv2.GaussianBlur(imageHSV, (3, 3), 0)
        mask = cv2.inRange(imageHSV, lower_blue, upper_blue)
        #skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)
        blueHSV = cv2.bitwise_and(frame, frame, mask = mask)
        cv2.imshow("pen.png", blueHSV)
        #Loop to move the turtle in an specified distance
        ##while(current_distance < distance):
            #Publish the velocity
          ##  velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            ##t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            ##current_distance= t1-t0
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    #Receiveing the user's input
    distance = 3
    ##directiom=
   
    #Checking if the movement is forward or backwards
    if(direction=="f"):
        vel_msg.linear.x = 1
    else:
        vel_msg.linear.x = -1
       #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
   
    while not rospy.is_shutdown():
   
        #Setting the current time for distance calculus
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
   
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass