from tkinter import *
import requests
root = Tk()


def get_weather():
    city = cityField.get()
    key = '5d0c58accff3d11454395f680f149bcd'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    options = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=options)
    weather = result.json()
    print(dir(info))
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]} градусов'


root['bg']='SteelBlue1'
root.title('Погода')
root.geometry('500x500')
root.resizable(width=False, height=False)

frame_city = Frame(root, bg='MediumPurple1', bd=5)
frame_city.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_weather = Frame(root, bg='MediumPurple1', bd=5)
frame_weather.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_city, bg='lavender', font='Courier 30 bold')
cityField.pack()

button = Button(frame_city, text=' Узнать погоду ',font='Courier 20 bold', command=get_weather)
button.pack()

info = Label(frame_weather, bg='lavender', font='Courier 18 bold')
info.pack()

root.mainloop()