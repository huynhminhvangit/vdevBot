import speech_recognition
import pyttsx3
import openai
import os
from dotenv import load_dotenv
from googletrans import Translator

detector = Translator()

load_dotenv()

MY_API_KEY = os.getenv("api_key")
openai.api_key = MY_API_KEY


robot_ear = speech_recognition.Recognizer()
# Loop
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio, language="vi-VN")
    except:
        you = ""

    if you == "":
        robot_brain = "Tôi không hiểu bạn nói gì, vui lòng nói lại"
    elif "tạm biệt" in you:
        robot_brain = "Chúc bạn một ngày tốt lành"
        # initial engine
        robot_mouth = pyttsx3.init()
        # setting voice
        # getting details of current voice
        voices = robot_mouth.getProperty('voices')
        # changing index, changes voices. o for male
        robot_mouth.setProperty('voice', voices[1].id)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        model_engine = "gpt-3.5-turbo"
        print(you)
        prompt = you

        completion = openai.ChatCompletion.create(
            model=model_engine,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        robot_brain = completion.choices[0].message.content

    # log robot_brain
    print(robot_brain)
    
    dec_lan = detector.detect(robot_brain)
    index = 1
    if dec_lan.lang =="en" and dec_lan.confidence == 1:
        index = 0

    # initial engine
    robot_mouth = pyttsx3.init()
    # setting voice
    # getting details of current voice
    voices = robot_mouth.getProperty('voices')
    # changing index, changes voices. o for male
    robot_mouth.setProperty('voice', voices[index].id)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
