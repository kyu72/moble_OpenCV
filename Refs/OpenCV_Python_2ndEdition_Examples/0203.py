# 0203.py
from queue import Full
import cv2
from   matplotlib import pyplot as plt 
#matplotlib패키지에서 pyplot를 plt 이름으로 import한다

imageFile = './data/Lena.jpg' #이미지 파일 불러오기

imgBGR = cv2.imread(imageFile) #이미지 파일 읽어 변수에 저장
#cv는 RGB방식이 아닌 BGR방식으로 관리한다

plt.axis('off') #x, y축을 표시하지 않는다

imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB) #BGR을 RGB로 변환
plt.imshow(imgRGB)
plt.show()
