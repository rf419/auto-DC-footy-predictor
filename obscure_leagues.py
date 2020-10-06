import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

div = 'sw1'

url = 'https://footystats.org/norway/first-division/fixtures#2012'#'https://footystats.org/sweden/division-1/fixtures'

page = requests.get(url, headers={"User-Agent": "Requests"})

soup = BeautifulSoup(page.text, 'html.parser')

match_tables = soup.findAll(class_="matches-table inactive-matches")

matches_data = []

for match in match_tables:

    for completed_match in match.findAll(class_="match complete"):

        if completed_match is not None:
            date        = datetime.fromtimestamp(int(completed_match.find(class_="date convert-months")['data-time']))
            date        = date.strftime('%Y-%m-%d')
            score       = completed_match.find(class_="bold ft-score").text.split(" - ")
            home_goals  = score[0]
            away_goals  = score[1]

            home_team   = completed_match.find(class_="team-home").text
            away_team   = completed_match.find(class_="team-away").text

            matches_data.append([div,date,home_team,away_team,home_goals,away_goals])
            print(f'{date} {home_team} {home_goals} - {away_goals} {away_team}')

# matches_df = pd.DataFrame(matches_data,columns=['Div','Date','HomeTeam','AwayTeam','FTHG','FTAG'])
#
# print(matches_df)
