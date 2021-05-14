import cv2
import numpy as np

small_img = cv2.imread('s.jpg')
small_h, small_w = small_img.shape[0], small_img.shape[1]

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("videoTest.avi")
while(True):
    ret, img = cap.read()
    if img is not None:
        cv2.imshow('img', img)

    k = cv2.waitKey(10)
    if k == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
