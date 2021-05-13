import cv2

img = cv2.imread('1.jpg')

print(img.shape)
# 高 寬  顏色 (302, 403, 3)
img[0, 0] = [0, 0, 255]
img[10:20, 20:50] = [0, 255, 0]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
