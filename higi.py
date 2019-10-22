import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour: int= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<=14:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am siri. please tell me how may i help you")

def takecommand():

    #it takes microphoonoe input from user and returns string output.

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)
        audio=r.listen(source)
    try:
        print("Recognizing.........")
        query=r.recognize_google(audio,language='en-in')
        print("user said:",query)
    except Exception as e:
        #print(e)
        print("say that again please.....")
        return "NONE"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your mail@gmail.com','your mail passcode')
    server.sendmail('recievers mail@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishme()
    if 1:
        query=takecommand().lower()
        ''' logic for executing tasks based on query'''
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir ='location of the music file'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%M:%M:%S")
            speak(f"sir, the time is{strtime}")

        elif 'mail' in query:
            try:
                speak("what should i say?")
                content =takecommand()
                to = \
                    "recievers @gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except:
                speak("sorry email not sent")



