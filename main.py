import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from googlesearch import search

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("Hello Sir, I am VAPA. How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except Exception as e:
        print("I didn't hear properly, can you repeat please...")
        return "None"
    return query

def activate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'VAPA' to activate...")
        audio = r.listen(source)
    try:
        activation_phrase = r.recognize_google(audio, language='en')
        if "vapa" in activation_phrase.lower():
            return True
    except Exception as e:
        pass
    return False

if __name__ == "__main__":
    while True:
        if activate():
            wish()
            while True:
                query = takeCommand().lower()
                if 'wikipedia' in query:
                    print("Searching Wikipedia....")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'open youtube' in query:
                    webbrowser.open("https://www.youtube.com/")
                elif 'open google' in query:
                    webbrowser.open("https://www.google.com/")
                elif 'search on google' in query:
                    print("Searching in Google.....")
                    query = query.replace("search on google", "")
                    results = search(query, tld="co.in", num=10, stop=10, pause=2)
                    for result in results:
                        print(result)
                elif 'exit' in query:
                    speak("As you wish Sir, Bye")
                    break
                    
