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
from multi import compositePredict

METRIC_SETS = 5
PLAYER_DATA = []

#OLD FORMAT
#TS%/PPG
# scoring_svm = statFit(9,28)

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

		prediction = compositePredict(PLAYER_DATA) + 0.1 # bias
		color = ''
		if(prediction >= 0.8):
			color = 'green'
		elif(prediction >= 0.5):
			color = 'cyan'
		elif(prediction >= 0.2):
			color = 'yellow'
		else:
			color = 'red'

		final = colored(prediction, color, attrs = ['bold'])
		print("Composite STAR Rating:",final)

		#OLD FORMAT
		# scoring_rating = scoring_svm.predict([[ PLAYER_DATA[1][3], PLAYER_DATA[0][23] ]])
			
		# print("STAR rating based on TS/PPG: ",scoring_rating[0])

		# star_rating = (scoring_rating+efficiency_rating+value_rating+
		# 	further_efficiency_rating+durability_rating)/METRIC_SETS

	print()
	print("******************************************************")
