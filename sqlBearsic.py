import sqlite3
import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)

database = 'world.db'

conn = sqlite3.connect(database)

#record = conn.execute('SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy > 80 ORDER BY LifeExpectancy;')
#record = conn.execute("SELECT Name, HeadOfState, GovernmentForm FROM Country WHERE GovernmentForm = 'Republic' ORDER BY Name")
#record = conn.execute("SELECT Name, GNP, Population FROM Country WHERE GNP > 10000 ORDER BY GNP")
#record = conn.execute("SELECT Name, Population, SurfaceArea FROM Country WHERE Population > 1000000000 ORDER BY Population")
record = conn.execute("SELECT Name, Population, SurfaceArea FROM Country WHERE SurfaceArea < 10000000 AND Population > 1000000000")
for row in record:
    print(row)
    #tts.say(row)
    #tts.runAndWait()

