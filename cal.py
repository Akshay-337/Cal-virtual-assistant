import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
from googletrans import Translator
import smtplib
from googlesearch import *
from youtubesearchpython import SearchPlaylists
from youtubesearchpython import SearchVideos

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

exitcmd = ["what is the next plan boss", "are u tired boss", "what is your next destination boss"]

jokes = ["I once had a lot of arguments and rants with my bank manager. But then I decided to consolidate all my rants "
         "into one simple monthly outburst.",
         "Cheer yourself up at the next funeral you go to by hiding a tenner in your black suit today",
         "\"Give a man a fire and you keep him warm for a day. Set a man on fire and you keep him warm for the rest of "
         "his life!\"", "My father once told me, \"Son, if you want people to listen to what you have to say, "
                        "claim it's something your father told you.\" "]

invalid = ["i am sorry boss i did not understand u",
           "boss i did not get u",
           "pardon boss"]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('your email', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning boss")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon boss")

    else:
        speak("Good Evening boss")

    speak("I am cal ! Please tell me how may I help you")
if __name__ == "__main__":
    wishMe()
    while True:
        query = input("enter command--").lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'youtube' in query:
            speak("boss please enter the topic of search")
            searchf = input("enter the input of search\n")
            speak('boss do u want to search for playlists or videos! for playlists type pl and for videos type vi')
            sea=input("do u want to search for playlists or videos for playlists type pl and for videos type vi\n")
            if 'pl' in sea:
                speak("searching for the top 5 playlists")
                search2 = SearchPlaylists(searchf, offset=1, mode="json", max_results=20)

                c = search2.titles
                d = search2.links

                print(c[1], "-", d[1])
                print(c[2], "-", d[2])
                print(c[3], "-", d[3])
                print(c[4], "-", d[4])
                print(c[5], "-", d[5])
                speak("these are the top 5 results")
            elif 'vi' in sea:
                speak("searching for the top 5 videos")
                search1 = SearchVideos(searchf, offset=1, mode="json", max_results=20)

                print(search1)

                a = search1.titles
                b = search1.links

                print(a[1], "-", b[1])
                print(a[2], "-", b[2])
                print(a[3], "-", b[3])
                print(a[4], "-", b[4])
                print(a[5], "-", b[5])
                speak("these are the top 5 results")
            else:
                speak("boss i did not get what u are saying")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'google' in query:
            speak("what topic do u want to search boss")
            query = input("Input your query:")
            speak("opening google")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'music' in query:
            music_dir = 'path n ur pc'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[int(input(print(songs)))]))

        elif 'movie' in query:
            movie_dir = 'path in your pc'
            movies = os.listdir(movie_dir)
            print(movies)
            os.startfile(os.path.join(movie_dir, movies[int(input(print(movies)))]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query:
            codePath = "path in your pc"
            os.startfile(codePath)

        elif 'stop' in query:
            speak(exitcmd[random.randint(0, 2)])

        elif 'bored' in query:
            speak("let me entertain you by narrating a joke")
            speak(jokes[random.randint(0, 3)])

        elif 'joke' in query:
            speak("let me entertain you by narrating a joke")
            speak(jokes[random.randint(0, 3)])

        elif 'translate' in query:
            speak("sure!what should i translate")
            speak("i will open a document for selection of language code")
            codePath = "C:\\Users\\akshay\\PycharmProjects\\python3\\virtual assisstant\\languages.txt"
            os.startfile(codePath)
            translator = Translator()
            translations = translator.translate([input("enter the sentence\n")],
                                                dest=input("enter the language code of conversion\n"))
            for translation in translations:
                print(translation.text)
                speak("boss the translation is complete")

        elif 'bye' in query:
            speak("bye boss!take good rest !i will always be there for u")
            break

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = input("content")
                speak("to whom should i mail this content")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry boss! I am not able to send this email")
        else:
            speak(invalid[random.randint(0, 2)])
