import sqlite3
import matplotlib.pyplot as plt

#Constants for fontsizing
SMALL_SIZE = 3
MEDIUM_SIZE = 8
DEFAULT_SIZE = 12

database = 'BabyNames2018.db'  # create variable name for db

conn = sqlite3.connect(database)  # connect/open to db

record = conn.execute("SELECT Girl_Names, Count_of_Girl_Names FROM babyNames2018")  # execute the query for the database

xlist = []
ylist = []

plt.rc('font', size=DEFAULT_SIZE)  # default fontsize
plt.rc('xtick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels

# for each row in the query, append the data of the first value for the xlist and the second value for the ylist
for row in record:
    xlist.append(row[0])
    ylist.append(row[1])

plt.xlabel('Names')
plt.ylabel('Number of names')

plt.title('Top 100 Girl names')

plt.barh(xlist, ylist, color='pink')

plt.show()
