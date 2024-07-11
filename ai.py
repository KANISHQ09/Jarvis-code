import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import subprocess
import pywhatkit
import calendar



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
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

    speak("I am Warrivo Sir. Please tell me how may I help you")       

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'location of your music file...'
            songs = os.startfile(music_dir)

        elif 'open calculator' in query:
            subprocess.call('calc.exe')


        elif 'date' in query:
            today = datetime.date.today()
            speak("Today's date")
            print(today)
            speak(today)
        
        elif 'day' in query:
            day = calendar.day_name[datetime.date.today().weekday()]
            speak("Today is")
            print(day)
            speak(day)

        elif 'time' in query:
            Time = datetime.datetime.now().strftime('%H:%M:%S')
            speak('time is')
            print(Time)
            speak(Time)
                

        elif 'open brave' in query:
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk')
            #change loaction according to your pc
        
        elif 'open spotify' in query:
            os.startfile('C:\\Users\\Asus\\Desktop\\Spotify.lnk')  #change loaction according to your pc

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com//')

        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com//')

        elif 'email to kanishq' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kanishqyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    

        elif 'send whatsapp message' in query:
            pywhatkit.sendwhatmsg("+91_______","hello",18,3)  #phone no. to send the message $ also change the time according to you
            print("message sent")

        
        elif 'goodbye' in query:
            exit()
