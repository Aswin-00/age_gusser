from datetime import * # 
from tkinter import * #only worker if tkinter is installed 

win=Tk()
win.geometry("288x100")
win.columnconfigure(0,weight=1)
win.rowconfigure(2,weight=1)
win.title("AGE TELLER")

today=date.today()
op=StringVar()


def prin():
    v=''
    display_age.delete(0,END)
    v=op.get()
    v=v.split(".")
    day=str(today.day-(int(v[0])))
    month=str(today.month-(int(v[1])))
    yr=str(today.year-(int(v[2])))
    v="Your are "+day +" day "+month+" moths "+yr+" years old"
    display_age.insert(0,v)



Label(win,text=("Enter Your DOB"),font=("15")
    ).grid(column=0,row=0,sticky=E+N+S+W,columnspan=2)

age_entry=Entry(win,textvariable=op,font=("10"))
age_entry.grid(column=0,row=1,sticky=E+N+S+W)


Button(win,text="tell",command=prin,font=("10")
    ).grid(column=1,row=1)

display_age=Entry(win,width=20,font=("10"))
display_age.grid(columnspan=2,column=0,row=2,sticky=S+W+E+N)
display_age.insert(0,"Enter in (Day.Month.Year) formate")

win.mainloop() 
