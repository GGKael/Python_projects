import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PyDictionary

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def gesture():
    engine.say('Hi, I am Alexa, what is your name?')
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            name = listener.recognize_google(voice)
        engine.say('Hi ' + name + ' what can i do for you today?')
        engine.runAndWait()
        return name
    except:
        pass

def start(name):
    engine.say('Hi ' + name + ' what can i do for you today?')
    engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def command_alexa():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa():
    gesture()
    command = command_alexa()
    if 'play' in command_alexa():
        song = command.replace("play", "")
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is the meaning of ' in command:
        word = command.replace('what is the meaning of ', '')
        meaning = PyDictionary.meaning(word)
        print(meaning)
        talk(meaning)
    elif 'will you go on a date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    else:
        talk('Hey, i did not understand')

x = 0

while x == 0:
    run_alexa()
    ques = engine.say('Anything else?')
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sleep' in command:
                engine.say("Good bye! Have a nice day")
                engine.runAndWait()
                x = 1
            elif 'yes' in command:
                start()

    except:
        pass
