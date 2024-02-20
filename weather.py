import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = '3095e3e497e145d4bcf85814241702'  
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

    try:
        response = requests.get(url)
        data = response.json()

        if 'error' not in data:
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']
            wind_speed = data['current']['wind_kph']
            description = data['current']['condition']['text']

            weather_display.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h\nDescription: {description}")
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Weather Forecast")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

city_label = tk.Label(frame, text="Enter City:")
city_label.grid(row=0, column=0, padx=5, pady=5)

city_entry = tk.Entry(frame)
city_entry.grid(row=0, column=1, padx=5, pady=5)

get_weather_button = tk.Button(frame, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

weather_display = tk.Label(root, text="", font=("Helvetica", 12), padx=10, pady=10)
weather_display.pack()
  
root.mainloop()
