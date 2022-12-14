# 0207.py
import cv2

#cap = cv2.VideoCapture(0)  # 0번 카메라
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
    
    text = 'Text Output'
    org = (200,50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text, org, font, 1, (255,255,255), 2)
    
    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(25) #25/1000초 대기시간을 가진다
    if key == 27: # Esc입력하면 종료
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
