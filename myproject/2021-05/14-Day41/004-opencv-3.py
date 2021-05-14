import cv2

cap = cv2.VideoCapture("https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=19970")

fps = cap.get(cv2.CAP_PROP_FPS)  # 25.0  每秒幾張
print("fps",fps)
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 總長度
print('Total:', num_frames)
print('during time sec:', num_frames/fps)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬
print('H：', frame_height )
print('w：', frame_width)
FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 現在位置 在第幾張
print('frame:', FRAME_NOW)  # 当前帧数 0.0

#  跳到第(fps*10 ) frame, 也就是10sec 後
cap.set(1, fps*40)

while cap.isOpened():
    ret, frame = cap.read()
    if ret==True:
        FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)   # 現在的張數
        print('Current frame:', FRAME_NOW)
        # cap.set(1, FRAME_NOW+1)   # 1倍數
        # cap.set(1, FRAME_NOW+2)   # 2倍數
        cap.set(1, FRAME_NOW-2)   # 4倍數
        cv2.imshow('frame', frame)
        key = cv2.waitKey(int(1000/fps))
        if key == 27:  # ESC
          break
    else:
        #break
        print("")


cap.release()
cv2.destroyAllWindows()