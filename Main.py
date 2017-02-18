import cv2
import numpy as np
import time
import volume
import Media_Controll
import BrowserCommand


def action(modeNo,Direction):
        if Direction == 'left':
            if(modeNo == 1):
                volume.volume_down()
            elif(modeNo == 2):
                BrowserCommand.previousTab()
        elif Direction == 'Right':
            if(modeNo == 1):
                volume.volume_up()
            elif(modeNo == 2):
                BrowserCommand.netxTab()
        elif Direction == 'up':
            if(modeNo == 1):
                Media_Controll.PlayPrevious_Music()
            elif(modeNo == 2):
                BrowserCommand.openTab()
        elif Direction == 'down':
            if(modeNo == 1):
                Media_Controll.Playnext_Music()
            elif(modeNo == 2):
                BrowserCommand.closeTab()

def start(ModeNo):
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
                action(ModeNo,'Right')
                #print ('Right')

            if(deltaX < -15):
                action(ModeNo,'left')
                #print ('left')

            if(deltaY < -40):
                action(ModeNo,'down')
                #print ('down')

            if(deltaY > 40):
                action(ModeNo,'up')
                #print ('up')

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
