import pyttsx3
import datetime

engine = pyttsx3.init('sapi5') # To take voice input
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def GreetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")        

    speak("I am jarvis, How can I help you?")
