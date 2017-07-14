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

METRIC_SETS = 3

#SVM TRAINING 

#TS%/PPG
scoring_svm = statFit(9,28)
#usage/PER
efficiency_svm = statFit(19, 8)  
#VORP/WS
value_svm = statFit(27, 22)

#CSV Reading and Predict 
#we still haven't trained on enough data so some STAR ratings will be blasphemous
# e.g. Kobe Bryant has a 0.0 star rating right now!

name = ''
while(name != 'quit'):
	name = input('Enter player name: ')
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

		print(stat_row[0], "STAR rating based on TS/PPG: ",scoring_rating)
		print(stat_row[0], "STAR rating based on Usage/PER",efficiency_rating)
		print(stat_row[0], "STAR rating based on VORP/WS",value_rating)
		print()

		star_rating = (scoring_rating+efficiency_rating+value_rating)/METRIC_SETS
		print(stat_row[0], "has a total rookie STAR rating of ",star_rating)
	else:
		print("No player found! Our humblest apologies!")

	print()
