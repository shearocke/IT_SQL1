import sqlite3
import matplotlib.pyplot as plt
from guizero import App, PushButton

database = ''  # create variable name for db

conn = sqlite3.connect(database)

#`vehicleinvolvement`(`Crash_Year`, `Crash_Police_Region`, `Crash_Severity`, `Involving_Motorcycle_Moped`,
 #                    `Involving_Truck`, `Involving_Bus`, `Count_Crashes`, `Count_Casualty_Fatality`,
  #                   `Count_Casualty_Hospitalised`, `Count_Casualty_MedicallyTreated`, `Count_Casualty_MinorInjury`,
   #                  `Count_Casualty_All`);