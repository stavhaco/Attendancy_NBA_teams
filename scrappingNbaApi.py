import requests
import pandas as pd

def boxScoreApi(game_id=''):
    url = 'https://stats.nba.com/stats/boxscoresummaryv2?'
    api_param = {
        'GameID': game_id
    }
    u_a = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return data

def franchiseHistoryApi(league_id='00'):
    url = 'https://stats.nba.com/stats/franchisehistory?LeagueID=00'
    api_param = {
        'LeagueID': league_id
    }
    u_a = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return data
