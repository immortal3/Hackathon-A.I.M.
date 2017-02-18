import cv2
import numpy as np
import time
#import volume
#import Media_Controll
import math

videocam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('closed_frontal_palm.xml')
ret , img = videocam.read()
crop_img = img
gray_c = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
print ('program started')

i1 = 0
# height
i2 = np.size(img, 0)
i3 = 0
# width
i4 = np.size(img, 1)

w1 = i1
w2 = i2
w3 = i3
w4 = i4


while True:
    ret , img = videocam.read()
    crop_img = img[i1: i2, i3: i4]
    cv2.rectangle(img ,(w1,w2),(w3,w4),(255,0,0),2)

    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray , 1.1 , 5)
    for (x,y,w,h) in faces:
        X1 = x-w if x-w>0 else 0
        Y1 = y-2*h if y-2*h>0 else 0

        i1 = Y1
        i2 = y + 3*h
        i3 = X1
        i4 = x + 2*w

        w1 = x
        w2 = y
        w3 = x+w
        w4 = y+h

        # gray_c = gray[Y1: y + 4*h, X1: x + 4*w]

    # blur_c = cv2.GaussianBlur(gray_c,(5,5),0)
    gray_crop = cv2.cvtColor(crop_img , cv2.COLOR_BGR2GRAY)
    blur_crop = cv2.GaussianBlur(gray_crop,(5,5),0)

    # ret,thresh1 = cv2.threshold(blur_c,90,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # image, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    ret,thresh1 = cv2.threshold(blur_crop,130,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    image, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    ci = 0
    max_area=0
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i

    # if ci>0 and ci<len(contours):
    cnt=contours[ci]
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)

    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)

    count_defects = 0
    i=0
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img,far,1,[0,0,255],-1)
        dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_img,start,end,[0,255,0],2)

        if count_defects==0:
            print ('1')
        elif count_defects==1:
            print ('2')
        elif count_defects==2:
            print ('3')
        elif count_defects==3:
            print ('4')
        elif count_defects==4:
            print ('5')


    # mind=0
    # maxd=0
    # i=0
    # for i in range(defects.shape[0]):
    #     s,e,f,d = defects[i,0]
    #     start = tuple(cnt[s][0])
    #     end = tuple(cnt[e][0])

    #     far = tuple(cnt[f][0])
    #     dist = cv2.pointPolygonTest(cnt,start,True)
    #     cv2.line(img,start,end,[0,255,0],2)
    #     cv2.circle(img,far,5,[0,0,255],-1)

    cv2.imshow('drawing',drawing)

    cv2.imshow('frame',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

videocam.release()
cv2.destroyAllWindows()
