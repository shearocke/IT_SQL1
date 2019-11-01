import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)
tts.say("I'm blue, if i was green i would die")
tts.runAndWait()
