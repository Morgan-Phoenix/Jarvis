import datetime
import os
import smtplib
import time
import webbrowser

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
#  pip install pyaudio(In Case Of Error Saying "no module named pyaudio")
import wikipedia  # pip install wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        del e
        print("This is not in my program sir")
        speak("This is not in my program sir")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def calculate(first_number,operation,second_number):
    try:
        if operation == 'plus':
            try:
                speak(first_number + second_number)
                print(first_number + second_number)
            except Exception as e:
                del e
        if operation == 'minus':
            try:
                speak(first_number - second_number)
                print(first_number - second_number)
            except Exception as e:
                del e
        if operation == 'into':
            try:
                speak(first_number * second_number)
                print(first_number * second_number)
            except Exception as e:
                del e
        if operation == 'divided':
            try:
                speak(first_number / second_number)
                print(first_number / second_number)
                print("Remainder Is ",first_number % second_number )
                speak("Remainder Is ",first_number % second_number )
            except Exception as e:
                del e
    except Exception as e:
        del e
        speak("something went wrong")


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=20)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube")
            url = "https://www.youtube.com"
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")


        elif 'open google' in query:
            speak("Opening google")
            url2 = "https://www.google.com"
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url2)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")


        elif 'open stackoverflow' in query:
            speak("Opening stackflow")
            url3 = "https://www.stackoverflow.com"
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url3)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'open classroom' in query:
            speak("Opening classroom")
            url4 = "https://classroom.google.com"
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url3)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'open padlet' in query:
            speak("Opening padlet")
            url5 = "https://www.padlet.com"
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url3)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'open whatsapp' in query:
            speak("Opening whatsapp")
            url6 = "https://web.whatsapp.com"
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url6)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open this url' in query:
            speak("Please tell the URL")
            ourl = takeCommand()
            speak("Opening")
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(ourl)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")


        elif 'play music' in query:
            music_dir = 'C:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
           
        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
        
        elif 'what can you do' in query:
            speak("I can send emails(if configured), i can open many things in chrome, play music, etcetera")
        
        elif 'hello' in query:
            speak("Hello sir, how can i help you")
    
        elif 'calculator' in query:
            try:
                speak("What is the first number")
                a = int(takeCommand())
                speak("what is the operation")
                b = takeCommand()
                speak("What is the second number")
                c = int(takeCommand())
                calculate(a,b,c)
            except Exception as e:
                del e
                speak("prosses failed")
        
        elif 'set a timer' in query:
            speak("How many minutes sir?")
            timer = int(takeCommand())
            timer*=60
            speak("done sir")
            while timer != 0:
                timer-=1
                time.sleep(1)
                if timer == 0:
                    speak("Time is up")
                    speak("Time is up")
                    speak("Time is up")

        elif 'send a email' in query:
            try:
                speak("Whom to send")
                to = takeCommand()   
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        elif 'jarvis exit' in query:
            speak("Shuting down")
            exit(code="Shuting down") 
