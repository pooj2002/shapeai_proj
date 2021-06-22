import requests
#import os
from datetime import datetime

api_key = "b23ce64d5b6a7ac9b175a7850b19e633"
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %m %Y | %H:%M:%S")

a = "Weather Stats for - {}  || {}".format(location.upper(), date_time)
b = "Current temperature is: {:.2f} deg C".format(temp_city)
c =  "Current weather desc :", weather_desc
d = " Current Humidity     :", hmdt, '%'
e = "Current wind speed    :", wind_spd ,'kmph'

file_dis = input("enter file name to display the content:")
fd = open(file_dis,"x")
fd.write(str(a))
fd.write("\n")
fd.write(str(b))
fd.write("\n")
fd.write(str(c))
fd.write("\n")
fd.write(str(d))
fd.write("\n")
fd.write(str(e))
fd.close()