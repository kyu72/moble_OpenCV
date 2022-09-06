#0301.py
import cv2
import numpy as np

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
#img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
#"np.zeros + 255" -> 영상의 모든채널 값이 255로 변경되어 흰색 배경

#img = np.ones((512,512,3), np.uint8) * 255
#img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
#img = np.zeros((512,512, 3), np.uint8) # Black 배경

pt1 = 100, 100
pt2 = 400, 400
cv2.line(img,pt1,pt2,(0,0,0),3)
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2) #녹색

cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5) #파란색
cv2.line(img, (0, 0), (0, 500), (0,0,255), 5) #빨간색, 5 = 두께

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
