import cv2
import pyrealsense2
import numpy as np
from realsense_depth import *

## Kamera elokeszites
dc = DepthCamera()

## Eger kovetes
cv2.namedWindow("Color frame")


while True:
    
    avg = 0
    size = 0
    cleft = 130
    cright = 510
    left = False
    right = False
    
    ret, depth_frame, color_frame = dc.get_frame()
    
    cv2.rectangle(color_frame, (130, 120), (510, 280), (0, 0, 0), 2)
    cv2.rectangle(color_frame, (0, 0), (640, 50), (0, 0, 0), -1)    ## -1 == kitoltes
    
    for j in range (cleft, cright):
        for k in range (280, 120, -1):
            if depth_frame[k, j] < 600 and depth_frame[k, j] > 300:
                avg += depth_frame[k, j]
                size += 1
                cv2.circle(color_frame, (j, k), 6, (0, 0, 255), 1)
                
                if j > 130 and j < 320 and left == False:
                    left = True
                    cleft = 320
                if j > 280 and j < 510 and right == False:
                    right = True
                    cright = 320
                if left == True and right == True:
                    break;

                
    if size != 0:
        avg = avg / size - 345
    else:
        avg = 255.0

    
    if left == True and right ==False:
        cv2.putText(color_frame,
                "Turn right   Jobbra",
                (300, 30),
                cv2.FONT_HERSHEY_PLAIN,
                1.5, (255, 255, 255), 2)
    elif left == False and right == True:
        cv2.putText(color_frame,
                "Turn left    Balra",
                (300, 30),
                cv2.FONT_HERSHEY_PLAIN,
                1.5, (255, 255, 255), 2)
    elif left == False and right == False:
        cv2.putText(color_frame,
                "Go           Mehet",
                (300, 30),
                cv2.FONT_HERSHEY_PLAIN,
                1.5, (255, 255, 255), 2)
    else:
        cv2.putText(color_frame,
                "Stop         Allj",
                (300, 30),
                cv2.FONT_HERSHEY_PLAIN,
                1.5, (255, 255, 255), 2)
    
    
    cv2.putText(color_frame,            ## tavolsag kiiratasa
                "{} mm".format(round(avg, 1)),
                (10, 30),              ## kiiras helye
                cv2.FONT_HERSHEY_PLAIN,
                1.5, (255, 255, 255), 2)    ## meret, (szin), vastagsag
    
    cv2.imshow("Color frame", color_frame)
    # cv2.imshow("Depth frame", depth_frame)

    
    key = cv2.waitKey(1)
    if key == 27:
        break
