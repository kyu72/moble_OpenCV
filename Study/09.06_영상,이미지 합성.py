import cv2

#image
image = './data/lena.jpg'
img = cv2.imread(image)

#video
cap = cv2.VideoCapture('./data/vtest.avi')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

while True:   
    retval, frame = cap.read()
    if not retval:
        break
    
    re_frame = cv2.resize(frame, (300,400))
    re_img = cv2.resize(img, (300,400))
    
    hap = cv2.add(re_frame, re_img)
    
    cv2.imshow('frame', hap)
    
    key = cv2.waitKey(25) #25/1000초 대기시간을 가진다
    if key == 27: # Esc입력하면 종료
        break
    
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()