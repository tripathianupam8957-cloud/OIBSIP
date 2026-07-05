"""
Weather App - OASIS INFOBYTE Internship (Task 2)
Author: Anupam Tripathi

A simple GUI-based Weather Application using Tkinter and the
OpenWeatherMap API. Enter a city name and get live weather details:
temperature, feels-like, humidity, pressure, wind speed, and conditions.

Before running:
1. Sign up (free) at https://openweathermap.org/api
2. Get your API key from: https://home.openweathermap.org/api_keys
3. Paste it below in API_KEY (or set it as an environment variable
   OPENWEATHERMAP_API_KEY for better security).

Install dependency:
    pip install requests
"""

import os
import tkinter as tk
from tkinter import messagebox
import requests

# ------------------ CONFIG ------------------
# Option 1: paste your key directly here (quick, but don't upload it to GitHub)
API_KEY = "YOUR_API_KEY_HERE"

# Option 2 (recommended): read from environment variable instead
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY", API_KEY)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
# ---------------------------------------------


def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
        messagebox.showerror(
            "API Key Missing",
            "Please add your OpenWeatherMap API key in the script\n"
            "(API_KEY variable) or set OPENWEATHERMAP_API_KEY env variable.",
        )
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror(
                "Error", data.get("message", "City not found. Try again.").capitalize()
            )
            clear_labels()
            return

        # Extract data
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].title()
        country = data["sys"]["country"]

        # Update labels
        city_result_label.config(text=f"{city.title()}, {country}")
        temp_label.config(text=f"🌡  Temperature: {temp}°C")
        feels_label.config(text=f"🥵  Feels Like: {feels_like}°C")
        desc_label.config(text=f"☁  Condition: {description}")
        humidity_label.config(text=f"💧  Humidity: {humidity}%")
        pressure_label.config(text=f"📊  Pressure: {pressure} hPa")
        wind_label.config(text=f"🌬  Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Connection Error", "Could not connect to the internet / API server."
        )


def clear_labels():
    city_result_label.config(text="")
    for lbl in (temp_label, feels_label, desc_label, humidity_label, pressure_label, wind_label):
        lbl.config(text="")


# ------------------ GUI SETUP ------------------
root = tk.Tk()
root.title("Weather App - OASIS INFOBYTE")
root.geometry("400x480")
root.resizable(False, False)
root.configure(bg="#1e3d59")

heading = tk.Label(
    root, text="🌦 Weather App", font=("Segoe UI", 20, "bold"),
    bg="#1e3d59", fg="white"
)
heading.pack(pady=15)

input_frame = tk.Frame(root, bg="#1e3d59")
input_frame.pack(pady=5)

city_entry = tk.Entry(input_frame, font=("Segoe UI", 13), width=20, justify="center")
city_entry.grid(row=0, column=0, padx=5)
city_entry.insert(0, "Enter city name")
city_entry.bind("<FocusIn>", lambda e: city_entry.delete(0, tk.END))
city_entry.bind("<Return>", lambda e: get_weather())

search_btn = tk.Button(
    input_frame, text="Search", font=("Segoe UI", 11, "bold"),
    bg="#ff6e40", fg="white", command=get_weather, cursor="hand2"
)
search_btn.grid(row=0, column=1, padx=5)

result_frame = tk.Frame(root, bg="#1e3d59")
result_frame.pack(pady=20)

city_result_label = tk.Label(result_frame, text="", font=("Segoe UI", 15, "bold"), bg="#1e3d59", fg="#ffc13b")
city_result_label.pack(pady=(0, 10))

temp_label = tk.Label(result_frame, text="", font=("Segoe UI", 12), bg="#1e3d59", fg="white")
temp_label.pack(anchor="w", pady=3)

feels_label = tk.Label(result_frame, text="", font=("Segoe UI", 12), bg="#1e3d59", fg="white")
feels_label.pack(anchor="w", pady=3)

desc_label = tk.Label(result_frame, text="", font=("Segoe UI", 12), bg="#1e3d59", fg="white")
desc_label.pack(anchor="w", pady=3)

humidity_label = tk.Label(result_frame, text="", font=("Segoe UI", 12), bg="#1e3d59", fg="white")
humidity_label.pack(anchor="w", pady=3)

pressure_label = tk.Label(result_frame, text="", font=("Segoe UI", 12), bg="#1e3d59", fg="white")
pressure_label.pack(anchor="w", pady=3)

wind_label = tk.Label(result_frame, text="", font=("Segoe UI", 12), bg="#1e3d59", fg="white")
wind_label.pack(anchor="w", pady=3)

footer = tk.Label(
    root, text="OASIS INFOBYTE Internship - Task 2",
    font=("Segoe UI", 9), bg="#1e3d59", fg="#9fb3c8"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
