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

METRIC_SETS = 6

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


#FTr/FT%


#CSV Reading and Predict 
#we still haven't trained on enough data so some STAR ratings will be blasphemous
# e.g OJ MAYO!

name = ''
while(name != 'quit'):
	name = input('Enter player name: ')
	if(name == ''):
		break
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


		print(stat_row[0], "STAR rating based on TS/PPG: ",scoring_rating)
		print(stat_row[0], "STAR rating based on Usage/PER",efficiency_rating)
		print(stat_row[0], "STAR rating based on VORP/WS",value_rating)
		print(stat_row[0], "STAR rating based on Usage/TOV%",further_efficiency_rating)
		print(stat_row[0], "STAR rating based on GP/WS48",durability_rating)
		print(stat_row[0], "STAR rating based on IQ/PER",iq_rating)

		# print(stat_row[0], "STAR rating based on 3PAr/FTr",shoot_freq_rating)

		print()

		star_rating = (scoring_rating+efficiency_rating+value_rating+
			further_efficiency_rating+durability_rating+ iq_rating)/METRIC_SETS

		result_part_one = "{0} has a total rookie STAR rating of {1}".format(stat_row[0], star_rating)

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
		print(colored("No player found! Our humblest apologies!", 'red'))

	print()
