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
    t1=rospy.Time.now().to_sec()
    speed=1
    distance=1
    flag=True
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
        if(flag):
            _,cntsp,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
            flag=False
        elif((t0-t1)<1):
            _,cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        else:
            t1=t0    
            mc1 = max(cnts, key=cv2.contourArea)
            mc2 = max(cntsp, key=cv2.contourArea)
            M1=cv2.moments(cnts)
            M2=cv2.moments(cntsp)
            if(M1["m00"]!=0 and M2["m00"]!=0):
                x1=int(M1["m10"]/M1["m00"]) 
                x2=int(M2["m10"]/M2["m00"])
                y1=int(M1["m01"]/M1["m00"])
                y2=int(M2["m01"]/M2["m00"])
                #print(x1,y1,x2,y2,sep=',')
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0          
            if(np.abs(x2-x1)>np.abs(y2-y1)):
                if(x2>x1):
                    print("left")
                    vel_msg.linear.x = -abs(speed)       
                else:
                    print("right")
                    vel_msg.linear.x = abs(speed)
            else:
                if(y2<y1):
                    print("down")
                    vel_msg.linear.y = -abs(speed)
                else:
                    print("up")
                    vel_msg.linear.y = abs(speed)
            time=0        
                #Loop to move the turtle in an specified distance
            while(time < 1):
                #Publish the velocity
                velocity_publisher.publish(vel_msg)
                #Takes actual time to velocity calculus
                time=rospy.Time.now().to_sec()
                #Calculates distancePoseStamped
            #After the loop, stops the robot
            vel_msg.linear.x = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)
            cntsp=cnts
        cv2.imshow("pen.png", blueHSV)    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
   
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
