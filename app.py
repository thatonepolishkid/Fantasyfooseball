"""Change this file into a file that scrapes stats from the internet and then writes it into a MS Excel file.
   Once it is written into the Excel spreadsheet then I can write it into an SQL Database, and Query from there.
   Repeat this process for each URL that is scraped in the original app."""
   
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
import pytest
import xlsxwriter



pd.options.mode.chained_assignment = None  # default='warn'

player = {}
#BeautifulSoup syntax for scaping information, (find a way to iterate through the webpages changing only the year somehow)
#repeat this for passing players 

#Current in use Scrape
rush_URL_2022 = 'https://www.pro-football-reference.com/years/2022/rushing.htm'


rush_URL_2021 = 'https://www.pro-football-reference.com/years/2021/rushing.htm'
rush_URL_2020 = 'https://www.pro-football-reference.com/years/2020/rushing.htm'
rush_URL_2019 = 'https://www.pro-football-reference.com/years/2019/rushing.htm'
rush_URL_2018 = 'https://www.pro-football-reference.com/years/2018/rushing.htm'

#Current in use Scrape    
rush_HTML_2022 = urlopen(rush_URL_2022)
rush_HTML_2021 = urlopen(rush_URL_2021)
rush_HTML_2020 = urlopen(rush_URL_2020)
rush_HTML_2019 = urlopen(rush_URL_2019)
rush_HTML_2018 = urlopen(rush_URL_2018)

#Current in use scrape
rush_stats_2022 = BeautifulSoup(rush_HTML_2022, 'html.parser')


rush_stats_2021 = BeautifulSoup(rush_HTML_2021, 'html.parser')
rush_stats_2020 = BeautifulSoup(rush_HTML_2020, 'html.parser')
rush_stats_2019 = BeautifulSoup(rush_HTML_2019, 'html.parser')
rush_stats_2018 = BeautifulSoup(rush_HTML_2018, 'html.parser')


#Finds table headers
col_head_rush_2022 = rush_stats_2022.findAll('tr')[1]
col_head_rush_2022 = [i.getText() for i in col_head_rush_2022.findAll('th')]

#Gets table rows
rows2022 = rush_stats_2022.findAll('tr')[1:]

rb_stats = [
    [col.getText() for col in rows2022[i].findAll('td')]
    for i in range(len(rows2022))
]
print(rb_stats[1])


#Implement variety and clean up for wide recievers and quarterbacks
runningback_url = 'https://www.pro-football-reference.com/years/2018/rushing.htm'
quarterback_url = 'https://www.pro-football-reference.com/years/2018/receiving.htm'
widereceiver_url = 'https://www.pro-football-reference.com/years/2018/passing.htm'


#Implementing this so that I can iterate through the Years and compare yearly stats instead of players head to head.(Eventually)
def year_creation(start_year, end_year):
    return list(range(start_year, end_year + 1))
years = year_creation(2018, 2023)
runningback_year_dict = {}
quarterback_year_dict = {}
widereceiver_year_dict = {}


year = int(runningback_url[45:49:])

'''#Simple while loop that rewrites the year#
while year <= 2022:
    years.append(year)
    year += 1'''

#Iterates through and renames the links to be scraped.
for year in years:
    new_widereceiver_url = re.sub(r'2018', str(year), widereceiver_url)
    new_quarterback_url = re.sub(r'2018', str(year), quarterback_url)
    new_runningback_url = re.sub(r'2018', str(year), runningback_url)

    runningback_year_dict[str(year)] = new_runningback_url
    quarterback_year_dict[str(year)] = new_quarterback_url
    widereceiver_year_dict[str(year)] = new_widereceiver_url


#Not in use yet but in the future maybe create a list that can be iterated through and compared ??
#use .int() to convert to int and increment, then return back with .str()
rush_2018 = runningback_year_dict["2018"]
rush_2019 = runningback_year_dict["2019"]
rush_2020 = runningback_year_dict["2020"]
rush_2021 = runningback_year_dict["2021"]
rush_2022 = runningback_year_dict["2022"]
receiver_2018 = widereceiver_year_dict["2018"]
receiver_2019 = widereceiver_year_dict["2019"]
receiver_2020 = widereceiver_year_dict["2020"]
receiver_2021 = widereceiver_year_dict["2021"]
receiver_2022 = widereceiver_year_dict["2022"]
quarterback_2018 = quarterback_year_dict["2018"]
quarterback_2019 = quarterback_year_dict["2019"]
quarterback_2020 = quarterback_year_dict["2020"]
quarterback_2021 = quarterback_year_dict["2021"]
quarterback_2022 = quarterback_year_dict["2022"]


#Combine all of the Dictionaries into more concise variables to iterate over the list.
rush_dicts = [rush_2018, rush_2019, rush_2020, rush_2021, rush_2022]
receiver_dicts = [receiver_2018, receiver_2019, receiver_2020, receiver_2021, receiver_2022]
quarterback_dicts = [quarterback_2018, quarterback_2019, quarterback_2020, quarterback_2021, quarterback_2022]

def pd_to_excel(dictionary, path):
   for dict in dictionary:
       data = pd.DataFrame(dict, columns=col_head_rush_2022[1:])