from unittest import result
import pyttsx3
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google","")
        query = query.replace("google search","")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 2)
            speak(result)

        except:
            speak("Sorry I foung nothing on google")

def searchYoutube(query):
    if "youtube" in query:
        speak("Opening youtube")
        query = query.replace("jarvis","")
        query = query.replace("youtube","")
        query = query.replace("youtube search","")
        web = "https://www.youtube.com/results?sp=mAEB&search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Seraching from wikipedia...")
        query = query.replace("jarvis","")
        query = query.replace("wikipedia","")
        query = query.replace("wikipedia search","")
        query = query.replace("search wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia...")
        print(results)
        speak(results)