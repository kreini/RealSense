import cv2
import pyrealsense2
from realsense_depth import *

point = (300, 400)

def show_distance(event, x, y, args, params):
    global point
    point = (x, y)


## Kamera elokeszites
dc = DepthCamera()

## Eger kovetes
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)

while True:
    ret, depth_frame, color_frame = dc.get_frame()

    # point = (400, 300)
    cv2.circle(color_frame, point, 5, (0, 0, 255), 2)   ## kor rajz a kepre
    distance = depth_frame[point[1], point[0]]          ## tavolsag meghatarozasa
    
    cv2.putText(color_frame,                            ## tavolsag kiiratasa
                "{} mm".format(distance),
                (point[0], point[1] - 20),              ## kiiras feljebb tolasa 20 pixellel
                cv2.FONT_HERSHEY_PLAIN,
                1, (0, 0, 255), 2)                      ## meret, (szin), vastagsag

    cv2.putText(color_frame,
                "x: ".format(point[0]),
                (point[0]-100, point[1] - 20),
                cv2.FONT_HERSHEY_PLAIN,
                1, (0, 0, 255), 2)
    cv2.putText(color_frame,
                "y: ".format(point[1]),
                (point[0]-100, point[1]),
                cv2.FONT_HERSHEY_PLAIN,
                1, (0, 0, 255), 2)

    cv2.imshow("Color frame", color_frame)
    print(point)
    # cv2.imshow("Depth frame", depth_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
