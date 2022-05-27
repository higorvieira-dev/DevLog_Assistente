from time import sleep
import speech_recognition as sr # recognise 
import keyboard  
import Devlog

recognizer = sr.Recognizer()


BOT_NAMES = ['devlog', 'tedlog', 'deblog', "mommy" ]

def record_audio():
  with sr.Microphone() as source: 
    audio = recognizer.listen(source, None, 3)  
    voice_data = ''

    try:
      voice_data = recognizer.recognize_google(audio, language="en-US").lower()
    except sr.UnknownValueError: 
      print()
    except sr.RequestError:
      print('Serviço offline')

    print(">>", voice_data) 
    for bot_name_variation in BOT_NAMES:
      if (bot_name_variation in voice_data):
        Devlog.listen()
        break


while True:
  sleep(0.05) 
  if keyboard.is_pressed('ctrl+alt+m'):
    Devlog.listen()
  sleep(0.05)

