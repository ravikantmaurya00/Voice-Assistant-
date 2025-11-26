# 🧠 Voice Assistant using Python

A fully featured, AI-powered **Voice Assistant** built with Python. It
can perform system tasks, search the web, play music, open apps, fetch
location, take screenshots, respond conversationally, manage notes, and
more --- all through **voice commands**.

## 🚀 Features

### 🎙 Voice Recognition

-   Converts speech to text using **Google Speech Recognition**
-   Continuous listening mode
-   Noise adjustment for better accuracy

### 🔊 Text-to-Speech

-   Uses **pyttsx3** for offline speech output
-   Adjustable voice speed

### 🔥 Advanced Functionalities

  Feature                  Description
  ------------------------ --------------------------------------------------
  **Google Search**        Search anything online using your voice
  **Play Local Music**     Automatically plays songs from a music folder
  **Play YouTube Songs**   Search & play songs on YouTube
  **Open Websites**        Google, YouTube, GitHub, LinkedIn
  **Open Apps**            Notepad, Calculator, CMD etc.
  **Volume Control**       Increase, decrease, or mute system volume
  **Screenshot**           Captures screenshots with a single voice command
  **Battery Status**       Reads out battery percentage
  **Location Detection**   Fetches current location using IP
  **Notes Manager**        Save notes and read them aloud
  **AI Chat Mode**         Offline chatbot responses
  **Friendly Greetings**   Time-based dynamic greetings

## 🛠 Technologies Used

-   Python 3.x
-   speech_recognition
-   pyttsx3
-   pyautogui
-   pywhatkit
-   youtube-search-python
-   requests
-   psutil
-   os, datetime, json

## 📂 Project Structure

    voice-assistant/
    │
    ├── assistant.py        # Main program
    ├── notes.json          # Auto-generated notes storage
    ├── music/              # Add your music files here
    └── README.md           # Project documentation

## 📦 Installation

### 1️⃣ Clone the repository

    git clone https://github.com/ravikantmaurya00/voice-assistant.git
    cd voice-assistant

### 2️⃣ Install required libraries

    pip install speechrecognition pyttsx3 pyaudio requests psutil pyautogui youtube-search-python pywhatkit

If PyAudio fails: Download from
https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio

    pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl

## ▶️ Running the Assistant

    python assistant.py

## 🎤 Example Commands

### Web Search

-   "search python tutorials"
-   "search latest news"

### Open Sites

-   "open youtube"
-   "open linkedin"

### System Control

-   "open notepad"
-   "open calculator"
-   "take screenshot"
-   "increase volume"
-   "battery percentage"

### Music

-   "play music"
-   "play song despacito"

### Notes

-   "make a note"
-   "read notes"

### AI Chat

-   "how are you?"
-   "what can you do?"

### Exit

-   "exit"
-   "stop"

## 🧩 Troubleshooting

-   Mic not detected → check system permissions
-   PyAudio error → install via .whl
-   No voice response → check internet / background noise

## 📌 Future Improvements

-   Weather API\
-   News integration\
-   Wake-word detection\
-   GUI version\
-   Offline STT using Vosk

## 📝 License

MIT License
