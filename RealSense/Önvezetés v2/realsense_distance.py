import cv2
import pyrealsense2
import numpy as np
from realsense_depth import *

## Kamera elokeszites
dc = DepthCamera()

## Eger kovetes
cv2.namedWindow("Color frame")

## Szines korok
def color_circle(a1, a2):
    if depth_frame[a2, a1] > 500:
        R = 250 - ((depth_frame[a2, a1] - 500) / 2)
        G = 255
    elif depth_frame[a2, a1] > 350:
        R = 255
        G = depth_frame[a2, a1] / 2
    else:
        R = 255
        G = 0
    cv2.circle(color_frame, (a1, a2), 5, (0, G, R), 2)

while True:
    
    avg = 0
    size = 0
    cleft = 130
    cright = 510
    sleft = 0
    sright = 0
    left = False
    right = False
    
    ret, depth_frame, color_frame = dc.get_frame()
    
    cv2.rectangle(color_frame, (130, 120), (510, 280), (0, 0, 0), 2)
    cv2.rectangle(color_frame, (0, 0), (640, 50), (0, 0, 0), -1)    ## -1 == kitoltes
    
    for j in range (cleft, cright, 10):
        for k in range (280, 120, -10):
            if depth_frame[k, j] < 1000 and depth_frame[k, j] > 300:
                avg += depth_frame[k, j]
                size += 1
                color_circle(j, k)
                
                if j > 130 and j < 320 and left == False:
                    left = True
                    cleft = 320
                    sleft += 1
                if j > 280 and j < 510 and right == False:
                    right = True
                    cright = 320
                    sright += 1
                
    if size != 0:
        avg = avg / size - 345
    else:
        avg = 655.0

    
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
