#!/Users/ryanshiz/anaconda/bin/python

from DC_Functions import *
params = []
def main() :

	lates_fixtures = pd.read_csv('https://www.football-data.co.uk/fixtures.csv')[['Div','Date', 'HomeTeam', 'AwayTeam']]

	season_dict = {
				  'epl':'https://www.football-data.co.uk/mmz4281/1920/E0.csv',
				  'ech':'https://www.football-data.co.uk/mmz4281/1920/E1.csv',
				  'el1':'https://www.football-data.co.uk/mmz4281/1920/E2.csv',
				  'el2':'https://www.football-data.co.uk/mmz4281/1920/E3.csv',
				  'eco':'https://www.football-data.co.uk/mmz4281/1920/EC.csv',
				  'sp1':'https://www.football-data.co.uk/mmz4281/1920/SP1.csv',
				  'sp2':'https://www.football-data.co.uk/mmz4281/1920/SP2.csv',
				  'it1':'https://www.football-data.co.uk/mmz4281/1920/I1.csv',
				  'it2':'https://www.football-data.co.uk/mmz4281/1920/I2.csv',
				  'ge1':'https://www.football-data.co.uk/mmz4281/1920/D1.csv',
				  'ge2':'https://www.football-data.co.uk/mmz4281/1920/D2.csv',
				  'por':'https://www.football-data.co.uk/mmz4281/1920/P1.csv',
				  'tur':'https://www.football-data.co.uk/mmz4281/1920/T1.csv',
				  'gre':'https://www.football-data.co.uk/mmz4281/1920/G1.csv',
				  'aut':'https://www.football-data.co.uk/new/AUT.csv',
				  'rus':'https://www.football-data.co.uk/new/RUS.csv',
				  'den':'https://www.football-data.co.uk/new/DNK.csv',
				  'rom':'https://www.football-data.co.uk/new/ROU.csv'
			  }

	for season in season_dict:
		
		results_csv = pd.read_csv(season_dict[season],dtype={'Date': str })

		if 'HomeTeam' not in results_csv.columns:
			results_csv = results_csv.rename(columns={"League":"Div", 
								  		 			  "Home":"HomeTeam", 
								  		 			  "Away":"AwayTeam", 
								    	 			  "HG":"FTHG", 
								    	 			  "AG":"FTAG", 
								   		 			  "Res":"FTR"})
		for row in lates_fixtures.index:

			if lates_fixtures.loc[row,['HomeTeam']].values[0] in results_csv.values:

				teams = results_csv['HomeTeam'].unique()
				"""Read previous season's results"""
				results_list = results_array(results_csv,teams)
			
				home_pred = lates_fixtures.loc[row,['HomeTeam']].values[0]#input("Enter home team: ")
				away_pred = lates_fixtures.loc[row,['AwayTeam']].values[0]#input("Enter away team: ")
				
				print (" ")
				print ("Predicting...")
				print (home_pred, 'vs.', away_pred)
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

				div = lates_fixtures.loc[row,['Div']].values[0]
				DCHomeOdds = odds[0]
				DCDrawOdds = odds[1]
				DCAwayOdds = odds[2]
				date 	   = lates_fixtures.loc[row,['Date']].values[0]

				params.append([div,date,0,home_pred,away_pred,DCHomeOdds,DCDrawOdds,DCAwayOdds,0,0,0,0,0,0,0])

	pred = pd.DataFrame(params, columns=['Div','Date','MarketId','HomeTeam','AwayTeam','DCHomeOdds','DCDrawOdds','DCAwayOdds','BFCHome','BFCDraw', 'BFCAway','HomeMargin','DrawMargin','AwayMargin','FTR'])

	pred.to_csv("pred.csv", mode='a',header=False, index=False)

if __name__ == '__main__':
	main()