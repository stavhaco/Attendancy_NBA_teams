import scrappingNbaApi
import pandas as pd
import csv

data = scrappingNbaApi.franchiseHistoryApi()
teams = data['resultSets'][0]['rowSet']

team_name_dictionary = {}
for team in teams:
    team_name = team[3]
    team_id = team[1]
    team_name_dictionary[team_id] = team_name

print(team_name_dictionary)

with open('team_id_name.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ID','Team name'])
    for key, value in team_name_dictionary.items():
       writer.writerow([key, value])
