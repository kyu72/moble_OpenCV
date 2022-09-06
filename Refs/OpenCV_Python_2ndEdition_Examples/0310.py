#0310.py
import numpy as np
import cv2

speed = 10
width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0 # right
imageFile = './data/lena.jpg'

while True:   
    key = cv2.waitKeyEx(10)    
    if key == 0x1B: 
        break;
    
# 방향키 방향전환 
    elif key == 0x270000: # right
        direction = 0
    elif key == 0x280000: # down
        direction = 1
    elif key == 0x250000: # left
        direction = 2
    elif key == 0x260000: # up
        direction = 3
        
# 방향으로 이동 
    if direction == 0:     # right
        x += speed
    elif direction == 1:   # down
        y += speed
    elif direction == 2:   # left
        x -= speed
    else: # 3, up
        y -= speed
        
#   경계확인 
    if x < R:
        x = R
        direction = 0
    if x > width - R:
        x = width - R
        direction = 2
    if y < R:
        y = R
        direction = 1
    if y > height - R:
        y = height - R
        direction = 3
        
# 지우고, 그리기        
    img = cv2.imread(imageFile) #배경에 이미지 넣기
    cv2.circle(img, (x, y), R, (255, 100, 255), -1) 
    cv2.imshow('img', img)
    
cv2.destroyAllWindows()
