
from tkinter import *
import requests
from tkinter import PhotoImage

window= Tk()
window.minsize(width="400",height="600")
window.config(bg="light blue")
window.title("What is the weather like?")


image=PhotoImage(file="sun2.png")
bg_image=Label(window,image=image)
bg_image.place(relheight=1,relwidth=1)

api_key = 'e67efd148cb56f7b9d071d773332e5a6'


def get_city_name():
    api_key = 'e67efd148cb56f7b9d071d773332e5a6'
    city = enter_city_name.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'


    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        temp = temp-273.15
        temp=round(temp,1)
        desc = data['weather'][0]['description']
        wind=data['wind']['speed']
        pressure=data['main']['pressure']
        result_label = Label(width="30", height="5")
        result_label.place(x="15", y="450")
        result_label.config(text=f'Temperature: {temp} C degree\n sky:{desc}\n Pressure:{pressure}\n wind={wind} km/h')
        result_label.config(bg="yellow",font=("Verdana",13,"bold"))


        print(f'Temperature: {temp} C')
        print(f'Description: {desc}')

    else:
        error_label=Label(text='Error!!! fetching weather data2')
        error_label.place(x="75",y="470")
        error_label.config(background="light grey", font=("times new roman",15,"bold"))






label=Label(text="Enter City Name",font=("arial",15,"bold"))
label.place(x="110",y="40")
label.config(background="light yellow")
enter_city_name=Entry(width="35")
enter_city_name.place(x="90",y="90")
button=Button(text="Search",width="11",bg="light grey",command=get_city_name)

button.place(x="150",y="115")
















window.mainloop()