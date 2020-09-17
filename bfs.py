import pandas as pd
import json
import requests as r
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import dateutil.parser

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# # add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('pm.json', scope)

# # authorize the clientsheet 
client = gspread.authorize(creds)

# # get the instance of the Spreadsheet
sheet = client.open('results')

# # get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# get all the records of the data
records_data = sheet_instance.get_all_records(numericise_ignore=['all'])

# convert the json to dataframe
runner_df = pd.DataFrame.from_dict(records_data)

# Get only the rows with market IDs
runner_df = runner_df[runner_df["MID"] != ""]


def refresh_odds(row):

	marketId = str(row['MID'])
	print(marketId)
	cell = sheet_instance.find(marketId)

	# Get the current row in the spreadsheet
	srow = cell.row

	# Check if a stake has been set in the liability cell
	lcell = sheet_instance.cell(srow, 32).value
	
	# If a stake exists then the bet has been placed so don't update the odds
	if lcell == "":
		
		url  = 'https://ero.betfair.com/www/sports/exchange/readonly/v1/bymarket?_ak=nzIFcwyWhrlwYMrh&alt=json&currencyCode=GBP&locale=en_GB&marketIds='+marketId+'&rollupLimit=2&rollupModel=STAKE&types=MARKET_DESCRIPTION,EVENT,RUNNER_DESCRIPTION,RUNNER_EXCHANGE_PRICES_BEST'

		res = r.get(url)

		data = res.json()
		
		eventNodes  = data['eventTypes'][0]['eventNodes']

		for events in eventNodes:

			for marketNodes in events['marketNodes']:

				marketTime = marketNodes['description']['marketTime']
				marketTime = dateutil.parser.parse(marketTime)
				marketTime = marketTime.replace(tzinfo=None) + timedelta(hours=1)
				currentTime = datetime.now().replace(microsecond=0)
				# timeDelta =  marketTime - currentTime
				print(currentTime)
				print(marketTime)
				if (marketTime > currentTime):

					marketTime = str(marketTime)
					currentTime = str(currentTime)

					homePrice = marketNodes['runners'][0]['exchange']['availableToLay'][0]['price']
					awayPrice = marketNodes['runners'][1]['exchange']['availableToLay'][0]['price']
					drawPrice = marketNodes['runners'][2]['exchange']['availableToLay'][0]['price']

					runner_df.loc[row.name,'BF1'] = homePrice
					runner_df.loc[row.name,'BFX'] = drawPrice
					runner_df.loc[row.name,'BF2'] = awayPrice

					sheet_instance.update_cell(srow, 2, marketTime)
					sheet_instance.update_cell(srow, 3, currentTime)
					sheet_instance.update_cell(srow, 6, homePrice)
					sheet_instance.update_cell(srow, 7, drawPrice)
					sheet_instance.update_cell(srow, 8, awayPrice)

				print("Done")

if not runner_df.empty:
	runner_df.apply(refresh_odds, axis=1)
