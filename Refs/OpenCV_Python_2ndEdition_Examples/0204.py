# 0204.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
#cv2.IMREAD_GRAYSCALE -> 그레이스케일로 영상을 읽어 imageGray에 할당
plt.axis('off')

plt.imshow(imgGray, cmap = "gray", interpolation='bicubic')
#interpolation='bicubic' -> 보간식
plt.show()
