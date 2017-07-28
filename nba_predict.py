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
from multi import compositePredict, offenseSkillWord, defenseSkillWord, efficiencySkillWord, durabilitySkillWord, sumUp
from sentence import efficiencySent, scoringSent, defenseSent, durableSent, sumUpSent

from flask import Flask, request, render_template

app = Flask(__name__)

METRIC_SETS = 5
PLAYER_DATA = []

#OLD FORMAT
#TS%/PPG
# scoring_svm = statFit(9,28)

def hello(who='world'):
    return 'Hello %s' % who

#main sauce
@app.route("/")
@app.route("/<name>")
def predict(name=None):
	if(name!=None):
		try:
			data = statRetrieval(name)
			prediction = compositePredict(data)

			if(prediction == 0):
				return render_template("index.html", prediction="0.0")

			return render_template("index.html", prediction=prediction)

		except(RuntimeError, TypeError, NameError, KeyError, ValueError, IndexError):
			#for this you have to render a different HTML file with the display of this text so it doesn't look whack
			return render_template("noplayer.html") 

	else:
		#means no player has been searched! make a different html file with presentation for this so 
		#it doesn't say " ________ has a super potential of SEARCH!"
		return render_template("prompt.html", prediction=None)



#will implement later
def summary(name, PLAYER_DATA):
	summary = ''
	try:
		summary += efficiencySent(name, efficiencySkillWord(PLAYER_DATA)) + ' '
	except(TypeError):
		pass
	try:	
		summary += scoringSent(name, offenseSkillWord(PLAYER_DATA)) + ' '
	except(TypeError):
		pass
	try:
		summary += defenseSent(name, defenseSkillWord(PLAYER_DATA)) + ' '
	except(TypeError):
		pass
	try:
		summary += durableSent(name, durabilitySkillWord(PLAYER_DATA)) + ' '
	except(TypeError):
		pass
	try:
		summary += sumUpSent(name, sumUp(prediction))
	except(TypeError):
		pass

	return summary


if __name__ == "__main__":
	app.run(debug=True)

	# name = ''
	# while(name != 'quit'):
		
	# 	print()
	# 	name = input('Enter player name: ')

	# 	if(name == 'quit' or name == ''):
	# 		break

	# 	#this is the main sauce
	# 	try:
	# 		PLAYER_DATA = statRetrieval(name)

	# 	except(RuntimeError, TypeError, NameError, KeyError, ValueError):
	# 		print(colored("We weren't able to get this player's stats!",'red'))

	# 	if(PLAYER_DATA != False):

	# 		prediction = compositePredict(PLAYER_DATA)			
	# 		print()
	# 		print(summary(name, PLAYER_DATA))
	# 		print()

	# 		color = ''
	# 		if(prediction >= 2):
	# 			color = 'green'
	# 		elif(prediction >= 1):
	# 			color = 'cyan'
	# 		elif(prediction >= 0.2):
	# 			color = 'yellow'
	# 		else:
	# 			color = 'red'

	# 		final = colored(prediction, color, attrs = ['bold'])
	# 		print("Composite STAR Rating:",final)

	# 		#OLD FORMAT
	# 		# scoring_rating = scoring_svm.predict([[ PLAYER_DATA[1][3], PLAYER_DATA[0][23] ]])
				
	# 		# print("STAR rating based on TS/PPG: ",scoring_rating[0])

	# 		# star_rating = (scoring_rating+efficiency_rating+value_rating+
	# 		# 	further_efficiency_rating+durability_rating)/METRIC_SETS

	# 	print()
	# 	print("******************************************************")
