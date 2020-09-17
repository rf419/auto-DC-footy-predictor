#!/Users/ryanshiz/anaconda/bin/python

from DC_Functions import *

params = []
results_csv = pd.DataFrame()
fixtures = pd.read_csv('fixtures.csv', dtype={'MarketId': str})
print(fixtures)
seasons_dict = {

    'main_leagues': {

        'current_seasons': {
            'epl': 'https://www.football-data.co.uk/mmz4281/2021/E0.csv',
            'ech': 'https://www.football-data.co.uk/mmz4281/2021/E1.csv',
            'el1': 'https://www.football-data.co.uk/mmz4281/2021/E2.csv',
            'el2': 'https://www.football-data.co.uk/mmz4281/2021/E3.csv',
            'sp1': 'https://www.football-data.co.uk/mmz4281/2021/SP1.csv',
            'sp2': 'https://www.football-data.co.uk/mmz4281/2021/SP2.csv',
            'fr1': 'https://www.football-data.co.uk/mmz4281/2021/F1.csv',
            'fr2': 'https://www.football-data.co.uk/mmz4281/2021/F2.csv',
            'hol': 'https://www.football-data.co.uk/mmz4281/2021/N1.csv',
            'bel': 'https://www.football-data.co.uk/mmz4281/2021/B1.csv',
            'sco': 'https://www.football-data.co.uk/mmz4281/2021/SC0.csv',
            'tur': 'https://www.football-data.co.uk/mmz4281/2021/T1.csv',
            'gre': 'https://www.football-data.co.uk/mmz4281/2021/G1.csv'
        },

        'previous_seasons': {
            'epl': 'https://www.football-data.co.uk/mmz4281/1920/E0.csv',
            'ech': 'https://www.football-data.co.uk/mmz4281/1920/E1.csv',
            'el1': 'https://www.football-data.co.uk/mmz4281/1920/E2.csv',
            'el2': 'https://www.football-data.co.uk/mmz4281/1920/E3.csv',
            'sp1': 'https://www.football-data.co.uk/mmz4281/1920/SP1.csv',
            'sp2': 'https://www.football-data.co.uk/mmz4281/1920/SP2.csv',
            'fr1': 'https://www.football-data.co.uk/mmz4281/1920/F1.csv',
            'fr2': 'https://www.football-data.co.uk/mmz4281/1920/F2.csv',
            'hol': 'https://www.football-data.co.uk/mmz4281/1920/N1.csv',
            'bel': 'https://www.football-data.co.uk/mmz4281/1920/B1.csv',
            'sco': 'https://www.football-data.co.uk/mmz4281/1920/SC0.csv',
            'tur': 'https://www.football-data.co.uk/mmz4281/1920/T1.csv',
            'gre': 'https://www.football-data.co.uk/mmz4281/1920/G1.csv'
        }
    },

    'extra_leagues': {
        'rom': 'https://www.football-data.co.uk/new/ROU.csv',
        'pol': 'https://www.football-data.co.uk/new/POL.csv',
        'rus': 'https://www.football-data.co.uk/new/RUS.csv',
        'chn': 'https://www.football-data.co.uk/new/CHN.csv',
        'jpn': 'https://www.football-data.co.uk/new/JPN.csv',
        'nor': 'https://www.football-data.co.uk/new/NOR.csv',
        'swe': 'https://www.football-data.co.uk/new/SWE.csv',
        'fin': 'https://www.football-data.co.uk/new/FIN.csv',
        'usa': 'https://www.football-data.co.uk/new/USA.csv',
        'mex': 'https://www.football-data.co.uk/new/MEX.csv',
        'bra': 'https://www.football-data.co.uk/new/BRA.csv',
        'irl': 'https://www.football-data.co.uk/new/IRL.csv'
    }
}

main_latest = seasons_dict['main_leagues']['current_seasons']
main_past = seasons_dict['main_leagues']['previous_seasons']
extra = seasons_dict['extra_leagues']
divisions = fixtures['Div'].unique()

team_name_dict = {
 'Inter Miami CF': 'Inter Miami'
}

remove_team_name_list = ['Verdy']

def team_name_correction(row):
    for key, val in team_name_dict.items():
        if key in row['HomeTeam']:
            results_csv.loc[row.name, 'HomeTeam'] = val
        elif key in row['AwayTeam']:
            results_csv.loc[row.name, 'AwayTeam'] = val

    # for name in remove_team_name_list:
    #     if name in row['HomeTeam']:
    #         results_csv.drop([row.name], inplace=True)
    #     elif name in row['AwayTeam']:
    #         results_csv.drop([row.name], inplace=True)

def aggregate(div):

    if ((div in main_latest) & (div in main_past)):

        data_current = seasons_dict['main_leagues']['current_seasons'][div]
        data_current = pd.read_csv(data_current, dtype={'Date': str})
        data_past = seasons_dict['main_leagues']['previous_seasons'][div]
        data_past = pd.read_csv(data_past, dtype={'Date': str})
        return data_past.append(data_current)

    elif div in extra:

        data_extra = extra[div]
        data_extra = pd.read_csv(data_extra, dtype={'Date': str})
        return data_extra.rename(columns={"League": "Div",
                                          "Home": "HomeTeam",
                                          "Away": "AwayTeam",
                                          "HG": "FTHG",
                                          "AG": "FTAG",
                                          "Res": "FTR"})


def main():

    for div in divisions:

        results_csv = aggregate(div)

        results_csv.apply(team_name_correction,axis=1)

        for row in fixtures.index:

            if fixtures.loc[row,['HomeTeam']].values[0] in results_csv.values:

                home_teams = results_csv['HomeTeam']
                away_teams = results_csv['AwayTeam']
                teams = home_teams.append(away_teams)
                teams = teams.unique()

                """Read previous season's results"""
                results_list = results_array(results_csv,teams)

                home_pred = fixtures.loc[row,['HomeTeam']].values[0]#input("Enter home team: ")
                away_pred = fixtures.loc[row,['AwayTeam']].values[0]#input("Enter away team: ")

                print (" ")
                print ("Predicting...")
                print (home_pred, 'vs.', away_pred, "Last update: ", results_csv.tail(1)['Date'])
                print (" ")

                """ Assign each team an attacking parameter and a defensive parameter (randomly)"""
                ability_dict = random_abilities(teams)

                log_like = log_likelihood(results_list, ability_dict)
                print ('Random log likelihood = ', log_like)

                (ability_list, conv, k) = monte_carlo_opt(log_like, ability_dict, results_list)
                log_like = log_likelihood(results_list, ability_dict)

                print ('After ', k, ' cycles:')
                print ('Minimised log likelihood = ', log_like)

                """Prints convergence of likelihood function """
                f = open("Convergence.txt", "w")
                for i in range(1, k) :
                	f.write(str(i) + " " + str(conv[i]) + "\n")
                f.close()

                """ Prints table of teams' abilities """
                rank_dict = {}
                g = open("Stats.txt", "w")
                g.write('%-15s %-12s %-10s \n' % ('Team', 'Attack', 'Defense'))
                for key in sorted(ability_dict.keys()) :
                	a = key
                	b = ability_dict[key][0]
                	c = ability_dict[key][1]
                	bb = format(float(b), '.2f')
                	cc = format(float(c), '.2f')
                	g.write('%-15s %-12s %-10s \n' % (a, bb, cc))
                g.close()

                """ Calculates probabilities of outcomes """
                home_mean = home_adv * ability_dict[home_pred][0] \
                * ability_dict[away_pred][1]
                away_mean = ability_dict[home_pred][1] * ability_dict[away_pred][0]
                home_dist = poisson(home_mean, 10)
                away_dist = poisson(away_mean, 10)
                #	print 'bla', home_mean, away_mean
                #	for i in range(0,10) :
                #		print home_dist[i], away_dist[i]
                """ Creates matrix of possible scores 'c' """
                a = np.array(home_dist)
                b = np.array(away_dist)
                #	c = np.outer(a,b)

                d = np.zeros((10,10))
                for i in range(0,10) :
                	for j in range(0,10):
                		d[i,j] = tau_matrix(home_mean, away_mean, i, j)*a[i]*b[j]
                odds = print_probs(d)

                # print_ability_table(ability_dict)
                # prob_dist = pd.DataFrame( data=d,
                #                           index=[0,1,2,3,4,5,6,7,8,9],
                #                           columns=[0,1,2,3,4,5,6,7,8,9])
                #
                # prob_dist.to_csv('prob_dist.csv',mode='a')

                div = fixtures.loc[row,['Div']].values[0]
                DCHomeOdds = odds[0]
                DCDrawOdds = odds[1]
                DCAwayOdds = odds[2]
                date 	   = fixtures.loc[row,['OpenDate']].values[0]
                mid        = fixtures.loc[row,['MarketId']].values[0]

                params.append([div,date,mid,home_pred,away_pred,DCHomeOdds,DCDrawOdds,DCAwayOdds])

    pred = pd.DataFrame(params, columns=['Div','Date','MarketId','HomeTeam','AwayTeam','DCHomeOdds','DCDrawOdds','DCAwayOdds'])

    pred.to_csv("pred.csv", mode='a',header=False, index=False)

if __name__ == '__main__':
	main()
