import numpy as np
import cv2

img = cv2.imread('1.jpg')
img2 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)  # BGRA
print(img.shape)
print(img2.shape)

img[10:10+img2.shape[0], 20:20+img2.shape[1], :]\
    = img2[:, :, :3]*(img2[:, :, -1:]/255)\
    + img[10:10+img2.shape[0], 20:20+img2.shape[1], :]*(1-img2[:, :, -1:]/255)
cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
