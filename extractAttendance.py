import scrappingNbaApi
import pandas as pd
import csv

id_list = pd.read_csv('game_ids_2017_18.csv')
game_attendancy = {}

for index, game_id in id_list.iterrows():
    data = scrappingNbaApi.boxScoreApi('00'+str(game_id['id']))
    print(index)
    attendance = data['resultSets'][4]['rowSet'][0][1]
    home_team_id = data['resultSets'][5]['rowSet'][0][3]
    home_team_score = data['resultSets'][5]['rowSet'][0][22]
    away_team_id = data['resultSets'][5]['rowSet'][1][3]
    away_team_score = data['resultSets'][5]['rowSet'][1][22]
    game_attendancy[game_id['id']] = {'attendance': attendance, 
                                    'home_team_id': home_team_id, 
                                    'home_team_score': home_team_score, 
                                    'away_team_id': away_team_id, 
                                    'away_team_score': away_team_score}

with open('attendancy.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ID','Attendancy','Home Team ID', 'Home Team Score', 'Away Team ID', 'Away Team Score'])
    for key, value in game_attendancy.items():
       writer.writerow([key, value['attendance'], value['home_team_id'], value['home_team_score'], value['away_team_id'], value['away_team_score']])

