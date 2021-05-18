import cv2

img2 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)  # BGRA
print(img2.shape)
img2_h, img2_w = img2.shape[0], img2.shape[1]

recVideo = False
width = 1440
height = 720
cap = cv2.VideoCapture('C:/Users/miku/Videos/2021-05-17 17-00-10.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
while cap.isOpened():
    ret, img = cap.read()
    if img is not None:
        img = cv2.resize(img, (width, height))
        img5 = img.copy()
        img5[10:10 + img2_h, 20:20 + img2_w, :] \
            = img2[:, :, :3] * (img2[:, :, -1:] / 255) \
            + img[10:10 + img2_h, 20:20 + img2_w, :] * (1 - img2[:, :, -1:] / 255)
        cv2.imshow('img5', img5)

        if recVideo == True:
            out.write(img5)

        key = cv2.waitKey(int(1000 / fps))
        if key == 27:  # ESC
            break
        elif key == ord('s'):
            cv2.imwrite("save.png", img5)
            print("save")
        elif key == ord('z'):
            if recVideo == True:
                out.release()
            capSize = (width, height)

            from sys import platform

            if platform == "linux" or platform == "linux2":
                # linux
                print("linux")
            elif platform == "darwin":
                # OS X
                fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # note the lower case
                out = cv2.VideoWriter("output.mov", fourcc, fps, capSize, True)
            elif platform == "win32":
                # Windows...
                fourcc = cv2.VideoWriter_fourcc(*'XVID')  # opencv 3.0
                out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))  # FPS

            recVideo = True

            print("save video")
    else:
        break

cap.release()

out.release()
cv2.destroyAllWindows()
