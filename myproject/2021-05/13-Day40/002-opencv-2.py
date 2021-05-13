import cv2

img = cv2.imread('1.jpg')
cv2.imshow('image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 轉顏色
k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('output.png', gray)  # png, bmp, jpg
    cv2.destroyAllWindows()
