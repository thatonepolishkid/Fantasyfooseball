
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
rush_URL = 'https://www.pro-football-reference.com/years/2022/rushing.htm'
pass_URL = 'https://www.pro-football-reference.com/years/2018/passing.htm'
rec_URL = 'https://www.pro-football-reference.com/years/2018/receiving.htm'
#Current in use Scrape    
rush_HTML_2022 = urlopen(rush_URL)



#Current in use scrape
rush_stats_2022 = BeautifulSoup(rush_HTML_2022, 'html.parser')


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


#Current Bit of code that I have been working on Still commented out until I properly implement it. Everything works, however I need to do some renaming and commits for transforming the variables to match.
#Most of this was done on VScode so I have to double check that it works here as well.
'''year = int(rush_url[45:49:]) 

#Iterates through and creates a list based on the years
def year_creation(start_year, end_year):
    return list(range(start_year, end_year + 1))
years = year_creation(2018, 2023)

#creation of dictionaries for each category of player
rush_year_dict = {}
pass_year_dict = {}
receiver_year_dict = {}


#loops through and rewrites the url string for each year
for year in years:
    new_receiver_url = re.sub(r'2018', str(year), receiving_url)
    new_passing_url = re.sub(r'2018', str(year), pass_url)
    new_rush_url = re.sub(r'2018', str(year), rush_url)

    rush_year_dict[str(year)] = new_rush_url
    pass_year_dict[str(year)] = new_passing_url
    receiver_year_dict[str(year)] = new_receiver_url


#This works to create the scraped url
def soupify(year_dict):
    return BeautifulSoup(urlopen(year_dict), 'html.parser')

#Defines empty dictionaries that will hold the information scraped from the website.
scraped_websites_rush = {}
scraped_websites_pass = {}
scraped_websites_receiver = {}

#loops through the years dictionary to assign a year to each website scraped(matching the url)
for year in years:
    scraped_rush_url = soupify(rush_year_dict[str(year)])
    scraped_pass_url = soupify(pass_year_dict[str(year)])
    scraped_receiver_url = soupify(receiver_year_dict[str(year)])
    
    scraped_websites_rush[str(year)] = scraped_rush_url #changed scraped_websites_rush to rush_year_dict
    scraped_websites_pass[str(year)] = scraped_pass_url #changed scraped_websites_pass to pass_year_dict
    scraped_websites_receiver[str(year)] = scraped_receiver_url #changed scraped_websites_receiver to receiver_year_dict
    time.sleep(1)
    


Breakdown of what this function should do:

1.) Take in a parameter 'scraped_website' a dictionary and iterate through each value of a given dictionary
for each value in 'scraped_website' use the pd.DataFrame() built in function of pandas to 
create a table of data and return it.


    

#Takes param of identified webpage to be scraped 
def column_finder(website_data, x):
    col_scraped = website_data.findAll('tr')[x]
    col_scraped = [i.getText() for i in col_scraped.findAll('th')] 
    return col_scraped

def row_finder(website_data):
    rows_scraped = website_data.findAll('tr')[1:]
    rows_scraped = [[col.getText() for col in rows_scraped[i].findAll('td')]
                    for i in range(len(rows_scraped))]
    return rows_scraped

#find a way to perhaps send these dataframes to an SQL Database for easier/stored access and not as many
#queries to the nfl page, resulting in an automatic page timeout.









#Quick check to see if the functions work WHICH THEY DOOOOO!!!!
rush_data_2018 = pd.DataFrame(row_finder(scraped_websites_rush['2018']), columns=column_finder(scraped_websites_rush['2018'], 1)[1:])
rush_data_2019 = pd.DataFrame(row_finder(scraped_websites_rush['2019']), columns=column_finder(scraped_websites_rush['2019'], 1)[1:])
rush_data_2020 = pd.DataFrame(row_finder(scraped_websites_rush['2020']), columns=column_finder(scraped_websites_rush['2020'], 1)[1:])
rush_data_2021 = pd.DataFrame(row_finder(scraped_websites_rush['2021']), columns=column_finder(scraped_websites_rush['2021'], 1)[1:])
rush_data_2022 = pd.DataFrame(row_finder(scraped_websites_rush['2022']), columns=column_finder(scraped_websites_rush['2022'], 1)[1:])
pass_data_2018 = pd.DataFrame(row_finder(scraped_websites_pass['2018']), columns=column_finder(scraped_websites_pass['2018'], 0)[1:])
pass_data_2019 = pd.DataFrame(row_finder(scraped_websites_pass['2019']), columns=column_finder(scraped_websites_pass['2019'], 0)[1:])
pass_data_2020 = pd.DataFrame(row_finder(scraped_websites_pass['2020']), columns=column_finder(scraped_websites_pass['2020'], 0)[1:])
pass_data_2021 = pd.DataFrame(row_finder(scraped_websites_pass['2021']), columns=column_finder(scraped_websites_pass['2021'], 0)[1:])
pass_data_2022 = pd.DataFrame(row_finder(scraped_websites_pass['2022']), columns=column_finder(scraped_websites_pass['2022'], 0)[1:])
rec_data_2018 = pd.DataFrame(row_finder(scraped_websites_receiver['2018']), columns=column_finder(scraped_websites_receiver['2018'], 0)[1:])
rec_data_2019 = pd.DataFrame(row_finder(scraped_websites_receiver['2019']), columns=column_finder(scraped_websites_receiver['2019'], 0)[1:])
rec_data_2020 = pd.DataFrame(row_finder(scraped_websites_receiver['2020']), columns=column_finder(scraped_websites_receiver['2020'], 0)[1:])
rec_data_2021 = pd.DataFrame(row_finder(scraped_websites_receiver['2021']), columns=column_finder(scraped_websites_receiver['2021'], 0)[1:])
rec_data_2022 = pd.DataFrame(row_finder(scraped_websites_receiver['2022']), columns=column_finder(scraped_websites_receiver['2022'], 0)[1:])



#cleans up the * and + characters as well as introducing a new column with the value of year.
def data_cleanup(data_set, year):
    data_set['Player'] = data_set['Player'].str.replace('*', '')
    data_set['Player'] = data_set['Player'].str.replace('+', '')
    data_set['Year'] = year
    data_set = (data_set.dropna()).reset_index(drop=True)
    return data_set
print(data_cleanup(rush_data_2018, 2018).head())'''






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

#Changes values into a percentage so that they properly plot within the scope of the Radar Chart
for i in categories:
    data_radar_filtered[i + '_Rank'] = data_radar_filtered[i].rank(pct=True)

#Helper function to get player data based on team
def get_rb_data(data, team):
    return np.asarray(data[data['Tm'] == team])[0]

#creating the function to plot data
def create_radar_chart(ax, angles, player_data, color='blue'):
    
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
