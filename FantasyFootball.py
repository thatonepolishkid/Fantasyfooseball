
#Create a program that maps the key statistics of players in the Quarterback, Runningback, and Widereciever positions.
#Then try to map these datapoints according to each year, and find any corrilations between years in league and increase in production.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import re



pd.options.mode.chained_assignment = None  # default='warn'

player = {}
#BeautifulSoup syntax for scaping information, (find a way to iterate through the webpages changing only the year somehow)
#Repeat this for passing players 

#Current in use Scrape
rush_URL_2022 = 'https://www.pro-football-reference.com/years/2022/rushing.htm'


"""rush_URL_2021 = 'https://www.pro-football-reference.com/years/2021/rushing.htm'
rush_URL_2020 = 'https://www.pro-football-reference.com/years/2020/rushing.htm'
rush_URL_2019 = 'https://www.pro-football-reference.com/years/2019/rushing.htm'
rush_URL_2018 = 'https://www.pro-football-reference.com/years/2018/rushing.htm'"""
    
#Current in use Scrape    
rush_HTML_2022 = urlopen(rush_URL_2022)


"""rush_HTML_2021 = urlopen(rush_URL_2021)
rush_HTML_2020 = urlopen(rush_URL_2020)
rush_HTML_2019 = urlopen(rush_URL_2019)
rush_HTML_2018 = urlopen(rush_URL_2018)"""

#Current in use scrape
rush_stats_2022 = BeautifulSoup(rush_HTML_2022, 'html.parser')


"""rush_stats_2021 = BeautifulSoup(rush_HTML_2021, 'html.parser')
rush_stats_2020 = BeautifulSoup(rush_HTML_2020, 'html.parser')
rush_stats_2019 = BeautifulSoup(rush_HTML_2019, 'html.parser')
rush_stats_2018 = BeautifulSoup(rush_HTML_2018, 'html.parser')"""


#Finds table headers
col_head_rush_2022 = rush_stats_2022.findAll('tr')[1]
col_head_rush_2022 = [i.getText() for i in col_head_rush_2022.findAll('th')]

#Gets table rows
rows2022 = rush_stats_2022.findAll('tr')[1:]

#Gets stats from each row
rb_stats = []
for i in range(len(rows2022)):
    rb_stats.append([col.getText() for col in rows2022[i].findAll('td')])
print(rb_stats[1])


#Implement variety and clean up for wide recievers and quarterbacks
"""runningback_url = 'https://www.pro-football-reference.com/years/2018/rushing.htm'
quarterback_url = 'https://www.pro-football-reference.com/years/2018/receiving.htm'
widereciever_url = 'https://www.pro-football-reference.com/years/2018/passing.htm'"""


#Implementing this so that I can iterate through the Years and compare yearly stats instead of players head to head.(Eventually)
"""years = []
runningback_year_dict = {}
quarterback_year_dict = {}
widereciever_year_dict = {}


year = int(runningback_url[45:49:])

#Simple while loop that rewrites the year#
while year <= 2022:
    years.append(year)
    year += 1

#Iterates through and renames the links to be scraped.
for year in years:
    new_widereciever_url = re.sub(r'2018', str(year), widereciever_url)
    new_quarterback_url = re.sub(r'2018', str(year), quarterback_url)
    new_runningback_url = re.sub(r'2018', str(year), runningback_url)
    
    runningback_year_dict[str(year)] = new_runningback_url
    quarterback_year_dict[str(year)] = new_quarterback_url
    widereciever_year_dict[str(year)] = new_widereciever_url


#Not in use yet but in the future maybe create a list that can be iterated through and compared ??
rush_2018 = runningback_year_dict["2018"]
rush_2019 = runningback_year_dict["2019"]
rush_2020 = runningback_year_dict["2020"]
rush_2021 = runningback_year_dict["2021"]
rush_2022 = runningback_year_dict["2022"]
reciever_2018 = widereciever_year_dict["2018"]
reciever_2019 = widereciever_year_dict["2019"]
reciever_2020 = widereciever_year_dict["2020"]
reciever_2021 = widereciever_year_dict["2021"]
reciever_2022 = widereciever_year_dict["2022"]
quarterback_2018 = quarterback_year_dict["2018"]
quarterback_2019 = quarterback_year_dict["2019"]
quarterback_2020 = quarterback_year_dict["2020"]
quarterback_2021 = quarterback_year_dict["2021"]
quarterback_2022 = quarterback_year_dict["2022"]
"""



data = pd.DataFrame(rb_stats, columns=col_head_rush_2022[1:])
#This removes the first row which had none and NaN values.
data = data.drop(labels=0, axis=0) 

#Filtering out all players who are QB's but also rushed
data.drop(data[data['Pos'] == 'QB'].index, inplace = True)

#Shrinking DataFrame
categories = ['Age', 'Att', 'Yds', 'TD', 'Y/A', 'Y/G', 'Fmb']
data_radar = data[['Player', 'Tm'] + categories]

#Objects into ints/floats
for i in categories:
    data_radar[i] = pd.to_numeric(data[i])

#cleaning up post season acheivements
data_radar['Player'] = data_radar['Player'].str.replace('*', '')
data_radar['Player'] = data_radar['Player'].str.replace('+', '')

#Filtering... This is needed for when I compare by age but at the moment, not being used.?
row_names = data_radar.index
data_radar.drop(data_radar[data_radar["Age"] == None].index, inplace = True)

#Setting defaults for Matplot
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 16
mpl.rcParams['axes.linewidth'] = 0
mpl.rcParams['xtick.major.pad'] = 15

#Team colors based off of NFL website
team_colors = {'ARI':'#97233f', 'ATL':'#a71930', 'BAL':'#241773', 'BUF':'#00338d', 'CAR':'#0085ca', 
               'CHI':'#0b162a', 'CIN':'#fb4f14', 'CLE':'#311d00', 'DAL':'#041e42', 'DEN':'#002244', 
               'DET':'#0076b6', 'GNB':'#203731', 'HOU':'#03202f', 'IND':'#002c5f', 'JAX':'#006778', 
               'KAN':'#e31837', 'LAC':'#002a5e', 'LAR':'#003594', 'MIA':'#008e97', 'MIN':'#4f2683', 
               'NWE':'#002244', 'NOR':'#d3bc8d', 'NYG':'#0b2265', 'NYJ':'#125740', 'OAK':'#000000', 
               'PHI':'#004c54', 'PIT':'#ffb612', 'SFO':'#aa0000', 'SEA':'#002244', 'TAM':'#d50a0a', 
               'TEN':'#0c2340', 'WAS':'#773141'
               }

#Even parts of a circle
offset = np.pi/7
angles = np.linspace(0, 2*np.pi, len(categories) + 1) + offset

#filtering by RB's who have over 400 yds
data_radar_filtered = data_radar[data_radar['Yds'] > 400]


#Helper function to get player data based on team
def get_rb_data(data, team):
    return np.asarray(data[data['Tm'] == team])[0]

#creating the function to plot data
def create_radar_chart(ax, angles, player_data, color='blue'):
    

        #This is where I think the Error is occuring that I am not properly filling in the information into the graph.


        ax.plot(angles, np.append(player_data[-(len(angles)-1):],
                    player_data[-(len(angles)-1)]), color='red', linewidth=2)
        ax.fill(angles, np.append(player_data[-(len(angles)-1):],
                    player_data[-(len(angles)-1)]), color=color, alpha=0.2)
        
        #Set category labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)

        #Removes radial labels
        ax.set_yticklabels([])

        #Populates the header with player Name
        ax.text(np.pi/2, 1.7, player_data[0], ha='center', va='center', size=18, color=color)

        #White grid
        ax.grid(color='white', linewidth=1.5)

        #Sets axis limits
        ax.set(xlim=(0, 2*np.pi), ylim=(0, 1))

        return ax


#Starting with the AFC East
#Creates the figure
fig = plt.figure(figsize=(8, 8), facecolor='white')
# Add subplots
ax1 = fig.add_subplot(221, projection='polar', facecolor='#ededed')
ax2 = fig.add_subplot(222, projection='polar', facecolor='#ededed')
ax3 = fig.add_subplot(223, projection='polar', facecolor='#ededed')
ax4 = fig.add_subplot(224, projection='polar', facecolor='#ededed')
# Adjust space between subplots
plt.subplots_adjust(hspace=0.8, wspace=0.5)
# Get RB data
pt_data = get_rb_data(data_radar_filtered, 'NWE')
jet_data = get_rb_data(data_radar_filtered, 'NYJ')
mia_data = get_rb_data(data_radar_filtered, 'MIA')
buf_data = get_rb_data(data_radar_filtered, 'BUF')
# Plot RB data
ax1 = create_radar_chart(ax1, angles, pt_data, team_colors['NWE'])
ax2 = create_radar_chart(ax2, angles, jet_data, team_colors['NYJ'])
ax3 = create_radar_chart(ax3, angles, mia_data, team_colors['MIA'])
ax4 = create_radar_chart(ax4, angles, buf_data, team_colors['BUF'])
plt.show()
