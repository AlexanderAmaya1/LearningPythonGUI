#########################################################
#   File:           weather_app.pyw
#   Author:         Alexander Amaya
#   Email:          amamaya2@asu.edu
#   Date:           October 2021
#   
#   Description: A very simple weather app to learn the
#   basics of Python GUI programming. It displays the 
#   current weather info for Tempe, AZ using the NWS API.
#
#########################################################

from tkinter import *
from tkinter import ttk
from pip._vendor import requests
import json

def getWeatherReport():

    # Makes an API request to the National Weather Service API to get the latest observations for KPHX (Sky Harbor Airport)
    url = "https://api.weather.gov/stations/KPHX/observations/latest"
    response = requests.get(url=url)

    # Gets the weather description icon and writes to a local file
    iconURL = response.json()["properties"]['icon']
    image_response = requests.get(iconURL)
    file = open('weather_image.png', "wb")
    file.write(image_response.content)
    file.close()

    # Gets the text description of the weather from the API request
    textDescription = response.json()["properties"]['textDescription']
 

    # Gets the temperature from the request and converts it to fahrenheit 
    temperature = response.json()["properties"]["temperature"]["value"]
    temperature = round((temperature * (9/5))+32)
    print("Temperature: "+str(temperature)+" degrees F")


    return textDescription, temperature



def main():

    # Gets weather information 
    description, temperature = getWeatherReport()

    # Sets up the window
    root = Tk()
    root.title("Weather")
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    
    # Loads the weather icon image
    image = PhotoImage(file="weather_image.png")

    # Places all the information on the window
    titleLabel  = ttk.Label(frame, text="Current Weather for Tempe, Arizona:").grid(column=0, row=0)
    picLabel    = ttk.Label(frame, image=image).grid(column=0,row=1)
    descLabel   = ttk.Label(frame, text=description).grid(column=0,row=2)
    tempLabel   = ttk.Label(frame, text=str(temperature)+" \xb0 F").grid(column=0,row=3)
    
    # It will update when a user interacts with the window
    root.mainloop()


if __name__ == "__main__":
    main()