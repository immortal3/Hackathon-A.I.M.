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
    for (x,y,w,h) in faces:
        deltaX = StartX - x
        deltaY = StartY - y
        #print (deltaX)
        #print (deltaY)
        if(deltaX > 15):
            print ('Right')
        if(deltaX < -15):
            print ('left')
        if(deltaY < -10):
            print ('down')
        if(deltaY > 10):
            print ('up')

        # time.sleep(0.01)
        StartX = x
        StartY = y
        cv2.rectangle(img ,(x,y),(x+w,y+h),(255,0,0),2)
    #time.sleep(0.2)


    cv2.imshow('frame',img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

videocam.release()
cv2.destroyAllWindows()
