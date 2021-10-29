"""
Name:   Rawlings Ozeh
Project: Python Project Stage 1; Voice Assistance (Alexa)
"""
import pyjokes
import pyttsx3 as p
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia

#Speech recognition enables the program to listen to what we say.
listener = sr.Recognizer()

engine = p.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 130)
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
#talk("Hello, my name is Toya, I am your voice assistant. How are you doing?")


#create a function that'll accept voice command
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try: #incase of an error
        with sr.Microphone() as source:
            listener.energy_threshold=10000
            listener.adjust_for_ambient_noise(source,1.2)
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
               command = command.replace('alexa', '') #to remove 'alexa' from the string
           # print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt('playing ' + song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('the time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I dont date broke dudes')
    elif 'are you single' in command:
        talk('I am in love with wifi')
    elif 'how are you' in command:
        talk('do you really care?')
    elif 'go to sleep' in command:
        talk('humans first')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please repeat that command')

while True:
    run_alexa()