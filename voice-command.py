import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
from datetime import datetime

recognizer = sr.Recognizer()

# Initialize engine only once (better performance)
engine = pyttsx3.init(driverName="sapi5")
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is not available right now.")
        return ""
    except Exception as e:
        print("Error:", repr(e))
        speak("Something went wrong.")
        return ""

def open_app_or_website(command):

    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
        "chatgpt": "https://chat.openai.com",
        "github": "https://github.com",
        "twitter": "https://twitter.com"
    }

    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "command prompt": "cmd.exe",
        
    }

    # Open websites
    for key in websites:
        if key in command:
            speak(f"Opening {key}")
            webbrowser.open(websites[key])
            return True

    # Open apps
    for key in apps:
        if key in command:
            speak(f"Opening {key}")
            subprocess.Popen([apps[key]])
            return True

    # Extra features
    if "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "who are you" in command:
        speak("I am your Python voice assistant.")

    elif "stop" in command or "exit" in command or "bye" in command:
        speak("Goodbye. See you again.")
        return False

    elif command != "":
        speak("I don't know that command yet.")

    return True

def main():
    speak("Hello. I am ready. Say a command.")
    running = True

    while running:
        command = listen_command()
        running = open_app_or_website(command)

if __name__ == "__main__":
    main()