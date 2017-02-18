from tkinter import *
import Main
from PIL import ImageTk,Image
import ModeFile

modeNo = 0
def Modesetfinger():
	ModeFile.run()

def startbutton():
	print ('Mode is given to Main program',ModeNo)
	Main.start(ModeNo.get())



def setmode(tempModeNo):
	print ('Set Mode is called')
	ModeNo.set(tempModeNo)
	print ('Mode is set to :' ,ModeNo.get())

def settingTab():
	#print ('setting tab')
	setting_frame = Tk()
	setting_frame.title('setting')
	setting_Label = Label(setting_frame, text="Modes")
	setting_Label.pack()
	#Mode2 = IntVar(setting_frame)
	Mode1btn = Button(setting_frame, text="Music", fg="Brown", command=lambda :setmode(1))
	Mode2btn = Button(setting_frame, text="Browser", fg="Brown", command= lambda :setmode(2))
	Mode3btn = Button(setting_frame, text="Custom", fg="Brown", command= lambda :setmode(3))
	Mode1btn.pack()
	Mode2btn.pack()
	Mode3btn.pack()




root = Tk()
frame = Frame(root)
root.title('A.I.M.')
ModeNo = IntVar(frame)

startbutton = Button(frame, text="Start A.I.M", fg="Brown", command=startbutton)
startbutton.pack(side = BOTTOM)

setingbutton = Button(frame , text = 'Setting', fg ='Brown' , command = settingTab)
setingbutton.pack(side = BOTTOM)

img = ImageTk.PhotoImage(Image.open('H:\Codes\Python\CompEye\logo_hackathon.png'))
panel = Label(root, image = img)
panel.pack()

Modesetbtn = Button(frame, text="Set Mode using Finger(not complete)",fg = 'Brown',command=Modesetfinger)
Modesetbtn.pack()

frame.pack()

root.mainloop()
