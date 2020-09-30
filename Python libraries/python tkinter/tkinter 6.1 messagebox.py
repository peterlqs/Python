from tkinter import *
from tkinter import messagebox
win = Tk()
def hi():
    messagebox.showinfo("From Attitude","Hey there")
b = Button(win,text ="Press me",command = hi)
b.pack()







win.mainloop()