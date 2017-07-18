#NBA_PREDICT 
#this file serves as the collective source file that we'll be using finally
#but for now it serves as a playground  

import numpy as np
from termcolor import colored
from sklearn import svm
import csv

import matplotlib.pyplot as plt #visualization
from matplotlib import style # ^
style.use("ggplot")
from nba_predict_svm import statFit
from scraper import statRetrieval

METRIC_SETS = 5
PLAYER_DATA = []

#SVM TRAINING OFF STATISTIC.CSV DATASET
#TS%/PPG
scoring_svm = statFit(9,28)
#usage/PER
efficiency_svm = statFit(19, 8)  
#VORP/WS
value_svm = statFit(27, 22)
#usage/TOV%
further_efficiency_svm = statFit(19,18)
#GP/WS48
durability_svm = statFit(6, 23)
#3PAr/FTr
shooting_freq_svm = statFit(10,11)
#IQ/PER
iq_svm = statFit(30, 8)  
#injury/Dleague
uhoh_svm = statFit(43, 44)


#FTr/FT%


#CSV Reading and Predict 
#we still haven't trained on enough data so some STAR ratings will be blasphemous
# e.g OJ MAYO!

name = ''
while(name != 'quit'):
	
	print()
	name = input('Enter player name: ')

	if(name == 'quit' or name == ''):
		break

	#this is the main sauce
	try:
		PLAYER_DATA = statRetrieval(name)

	except(RuntimeError, TypeError, NameError, KeyError, ValueError):
		print(colored("We weren't able to get this player's stats!",'red'))

	if(PLAYER_DATA != False):
		print(colored("ROOKIE STATS FETCHED", 'green'))

		print("projecting off:")
		print("TS%",PLAYER_DATA[1][3])
		print("PPG",PLAYER_DATA[0][23])
		scoring_rating = scoring_svm.predict([[ PLAYER_DATA[1][3], PLAYER_DATA[0][23] ]])
		print()
		print("projecting off:")
		print("USG",PLAYER_DATA[1][13])
		print("PER",PLAYER_DATA[1][2])
		efficiency_rating = efficiency_svm.predict([[ PLAYER_DATA[1][13], PLAYER_DATA[1][2] ]])
		print()
		print("projecting off:")
		print("VORP%",PLAYER_DATA[1][23])
		print("WS",PLAYER_DATA[1][17])
		value_rating = value_svm.predict([[ PLAYER_DATA[1][23], PLAYER_DATA[1][17] ]])
		print()
		print("projecting off:")
		print("USG",PLAYER_DATA[1][13])
		print("TOV%",PLAYER_DATA[1][12])
		further_efficiency_rating = further_efficiency_svm.predict([[ PLAYER_DATA[1][13], PLAYER_DATA[1][12] ]])
		print()		
		print("projecting off:")
		print("GP",PLAYER_DATA[1][0])
		print("WS/48",PLAYER_DATA[1][18])
		durability_rating = durability_svm.predict([[ PLAYER_DATA[1][0], PLAYER_DATA[1][18] ]])
		print()

			
		# iq_rating = iq_svm.predict([[ stat_row[30], stat_row[8]]])
		# uhoh_rating = uhoh_svm.predict([[ stat_row[43], stat_row[44]]])


		print("STAR rating based on TS/PPG: ",scoring_rating[0])
		print("STAR rating based on Usage/PER",efficiency_rating[0])
		print("STAR rating based on VORP/WS",value_rating[0])
		print("STAR rating based on Usage/TOV%",further_efficiency_rating[0])
		print("STAR rating based on GP/WS48",durability_rating[0])
		# print(stat_row[0], "STAR rating based on IQ/PER",iq_rating[0])
		# print(stat_row[0], "STAR rating based on Injuries/Dleague",uhoh_rating[0])
		# print(stat_row[0], "STAR rating based on 3PAr/FTr",shoot_freq_rating[0])
		print()


		star_rating = (scoring_rating+efficiency_rating+value_rating+
			further_efficiency_rating+durability_rating)/METRIC_SETS

		result_part_one = "This player has a total rookie STAR rating of {0}".format(round(star_rating[0], 3))

		if(star_rating >= 1):
			result_string = colored(result_part_one, 'green')
		elif(star_rating >= 0.6):
			result_string = colored(result_part_one, 'cyan')
		elif(star_rating >= 0.2):
			result_string = colored(result_part_one, 'yellow')
		else:
			result_string = colored(result_part_one, 'red')

		print(result_string)

	print()
	print("******************************************************")
