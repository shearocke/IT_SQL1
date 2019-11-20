import sqlite3
import matplotlib.pyplot as plt

#Constants for fontsizing
MEDIUM_SIZE = 6.5
DEFAULT_SIZE = 12

database = 'BabyNames2018.db'  # create variable name for db

conn = sqlite3.connect(database)  # connect/open to db

record = conn.execute("SELECT Girl_Names, Count_of_Girl_Names FROM babyNames2018")  # execute the query for the database

xlist = []
ylist = []

plt.rc('font', size=DEFAULT_SIZE)  # default fontsize
plt.rc('xtick', labelsize=MEDIUM_SIZE)  # fontsize of the x tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)  # fontsize of the y tick labels

plt.xticks(rotation='vertical')  # rotates the x tick labels

# for each row in the query
for row in record:
    xlist.append(row[0])
    ylist.append(row[1])

# Sets the X and Y titles
plt.xlabel('Names')
plt.ylabel('Number of names')

# Sets the title
plt.title('Top 100 Girl Names')

# Sets the bar graph values and colour
plt.bar(xlist, ylist, color='pink')

# Shows the graph
plt.show()
