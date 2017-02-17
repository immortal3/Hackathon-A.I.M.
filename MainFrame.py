from tkinter import *
import Main
from PIL import ImageTk,Image

def startbutton():
	Main.start()

def settingTab():
	#print ('setting tab')
	setting_frame = Tk()
	setting_frame.title('setting')
	setting_Label = Label(setting_frame, text="Modes")
	setting_Label.pack()
	Mode1 = IntVar()
	#Mode2 = IntVar(setting_frame)
	Mode1 = Checkbutton(setting_frame, text = "Music",onvalue = 1, offvalue = 0, height=5, width = 20)
	print (Mode1.getvar())
	Mode1.pack()


root = Tk()
frame = Frame(root)
root.title('A.I.M.')


startbutton = Button(frame, text="Start A.I.M", fg="Brown", command=startbutton)
startbutton.pack(side = BOTTOM)

setingbutton = Button(frame , text = 'Setting', fg ='Brown' , command = settingTab)
setingbutton.pack(side = BOTTOM)

img = ImageTk.PhotoImage(Image.open('H:\Codes\Python\CompEye\logo_hackathon.png'))
panel = Label(root, image = img)
panel.pack()



frame.pack()

root.mainloop()
