import sqlite3
import matplotlib.pyplot as plt
from guizero import App, Box, PushButton, Text

database = 'CrashStatsQLD.sqlite'  # create variable name for db

conn = sqlite3.connect(database)  # connect/open to db

app = App(layout="grid")  # sets the application layout to grid

fatalCrash_box = Box(app, grid=[0, 1, 2, 1], border=True)  # creates a box with a border, grid reference that spans specified amount of columns/rows
Text(fatalCrash_box, text="Sum of Fatal Accidents by Year")  # adds text to the box

graph_box = Box(app, grid=[3, 1, 2, 1], border=True)  # creates a box with a border in the grid reference that spans specified amount of columns/rows
Text(graph_box, text="Graphs of the Yearly Fatal Accidents Involving Trucks by Region") #adds text to the box


def select1():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2001'")
    printer(record)


button = PushButton(app, grid=[0, 2], text="2001 Fatal Crashes", command=select1)


def select2():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2002'")
    printer(record)


button2 = PushButton(app, grid=[0, 3], text="2002 Fatal Crashes", command=select2)


def select3():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2003'")
    printer(record)


button3 = PushButton(app, grid=[0, 4], text="2003 Fatal Crashes", command=select3)


def select4():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2004'")
    printer(record)


button4 = PushButton(app, grid=[0, 5], text="2004 Fatal Crashes", command=select4)


def select5():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2005'")
    printer(record)


button5 = PushButton(app, grid=[0, 6], text="2005 Fatal Crashes", command=select5)


def select6():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2006'")
    printer(record)


button6 = PushButton(app, grid=[0, 7], text="2006 Fatal Crashes", command=select6)


def select7():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2007'")
    printer(record)


button7 = PushButton(app, grid=[0, 8], text="2007 Fatal Crashes", command=select7)


def select8():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2008'")
    printer(record)


button8 = PushButton(app, grid=[0, 9], text="2008 Fatal Crashes", command=select8)


def select9():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2009'")
    printer(record)


button9 = PushButton(app, grid=[0, 10], text="2009 Fatal Crashes", command=select9)


def select10():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2009'")
    printer(record)


button10 = PushButton(app, grid=[1, 2], text="2010 Fatal Crashes", command=select10)


def select11():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2011'")
    printer(record)


button11 = PushButton(app, grid=[1, 3], text="2011 Fatal Crashes", command=select11)


def select12():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2012'")
    printer(record)


button12 = PushButton(app, grid=[1, 4], text="2012 Fatal Crashes", command=select12)


def select13():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2013'")
    printer(record)


button13 = PushButton(app, grid=[1, 5], text="2013 Fatal Crashes", command=select13)


def select14():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2014'")
    printer(record)


button14 = PushButton(app, grid=[1, 6], text="2014 Fatal Crashes", command=select14)


def select15():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2015'")
    printer(record)


button15 = PushButton(app, grid=[1, 7],  text="2015 Fatal Crashes", command=select15)


def select16():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2016'")
    printer(record)


button16 = PushButton(app, grid=[1, 8], text="2016 Fatal Crashes", command=select16)


def select17():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2017'")
    printer(record)


button17 = PushButton(app, grid=[1, 9], text="2017 Fatal Crashes", command=select17)


def select18():
    record = conn.execute("SELECT sum(Count_Casualty_Fatality) FROM vehicleinvolvement WHERE Crash_Year = '2018'")
    printer(record)


button18 = PushButton(app, grid=[1, 10], text="2018 Fatal Crashes", command=select18)


def printer(record):
    for row in record:
        print(row)


def graph1():
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


button19 = PushButton(app, grid=[3, 2], text="2001", command=graph1)


def graph2():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2002' GROUP BY Crash_Police_Region LIMIT 5")
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


button20 = PushButton(app, grid=[3, 3], text="2002", command=graph2)


def graph3():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2003' GROUP BY Crash_Police_Region LIMIT 5")
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


button21 = PushButton(app, grid=[3, 4], text="2003", command=graph3)


def graph4():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2004' GROUP BY Crash_Police_Region LIMIT 5")
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


button22 = PushButton(app, grid=[3, 5], text="2004", command=graph4)


def graph5():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2005' GROUP BY Crash_Police_Region LIMIT 5")
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


button23 = PushButton(app, grid=[3, 6], text="2005", command=graph5)


def graph6():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2006' GROUP BY Crash_Police_Region LIMIT 5")
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


button24 = PushButton(app, grid=[3, 7], text="2006", command=graph6)


def graph7():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2007' GROUP BY Crash_Police_Region LIMIT 5")
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


button25 = PushButton(app, grid=[3, 8], text="2007", command=graph7)


def graph8():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2008' GROUP BY Crash_Police_Region LIMIT 5")
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


button26 = PushButton(app, grid=[3, 9], text="2008", command=graph8)


def graph9():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2009' GROUP BY Crash_Police_Region LIMIT 5")
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


button27 = PushButton(app, grid=[3, 10], text="2009", command=graph9)


def graph10():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2010' GROUP BY Crash_Police_Region LIMIT 5")
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


button28 = PushButton(app, grid=[4, 2], text="2010", command=graph10)


def graph11():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2011' GROUP BY Crash_Police_Region LIMIT 5")
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


button29 = PushButton(app, grid=[4, 3], text="2011", command=graph11)


def graph12():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2012' GROUP BY Crash_Police_Region LIMIT 5")
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


button30 = PushButton(app, grid=[4, 4], text="2012", command=graph12)


def graph13():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2013' GROUP BY Crash_Police_Region LIMIT 5")
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


button31 = PushButton(app, grid=[4, 5], text="2013", command=graph13)


def graph14():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2014' GROUP BY Crash_Police_Region LIMIT 5")
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


button32 = PushButton(app, grid=[4, 6], text="2014", command=graph14)


def graph15():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2015' GROUP BY Crash_Police_Region LIMIT 5")
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


button33 = PushButton(app, grid=[4, 7], text="2015", command=graph15)


def graph16():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2016' GROUP BY Crash_Police_Region LIMIT 5")
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


button34 = PushButton(app, grid=[4, 8], text="2016", command=graph16)


def graph17():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2017' GROUP BY Crash_Police_Region LIMIT 5")
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


button35 = PushButton(app, grid=[4, 9], text="2017", command=graph17)


def graph18():
    record = conn.execute("SELECT Crash_Police_Region, sum(Count_Casualty_Fatality) FROM vehicleinvolvement "
                          "WHERE Involving_Truck = 'Yes' AND Crash_Year = '2018' GROUP BY Crash_Police_Region LIMIT 5")
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


button36 = PushButton(app, grid=[4, 10], text="2018", command=graph18)

app.display()
conn.close()

# `vehicleinvolvement`(`Crash_Year`, `Crash_Police_Region`, `Crash_Severity`, `Involving_Motorcycle_Moped`,
#                    `Involving_Truck`, `Involving_Bus`, `Count_Crashes`, `Count_Casualty_Fatality`,
#                   `Count_Casualty_Hospitalised`, `Count_Casualty_MedicallyTreated`, `Count_Casualty_MinorInjury`,
#                   `Count_Casualty_All`);
