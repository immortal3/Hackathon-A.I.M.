import cv2
import numpy as np
import time
import volume
import Media_Controll

videocam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('palm.xml')

StartX = 0
StartY = 0
deltaX = 0
deltaY = 0

while True:
    ret , img = videocam.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray , 1.1 , 6)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    max_area=0
    
    ret,thresh1 = cv2.threshold(blur,130,200,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    image, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img ,(x,y),(x+w,y+h),(255,0,0),2)
        f=0
        if w>15 and h>15 :
            crop_img = img[x:y, w:h] # Crop from x, y, w, h -> 100, 200, 300, 400
          # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
            # while True :
        else:
            break

    
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i

    cnt=contours[ci]
    print ci
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    cv2.drawContours(drawing,[hull],0,(0,0,255),2)

    cv2.imshow('frame',img)
    cv2.imshow('drawing',drawing)
    cv2.imshow('thresh',thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videocam.release()
cv2.destroyAllWindows()
