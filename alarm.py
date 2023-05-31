from playsound import playsound
from tkinter import *
import time,sys
from tkinter import messagebox
from pygame import mixer
from PIL import Image,ImageTk


def alarm():
    alarm_time = user_input.get()
    if alarm_time =="":
        messagebox.askretrycancel("Error Messge" , "Please Enter Value")
    else:
        while True:
            time.sleep(1)
            if (alarm_time == time.strftime("%H:%M")):
                print("Playing..")
                playsound("punky.mp3")
                sys.exit()





root=Tk()
root.title("Alarm Clock")
root.geometry("600x380")
canvas = Canvas(root,width=600 , height=380)
image =ImageTk.PhotoImage(Image.open("clock.jpg"))
canvas.create_image(0,0,anchor=NW,image= image)
canvas.pack()
header = Frame(root)

box1 = Frame(root)
box1.place(x=220 , y=180)
box2 = Frame(root)
box2.place(x=220 , y = 260)

user_input = Entry(box1,font=('Arial Narrow',20),width = 12)
user_input.grid(row=0,column =2)

start_button = Button(box2,text="Set Alarm" , font=('Arial',16,'bold'),command = alarm)
start_button.grid(row=3,column =2)


root.mainloop()

