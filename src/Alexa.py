"""
Name:   Rawlings Ozeh
Project: Python Project Stage 1; Voice Assistance (Alexa)
"""
import sys
import pyjokes
import pyttsx3 as p
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia

#Speech recognition enables the program to under our commands
listener = sr.Recognizer()

#Speech to Text enables the program to communicate with us
engine = p.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 140)
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)


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
            #print(command)
    except:
        pass
    return command


def say(text):
    engine.say(text)
    engine.runAndWait()
say("Hello, my name is Alexa, I am your voice assistant. How are you?")


#run the voice assistant
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        say('playing ' + song)
        pywhatkit.playonyt('playing ' + song) #connect to youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        say('the time is ' + time)  # time
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info) #get info from wiki
        say(info)
    elif 'joke' in command:
        say(pyjokes.get_joke())
    elif 'halloween' in command:
        say('ha haha, I will reserve my comment')
    elif 'date' in command:
        say('sorry, I do not date broke dudes')
    elif 'really' in command:
        say('Yeah, really! I am a hustler')
    elif 'are you single' in command:
        say('I am in love with wifi')
    elif 'how are you' in command:
        say('do you really care?')
    elif 'no' in command:
        say('I thought as much. Anything else?')
    elif 'go to sleep' in command:
        say('humans first')
    elif 'stop' in command:
        sys.exit() #stop Alexa
    else:
        say('Please repeat that command')

while True:
    run_alexa()