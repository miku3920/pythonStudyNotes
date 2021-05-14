import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

# 畫線
# Draw a diagonal blue line with thickness of 5 px
# (0,0) (511,511)劃出藍色的線, 寬度為5
cv2.line(img, pt1=(0, 0), pt2=(511, 511), color=(255, 0, 0), thickness=5)
cv2.line(img, pt1=(511, 0), pt2=(0, 511), color=(255, 255, 0), thickness=10)

# 畫多邊形  [x,y]
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
print(pts.shape)
# (4, 2)
pts = pts.reshape((-1, 1, 2))
print(pts.shape)
# (4, 1, 2)
cv2.polylines(img, [pts], True, (0, 255, 255))   # True 最後一筆,是否要連到第一筆

# 箭頭
cv2.arrowedLine(
    img, pt1=(21, 13),
    pt2=(151, 401), color=(0, 0, 255),
    thickness=5
)


# 正方形
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 畫實心的園
cv2.circle(
    img, center=(447, 63), radius=63,
    color=(0, 0, 255), thickness=-1
)
cv2.circle(
    img, center=(200, 63), radius=20,
    color=(0, 255, 255), thickness=5
)

# 圓餅
cv2.ellipse(
    img, center=(256, 256), axes=(100, 50),
    angle=0, startAngle=0, endAngle=180,
    color=(0, 0, 255), thickness=-1
)
cv2.ellipse(
    img, center=(156, 256), axes=(30, 50),
    angle=0, startAngle=0, endAngle=360,
    color=(0, 255, 0), thickness=1
)


# 文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(
    img, text='bottomLeftOrigin',
    org=(10, 400), fontFace=font,
    fontScale=1, color=(255, 255, 255),
    thickness=1, bottomLeftOrigin=True
)
cv2.putText(
    img, text='miku3920',
    org=(10, 500), fontFace=font, fontScale=2,
    color=(255, 255, 255), thickness=2
)

winname = 'example'
cv2.namedWindow(winname, 0)
cv2.imshow(winname, img)

cv2.imwrite("example.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
