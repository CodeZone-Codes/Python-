# Import required modules
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap
#################----------------------------------------------------------------------------

# Function to get weather data by city name
def get_weather(city):
    # API key for OpenWeatherMap
    API_key = "1b2f8c4cbcbd0ee0ce628c4130e28dc2"
    # URL for API request
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    # Send GET request
    res = requests.get(url)

    # Check for 404 error
    if res.status_code == 404:
        # Display error message
        messagebox.showerror("Error", "City not found")
        # Return None if city not found
        return None
    
    # Parse JSON response
    weather = res.json()
    # Get icon ID
    icon_id = weather['weather'][0]['icon']
    # Get temperature in Celsius
    temperature = weather['main']['temp'] - 273.15
    # Get weather description
    description = weather['weather'][0]['description']
    # Get city name
    city = weather['name']
    # Get country code
    country = weather['sys']['country']

    # Get icon URL
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    # Return weather data
    return (icon_url, temperature, description, city, country)
#################----------------------------------------------------------------------------
root = ttkbootstrap.Window(themename="morph")
root.title("Weather App | CodeZone")
root.geometry("400x400")
#################----------------------------------------------------------------------------
# Create an entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)
#################----------------------------------------------------------------------------
# Get user input for city search
def search():
    city = city_entry.get()  # Get user input for city

    # Get weather data for the city
    result = get_weather(city)

    # Check if city is found
    if result is None:
        return
    

    # Unpack weather data
    icon_url, temperature, description, city, country = result

    # Update location label
    location_label.configure(text=f"{city}, {country}")

    # Get and display weather icon
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")
#------------------------------------------------------------------------------------------
# Create a button widget -> to search for the weather information
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)
#################----------------------------------------------------------------------------
# Create a label widget -> to show the city/country name
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)
#################----------------------------------------------------------------------------
# Create a label widget -> to show the weather icon
icon_label = tk.Label(root)
icon_label.pack()
#################----------------------------------------------------------------------------
# Create a label widget -> to show the temperature
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()
#################----------------------------------------------------------------------------
# Create a label widget -> to show the weather description
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()
#################----------------------------------------------------------------------------
root.mainloop()