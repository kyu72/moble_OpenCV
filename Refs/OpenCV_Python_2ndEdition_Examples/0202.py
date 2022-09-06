# 0202.py
import cv2
import numpy as np

imageFile = './data/lena.jpg'

img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR
img2 = cv2.imread(imageFile) # cv2.IMREAD_GRAYSCALE

#cv2.imwrite('./data/Lena.bmp', img)
#cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena.jpg', img2, [cv2.IMWRITE_JPEG_QUALITY, 90])

##encode_img = np.fromfile(imageFile, np.uint8)
##img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)
imagefile2 = './data/Lena.png'
imagefile3 = './data/Lena.bmp'
img3 = cv2.imread(imagefile2)
img4 = cv2.imread(imagefile3)
cv2.imshow('Lena png',img3)
cv2.imshow('Lena bmp',img4)

cv2.waitKey()
cv2.destroyAllWindows()