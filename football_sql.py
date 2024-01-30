import sqlite3
import pandas as pd


connection = sqlite3.connect('footballstats.database.windows.net')

# Creates a pointer for looking inside the SQLite DB
con = connection.cursor()

# Creation of Database - now commented out
'''passer_stats = pd.read_excel('passer_stats.xlsx')
receiver_stats = pd.read_excel('receiver_stats.xlsx')
rush_stats = pd.read_excel('rush_stats.xlsx')

passer_stats.to_sql('QuarterBack_Stats', connection, if_exists='replace', index=False)
rush_stats.to_sql('RunningBack_Stats', connection, if_exists='replace', index=False)
receiver_stats.to_sql('WideReceiver_Stats', connection, if_exists='replace', index=False)
'''

# Tested to see the functionality of the method execute()
con.execute("SELECT * FROM RunningBack_Stats WHERE year=2020")
print(con.fetchall())

# Converting SQLite DB back into pandas df to confirm things work in a later query
'''df = pd.read_sql_query("SELECT * FROM RunningBack_Stats", connection)

print(df.head())'''




connection.close()
print("Connection with Football_DB closed.")