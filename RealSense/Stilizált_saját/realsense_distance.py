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
    if depth_frame[a2, a1] > 1000:
        R = 0
        G = 255 - (depth_frame[a2, a1] / 40)
        B = (depth_frame[a2, a1] / 40)
    elif depth_frame[a2, a1] > 500:
        R = 255 - ((depth_frame[a2, a1] - 500) / 2)
        G = 255
        B = 0
    elif depth_frame[a2, a1] > 10:
        R = 255
        G = depth_frame[a2, a1] / 2
        B = 0
    else:
        R = 0
        G = 0
        B = 0
        
    cv2.circle(color_frame, (a1, a2), 1, (B, G, R), 1)

while True:

    cleft = 0
    cright = 640
    
    ret, depth_frame, color_frame = dc.get_frame()
    cv2.rectangle(color_frame, (0, 0), (640, 480), (0, 0, 0), -1)    ## -1 == kitoltes
    
    for j in range (cleft, cright, 1):
        for k in range (480-1, 0, -1):
            color_circle(j, k)
    
    cv2.imshow("Color frame", color_frame)

    
    key = cv2.waitKey(1)
    if key == 27:
        break
