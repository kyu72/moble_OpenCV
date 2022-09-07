import easyocr
import cv2
import matplotlib.pyplot as plot
import numpy as np

IMG_P= './data/opencv.jpg'

reader = easyocr.Reader(['en'])
RST = reader.readtext(IMG_P)

font = cv2.FONT_HERSHEY_SIMPLEX
plot.axis('off') #x, y축을 표시하지 않는다

IMG = cv2.imread(IMG_P)
spacer = 100
for detection in RST:
    T_LEFT = tuple(detection[0][0])
    B_RIGHT = tuple(detection[0][2])
    TEXT = detection[1]
    IMG = cv2.rectangle(IMG,T_LEFT,B_RIGHT,(255,0,255),3)
    IMG = cv2.putText(IMG,TEXT,(100,spacer), font, 3,(0,255,255),2,cv2.LINE_AA)
    spacer+=15

plot.imshow(IMG)
plot.show()