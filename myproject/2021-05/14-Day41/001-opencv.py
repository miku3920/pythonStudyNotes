import cv2

big_img = cv2.imread('b.jpg')
small_img = cv2.imread('s.jpg')

big_h, big_w, big_rgb = big_img.shape
small_h, small_w, small_rgb = small_img.shape

y, x = 200, 200
y_judgment, x_judgment = 1, 1
shift = 10
while True:
    img = big_img.copy()
    img[y:y+small_h, x:x+small_w] = small_img

    cv2.imshow('image', img)
    k = cv2.waitKey(10)
    if k > 0:
        cv2.destroyAllWindows()
        break

    if y <= shift:
        y_judgment = 1
    if y+small_h+shift >= big_h:
        y_judgment = -1
    if x <= shift:
        x_judgment = 1
    if x+small_w+shift >= big_w:
        x_judgment = -1

    x += shift*x_judgment
    y += shift*y_judgment
