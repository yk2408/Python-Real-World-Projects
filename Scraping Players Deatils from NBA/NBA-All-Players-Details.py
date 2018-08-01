# coding: utf-8


import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# initialize Chrome driver
driver = webdriver.Chrome()

url = "http://www.nba.com/players"

driver.get(url)

# Scroll down window to display all the coaches
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
data_list = []

player_details = soup.find_all('section', class_='nba-player-index__trending-item')

for player in player_details:
    data_dict = {}
    name = player.find("p", class_="nba-player-index__name")
    data_dict['name'] = name.text.replace("<br/>", "")
    rank = player.find("span", class_="nba-player-trending-item__number")
    data_dict['rank'] = rank.text
    details = player.find("div", class_="nba-player-index__details")
    span = details.find_all("span")
    data_dict['position'] = span[0].text
    h_w_data = span[1].text.split(" | ")
    data_dict['height'] = h_w_data[0].replace(" ft ", ".").replace("in", "")
    data_dict['weight(in lbs)'] = h_w_data[1].replace(" lbs", "")
    data_list.append(data_dict)
driver.quit()

df = pd.DataFrame(data_list)

# Rearrange the columns 
df = df[['name', 'rank', 'position', 'height', 'weight(in lbs)']]

# Convert data into CSV file
df.to_csv("NBA-All-Players-Details.csv")
