"""
=========================================================
   PERSONAL VOICE ASSISTANT
   OASIS INFOBYTE - Python Programming Internship (OIBSIP)
=========================================================

Features:
- Greets the user based on time of day
- Listens to voice commands via microphone
- Responds using text-to-speech
- Tells current time and date
- Opens websites (Google, YouTube, Wikipedia)
- Searches Wikipedia and reads summary aloud
- Tells a joke
- Performs basic calculations
- Exits gracefully on command

Author: <Your Name>
"""

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pyjokes
import os
import sys

# ---------------------------------------------------------
# INITIAL SETUP
# ---------------------------------------------------------

def speak(text):
    """
    Convert text to speech and print it on screen too.
    NOTE: A fresh pyttsx3 engine is created every call. This avoids a known
    Windows bug where reusing the same engine across multiple say()/runAndWait()
    calls causes the assistant to go silent after the first sentence.
    """
    print(f"Assistant: {text}")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)   # 0 = male, 1 = female (usually)
    engine.setProperty('rate', 175)             # speaking speed
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def wish_user():
    """Greet the user based on current time of day."""
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your personal voice assistant. How can I help you today?")


def take_command():
    """
    Listens to microphone input and converts speech to text.
    Returns the recognized text in lowercase, or 'None' if it fails.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception:
        speak("Sorry, I did not catch that. Could you please repeat?")
        return "None"

    return query.lower()


def run_assistant():
    """Main loop: keeps listening and responding until user says exit."""
    wish_user()

    while True:
        query = take_command()

        if query == "none":
            continue

        # ---------- TIME ----------
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        # ---------- DATE ----------
        elif "date" in query or "today's date" in query:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {today}")

        # ---------- OPEN WEBSITES ----------
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open wikipedia" in query:
            speak("Opening Wikipedia")
            webbrowser.open("https://www.wikipedia.org")

        # ---------- WIKIPEDIA SEARCH ----------
        elif "who is" in query or "what is" in query or "search wikipedia" in query:
            search_term = (
                query.replace("who is", "")
                .replace("what is", "")
                .replace("search wikipedia for", "")
                .replace("search wikipedia", "")
                .strip()
            )
            speak(f"Searching Wikipedia for {search_term}")
            try:
                result = wikipedia.summary(search_term, sentences=2)
                speak("According to Wikipedia,")
                speak(result)
            except Exception:
                speak("Sorry, I could not find relevant results on Wikipedia.")

        # ---------- JOKE ----------
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # ---------- BASIC CALCULATOR ----------
        elif "calculate" in query:
            speak("Please type the expression you want me to calculate, in the terminal.")
            try:
                expression = input("Enter expression (e.g. 5+3, 10*2): ")
                result = eval(expression)
                speak(f"The result is {result}")
            except Exception:
                speak("Sorry, I could not calculate that. Please check the expression.")

        # ---------- GREETING ----------
        elif "hello" in query or "hi" in query:
            speak("Hello! How can I assist you?")

        # ---------- EXIT ----------
        elif "exit" in query or "stop" in query or "quit" in query or "bye" in query:
            speak("Goodbye! Have a great day!")
            sys.exit()

        else:
            speak("I'm not sure how to help with that yet. You can ask me about time, date, jokes, or to open websites.")


if __name__ == "__main__":
    run_assistant()