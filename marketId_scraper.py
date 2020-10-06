import pandas as pd
import json
import requests as r
import dateutil.parser
from datetime import datetime, timedelta

params = []

competitions_dict = {

    	'epl': '10932509',
     	'ech': '7129730',
        'el1': '35',
        'el2': '37',
        'sp1': '117',
        'sp2': '12204313',
        'it1': '81',
        'fr1': '55',
        'fr2': '57',
        'hol': '9404054',
        'bel': '89979',
        'sco': '105',
        'tur': '194215',
        'gre': '67',
        'rom': '4905',
        'pol': '97',
        'rus': '101',
        'chn': '879931',
        'usa': '141',
        'swe': '129',
        'jpn': '89',
        'nor': '11068551',
        'den': '23',
        'mex': '5627174',
        'irl': '12203971',
        'fin': '45',
        'bra': '13',
        'por': '99',
        'aus': '10479956',
        'gm1': '59',
        'gm2': '61',
        'swz': '133',
        'enl': '11086347'
    }

def get_marketIds():

    for key,val in competitions_dict.items():

        events_url  = f'https://apieds.betfair.com/api/eds/navigation-aggregator/v2?_ak=nzIFcwyWhrlwYMrh&competitionId={val}&timezone=Europe%2FLondon'

        res = r.get(events_url)

        data = res.json()

        # todays_date = datetime.now().date()
        tomorrows_date = datetime.now().date() + timedelta(days=1)

        try:
            fixtures = data['fixtures'][str(tomorrows_date)]

            # for dates, events in fixtures.items():
            for event in fixtures:

                eventId = event['eventId']
                print(eventId)
                markets_url = f'https://ero.betfair.com/www/sports/exchange/readonly/v1/byevent?_ak=nzIFcwyWhrlwYMrh&currencyCode=GBP&eventIds={eventId}&locale=en_GB&rollupLimit=2&rollupModel=STAKE&types=MARKET_STATE,EVENT,MARKET_DESCRIPTION'

                market_res = r.get(markets_url)

                market_data = market_res.json()

                eventNodes = market_data['eventTypes'][0]['eventNodes']
                marketNodes = market_data['eventTypes'][0]['eventNodes'][0]['marketNodes']

                eventName = eventNodes[0]['event']['eventName']
                homeTeam = eventName.split(" v ")[0]
                awayTeam = eventName.split(" v ")[1]

                openDate = eventNodes[0]['event']['openDate']
                openDate = dateutil.parser.parse(openDate)
                openDate = openDate.replace(tzinfo=None) + timedelta(hours=1)

                print(homeTeam, awayTeam, openDate)

                for market in marketNodes:

                    marketType = market['description']['marketType']
                    marketId = str(market['marketId'])

                    if marketType == "MATCH_ODDS":
                        print(marketId)
                        params.append([key, homeTeam, awayTeam,openDate,marketId])
        except:
            continue

    marketId_df = pd.DataFrame(params, columns=['Div','HomeTeam','AwayTeam','OpenDate','MarketId'])
    marketId_df.to_csv("fixtures.csv", index=False)

get_marketIds()
