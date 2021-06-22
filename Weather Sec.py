'''This is a pyton program that fetch the wearher report of the requested area and
prints it in the terminal and also saves the data in a text file named WeatherData.txt'''
import requests
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#Print the weather report in terminal
line1 = "-------------------------------------------------------------\n"
line2 = f"Weather Stats for - {location.upper()}  || {date_time}\n"#.format(location.upper(), date_time)
line3 = "-------------------------------------------------------------\n"

line4 = f"Current temperature is: {temp_city:.2f} deg C\n".format(temp_city)
line5 = f"Current weather desc  : {weather_desc} \n"#,weather_desc,"\n"
line6 = f"Current Humidity      : {hmdt} %\n"#,hmdt, '%\n'
line7 = f"Current wind speed    : {wind_spd} kmph\n"#,wind_spd ,'kmph'

details = line1 + line2 + line3 + line4 + line5 + line6 + line7

print(details)

#Write weather report of requested area in WeatherData.txt file
file1 = open('WeatherData.txt', 'a')
file1.write(details)
file1.close()