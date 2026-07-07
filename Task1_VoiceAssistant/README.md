# 🎙️ Personal Voice Assistant
### OASIS INFOBYTE – Python Programming Internship (OIBSIP)

A simple desktop voice assistant built in Python that listens to your voice,
understands commands, and responds with speech.

---

## ✨ Features
- Greets you based on time of day (Good Morning / Afternoon / Evening)
- Tells current **time** and **date**
- Opens **Google**, **YouTube**, **Wikipedia** in your browser
- Searches **Wikipedia** and reads a short summary aloud
- Tells a random **joke**
- Performs basic **calculations**
- Exits gracefully on command ("exit" / "stop" / "bye")

---

## 🛠️ Setup Instructions

### 1. Install Python
Make sure Python 3.8+ is installed: https://www.python.org/downloads/

### 2. Install required libraries
Open terminal/command prompt in this folder and run:

```bash
pip install -r requirements.txt
```

> **Note (Windows users):** If `pyaudio` fails to install, run:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```
>
> **Note (Mac users):** Install portaudio first:
> ```bash
> brew install portaudio
> pip install pyaudio
> ```
>
> **Note (Linux users):**
> ```bash
> sudo apt-get install portaudio19-dev python3-pyaudio
> pip install pyaudio
> ```

### 3. Run the assistant
```bash
python voice_assistant.py
```

Speak clearly into your microphone after you see **"Listening..."** in the terminal.

---

## 🗣️ Sample Commands to Try
- "What's the time?"
- "What's today's date?"
- "Open Google"
- "Open YouTube"
- "Who is Albert Einstein?"
- "Tell me a joke"
- "Calculate"
- "Exit" / "Bye"

---

## 📹 For Video Demo (OIBSIP submission)
1. Start the video by showing your **name** on the first frame.
2. Run the script and demonstrate at least 4–5 commands live.
3. Show the terminal output along with the assistant's spoken responses.
4. Upload the video to LinkedIn with hashtags **#oasisinfobyte #internship #python**

---

## 📂 GitHub Submission
Push this project to a repository named **OIBSIP** (as required by Oasis Infobyte),
inside a folder like `Python_Programming/Task_X_VoiceAssistant`.

---

## 🚀 Possible Future Improvements
- Wake word detection (e.g., "Hey Assistant")
- Weather updates via API
- Send emails / WhatsApp messages
- GUI using Tkinter
