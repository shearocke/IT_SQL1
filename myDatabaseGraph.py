import sqlite3
import matplotlib.pyplot as plt

database = 'world.db'  # create variable name for db

conn = sqlite3.connect(database)  # connect/open to db

record = conn.execute("SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy > 78.5 ORDER BY Name")

xlist = []
ylist = []


for row in record:
    xlist.append(row[0])
    ylist.append(row[1])

plt.ylabel('Country Name')
plt.xlabel('Life Expectancy')

plt.title('Countries with life expectancy greater than 78.5')

plt.barh(xlist, ylist)

plt.show()
