import sqlite3
import matplotlib.pyplot as plt

database = 'BabyNames2018.db'  # create variable name for db

conn = sqlite3.connect(database)  # connect/open to db

record = conn.execute("SELECT Girl_Names, Count_of_Girl_Names FROM babyNames2018")

xlist = []
ylist = []


for row in record:
    xlist.append(row[0])
    ylist.append(row[1])

plt.xlabel('Names')
plt.ylabel('Number of names')

plt.title('Top 100 Girl names')


graph = plt.barh(xlist, ylist)


plt.show()
