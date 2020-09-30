from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Hello World')
my_img = ImageTk.PhotoImage(Image.open("Warframe0000.jpg"))
my_label = Label(image=my_img)
my_label.pack()
#The picture is too big so it didnt show the quit button/cover it
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()
root.mainloop()
