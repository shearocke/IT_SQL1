import sqlite3
import matplotlib.pyplot as plt
from guizero import App, PushButton

database = 'CrashStatsQLD.sqlite'  # create variable name for db

conn = sqlite3.connect(database) # connect/open to db

app = App()


def select1():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2001'")
    printer(record)


button = PushButton(app, text="2001 Fatal Crashes", command=select1)


def select2():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2002'")
    printer(record)


button2 = PushButton(app, text="2002 Fatal Crashes", command=select2)


def select3():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2003'")
    printer(record)


button3 = PushButton(app, text="2003 Fatal Crashes", command=select3)


def select4():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2004'")
    printer(record)


button4 = PushButton(app, text="2004 Fatal Crashes", command=select4)


def select5():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2005'")
    printer(record)


button5 = PushButton(app,  text="2005 Fatal Crashes", command=select5)


def select6():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2006'")
    printer(record)


button6 = PushButton(app, text="2006 Fatal Crashes", command=select6)


def select7():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2007'")
    printer(record)


button7 = PushButton(app, text="2007 Fatal Crashes", command=select7)


def select8():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2008'")
    printer(record)


button8 = PushButton(app, text="2008 Fatal Crashes", command=select8)


def select9():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2009'")
    printer(record)


button9 = PushButton(app, text="2009 Fatal Crashes", command=select9)


def select10():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2009'")
    printer(record)


button10 = PushButton(app, text="2010 Fatal Crashes", command=select10)


def select11():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2011'")
    printer(record)


button11 = PushButton(app, text="2011 Fatal Crashes", command=select11)


def select12():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2012'")
    printer(record)


button12 = PushButton(app, text="2012 Fatal Crashes", command=select12)


def select13():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2013'")
    printer(record)


button13 = PushButton(app, text="2013 Fatal Crashes", command=select13)


def select14():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2014'")
    printer(record)


button14 = PushButton(app, text="2014 Fatal Crashes", command=select14)


def select15():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2015'")
    printer(record)


button15 = PushButton(app,  text="2015 Fatal Crashes", command=select15)


def select16():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2016'")
    printer(record)


button16 = PushButton(app, text="2016 Fatal Crashes", command=select16)


def select17():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2017'")
    printer(record)


button17 = PushButton(app, text="2017 Fatal Crashes", command=select17)


def select18():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2018'")
    printer(record)


button18 = PushButton(app, text="2018 Fatal Crashes", command=select18)


def printer(record):
    for row in record:
        print(row)


app.display()
conn.close()

# `vehicleinvolvement`(`Crash_Year`, `Crash_Police_Region`, `Crash_Severity`, `Involving_Motorcycle_Moped`,
#                    `Involving_Truck`, `Involving_Bus`, `Count_Crashes`, `Count_Casualty_Fatality`,
#                   `Count_Casualty_Hospitalised`, `Count_Casualty_MedicallyTreated`, `Count_Casualty_MinorInjury`,
#                   `Count_Casualty_All`);
