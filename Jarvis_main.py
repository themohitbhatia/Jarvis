from importlib.resources import contents
from re import search
from urllib import request
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import datetime

engine = pyttsx3.init('sapi5') # To take voice input
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    '''
        It takes microphone input from the user and returns strinf output
    '''
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query # Will return to listening mode

def alarm(query):
    timehere = open("AlarmText.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")

if __name__ == "__main__":

    while True:
        query = takeCommand().lower()
        if "wake up jarvis" in query:
            from GreetMe import GreetMe
            GreetMe()

            while True:
                query = takeCommand().lower()

                if 'go to sleep' in query:
                    speak("Ok Sir! You can call me anytime")
                    break


                # <----- NORMAL CONVERSATION ----->
                elif "hello" in query:
                    speak("Hello sir, how are you")
                elif "i am fine" in query:
                    speak("Thats great! sir")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "thank you" in query:
                    speak("Its my pleasure, I am always here for you")


                # <----- YouTube Controls ----->
                


                # <----- OPENING AND CLOSING APPS ----->
                elif 'open' in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif 'close' in query:
                    from Dictapp import closeapp
                    closeapp(query)


                # <----- ALARM ----->
                elif "set alarm" in query:
                    print("input time expample :- 10 and 10 and 10")
                    speak("Set the Time")
                    a = input("Time :- ")
                    alarm(a)
                    speak(f"Alarm set for {a}")


                # <----- SEARCHING WEB ----->
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)            
                

                # <----- BASIC INFO ----->
                elif "temprature" in  query:
                    search = "temprature in alwar"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "weather" in  query:
                    search = "weather in alwar"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeaWE").text
                    speak(f"current {search} is {temp}")

                elif 'tell me time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strTime}")




                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
                    
                elif 'open youtube studio' in query:
                    webbrowser.open("studio.youtube.com")

                elif 'open instagram' in query:
                    webbrowser.open("instagram.com")

                elif 'open facebook' in query:
                    webbrowser.open("facebook.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'play music' in query:
                    music_dir = 'C:\\Users\\lenovo\\Desktop\\MOHIT\\MUSIC'
                    songs = os.listdir(music_dir)
                
                    os.startfile(os.path.join(music_dir, songs[0]))
                
                elif 'play Adhi Adhi Raat' in query:
                    s1 = 'C:\\Users\\lenovo\\Desktop\\MOHIT\\MUSIC\\Adhi Adhi Raat_320(PaglaSongs).mp3'
                    
                    os.startfile(s1)
                
                elif 'play Amplifier' in query:
                    s2 = 'C:\\Users\\lenovo\\Desktop\\MOHIT\\MUSIC\\Amplifier_320(PaglaSongs).mp3'
                    os.startfile(s2)

                elif 'open code' in query:
                    codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'open word' in query:
                    wordPath = "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                    os.startfile(wordPath)

                elif 'goodbye' in query:
                    speak("Hope I was a good company sir. Have a good day")
                    exit()
