import pandas as pd
# # from fuzzywuzzy import process
# # from fuzzywuzzy import fuzz
# #
# # bf_fixtures = pd.read_csv('fixtures_test.csv',dtype={'MarketId': str})
# # bf_teams = bf_fixtures['HomeTeam']
# #
# # fbd_teams = pd.read_csv('fbd_teams.csv').values.tolist()
# #
# # def translate(row):
# #
# #
# #     for team in fbd_teams:
# #
# #         h_ratio = fuzz.ratio(row['HomeTeam'].lower(),team[0].lower())
# #         h_partial_ratio = fuzz.partial_ratio(row['HomeTeam'].lower(),team[0].lower())
# #         h_token_sort_ratio = fuzz.token_sort_ratio(row['HomeTeam'],team[0])
# #         h_token_set_ratio = fuzz.token_set_ratio(row['HomeTeam'],team[0])
# #
# #         a_ratio = fuzz.ratio(row['AwayTeam'].lower(),team[0].lower())
# #         a_partial_ratio = fuzz.partial_ratio(row['AwayTeam'].lower(),team[0].lower())
# #         a_token_sort_ratio = fuzz.token_sort_ratio(row['AwayTeam'],team[0])
# #         a_token_set_ratio = fuzz.token_set_ratio(row['AwayTeam'],team[0])
# #
# #         if h_token_set_ratio > 70:
# #             print("HOME TEAM: ", h_token_set_ratio, row['HomeTeam'], team[0] )
# #         if a_token_set_ratio > 70:
# #             print("AWAY TEAM: ", a_token_set_ratio, row['AwayTeam'], team[0] )
#
#     # ratio_home = process.extract( row['HomeTeam'], fbd_teams )
#     # ratio_away = process.extract( row['AwayTeam'], fbd_teams )
#     # # print(Ratios)
#     #
#     # # You can also select the string with the highest matching percentage
#     # highest_home = process.extractOne( row['HomeTeam'], fbd_teams )
#     # highest_away = process.extractOne( row['AwayTeam'], fbd_teams )
#     # # print(highest)
#     #
#     # if highest_home[1] >= 75:
#     #     print(highest_home[0][0])
#     #     bf_fixtures.loc[row.name, 'HomeTeam'] = highest_home[0][0]
#     #     bf_fixtures.loc[row.name, 'HomeTrans'] = "TRUE"
#     # if highest_away[1] >= 75:
#     #     print(highest_away[0][0])
#     #     bf_fixtures.loc[row.name, 'AwayTeam'] = highest_away[0][0]
#     #     bf_fixtures.loc[row.name, 'AwayTrans'] = "TRUE"
#
# # bf_fixtures.apply(translate,axis=1)
# #
# # bf_fixtures.to_csv('fixtures_after_translation.csv',index=False)
#
#
# seasons_dict = {
#
#     'main_leagues': {
#
#         'current_seasons': {
#             'epl': 'https://www.football-data.co.uk/mmz4281/2021/E0.csv',
#             'ech': 'https://www.football-data.co.uk/mmz4281/2021/E1.csv',
#             'el1': 'https://www.football-data.co.uk/mmz4281/2021/E2.csv',
#             'el2': 'https://www.football-data.co.uk/mmz4281/2021/E3.csv',
#             'enl': 'https://www.football-data.co.uk/mmz4281/2021/EC.csv',
#             'gm1': 'https://www.football-data.co.uk/mmz4281/2021/D1.csv',
#             'gm2': 'https://www.football-data.co.uk/mmz4281/2021/D2.csv',
#             'it1': 'https://www.football-data.co.uk/mmz4281/2021/I1.csv',
#             'sp1': 'https://www.football-data.co.uk/mmz4281/2021/SP1.csv',
#             'sp2': 'https://www.football-data.co.uk/mmz4281/2021/SP2.csv',
#             'fr1': 'https://www.football-data.co.uk/mmz4281/2021/F1.csv',
#             'fr2': 'https://www.football-data.co.uk/mmz4281/2021/F2.csv',
#             'hol': 'https://www.football-data.co.uk/mmz4281/2021/N1.csv',
#             'bel': 'https://www.football-data.co.uk/mmz4281/2021/B1.csv',
#             'sco': 'https://www.football-data.co.uk/mmz4281/2021/SC0.csv',
#             'tur': 'https://www.football-data.co.uk/mmz4281/2021/T1.csv',
#             'gre': 'https://www.football-data.co.uk/mmz4281/2021/G1.csv',
#             'por': 'https://www.football-data.co.uk/mmz4281/2021/P1.csv'
#         },
#
#         'previous_seasons': {
#             'epl': 'https://www.football-data.co.uk/mmz4281/1920/E0.csv',
#             'ech': 'https://www.football-data.co.uk/mmz4281/1920/E1.csv',
#             'el1': 'https://www.football-data.co.uk/mmz4281/1920/E2.csv',
#             'el2': 'https://www.football-data.co.uk/mmz4281/1920/E3.csv',
#             'enl': 'https://www.football-data.co.uk/mmz4281/1920/EC.csv',
#             'gm1': 'https://www.football-data.co.uk/mmz4281/1920/D1.csv',
#             'gm2': 'https://www.football-data.co.uk/mmz4281/1920/D2.csv',
#             'it1': 'https://www.football-data.co.uk/mmz4281/1920/I1.csv',
#             'sp1': 'https://www.football-data.co.uk/mmz4281/1920/SP1.csv',
#             'sp2': 'https://www.football-data.co.uk/mmz4281/1920/SP2.csv',
#             'fr1': 'https://www.football-data.co.uk/mmz4281/1920/F1.csv',
#             'fr2': 'https://www.football-data.co.uk/mmz4281/1920/F2.csv',
#             'hol': 'https://www.football-data.co.uk/mmz4281/1920/N1.csv',
#             'bel': 'https://www.football-data.co.uk/mmz4281/1920/B1.csv',
#             'sco': 'https://www.football-data.co.uk/mmz4281/1920/SC0.csv',
#             'tur': 'https://www.football-data.co.uk/mmz4281/1920/T1.csv',
#             'gre': 'https://www.football-data.co.uk/mmz4281/1920/G1.csv',
#             'por': 'https://www.football-data.co.uk/mmz4281/1920/P1.csv'
#         }
#     },
#
#     'extra_leagues': {
#         'rom': 'https://www.football-data.co.uk/new/ROU.csv',
#         'pol': 'https://www.football-data.co.uk/new/POL.csv',
#         'rus': 'https://www.football-data.co.uk/new/RUS.csv',
#         'chn': 'https://www.football-data.co.uk/new/CHN.csv',
#         'jpn': 'https://www.football-data.co.uk/new/JPN.csv',
#         'nor': 'https://www.football-data.co.uk/new/NOR.csv',
#         'swe': 'https://www.football-data.co.uk/new/SWE.csv',
#         'fin': 'https://www.football-data.co.uk/new/FIN.csv',
#         'usa': 'https://www.football-data.co.uk/new/USA.csv',
#         'mex': 'https://www.football-data.co.uk/new/MEX.csv',
#         'bra': 'https://www.football-data.co.uk/new/BRA.csv',
#         'irl': 'https://www.football-data.co.uk/new/IRL.csv',
#         'den': 'https://www.football-data.co.uk/new/DNK.csv',
#         'aus': 'https://www.football-data.co.uk/new/AUT.csv',
#         'swz': 'https://www.football-data.co.uk/new/SWZ.csv'
#     }
# }
#
# main_latest = seasons_dict['main_leagues']['current_seasons']
# main_past = seasons_dict['main_leagues']['previous_seasons']
# extra = seasons_dict['extra_leagues']
#
# teams = []
#
# for k,v in main_past.items():
#
#     main_past_df = pd.read_csv(v)['HomeTeam'].unique()
#
#     for t in main_past_df:
#         teams.append(t)
#
# for k,v in extra.items():
#
#     extra_df = pd.read_csv(v)['Home'].unique()
#
#     for t in extra_df:
#         teams.append(t)
#
#
# teams_df = pd.DataFrame(teams,columns=['Teams'])
# teams_df.to_csv('teams.csv',index=False)

teams_df = pd.read_csv('teams.csv')
teams_list = [teams_df["Teams"].values]

fixtures = pd.read_csv('fixtures.csv')

for idx in fixtures.index:

    if ( (fixtures.loc[idx,'HomeTeam'] not in teams_df["Teams"].values) or
         (fixtures.loc[idx,'AwayTeam'] not in teams_df["Teams"].values) ):

        fixtures.loc[idx,"NameError"] = "ERROR"

fixtures.to_csv('fixtures.csv',index=False)





# df["Target"] = df.apply(lambda x: 0 if x["FTHG"] > x["FTAG"] else 1 if x["FTHG"] == x["FTAG"] else 2, axis=1)
