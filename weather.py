from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
api_key='d8d398c177d3424da1e182559240106'

root=Tk()
root.title("WEATHER APP")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False,False)

def getweather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercise")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,2)}°N,{round(location.longitude,2)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)
    #weather
    api="http://api.weatherapi.com/v1/forecast.json?key=d8d398c177d3424da1e182559240106&q=city&days=7&aqi=no&alerts=no"
    json_data = requests.get(api).json()
    #current
    temp = json_data["current"]['temp_c']
    humidity = json_data["current"]['humidity']
    pressure  = json_data["current"]['pressure_in']
    wind = json_data["current"]['wind_mph']
    cloud = json_data["current"]['cloud']
    condition = json_data["current"]['condition']['text']

    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"in"))
    w.config(text=(wind,"mph"))
    c.config(text=(cloud))
    c2.config(text=(condition))

    #firstcell
    firstdayimage = json_data["current"]['condition']['icon']
    x=str(firstdayimage)
    # print(x)
    # print(type(x))
    y=(x[-7:-4])
    
    photo1  = ImageTk.PhotoImage(file=f"weather icon/{y}.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1
    localtime1 = json_data["location"]["localtime"]
    day1time.config(text=f"{localtime1}")

    #secondcell
    seconddayimage = json_data["forecast"]['forecastday'][0]['day']['condition']['icon']
    x=str(seconddayimage)
    # print(x)
    # print(type(x))
    z=(x[-7:-4])
    img = (Image.open(f"weather icon/{z}.png"))
    resized_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2
    tempdaymax2 = json_data["forecast"]['forecastday'][0]['day']['maxtemp_c']
    tempdaymin2 = json_data["forecast"]['forecastday'][0]['day']['mintemp_c']
    day2temp.config(text=f"MAX:{tempdaymax2}°C\nMIN:{tempdaymin2}°C")
    
    #thirdcell
    thirddayimage = json_data["forecast"]['forecastday'][1]['day']['condition']['icon']
    x=str(thirddayimage)
    # print(x)
    # print(type(x))
    q=(x[-7:-4])
    img = (Image.open(f"weather icon/{q}.png"))
    resized_image = img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3
    tempdaymax3 = json_data["forecast"]['forecastday'][1]['day']['maxtemp_c']
    tempdaymin3 = json_data["forecast"]['forecastday'][1]['day']['mintemp_c']
    day3temp.config(text=f"MAX:{tempdaymax3}°C\nMIN:{tempdaymin3}°C")

    #fourthcell
    fourthdayimage = json_data["forecast"]['forecastday'][2]['day']['condition']['icon']
    x=str(fourthdayimage)
    # print(x)
    # print(type(x))
    r=(x[-7:-4])
    img = (Image.open(f"weather icon/{r}.png"))
    resized_image = img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4
    tempdaymax4 = json_data["forecast"]['forecastday'][2]['day']['maxtemp_c']
    tempdaymin4 = json_data["forecast"]['forecastday'][2]['day']['mintemp_c']
    day4temp.config(text=f"MAX:{tempdaymax4}°C\nMIN:{tempdaymin4}°C")

    #fifthcell
    fifthdayimage = json_data["forecast"]['forecastday'][3]['day']['condition']['icon']
    x=str(fifthdayimage)
    # print(x)
    # print(type(x))
    s=(x[-7:-4])
    img = (Image.open(f"weather icon/{s}.png"))
    resized_image = img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5
    tempdaymax5 = json_data["forecast"]['forecastday'][3]['day']['maxtemp_c']
    tempdaymin5 = json_data["forecast"]['forecastday'][3]['day']['mintemp_c']
    day5temp.config(text=f"MAX:{tempdaymax5}°C\nMIN:{tempdaymin5}°C")
    
    #sixthcell
    sixthdayimage = json_data["forecast"]['forecastday'][4]['day']['condition']['icon']
    x=str(sixthdayimage)
    # print(x)
    # print(type(x))
    e=(x[-7:-4])
    img = (Image.open(f"weather icon/{e}.png"))
    resized_image = img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6
    tempdaymax6 = json_data["forecast"]['forecastday'][4]['day']['maxtemp_c']
    tempdaymin6 = json_data["forecast"]['forecastday'][4]['day']['mintemp_c']
    day6temp.config(text=f"MAX:{tempdaymax6}°C\nMIN:{tempdaymin6}°C")

    #seventhcell
    seventhdayimage = json_data["forecast"]['forecastday'][5]['day']['condition']['icon']
    x=str(seventhdayimage)
    # print(x)
    # print(type(x))
    f=(x[-7:-4])
    img = (Image.open(f"weather icon/{f}.png"))
    resized_image = img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7
    tempdaymax7 = json_data["forecast"]['forecastday'][5]['day']['maxtemp_c']
    tempdaymin7 = json_data["forecast"]['forecastday'][5]['day']['mintemp_c']
    day7temp.config(text=f"MAX:{tempdaymax7}°C\nMIN:{tempdaymin7}°C")


    #days

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

    
##icon
image_icon=PhotoImage(file="weather icon/logo.png")
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="weather icon/Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)

##label
label1=Label(root,text="TEMPERATURE",font=("Helvetica",11),fg="White",bg="#203243")
label1.place(x=40,y=120)

label1=Label(root,text="HUMIDITY",font=("Helvetica",11),fg="White",bg="#203243")
label1.place(x=40,y=140)

label1=Label(root,text="PRESSURE",font=("Helvetica",11),fg="White",bg="#203243")
label1.place(x=40,y=160)

label1=Label(root,text="WIND SPEED",font=("Helvetica",11),fg="White",bg="#203243")
label1.place(x=40,y=180)

label1=Label(root,text="CLOUD",font=("Helvetica",11),fg="White",bg="#203243")
label1.place(x=40,y=200)

label1=Label(root,text="CONDITION ",font=("Helvetica",11),fg="White",bg="#203243")
label1.place(x=300,y=220)

##searchbox
Search_image=PhotoImage(file="weather icon/Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="weather icon/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

search_icon=PhotoImage(file="weather icon/Layer 6.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getweather)
myimage_icon.place(x=645,y=125)

##Bottom box
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="weather icon/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="weather icon/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=20)

#clock(Here we will place time)
clock=Label(root,font=("Helvetica",30,"bold"),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=650,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=650,y=50)

#thpwd
t=Label(root,font=("Helvetica",11),fg="white",bg="#57adff")
t.place(x=156,y=120)
h=Label(root,font=("Helvetica",11),fg="white",bg="#57adff")
h.place(x=156,y=140)
p=Label(root,font=("Helvetica",11),fg="white",bg="#57adff")
p.place(x=156,y=160)
w=Label(root,font=("Helvetica",11),fg="white",bg="#57adff")
w.place(x=156,y=180)
c=Label(root,font=("Helvetica",11),fg="white",bg="#57adff")
c.place(x=156,y=200)
c2=Label(root,font=("Helvetica",11),fg="white",bg="#57adff")
c2.place(x=390,y=220)

#firstcell
firstframe = Frame(root,width=230,height=132,bg='white')
firstframe.place(x=35,y=315)

day1=Label(firstframe,font='areal 20',bg="white",fg="black")
day1.place(x=68,y=5)

firstimage = Label(firstframe,bg="white")
firstimage.place(x=1,y=15)

day1time = Label(firstframe,bg="white",fg="black",font="areal 10 bold")
day1time.place(x=100,y=50)

#secondcell
secondframe = Frame(root,width=70,height=115,bg='white')
secondframe.place(x=305,y=315)

day2=Label(secondframe,bg="white",fg="black")
day2.place(x=4,y=5)

secondimage = Label(secondframe,bg="white")
secondimage.place(x=7,y=22)

day2temp = Label(secondframe,bg="white",fg="black",font="areal 8 bold")
day2temp.place(x=3,y=70)

#thirdcell
thirdframe = Frame(root,width=70,height=115,bg='white')
thirdframe.place(x=405,y=315)

day3=Label(thirdframe,bg="white",fg="black")
day3.place(x=4,y=5)

thirdimage = Label(thirdframe,bg="white")
thirdimage.place(x=7,y=22)

day3temp = Label(thirdframe,bg="white",fg="black",font="areal 8 bold")
day3temp.place(x=3,y=70)

#fourthcell
fourthframe = Frame(root,width=70,height=115,bg='white')
fourthframe.place(x=505,y=315)

day4=Label(fourthframe,bg="white",fg="black")
day4.place(x=4,y=5)

fourthimage = Label(fourthframe,bg="white")
fourthimage.place(x=7,y=22)

day4temp = Label(fourthframe,bg="white",fg="black",font="areal 8 bold")
day4temp.place(x=3,y=70)

#fifthcell
fifthframe = Frame(root,width=70,height=115,bg='white')
fifthframe.place(x=605,y=315)

day5=Label(fifthframe,bg="white",fg="black")
day5.place(x=4,y=5)

fifthimage = Label(fifthframe,bg="white")
fifthimage.place(x=7,y=22)

day5temp = Label(fifthframe,bg="white",fg="black",font="areal 8 bold")
day5temp.place(x=3,y=70)

#sixthcell
sixthframe = Frame(root,width=70,height=115,bg='white')
sixthframe.place(x=705,y=315)

day6=Label(sixthframe,bg="white",fg="black")
day6.place(x=4,y=5)

sixthimage = Label(sixthframe,bg="white")
sixthimage.place(x=7,y=22)

day6temp = Label(sixthframe,bg="white",fg="black",font="areal 8 bold")
day6temp.place(x=3,y=70)

#seventhcell
seventhframe = Frame(root,width=70,height=115,bg='white')
seventhframe.place(x=805,y=315)

day7=Label(seventhframe,bg="white",fg="black")
day7.place(x=4,y=5)

seventhimage = Label(seventhframe,bg="white")
seventhimage.place(x=7,y=22)

day7temp = Label(seventhframe,bg="white",fg="black",font="areal 8 bold")
day7temp.place(x=3,y=70)

root.mainloop()