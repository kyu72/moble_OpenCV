import cv2

image='./data/lena.jpg'
img=cv2.imread(image)

text = 'Hello'
org = (200,50)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,text, org, font, 1, (255,255,255), 2)

cv2.imshow('img',img)
cv2.imwrite('./data/sample.jpg',img)

cv2.waitKey()
cv2.destroyAllWindows()