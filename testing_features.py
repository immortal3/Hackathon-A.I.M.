import cv2
import numpy as np
import time

videocam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('closed_frontal_palm.xml')

StartX = 0
StartY = 0
deltaX = 0
deltaY = 0


while True:
    ret , img = videocam.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray , 1.1 , 5)
    cropimg = 0
    blur = cv2.GaussianBlur(gray, (21, 21), 0)
    gray = np.float32(gray)

    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)
    for (x,y,w,h) in faces:
        cropimg = gray[y: y + h, x: x + w]
        StartX = x
        StartY = y
        cv2.rectangle(img ,(x,y),(x+w,y+h),(255,0,0),2)
    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(img,(x,y),3,255,-1)

    #time.sleep(0.2)

    cv2.imshow('frame2',cropimg)

    cv2.imshow('frame',img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

videocam.release()
cv2.destroyAllWindows()
