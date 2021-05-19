import cv2
import numpy as np

img = im = cv2.imread('lightning.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("there are " + str(len(contours)) + " contours")

cnt = contours[0]
print("there are " + str(len(cnt)) + " points in contours[0]")

hull = cv2.convexHull(cnt)
print("after convexHull, there are " + str(len(hull)) + " points")
cv2.drawContours(im, [hull], 0, (255, 0, 0), -1)
cv2.imshow('im', im)
cv2.waitKey(0)

k = cv2.isContourConvex(cnt)

x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)  # 紅色的外框
cv2.imshow('minAreaRect ', im)
cv2.waitKey(0)

(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (0, 255, 255), 2)
cv2.imshow('circle ', img)
cv2.waitKey(0)


ellipse = cv2.fitEllipse(cnt)
angle = ellipse[2]
im = cv2.ellipse(img, ellipse, (255, 255, 255), 1)
cv2.imshow('ellipse ', im)
cv2.waitKey(0)

rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(img, (cols - 1, righty), (0, lefty), (255, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
