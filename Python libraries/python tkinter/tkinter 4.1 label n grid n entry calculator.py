from tkinter import *
win = Tk()
l1 = Label(win,text="First")
l1.grid(row=1,column=0)
l2 = Label(win,text="Two")
l2.grid(row=2,column=0)
label = Label(win)
label.grid(row=3,column=1)
x1 = StringVar()
x2 = StringVar()
e1 = Entry(win,textvariable=x1)
e1.grid(row=1,column=1)
e2 = Entry(win,textvariable=x2)
e2.grid(row=2,column=1)
def sum():
    n1= x1.get()
    n2= x2.get()
    sum = int(n1) + int(n2)
    label = Label(win, text ="The sum is : "+ str(sum))
    label.grid(row=3, column=1)
    return
but = Button(win,text="Calculate",command = sum)
but.grid(row=3,column=0)
win.mainloop()
"""from tkinter import *
from functools import partial
win = Tk()
def sum(label,x1,x2):
    n1= (x1.get())
    n2= (x2.get())
    sum = int(n1) + int(n2)
    label.config(text = "The sum is: %d"%sum)
    return
l1 = Label(win,text="First")
l1.grid(row=1,column=0)
l2 = Label(win,text="Two")
l2.grid(row=2,column=0)
label = Label(win)
label.grid(row=3,column=1)
x1 = StringVar()
x2 = StringVar()
e1 = Entry(win,textvariable=x1)
e1.grid(row=1,column=1)
e2 = Entry(win,textvariable=x2)
e2.grid(row=2,column=1)
sum = partial(sum,label,x1,x2)
but = Button(win,text="Calculate",command = sum)
but.grid(row=3,column=0)
win.mainloop()"""