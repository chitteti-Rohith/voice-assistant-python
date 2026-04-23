import speech_recognition as sr
import pyttsx3
from datetime import datetime
import time

recognizer = sr.Recognizer()

def speak(text):
    print("Bot:", text)

    # Create a fresh engine every time
    # For Windows, sapi5 is the usual driver
    engine = pyttsx3.init(driverName="sapi5")
    engine.setProperty("rate", 160)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    if voices:
        engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def get_reply(user_text):
    text = user_text.lower()

    if "hello" in text or "hi" in text:
        return "Hello! Nice to talk with you."
    elif "your name" in text:
        return "I am a basic Python voice bot."
    elif "time" in text:
        return "The time is " + datetime.now().strftime("%I:%M %p")
    elif "date" in text:
        return "Today is " + datetime.now().strftime("%d %B %Y")
    elif "python" in text:
        return "Python is simple, powerful, and fun to learn."
    elif "how are you" in text:
        return "I am doing great. Thanks for asking."
    elif "bye" in text or "exit" in text or "stop" in text:
        return "Goodbye! See you again."
    else:
        return "I heard you, but I do not have a reply for that yet."

speak("Hello! I am ready. Please speak.")

while True:
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        user_text = recognizer.recognize_google(audio, language="en-IN")
        print("You:", user_text)

        reply = get_reply(user_text)
        speak(reply)

        time.sleep(0.3)

        if any(word in user_text.lower() for word in ["bye", "exit", "stop"]):
            break

    except sr.WaitTimeoutError as e:
        print("WaitTimeoutError:", repr(e))
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your voice.")
    except sr.RequestError:
        speak("Speech service is not available right now.")
    except Exception as e:
        print("Error:", e)
        speak("Something went wrong.")
