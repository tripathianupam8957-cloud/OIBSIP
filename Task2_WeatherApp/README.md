# 🌦 Weather App — OASIS INFOBYTE Internship (Task 2)

A simple, GUI-based **Weather Application** built using **Python (Tkinter)** and the **OpenWeatherMap API**. Users can enter any city name and instantly get live weather details.

## Features
- 🔍 Search weather by city name
- 🌡 Current temperature & "feels like" temperature (°C)
- ☁ Weather condition/description
- 💧 Humidity, 📊 Pressure, 🌬 Wind speed
- ⚠ Error handling for invalid city names / no internet connection

## Tech Stack
- Python 3
- Tkinter (built-in GUI library)
- `requests` library
- [OpenWeatherMap API](https://openweathermap.org/api)

## Setup Instructions

1. Clone the repo:
```bash
   git clone https://github.com/tripathianupam8957-cloud/OIBSIP.git
   cd OIBSIP
```

2. Install dependencies:
```bash
   pip install requests
```

3. Get a free API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).

4. Add your API key in `weather_app.py`:
```python
   API_KEY = "YOUR_API_KEY_HERE"
```
   (or set it as an environment variable `OPENWEATHERMAP_API_KEY` — recommended, so your key doesn't get pushed to GitHub)

5. Run the app:
```bash
   python weather_app.py
```

## Screenshot
*(Add a screenshot of the running app here after you test it)*

## Author
Anupam Tripathi — OASIS INFOBYTE Python Internship
