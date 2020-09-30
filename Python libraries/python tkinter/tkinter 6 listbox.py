from tkinter import *
win = Tk()
win.title("first")

top =Toplevel()
top.title("ehhh")

lb = Listbox(win)
lb.insert(1,"python")
lb.insert(2,"java")
lb.insert(3,"c")
lb.insert(4,"c+")
lb.insert(5,"sql")

lb.pack()













win.mainloop()