import base64
import binhex
import ctypes
import datetime
import os
import smtplib
import subprocess
import time
import webbrowser

import pyjokes #pip install pyjokes
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
#  pip install pyaudio(In Case Of Error Saying "no module named pyaudio")
import wikipedia  # pip install wikipedia
import winshell # pip instsll winshell
import notify # pip install notify

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
        pass 
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
                print(first_number / second_number)
                speak(first_number / second_number)
                print("Remainder Is ",first_number % second_number )
                speak("Remainder Is ")
                speak(first_number % second_number)
            except Exception as e:
                del e
    except Exception as e:
        del e
        speak("something went wrong")

def encrypter(Message):
    b =  bytes(Message.encode())
    c = base64.urlsafe_b64encode(b)
    print(c)

def decrypter(Message):
    b = bytes(Message.encode())
    c = base64.urlsafe_b64decode(b)
    print(c)
    speak("After Decrypting The Sentence Is")
    speak(c)

def encrypt_file(Infile_path : str,outfile_path : str):
    binhex.binhex(Infile_path,outfile_path)
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

# tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=20)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("if i did not get you, you can type your question")
            search = takeCommand()
            if 'i want to type' in search:
                speak("Type Your Question")
                tsearch = input("Here ")
                speak('Searching Wikipedia...')
                tsearch = tsearch.replace("wikipedia", "")
                results = wikipedia.summary(tsearch, sentences=20)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'do not want to type' in query or 'you got me' in query:
                speak("ok, not searching")
                pass

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
        
        elif 'open facebook' in query:
            speak("Opening Facebook")
            url7 = "https://www.facebook.com"
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url6)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'open instagram' in query:
            speak("Opening Instagram")
            url8 = "https://www.instagram.com"
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url6)
            webbrowser.register('chrome',None)
            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open this url' in query:
            speak("Please Write the URL")
            notify.notification('Please Write The URL','Requset')
            ourl = input("Here  ") 
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

        elif 'open editor' in query:
            codePath = "C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'open powerpoint' in query:
            powerpoint = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(powerpoint)

        elif 'open excel' in query:
            excel = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(excel)
    
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
        elif "encrypt text" in query:
            speak("Please Write The Password Sir")
            notify.notification('Please Write The Password','Alert')
            passw = input("Here ")
            if passw == "1234567890@morgan":
                speak("Access Granted")
                time.sleep(1.1)
                speak("What Is The Message Sir")
                message = takeCommand()
                encrypter(message)
            else:
                speak("Wrong Password")
                speak("Access Not Granted")

        elif "decrypt text" in query:
            speak("Please Write The Password Sir")
            notify.notification('Please Write The Password','ALert')
            passwo = input("Here ")
            if passwo == "1234567890@morgan-phoenix":
                speak("Access Granted")
                time.sleep(1.1)
                speak("Sir, Please Write The Encrypted Text ")
                notify.notification('Please Write The Text To Encrypt','Request')
                text = input("Here  ")
                decrypter(text)
            else:
                speak("Access Not Granted")

        elif 'send a email' in query:
            epass = "emailunlock@3540P"
            speak("Please Write The Password")
            notify.notification('Please Write The Password','Alert')
            epass_t = input("Here ")
            if epass_t == epass:
                speak("Access Granted")
                time.sleep(1.1)
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
            else:
                speak("Access Not Granted")
        
        elif 'encrypt file' in query:
            filepass = "fileencrypto368OP0"
            speak("Please Write The Password")
            filepass_test = input("Here ")
            notify.notification('Please Write The Password','Alert')
            if filepass == filepass_test:
                try:
                    speak("Access Granted")
                    time.sleep(1.1)
                    speak("Please write the file path that you want to encrypt")
                    notify.notification('Please Write The File Path That You Want To Encrypt','Request')
                    infile = input("Here ")
                    speak("Please write file path in which you want to collect the output")
                    notify.notification('Please Write File Path In Which You Want To Collect The Output')
                    outfile = input("Here ")
                    encrypt_file(infile,outfile)
                except Exception as e:
                    del e
                    speak("Something Went Wrong")
            else:
                speak("Access Not Granted")
# System actions
 
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
             
        elif 'hibernate' in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
       
        elif 'restart' in query:
            subprocess.call(["shutdown", "/r"])

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
# Exit
        elif 'jarvis exit' in query:
            speak("Shut ing Down")
            exit(code="Shuting Down")
        
# Talking to the User 
        elif 'what can you do' in query:
            speak("I can send emails(if configured), i can open many things in chrome, play music, do some encrypting decrypting,open power point and excel, if you give the write path, etcetera")
        
        elif 'hello' in query:
            speak("Hello sir, how can i help you")
        
        elif 'say sorry' in query:
            speak("Sorry Sir If I Did Something Wrong") 
        
        elif 'how are you' in query:
            speak("i am fine sir, What about you?")

        elif 'i am fine' in query:
            speak("that is nice, please tell me how may i help you?")

        elif 'then what is in your program' in query:
            speak("I am in devloping stage please forgive me if i missed something.")
        elif 'bye' in query:
            speak("Bye sir") 
        
        elif 'joke' in query:
            speak("Here You Go")
            time.sleep(1.0)
            speak(pyjokes.get_joke())

        elif 'thank you'in query:
            speak("Welcom Sir")

        else:
            speak("i don't know want you want, should i search the web?")
            y = takeCommand()
            if 'yes' in y:
                speak("How Much Details You Want? Less Details, More Details, All details")
                details = takeCommand()
                if "less" in details:
                    try:
                        speak('searching...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=5)
                        speak(results)
                    except Exception as e:
                        del e
                        speak("Sorry Sir, I Did not found Anything")
                elif "more" in details:
                    try:
                        speak('searching...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=10)
                        speak(results)
                    except Exception as e:
                        del e
                        speak("Sorry Sir, I Did not found Anything")
                elif "all" in details:
                    try:
                        speak('searching...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=100)
                        speak(results)
                    except Exception as e:
                        del e
                        speak("Sorry Sir, I Did not found Anything")
                elif 'tell me more' in query:
                    speak('searching...')
                    query = query.replace("wikipedia", "")
                    result = results
                    results = wikipedia.summary(query, sentences=200)
                    if results == result:
                        speak("There is no more content provided on your question sir")
                    else:
                        speak(results)
            elif 'no' in query:
                speak("OK!")