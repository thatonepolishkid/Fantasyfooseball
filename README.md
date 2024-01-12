# Fantasyfooseball
Attempting my first project to scrape data and form graphs dependent on players stats over a number of years.

Todo list: 
1. Get rid of unnecessary imports in main file, and focus all the imports into the requirements.txt file. (needed currently go as follows - Urllib.requests import urlopen, from bs4 import BeautifulSoup, pandas as pd, re, time, as well as whatever is needed 
for the SQL creation and querying)

2. Create SQL database and move the excel files there. (Start diving into Database creation and import files into the database)

3. Cleanup data in the SQL database, it doesn't look that pretty atm. (Use pandas to cleanup the indexing and make sure that all the data is an appropriate datatype - ints/floats and strings)

4. Change main executeable file to query the SQL database to get stats. (Check Database query syntax)

5. Create website that will host these functionalities. (Look into Django, html, css and the like.)

6. Add data visualization customization into the Main file. (Dropdown selection, slider for years, search bar for players, etc.)

7. Add more graphing capabilities. (Bar graphs?, Scatter plots?, Pie charts?, others?)
