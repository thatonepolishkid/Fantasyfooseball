import sqlite3
import pandas as pd


connection = sqlite3.connect('footballstats.database.windows.net')


print("Connection with Football_DB initiated.")

# Creation of Database - now commented out
passer_stats = pd.read_excel('passer_stats.xlsx')
receiver_stats = pd.read_excel('receiver_stats.xlsx')
rush_stats = pd.read_excel('rush_stats.xlsx')

# Writes excel files into sqlite
passer_stats.to_sql('QuarterBack_Stats', connection, if_exists='replace', index=False)
rush_stats.to_sql('RunningBack_Stats', connection, if_exists='replace', index=False)
receiver_stats.to_sql('WideReceiver_Stats', connection, if_exists='replace', index=False)



connection.close()
print("Connection with Football_DB closed.")