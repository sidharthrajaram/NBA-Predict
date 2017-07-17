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

METRIC_SETS = 7

#SVM TRAINING 

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
# shooting_freq_svm = statFit(10,11)
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
	name = input('Enter player name: ')
	print()
	if(name == ''):
		break

	#this is the main sauce
	try:
		statRetrieval(name)
		print()
		print(colored("ROOKIE STATS FETCHED", 'green'))

	except(RuntimeError, TypeError, NameError, KeyError, ValueError):
		print(colored("We weren't able to get this player's stats!",'red'))


	#everything below will soon be phased out 
	found = False
	stat_row = 0
	with open('statistics.csv', 'rt') as f:
		stat_reader = csv.reader(f, delimiter=',')
		for row in stat_reader:
			if(name.lower() == row[0].lower()):
				stat_row = row
				found = True
	print()
	if(found):

		scoring_rating = scoring_svm.predict([[ stat_row[9], stat_row[28] ]])
		efficiency_rating = efficiency_svm.predict([[ stat_row[19], stat_row[8] ]])
		value_rating = value_svm.predict([[ stat_row[27], stat_row[22] ]])
		further_efficiency_rating = further_efficiency_svm.predict([[ stat_row[19], stat_row[18]]])
		durability_rating = durability_svm.predict([[ stat_row[6], stat_row[23]]])
		# shoot_freq_rating = shooting_freq_svm.predict([[ stat_row[10], stat_row[11]]])
		iq_rating = iq_svm.predict([[ stat_row[30], stat_row[8]]])
		uhoh_rating = uhoh_svm.predict([[ stat_row[43], stat_row[44]]])


		print(stat_row[0], "STAR rating based on TS/PPG: ",scoring_rating[0])
		print(stat_row[0], "STAR rating based on Usage/PER",efficiency_rating[0])
		print(stat_row[0], "STAR rating based on VORP/WS",value_rating[0])
		print(stat_row[0], "STAR rating based on Usage/TOV%",further_efficiency_rating[0])
		print(stat_row[0], "STAR rating based on GP/WS48",durability_rating[0])
		print(stat_row[0], "STAR rating based on IQ/PER",iq_rating[0])
		print(stat_row[0], "STAR rating based on Injuries/Dleague",uhoh_rating[0])


		# print(stat_row[0], "STAR rating based on 3PAr/FTr",shoot_freq_rating)

		print()

		star_rating = (scoring_rating+efficiency_rating+value_rating+
			further_efficiency_rating+durability_rating+ iq_rating+uhoh_rating)/METRIC_SETS

		result_part_one = "{0} has a total rookie STAR rating of {1}".format(stat_row[0], round(star_rating[0], 3))

		if(star_rating >= 1):
			result_string = colored(result_part_one, 'green')
		elif(star_rating >= 0.6):
			result_string = colored(result_part_one, 'cyan')
		elif(star_rating >= 0.2):
			result_string = colored(result_part_one, 'yellow')
		else:
			result_string = colored(result_part_one, 'red')

		print(result_string)

	else:
		if(name == ''):
			break

		print(colored("No player found in statistics.csv! Our humblest apologies!", 'red'))

	print()
	print("******************************************************")
	print()
