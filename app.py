# Create a program that writes football statistics into an excel files. 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

pd.options.mode.chained_assignment = None  # default='warn'

###!!! Ive fucked up the naming of Receivers and Quarterbacks when I renamed the Dictionaries. Look to fix that next time I work on this.

#creation of dictionaries for each category of player
rush_year_dict = {}
pass_year_dict = {}
receiver_year_dict = {}

#Iterates through and creates a list based on the years
def year_creation(start_year, end_year):
    return list(range(start_year, end_year + 1))
years = year_creation(2018, 2023)

#cleans up the * and + characters as well as introducing a new column with the value of year.
def data_cleanup(data_set, year):
    data_set['Player'] = data_set['Player'].str.replace('*', '')
    data_set['Player'] = data_set['Player'].str.replace('+', '')
    data_set['Year'] = year
    data_set = (data_set.dropna()).reset_index(drop=True)
    return data_set

#Implement variety and clean up for wide recievers and quarterbacks
runningback_url = 'https://www.pro-football-reference.com/years/2018/rushing.htm'
widereceiver_url = 'https://www.pro-football-reference.com/years/2018/receiving.htm'
quarterback_url = 'https://www.pro-football-reference.com/years/2018/passing.htm'


#This works to create the scraped url
def soupify(year_dict):
    return BeautifulSoup(urlopen(year_dict), 'html.parser')


#loops through and rewrites the url string for each year
for year in years:
    new_receiver_url = re.sub(r'2018', str(year), widereceiver_url)
    new_passing_url = re.sub(r'2018', str(year), quarterback_url)
    new_rush_url = re.sub(r'2018', str(year), runningback_url)
    rush_year_dict[str(year)] = new_rush_url
    pass_year_dict[str(year)] = new_passing_url
    receiver_year_dict[str(year)] = new_receiver_url


#Defines empty dictionaries that will hold the information scraped from the website.
scraped_websites_rush = {}
scraped_websites_pass = {}
scraped_websites_receiver = {}


#loops through the years dictionary to assign a year to each website scraped(matching the url)
#Iterates through and renames the links to be scraped.
for year in years:
    scraped_rush_url = soupify(rush_year_dict[str(year)])
    scraped_pass_url = soupify(pass_year_dict[str(year)])
    scraped_receiver_url = soupify(receiver_year_dict[str(year)])
    
    scraped_websites_rush[str(year)] = scraped_rush_url #changed scraped_websites_rush to rush_year_dict
    scraped_websites_pass[str(year)] = scraped_pass_url #changed scraped_websites_pass to pass_year_dict
    scraped_websites_receiver[str(year)] = scraped_receiver_url #changed scraped_websites_receiver to receiver_year_dict
    time.sleep(1)


'''Breakdown of what this function should do:
1.) Take in a parameter 'scraped_website' a dictionary and iterate through each value of a given dictionary
for each value in 'scraped_website' use the pd.DataFrame() built in function of pandas to 
create a table of data and return it.'''
    
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

# Transform each scraped website into a DataFrame
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

# Preliminary data cleanup for rushing data, and concat into one DF
rush_data_2018 = data_cleanup(rush_data_2018, 2018)
rush_data_2019 = data_cleanup(rush_data_2019, 2019)
rush_data_2020 = data_cleanup(rush_data_2020, 2020)
rush_data_2021 = data_cleanup(rush_data_2021, 2021)
rush_data_2022 = data_cleanup(rush_data_2022, 2022)
all_rush_data = pd.concat([rush_data_2018, rush_data_2019, rush_data_2020, rush_data_2021, rush_data_2022])

#Preliminary data cleanup for passing data, and concat into one DF
pass_data_2018 = data_cleanup(pass_data_2018, 2018)
pass_data_2019 = data_cleanup(pass_data_2019, 2019)
pass_data_2020 = data_cleanup(pass_data_2020, 2020)
pass_data_2021 = data_cleanup(pass_data_2021, 2021)
pass_data_2022 = data_cleanup(pass_data_2022, 2022)
all_pass_data = pd.concat([pass_data_2018, pass_data_2019, pass_data_2020, pass_data_2021, pass_data_2022])

#Preliminary data cleanup for receiving data, and concat into one DF
rec_data_2018 = data_cleanup(rec_data_2018, 2018)
rec_data_2019 = data_cleanup(rec_data_2019, 2019)
rec_data_2020 = data_cleanup(rec_data_2020, 2020)
rec_data_2021 = data_cleanup(rec_data_2021, 2021)
rec_data_2022 = data_cleanup(rec_data_2022, 2022)
all_receiver_data = pd.concat([rec_data_2018, rec_data_2019, rec_data_2020, rec_data_2021, rec_data_2022])

def to_excel(DataFrame, excel_file):
    DataFrame.to_excel(excel_file,
                             sheet_name='sheet1')

to_excel(all_rush_data, 'rush_stats.xlsx')
to_excel(all_pass_data, 'passer_stats.xlsx')
to_excel(all_receiver_data, 'receiver_stats.xlsx')

#Create a database with sql that can be queried for any one given stat based upon the years. I think this would make the whole 
#process much easier and I could just query based off of year.

#first create the sql database and restructure the data. Then try to index out of that - modifying data will most likely by 
#much different than modifying with pandas, so give it some time.
