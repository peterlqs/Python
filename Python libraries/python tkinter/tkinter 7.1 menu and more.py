from tkinter import *
win = Tk()
def nothing():
    file = Toplevel()
    but = Button(file,text = "Do nothing")
    but.pack()
menubar = Menu(win)
filemenu = Menu(menubar)
filemenu.add_command(label="New window",command = nothing)
filemenu.add_command(label="New file",command = nothing)
filemenu.add_command(label="Open",command = nothing)
filemenu.add_command(label="Close",command = nothing)
filemenu.add_command(label="Save",command = nothing)
filemenu.add_separator()
filemenu.add_command(label="Save as",command = nothing)
filemenu.add_command(label="Quit",command =win.quit)

menubar.add_cascade(label ="File",menu = filemenu)

addmenu = Menu(menubar)
addmenu.add_command(label="Candy",command = nothing)
addmenu.add_command(label="Cookie",command = nothing)
addmenu.add_separator()
addmenu.add_command(label="Rice",command = nothing)
addmenu.add_command(label="Sweet",command = nothing)
addmenu.add_command(label="Ideas",command = nothing)
addmenu.add_separator()
addmenu.add_command(label="Out",command = nothing)
addmenu.add_command(label="Quit2",command =win.quit)

menubar.add_cascade(label ="Edit",menu = addmenu)

win.config(menu=menubar)
win.mainloop()
