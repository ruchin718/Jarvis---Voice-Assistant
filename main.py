import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('jarvis', '')
            print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif "hi" in command or "hello" in command or "hey" in command:
        hey = 'Hey there, how can I help you'
        print(hey)
        talk(hey)

    elif "tell me your name" in command:
        who = "I am Jarvis. Your desktop Assistant"
        print(who)
        talk(who)

    elif 'what can you do' in command:
        i_can = "I can tell you a joke, the time, open your favourite websites, do a google search and a lot more"
        print(i_can)
        talk(i_can)

    elif 'search' in command:
        text = command.replace("search", "")
        webbrowser.open_new_tab(text)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'bye' in command:
        bye = 'goodbye, take care'
        print(bye)
        talk(bye)
        sys.exit()

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'open youtube' in command:
        webbrowser.open_new_tab("youtube.com")

    elif 'open google' in command:
        webbrowser.open_new_tab("google.com")

    elif 'open code gurukul' in command:
        cg= webbrowser.open_new_tab("code-gurukul.com")

    elif 'news' in command:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('Here are some headlines from the Times of India,Happy reading')

    else:
        talk('Please say the command again.')


while True:
    run_jarvis()