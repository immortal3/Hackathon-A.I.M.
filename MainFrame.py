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

def AboutUSmethod():
	about_us_frame = Tk()
	about_us_frame.title('About us')
	Ativ = Label(about_us_frame, text="Ativ")
	Pratik = Label(about_us_frame, text="pratik")
	Kartvaya = Label(about_us_frame, text="Kartvaya")
	Dip = Label(about_us_frame, text="Dip")
	Ativ.pack()
	Pratik.pack()
	Kartvaya.pack()
	Dip.pack()
	about_us.pack()


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
	setting_frame.minsize(width=200,height=200)
	#Mode2 = IntVar(setting_frame)
	Mode1btn = Button(setting_frame, text="Music", fg="Green", command=lambda :setmode(1) & setting_frame.destroy())
	Mode2btn = Button(setting_frame, text="Browser", fg="Red", command= lambda :setmode(2) & setting_frame.destroy())
	Mode3btn = Button(setting_frame, text="Mouse-Free-mode", fg="Green", command= lambda :setmode(3) & setting_frame.destroy())
	Mode1btn.pack()
	Mode2btn.pack()
	Mode3btn.pack()



root = Tk()
frame = Frame(root)
root.title('A.I.M.')
ModeNo = IntVar(frame)


startbutton = Button(frame, text="Start A.I.M", fg="Green", command=startbutton)
startbutton.pack(side = BOTTOM)

setingbutton = Button(frame , text = 'Setting', fg ='Green' , command = settingTab)
setingbutton.pack(side = BOTTOM)

img = ImageTk.PhotoImage(Image.open('H:\Codes\Python\CompEye\logo_hackathon.png'))
panel = Label(root, image = img)
panel.pack(side = TOP)

Modesetbtn = Button(frame, text="Set Mode using Finger(not complete)",fg = 'Red',command=Modesetfinger)
Modesetbtn.pack()

AboutUSbtn = Button(frame , text = 'About us',fg = 'Brown',command = AboutUSmethod)
AboutUSbtn.pack()
root.minsize(width=350,height=400)
frame.pack()

root.mainloop()
