# 0212.py
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 프로그램 시작    
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('./data/vtest.avi')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fig = plt.figure(figsize=(10, 6)) # fig.set_size_inches(10, 6)
fig.canvas.manager.set_window_title('Video Capture')
plt.axis('off')

def init():
    global im
    retval, frame = cap.read() # 첫 프레임 캡처
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
##    return im,

def updateFrame(k): 
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

ani = animation.FuncAnimation(fig, updateFrame, init_func=init, 
                             interval=50)
#부드럽게 만들어준다

plt.show()
if cap.isOpened():
    cap.release()
