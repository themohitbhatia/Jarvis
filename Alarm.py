import pyttsx3
import datetime
import os

engine = pyttsx3.init('sapi5') # To take voice input
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedTime = open("AlarmText.txt","rt")
time = extractedTime.read()
Time = str(time)
extractedTime.close()

deleteTime = open("AlarmText.txt","r+")
deleteTime.truncate(0)
deleteTime.close()

def ring(time):
    timeSet = str(time)
    timeNow = timeSet.replace("jarvis","")
    timeNow = timeNow.replace("set alarm","")
    timeNow = timeNow.replace(" and ",":")
    AlarmTime = str(timeNow)
    while True:
        currentTime  = datetime.datetime.now().strftime("%H:%M:%S")
        if currentTime == AlarmTime:
            speak("Alarm Ringing...")
            os.startfile("music.mp3")
        elif currentTime + "00:00:30" == AlarmTime:
            exit()

ring(time)