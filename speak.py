# import libs
import pyttsx3

# initial engine
engine = pyttsx3.init()
# setting voice
# getting details of current voice
voices = engine.getProperty('voices')
# changing index, changes voices. o for male 
engine.setProperty('voice', voices[1].id)
engine.say("Hello Vang, How are you?")
engine.runAndWait()