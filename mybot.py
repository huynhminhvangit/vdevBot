import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
# Loop
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Vang"
    elif "today" in you:
        today = date.today()
        now = datetime.now()
        robot_brain = today.strftime("Now is %B %d, %Y") + now.strftime(" %H hours %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "Goodbye, Vang"
        break
    else:
        robot_brain = "You are very handsome"


    # log robot_brain
    print(robot_brain)

    # initial engine
    robot_mouth = pyttsx3.init()
    # setting voice
    # getting details of current voice
    voices = robot_mouth.getProperty('voices')
    # changing index, changes voices. o for male
    robot_mouth.setProperty('voice', voices[1].id)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()