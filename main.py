import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

if __name__ == "__main__":
    speak("Initializing Nancy....")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  
                print("Listening..")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
            
            word = recognizer.recognize_google(audio).strip().lower()
            if word == "activate":
                speak("Yes sir")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    speak("AI teacher activated")
                    print("Nancy Activate...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
        except Exception as e:
            print(f"Error: {e}")