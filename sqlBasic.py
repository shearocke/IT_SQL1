import sqlite3
from guizero import App, PushButton

database = 'world.db'  # create variable name for db

conn = sqlite3.connect(database)  # connect/open to db

app = App()


def select1():
    record = conn.execute("SELECT Name, Population, IndepYear, LifeExpectancy FROM Country WHERE IndepYear > 1900 ORDER BY name")
    printer(record)


button = PushButton(app, command=select1)


def select2():
    record = conn.execute('SELECT Name, Population FROM Country WHERE Population < 1000000;')
    printer(record)


button2 = PushButton(app, command=select2)


def select3():
    record = conn.execute('SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy > 60;')
    printer(record)


button3 = PushButton(app, command=select3)


def select4():
    record = conn.execute("SELECT Name, Continent, GovernmentForm, LifeExpectancy FROM Country WHERE GovernmentForm = 'Republic' ORDER BY name;")
    printer(record)


button4 = PushButton(app, command=select4)



def printer(record):
    for row in record:
        print(row)


app.display()
conn.close()
