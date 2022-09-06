import cv2
import numpy

imgfile1 = "./data/lena.jpg"
imgfile2 = "./data/apple.jpg"

img_a = cv2.imread(imgfile1)
img_b = cv2.imread(imgfile2)

re_img_a = cv2.resize(img_a,(400,400))
re_img_b = cv2.resize(img_b,(400,400))

alpha = 0.5
beta = 0.5

img_c = re_img_a + re_img_b

cv2.imshow("A", re_img_a)
cv2.imshow("B", re_img_b)
cv2.imshow("C", img_c)

cv2.waitKey(0)
cv2.destroyAllWindows