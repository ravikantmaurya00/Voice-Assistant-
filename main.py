import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import requests
import json
import psutil
import pyautogui
import pywhatkit
from youtubesearchpython import VideosSearch

# ----------------------------------------------------
# INITIALIZATION
# ----------------------------------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 175)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

# ----------------------------------------------------
# LISTEN FUNCTION
# ----------------------------------------------------
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("\nListening...")
        audio = recognizer.listen(source, phrase_time_limit=6)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        return ""

# ----------------------------------------------------
# TIME & GREETINGS
# ----------------------------------------------------
def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning.")
    elif hour < 18:
        speak("Good afternoon.")
    else:
        speak("Good evening.")
    speak("How can I help you today?")

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")

# ----------------------------------------------------
# GOOGLE SEARCH
# ----------------------------------------------------
def google_search(query):
    speak("Searching on Google...")
    pywhatkit.search(query)
    speak("Here are the results.")

# ----------------------------------------------------
# MUSIC PLAYER
# ----------------------------------------------------
MUSIC_FOLDER = "music"

def play_local_music():
    if not os.path.exists(MUSIC_FOLDER):
        speak("Music folder not found.")
        return

    songs = os.listdir(MUSIC_FOLDER)
    if len(songs) == 0:
        speak("No songs found.")
        return

    song = os.path.join(MUSIC_FOLDER, songs[0])
    speak("Playing music.")
    os.startfile(song)

def play_youtube_song(song_name):
    speak("Searching on YouTube...")
    result = VideosSearch(song_name, limit=1).result()
    link = result["result"][0]["link"]
    webbrowser.open(link)
    speak(f"Playing {song_name} on YouTube.")

# ----------------------------------------------------
# SCREENSHOT
# ----------------------------------------------------
def take_screenshot():
    filename = "screenshot.png"
    img = pyautogui.screenshot()
    img.save(filename)
    speak("Screenshot saved as screenshot dot png.")

# ----------------------------------------------------
# BATTERY STATUS
# ----------------------------------------------------
def battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f"Battery is {percent} percent.")

# ----------------------------------------------------
# VOLUME CONTROL
# ----------------------------------------------------
def volume_control(command):
    if "increase" in command:
        for _ in range(5):
            pyautogui.press("volumeup")
        speak("Volume increased.")

    elif "decrease" in command:
        for _ in range(5):
            pyautogui.press("volumedown")
        speak("Volume decreased.")

    elif "mute" in command:
        pyautogui.press("volumemute")
        speak("Volume muted.")

# ----------------------------------------------------
# LOCATION
# ----------------------------------------------------
def get_location():
    try:
        ip_data = requests.get("https://ipinfo.io/json").json()
        city = ip_data.get("city")
        region = ip_data.get("region")
        country = ip_data.get("country")

        speak(f"You are currently in {city}, {region}, {country}.")
    except:
        speak("Sorry, I could not fetch your location.")

# ----------------------------------------------------
# NOTES SYSTEM
# ----------------------------------------------------
NOTES_FILE = "notes.json"

def save_note(text):
    notes = []
    if os.path.exists(NOTES_FILE):
        notes = json.load(open(NOTES_FILE, "r"))

    notes.append({"note": text, "time": str(datetime.datetime.now())})
    json.dump(notes, open(NOTES_FILE, "w"), indent=4)
    speak("Note saved.")

def read_notes():
    if not os.path.exists(NOTES_FILE):
        speak("No notes found.")
        return

    notes = json.load(open(NOTES_FILE, "r"))
    speak("Here are your notes:")
    for n in notes:
        speak(n["note"])

# ----------------------------------------------------
# AI CHAT MODE (Offline)
# ----------------------------------------------------
def ai_chat(command):
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you": "I'm functioning perfectly.",
        "your name": "I am your Python voice assistant.",
        "who made you": "I was created by a Python developer.",
        "what can you do": "I can open apps, search google, tell time, play music, and much more."
    }

    for key in responses:
        if key in command:
            speak(responses[key])
            return

    speak("I'm not sure, but I'm learning every day.")

# ----------------------------------------------------
# OPEN WEBSITES
# ----------------------------------------------------
def open_website(command):
    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "github": "https://github.com",
        "linkedin": "https://linkedin.com"
    }

    for site in sites:
        if site in command:
            webbrowser.open(sites[site])
            speak(f"Opening {site}.")
            return
    
    speak("Website not recognized.")

# ----------------------------------------------------
# OPEN APPS
# ----------------------------------------------------
def open_app(command):
    if "notepad" in command:
        os.system("notepad")
        speak("Opening Notepad.")
    elif "calculator" in command:
        os.system("calc")
        speak("Opening Calculator.")
    else:
        speak("App not found.")

# ----------------------------------------------------
# MAIN COMMAND HANDLER
# ----------------------------------------------------
def process(command):

    # Exit
    if "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    # Basic
    elif "time" in command:
        tell_time()

    elif "hello" in command or "hi" in command:
        ai_chat("hi")

    # Search
    elif "search" in command:
        query = command.replace("search", "").strip()
        google_search(query)

    # Music
    elif "play music" in command:
        play_local_music()

    elif "play song" in command:
        speak("Which song?")
        song = listen()
        play_youtube_song(song)

    # Volume
    elif "volume" in command:
        volume_control(command)

    # Screenshot
    elif "screenshot" in command:
        take_screenshot()

    # Battery
    elif "battery" in command:
        battery_status()

    # Location
    elif "where am i" in command or "location" in command:
        get_location()

    # Notes
    elif "make a note" in command or "save note" in command:
        speak("What should I write?")
        text = listen()
        save_note(text)

    elif "read notes" in command:
        read_notes()

    # Websites / Apps
    elif "open" in command:
        if any(x in command for x in ["youtube", "google", "github", "linkedin"]):
            open_website(command)
        else:
            open_app(command)

    # AI Chat
    else:
        ai_chat(command)

# ----------------------------------------------------
# MAIN LOOP
# ----------------------------------------------------
def start():
    greet_user()
    while True:
        command = listen()
        if command != "":
            process(command)

start()
