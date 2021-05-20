import numpy as np
import cv2

# mog = cv2.bgsegm.createBackgroundSubtractorMOG()
mog2 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
gmg = cv2.bgsegm.createBackgroundSubtractorGMG()
#knn = cv2.createBackgroundSubtractorKNN(detectShadows=True)


person_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap = cv2.VideoCapture('TownCentreXVID.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
count = 0
while cap.isOpened():
    ret, img = cap.read()
    # if ret==True:
    if img is not None:
        img = cv2.resize(img, (640, 480))  # 調整大小
        cv2.imshow('img', img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # ---- tracking start -----
        gmg_img = gmg.apply(gray)
        mog2_img = mog2.apply(gray)
        #cv2.imshow('mog2', mog2_img)
        #cv2.imshow('gmg', gmg_img)

        res = cv2.bitwise_and(img, img, mask=gmg_img)
        cv2.imshow('bitwise_and gmg', res)

        kernel = np.ones((3, 3), np.uint8)
        erosion = cv2.erode(mog2_img, kernel, iterations=1)  # 溶解
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(erosion, kernel, iterations=3)  # 擴充

        mog2_img = cv2.medianBlur(dilation, 5)
        res = cv2.bitwise_and(img, img, mask=mog2_img)
        cv2.imshow('bitwise_and mog2', res)

        # ---- tracking end -----

        # ----haar start
        img2 = img.copy()
        faces = person_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=3,
            minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
            )
        print("Detected ", len(faces), " full body")

        for (x, y, w, h) in faces:
            # save jpeg
            img3 = img[y:y + h, x:x + w]
            cv2.imwrite("person_" + str(count) + ".jpg", img3)
            count = count + 1
            # 框框
            img2 = cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('haar img2', img2)
        # ----haar end

        key = cv2.waitKey(int(1000 / fps))
        if key == 27:  # ESC
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
