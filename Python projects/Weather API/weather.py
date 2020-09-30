import requests
from tkinter import *
import os
os.chdir("D:\Python\Python projects\Weather API")
#city = input("Type in country/city :")
win = Tk()
win.title("Weather Forecast")
win.resizable(height=False,width=False)
win.geometry("600x400")

def get_weather():
    font= ("Times New Roman",30)
    refined = city_name.get()
    url = ("https://api.openweathermap.org/data/2.5/weather?appid=5d852d1dc718997f6fbca1103a6bcc3a&q={}".format(refined))
    res = requests.get(url)
    output = res.json()
    #print(output)
    tem = output["main"]["temp"] - 272.15
    temp = ("Temperature : %.2f Celsius" % tem)
    weather = output["weather"][0]["main"]
    weather2 = "Cloudiness : "+weather
    try:
        canva_down.delete("temp")
        canva_down.delete("weather")
    finally:
        ttt = canva_down.create_text(230,30,text=temp,font=font,tag="temp")
        jjj = canva_down.create_text(173,90,text=weather2,font=font,tag="weather")

background_image = PhotoImage(file="weatherbgtrue.png")
background_label = Label(win,image=background_image)
background_label.pack()


canva_down = Canvas(win,width=500,height=250,bg="lavender",highlightthickness=0)
canva_down.place(x=50,y=110)
canva_up = Canvas(win,width=500,height=45,bg="spring green",highlightthickness=0)
canva_up.place(x=50,y=35)

large = ("Times New Roman",18)
x1 = StringVar()
city_name = Entry(win,textvariable= x1,width = 34,font=large,bg="light green",borderwidth=0)
city_name.place(x=60,y=44)

but_weather = Button(win,text = "Weather!",height = 1,font=("Lobster",12),bg="light blue",borderwidth=1,command=lambda :get_weather())
but_weather.place(x=475,y=38)

win.mainloop()