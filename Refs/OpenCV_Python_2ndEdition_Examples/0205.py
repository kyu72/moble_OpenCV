# 0205.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(6,6)) #크기를 (6인치,6인치)로 설정
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
#영상의 출력범위를 조정
plt.imshow(imgGray, cmap = 'gray')

plt.axis('off')
plt.savefig('./data/0205.png')
plt.show()
