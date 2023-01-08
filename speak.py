# import libs
import pyttsx3

# initial engine
robot_mouth = pyttsx3.init()
# getting brain
robot_brain = "Hello Vang, How are you doing?"
# setting voice
# getting details of current voice
voices = robot_mouth.getProperty('voices')
# changing index, changes voices. o for male 
robot_mouth.setProperty('voice', voices[1].id)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()