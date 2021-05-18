import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    global img, drawing
    if event == cv2. EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 2, (255, 0, 0), -1)  # 畫園

    elif event == cv2.EVENT_MOUSEMOVE:        # 滑鼠 左鍵 移動
        if drawing == True:
            cv2.circle(img, (x, y), 2, (0, 255, 255), -1)  # 畫園

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 2, (0, 0, 255), -1)  # 畫園

def CNN():
    print("CNN")


img = np.full(shape=(640, 640, 3), fill_value=0, dtype=np.uint8)
drawing = False
lastX = -1
lastY = -1
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)   # 抓取滑鼠的Event

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
