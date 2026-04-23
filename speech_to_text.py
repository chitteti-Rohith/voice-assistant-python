import speech_recognition as sr

recognizer = sr.Recognizer()

print("🎤 Speech to Text started")
print("Say 'stop' to exit.\n")

try:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)

                text = recognizer.recognize_google(audio)
                print("You said:", text)

                if text.lower() == "stop":
                    print("Stopping program...")
                    break

            except sr.WaitTimeoutError:
                print("No speech detected. Try again.")

            except sr.UnknownValueError:
                print("Could not understand. Speak clearly.")

            except sr.RequestError as e:
                print("Speech service error:", e)
                break

except OSError:
    print("Microphone not found or access denied.")
