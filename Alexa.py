# Project1: Creating your own Alexa

#importing the necessary libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from PyDictionary import PyDictionary

#initializing the speech recognition and the Alexa voice
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#First encounter
def gesture():
    talk('Hi, I am Alexa, what is your name?')
    try:
        with sr.Microphone() as source:
            print("Listening for your name...")
            voice = listener.listen(source)
            name = listener.recognize_google(voice)
            talk('Hi ' + name + ', what can i do for you today?')
        return
    except:
        print("Alexa could not hear you")

#creating a method to let Alexa talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Speech recognition works only when you say 'Alexa'
def command_alexa():
    try:
        with sr.Microphone() as source:
            print("Listening for command...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')

    except:
        print("Alexa could not hear you")
    return command

#This flag will help me run_alexa() without the gesture()
flag = 1

# tasks that Alexa can perform
def run_alexa():
    if flag == 1:
        gesture()
        task_alexa()
    elif flag == 2:
        task_alexa()


def task_alexa():
    task = command_alexa()
    if 'play' in task:
        song = task.replace("play", "")
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'who is' in task or ('what is' in task and 'time' not in task):
        person = task.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is the meaning of ' in task:
        word = task.replace('what is the meaning of ', '')
        meaning = PyDictionary.meaning(word)
        print(meaning)
        talk(meaning)
    elif 'will you go on a date' in task:
        talk('sorry, I have a headache')
    elif 'are you single' in task:
        talk('I am in a relationship with wifi')
    elif 'joke' in task:
        talk(pyjokes.get_joke())
    elif 'time' in task:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    else:
        talk('Hey, i did not understand')

#Running Alexa, Say "Sleep Alexa" or "no Alexa" to quit.
x = 0

while x == 0:

    run_alexa()
    talk("Anything else?")

    try:
        with sr.Microphone() as source:
            print("Listening for further instructions...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sleep' in command or 'no' in command:
                talk("Good bye! Have a nice day")
                x = 1
            elif 'yes' in command:
                flag = 2
    except:
        print("Alexa could not hear you")
