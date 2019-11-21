import sqlite3
import matplotlib.pyplot as plt
from guizero import App, PushButton

database = 'CrashStatsQLD.sqlite'  # create variable name for db

conn = sqlite3.connect(database) # connect/open to db

app = App()


def select1():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2001'")
    printer(record)


button = PushButton(app, command=select1)


def select2():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2002'")
    printer(record)


button2 = PushButton(app, command=select2)


def select3():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2003'")
    printer(record)


button3 = PushButton(app, command=select3)


def select4():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2004'")
    printer(record)

button4 = PushButton(app, command=select4)


def select5():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2005'")
    printer(record)

button5 = PushButton(app, command=select5)


def select4():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2006'")
    printer(record)

button4 = PushButton(app, command=select4)

def printer(record):
    for row in record:
        print(row)

app.display()
conn.close()

# `vehicleinvolvement`(`Crash_Year`, `Crash_Police_Region`, `Crash_Severity`, `Involving_Motorcycle_Moped`,
#                    `Involving_Truck`, `Involving_Bus`, `Count_Crashes`, `Count_Casualty_Fatality`,
#                   `Count_Casualty_Hospitalised`, `Count_Casualty_MedicallyTreated`, `Count_Casualty_MinorInjury`,
#                   `Count_Casualty_All`);
