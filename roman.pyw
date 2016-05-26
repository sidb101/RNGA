import re
import RomanGenerator
import RomanParser
from tkinter import *
from tkinter import font

def process():
    try:
        v.set("")
        global tb1
        s = tb1.get()
        try:    
            i = int(s)
            v.set("The roman equivalent is: {0}".format(RomanGenerator.roman(i)))
        except (ValueError, NameError):
            v.set("A valid Roman string" if RomanParser.valid(s) else "An invalid Roman string")
    except NameError:
        pass
if __name__=='__main__':
    root = Tk()
    
    # setting the frame dimensions to a fixed size
    root.resizable(width=FALSE, height=FALSE)
    root.geometry('{}x{}'.format(560,350))
    
    # title
    root.title("Roman Numbers - Parser & generator")
    
    # icon
    root.iconbitmap('icon.ico')
    
    # frame-texts
    t1 = "\n\n\tEnter:\n\t - String to checks its validity \n\t - An Integer to get its roman equivalent"
    Label(text="Roman Numeral Parser\n&\nGenerator",font=font.Font(family="Times",size=20,underline=1)).pack()
    Message(root,text=t1,width=450,font=font.Font(family='Times',size=15)).pack(anchor=W,side=TOP)

    # Interactive widgets
    tb1 = Entry(root,width=50); tb1.pack(anchor=CENTER)
    btn = Button(root,text="process",font=font.Font(family="Times",size=13),command=process);btn.pack(anchor=CENTER)
    v=StringVar()
    l1  = Label(root,font=font.Font(family="Times",size=13),textvariable=v);l1.pack(anchor=CENTER)

    root.mainloop()
    

