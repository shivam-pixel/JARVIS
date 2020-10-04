import pyttsx3

import datetime

import speech_recognition as sr

import wikipedia

import webbrowser

import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Shivam")
        
    elif hour>=12 and hour<4:
        speak("Good afternoon Shivam")
        
    else:
        speak("hii Shivam ")

    speak("I am your Assistant Marvis")
    
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='hi-IN')
        print("user said : ", query)
        
    except Exception as e:
        print(e)
        speak("Sorry Shivam,may you please repeat that again?")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        speak("now what you want shivam?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened")
            
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "Jarvis Camera ", "img.jpg") 
  
        elif 'open google' in query:
            webbrowser.open("google.com")
  
        elif 'song' in query:
            speak("Happy Birthday to You Happy Birthday to You Happy Birthday Dear me Happy Birthday to You.From good friends and true,From old friends and new,May good luck go with you,And happiness too.")
            
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("gmail is opened")
            
        elif 'my channel' in query:
            webbrowser.open("https://youtu.be/pWERcGvCL5g")
            speak("done your channel is opened")
            
        elif 'tell weather' in query:
            webbrowser.open("accuweather.com")
            speak("done shivam")
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time u asked is {strTime}")
        
        elif 'stop' in query:
            speak("nice to meet you shivam Have a nice day")
            
        elif 'thank you' in query:
            speak("welcome shivam its  my pleasure to help you")
            
        elif 'how are you ' in query:
            speak("i am fine thank you. how are you??")
            
        elif 'corona count' in query:
            webbrowser.open("https://www.worldometers.info/coronavirus/")
            speak("corona count is opened")
            
        elif 'songs' in query:
            webbrowser.open("https://gaana.com/topcharts")
            speak("be happy and relax yourself by listening songs")
            
        elif 'find story' in query:
            webbrowser.open("http://www.hindikahani.hindi-kavita.com/")
            speak("is it a good story")
            
        elif 'cartton' in query:
            webbrowser.open("https://cdn1.vectorstock.com/i/1000x1000/87/85/cartoon-funny-bear-vector-16998785.jpg")
            speak("its cute")
            
        elif 'about weather' in query:
            speak("see")
            webbrowser.open("https://weather.com/en-IN/")
            
        elif 'my name' in query:
            speak("Shivam Tripathi")

        elif 'open my project' in query:
            webbrowser.open("https://create.arduino.cc/projecthub/stt4236/automatic-light-04d834?ref=user&ref_id=1547941&offset=12")
            speak("done !!! great project")

        elif 'social distancing' in query:
            webbrowser.open("https://create.arduino.cc/projecthub/stt4236/social-distancing-d25372?ref=user&ref_id=1547941&offset=3")
            speak("congratulationsz")
            
            
        elif 'quotes' in query:
            speak("just a second")
            webbrowser.open("https://www.yourquote.in/embed/qr827")
            
            exit()
            
        else :
            webbrowser.open(query)
   

