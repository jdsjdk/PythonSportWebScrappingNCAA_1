'''
Author: Jess Summerhill
Project: A sport betting analytics web scrapper
Date: 2-21-2020

Project Specs:
This is a web scrapper
1. The client wants all the team names from the first column
2. Ingore team rankings
3. I am scraping the first data column of from each team on that site,
   so 2 columns total.

This is my root URL = https://www.teamrankings.com/ncb/team-stats/
'''

# On v.0001, use selenium and not requests.
import csv
from bs4 import BeautifulSoup as bsoup
from selenium import webdriver as wdr

# Setup the webdriver
b_url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game"

browser = wdr.Chrome()
browser.get(b_url)

# Setup xpaths
soupy = bsoup(browser.page_source, 'lxml')

# Scrape site
no_wrap = soupy.find_all("td", {"class", "text-left nowrap"})

dlist = []

for nurl in no_wrap:
    tname = nurl.find("a", href=True).get_text()
    ds1 = nurl.find_next("td").contents[0]
    dlist.append({"Team Names": tname, "Score": ds1})

with open('ncaa_stats.csv', 'w') as file:
    fheaders = ["Team Names", "Score"]

    fwriter = csv.DictWriter(file, fieldnames=fheaders, delimiter='\t')

    fwriter.writeheader()

    for wrow in dlist:
        fwriter.writerow(wrow)
