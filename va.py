import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import calendar
from imdb import IMDb
import webbrowser

 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command="hi"
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'amigo' in command:
                command = command.replace('amigo', '')
                print(command)
    except:
        pass
    return command


def run_amigo():
    print("Your AMiGO is good to go")
    command="Hi, I'm your amigo, How can I help you?"
    talk(command)
    while ('stop' not in command):
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'open' in command:
            ws = command.replace('open ', '')
            webbrowser.open(command)
        elif 'browse' in command:
            ws = command.replace('browse ', '')
            webbrowser.open(ws)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        # elif 'google' in command:
        #     query = command.replace('google search ', '')
            
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'what is' in command:
            thing = command.replace('what is', '')
            info = wikipedia.summary(thing, 2)
            print(info)
            talk(info)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'date' in command:
            date=datetime.datetime.now().strftime("%d %B %Y")
            w_day=calendar.day_name[datetime.date.today().weekday()]
            talk('The Time is '+date+ 'and its '+w_day)
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'director' in command:
            ia = IMDb()
            d=''
            if 'who is the director of the movie ' in command:
                command=command.replace('who is the director of the movie ', '')
            elif 'who is the director of movie ' in command:
                command=command.replace('who is the director of movie ', '')
            elif 'who is the director of ' in command:
                command=command.replace('who is the director of ', '')
            elif 'who is director of ' in command:
                command=command.replace('who is director of ', '')
            elif 'the director of movie ' in command:
                command=command.replace('the director of movie ', '')
            elif 'director of ' in command:
                command=command.replace('director of ', '')
            for director in ia.get_movie(ia.search_movie(command)[0].movieID)['directors']:
                d=d+director['name']+', '
            talk(d)
        elif ('actors' in command) or ('actor' in command):
            ia = IMDb()
            a=''
            if 'name the actors of the movie ' in command:
                command=command.replace('name the actors of the movie ', '')
            elif 'name the actor of the movie ' in command:
                command=command.replace('name the actor of the movie ', '')
            elif 'name the actors of ' in command:
                command=command.replace('name the actors of ', '')
            elif 'name the actor of ' in command:
                command=command.replace('name the actor of ', '')
            elif 'who are the actors of the movie ' in command:
                command=command.replace('who are the actors of the movie ', '')
            elif 'who are actors of the movie ' in command:
                command=command.replace('who are actors of the movie ', '')
            elif 'the actors of the movie ' in command:
                command=command.replace('the actors of the movie ', '')
            elif 'actors of the movie ' in command:
                command=command.replace('actors of the movie ', '')
            elif 'the actors of movie ' in command:
                command=command.replace('the actors of movie ', '')
            elif 'actors of ' in command:
                command=command.replace('actors of ', '')
            for actor in ia.get_movie(ia.search_movie(command)[0].movieID)['actors'][0:15]:
                a=a+actor['name']+', '
            talk(a)
        elif ('plot' in command) or ('story' in command):
            ia = IMDb()
            if 'what is the story of the movie ' in command:
                command=command.replace('what is the story of the movie ', '')
            elif 'what is story of the movie ' in command:
                command=command.replace('what is story of the movie ', '')
            elif 'what is story of movie ' in command:
                command=command.replace('what is story of movie ', '')
            elif 'what is the story of movie ' in command:
                command=command.replace('what is the story of movie ', '')
            elif 'story of the movie ' in command:
                command=command.replace('story of the movie ', '')
            elif 'story of movie ' in command:
                command=command.replace('story of movie ', '')
            elif 'story of ' in command:
                command=command.replace('story of ', '')
            elif 'what is the plot of the movie ' in command:
                command=command.replace('what is the plot of the movie ', '')
            elif 'what is plot of the movie ' in command:
                command=command.replace('what is plot of the movie ', '')
            elif 'what is plot of movie ' in command:
                command=command.replace('what is plot of movie ', '')
            elif 'what is the plot of movie ' in command:
                command=command.replace('what is the plot of movie ', '')
            elif 'plot of the movie ' in command:
                command=command.replace('plot of the movie ', '')
            elif 'plot of movie ' in command:
                command=command.replace('plot of movie ', '')
            elif 'plot of ' in command:
                command=command.replace('plot of ', '')    
            p=ia.get_movie(ia.search_movie("command")[0].movieID)['plot']
            talk(p)
        else:
            talk('Please say the command again.')

run_amigo()
