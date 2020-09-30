from tkinter import *
win = Tk()
win.geometry("600x400")
l = Label(win,text="hi")
l.pack()
e = Entry(win)
e.pack()
t = Text(win)
t.insert(INSERT,"HIIII")
t.pack()



win.mainloop()