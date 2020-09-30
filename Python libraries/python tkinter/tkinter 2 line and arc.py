import tkinter
from tkinter import *
win = Tk()
c = Canvas(win, height = 300,width = 500,bg = 'red')
coord = 10,50,240,210
#start point x,y end point x,y
arc = c.create_arc(coord,start = 0, extent =180,fill ='blue')
line = c.create_line(250,150,500,300,fill ='black')
c.create_text(100, 200, text="Some text")
c.pack()

win.mainloop()