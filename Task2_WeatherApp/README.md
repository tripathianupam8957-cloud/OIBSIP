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
*(<img width="1915" height="1012" alt="Screenshot 2026-07-05 223424" src="https://github.com/user-attachments/assets/2c207cd0-d241-4117-8d7c-adeab23a5274" />
<img width="1911" height="1026" alt="Screenshot 2026-07-05 223407" src="https://github.com/user-attachments/assets/5fea19ad-d65a-4051-b689-2e09c42a9641" />
Add a screenshot of the running app here after you test it)*

## Author
Anupam Tripathi — OASIS INFOBYTE Python Internship
