# Text To Speech Conversion

import warnings

import js as js
import pyttsx3
import speech_recognition as sr
from gtts import gTTs
import playsound
import os
import datetime
import calendar
import webbrowser
import random
import ctypes
import winshell
import subprocess
import pyjokes
import smtplib
import requests
import json
import time

from pywin.debugger.fail import a

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


# Creating Functions

def rec_audio():
    recod = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listenting......")
        audio = recod.listen(source)

    data = " "

    try:
        data = recod.recognize_google(audio)
        print("You Said: " + data)


    except sr.UnknownValueError:
        print("Assistant could not understand the audio")

    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data


# Google Text To Speech

def response(text):
    print(text)

    tts = gTTs(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


# Wake Word

def call(text):
    action_call = "assistant"

    text = text.lower()

    if action_call in text:
        return True

    return False


# Working With Date And Time

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "january",
        "February",
        "March",
        "April",
        "May",
        "June",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
    ]

    return f'Today is {months[month_now - 1]} the {ordinals[day_now - 1]}'


def say_hello(text):
    great = ["hi", "hey", "greetings", "hello", "hey there"]

    response = ["hi", "hey", "greetings", "hello", "hey there"]

    for word in text.split():
        if word.lower() in great:
            return random.choice(response) + "."

    return ""


# Wikipedia Search

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "Who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "_") + "-note.txt"
    with open(file_name, "W") as f:
        f.write(text)

    subprocess.popen(["notepad.exe", file_name])


# Creating The main Program

while True:

    try:

        text = rec_audio()
        speak = " "

        if call(text):

            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today


            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "P.M"
                    hour = now.hour - 12
                else:
                    meridiem = "A.M"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)

                else:
                    minute = str(now.minute)
                    speak = speak + " " + "It is" + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in text or "wikipedia" in text:
                if "Who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentence=2)
                    speak = speak + " " + wiki

            # Answer to General Question

            elif "who are you" in text or "define yourself" in text:
                speak = speak + """Hello, i am an Assistant .I am here to make your life easier. you can command me 
                to perform various tasks such as solving mathematical questions or opening applications etcetera """

            elif " your name" in text:
                speak = speak + "my name is assistant"


            elif "who am I" in text:
                speak = speak + "you must probably be a human"

            elif " why do you exist" in text or "why did you come" in text:
                speak = speak + "It is a secret"

            elif "how are you" in text:
                speak = speak + "I am fine, thank you"
                speak = speak + "\nHow are you ?"

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that you are fine"

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "opening Google chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )

            elif "open" in text.lower():
                if "MicrosoftEdge" in text.lower():
                    speak = speak + "opening MicrosoftEdge"
                    os.startfile(
                        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                    )

            # Opening Applications and websites

            elif "youtube" in text.lower():
                speak = speak + "opening youtube"
                webbrowser.open("https://www.youtube.com/")


            else:
                speak = speak + "Application not available"


        # search on youtube and google

        elif "youtube" in text.lower():
            ind = text.lower().split().index("youtube")
            search = text.split()[ind + 1:]
            webbrowser.open(
                "http://www.youtube.com/results?search_query" +
                "+".join(search)
            )
            speak = speak + "opening " + str(search) + " on youtube"

        elif "search" in text.lower():
            ind = text.lower().split().index("search")
            search = text.split()[ind + 1:]
            webbrowser.open(
                "https://www.google.com/search?q="  "+".join(search)
            )
            speak = speak + "searching " + str(search) + " on google"

        elif "google" in text.lower():
            ind = text.lower().split().index("search")
            search = text.split()[ind + 1:]
            webbrowser.open(
                "https://www.google.com/search?q=" + " on google"
            )

        # working with operating system

        elif "change background" in text or "change wallpaper" in text:
            img = r'C:\Users\Riyad\Desktop\Wallpaper'
            list_img = os.listdir(img)
            randomImg = os.path.join(img, imgchoise)
            ctypes.windll.user32.systemparametersInfoW(20, 0, randomImg, 0)
            speak = speak + "Background changed successfully"


        elif "play music" in text or "play song" in text:
            talk("Here you go with music")
            music_dir = r'C:\Users\Riyad\Desktop\Music'
            songs = os.listdir(music_dir)
            d = random.choice(songs)
            random = os.path.join(music_dir, d)
            playsound.playsound(random)


        elif "empty recycle bin" in text:
            winshell.recycle_bin().empty(
                confirm=True, show_progress=False, sound=True
            )
            speak = speak + "recycle bin empty"

        # python jokes and  Making notes

        elif "note" in text or "remember this" in text:
            talk("what would you like me to write down?")
            note_text = rec_audio()
            note(note_text)
            speak = speak + "I have made a note of that"


        elif "joke" in text or "jokes" in text:
            speak = speak + pyjokes.get_joke()


        elif "weather" in text:
            key = ""
            weather_url = "http://api.openweathermap.org / data / 2.5 / weather?}"
            ind = text.split().index("in")
            location = text.split()[ind + 1:]
            location = "".join(location)
            url = weather_url + "appid" + key + "&q=" + location
            js + requests.get(url).json()
            if js["cod"] !="404":
                weather = js["main"]
                temperature = weather["temp"]
                temperature = temperature = 273.15
                humidity = weather["humidity"]
                desc = js["weather"][0]["descripition"]
                weather_response = "The tempareture in celcius is " + str(temperature) + "The humidity is" +str(humidity) + " and weather descripition is " + str(desc)
                speak = speak + weather_response
            else:
                speak =speak + "city not found"

# permanent or temporary exit

        elif "don't listen" in text or "syop listening" in text or "do not listen" in text:
            talk("for many seconds do you want me to sleep")
            time.sleep(a)
            speak = speak + str(a) + " seconds completed.Now you can ask me anythings"


        elif "exit" in text or "quit" in text:
            exit()


            response(speak)

    except:
        talk("speak")
