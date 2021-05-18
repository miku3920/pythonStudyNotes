import cv2
import numpy as np


def draw_line(event, x, y, flags, param):
    global img, drawing, lastX, lastY
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        if lastX != -1:
            cv2.line(img, pt1=(lastX, lastY), pt2=(x, y), color=(255, 196, 0), thickness=5)
        lastX = x
        lastY = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if lastX != -1:
                cv2.line(img, pt1=(lastX, lastY), pt2=(x, y), color=(255, 196, 0),
                         thickness=5)
            lastX = x
            lastY = y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, pt1=(lastX, lastY), pt2=(x, y), color=(255, 196, 0), thickness=5)

def CNN():
    print("CNN")


img = np.full(shape=(640, 640, 3), fill_value=0, dtype=np.uint8)
drawing = False
lastX = -1
lastY = -1
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_line)   # 抓取滑鼠的Event

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF   # 停1 ms
    if k == ord('s'):
        CNN()
    elif k == ord('c'):
        img = np.full(shape=(280, 280, 3), fill_value=0, dtype=np.uint8)
    elif k == 27:  # ESC
        break

cv2.destroyAllWindows()
