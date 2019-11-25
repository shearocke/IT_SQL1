import sqlite3
import matplotlib.pyplot as plt

database = 'CrashStatsQLD.sqlite'  # create variable name for db

conn = sqlite3.connect(database)  # connect/open to db

record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                      "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2001' GROUP BY Crash_Police_Region LIMIT 5")
# execute the query for the database for each year

# Creating empty x and y lists
xlist = []
ylist = []

# for each row in the query combine the first column into the x list and combine the second column into the y list
for row in record:
    xlist.append(row[0])
    ylist.append(row[1])

# Sets the X and Y titles
plt.xlabel('Region')
plt.ylabel('Number of fatal crashes')

# Sets the title
plt.title('Fatal Crashes Involving Truck')

# Sets the bar graph values
plt.bar(xlist, ylist)

# Shows the graph
plt.show()
