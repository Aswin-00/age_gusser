from tkinter import *
from random import *
win=Tk()
win.geometry('250x100')
win.title("die guesser")
def press():
    v=str(randrange(0,7))
    display.config(text=v)

x=("Arial",35)

display=Label(win,text="-",font=x)
display.pack()

press=Button(win,text="Again",command=press)
press.pack(padx=30,ipadx=2)
win.mainloop()
