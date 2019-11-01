import sqlite3
import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)

database = 'world.db'

conn = sqlite3.connect(database)

record = conn.execute('SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy > 80 ORDER BY LifeExpectancy;')

for row in record:
    print(row)
    tts.say(row)
    tts.runAndWait()

