import tkinter
from tkinter import * #* means everything
def hii():
    print("Hi")
win = Tk()
win.geometry("600x400")
b = Button(win, text ="hey")
b.grid(row=2,column=2)
b2 = Button(win, text ="Im a button")
b2.grid(row = 1, column = 1)
b3 = Button(win, text ="Another one", command =hii, padx = 50, pady = 60, activeforeground='lime')
# pad x/y : button size, activeforeground : letters' color when press
b3.place(x=300,y=200)


win.mainloop()