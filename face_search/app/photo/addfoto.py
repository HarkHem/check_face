
# example1.py - recording video from camera
# Code template from:
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

# import numpy as np
import cv2

cap = cv2.VideoCapture("http://192.168.1.149/video/mjpg.cgi?profileid=3")



while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,1)

        # write the flipped frame

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
