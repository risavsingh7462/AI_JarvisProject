'''
Author:--Sanjiv Paul
Date:-18-July-2021

About:- This is an artificial intelligence project I named Jarvis, part of a sci-fi movie Iron Man. This is a personal assistant like Google Assistant, Alexa, or Siri. With this Jarvis_project, we can get some work done automatically like opening youtube, opening a browser, and doing some searches on Wikipedia.

>>Here we have used modules:
1.pyttsx3 --- pip install pyttsx3
2.speech_recognition --- pip install SpeechRecognition==2.1.3
3.datetime
4.wikipedia --- pip install wikipedia
5.Webbrowser
6.os
7.pyaudio --- pip install PyAudio


'''
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    '''
    Speak function will Speak our audio string
    '''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    #WishMe=> return wish according to time.
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Aftrnoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may i help you")


def takeCommand():
    #takeCommand function takes input from the user microphone and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"

    return query


if __name__ == "__main__":
    # speak("sanjiv is good boy")
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\hollywood\\lofi'
            songs = os.listdir(music_dir)
            #    songs1 = songs.split(",")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\SANJIV PAUL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
