#????????????????????
from tkinter import *
win = Tk()
s = Scale(win)
s.pack()
sb = Spinbox(win, from_=0, to=10)
sb.pack()

scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT,fill=Y)
list = Listbox(win, yscrollcommand=scrollbar.set)#yscrollcommand to like when you scroll ur mouse thingy it moves too
for line in range(100):
    list.insert(END, "This is a line number is" + str(line))
list.pack(side=LEFT,fill=BOTH)

win.mainloop()
