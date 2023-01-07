# import libs
import pyttsx3

# initial engine
robotMouth = pyttsx3.init()
# getting brain
robotBrain = "Hello Vang, How are you doing?"
# setting voice
# getting details of current voice
voices = robotMouth.getProperty('voices')
# changing index, changes voices. o for male 
robotMouth.setProperty('voice', voices[1].id)
robotMouth.say(robotBrain)
robotMouth.runAndWait()