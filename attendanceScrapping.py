from selenium import webdriver
import re
import pandas as pd
import csv
import traceback
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"Using selenium to imitate legit web browsing - very slow performance but usefull for one time scraping (not used in this project, here for documentation"

id_list = pd.read_csv('game_ids_2017_18.csv')
path_to_chromedriver = '/home/stav/.local/bin/chromedriver' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

game_attendancy = {}
for index, game_id in id_list.iterrows():
    try:
        url = 'https://stats.nba.com/game/00'+str(game_id['id'])+'/'
        print(url)
        time0 = time.time()
        browser.get(url)
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME , "game-summary-additional__inner")))
        time1 = time.time()
        print(time1-time0)
        element_text = element.text
        content = ('{0}'.format(element_text))
        print(content)
        pattern = re.compile('[\s\S]*ATTENDANCE: (\d*,\d*)')
        m = pattern.match(content)
        attendance = m.group(1)
        game_attendancy[game_id['id']] = attendance
    except Exception as e: 
        traceback.print_exc()

print(game_attendancy)
with open('attendancy.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id','attendancy'])
    for key, value in game_attendancy.items():
       writer.writerow([key, value])
browser.close()