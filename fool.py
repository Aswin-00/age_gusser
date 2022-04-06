from random import *
from tkinter import *
win=Tk()
win.title("¯\_ツ_/¯")
def rand():
  rx=randrange(10,180)
  ry=randrange(80,170)
  if(rx==75 or ry==85):
    rand()
  bn.config(bn.place(x=rx,y=ry))
def trap():
  win.destroy()
  pop=Tk()
  pop.title(" ")
  p=Label(pop,text="I Knew IT ",font=('bold',80)).pack()
  p2=Label(pop,text=("\U0001F923 \U0001F923 "),font=("bold",50)).pack()
  pop.after(3000,pop.destroy)
  pop.mainloop()

win.geometry('250x200')
l=Label(win,text="  Are You A FooL \n (●'◡'●) ??",font=("bold",15))
by=Button(win,text="yes",command=trap,width=5)
bn=Button(win,text="No",command=rand,width=5)

by.place(x=70,y=80)
bn.place(x=115,y=80)
l.place(x=40,y=20)

win.mainloop()
