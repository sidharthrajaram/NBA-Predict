#NBA_PREDICT
#this file serves as the collective source file that we'll be using finally
#but for now it serves as a playground

# from termcolor import colored

# import matplotlib.pyplot as plt #visualization
# from matplotlib import style # ^
# style.use("ggplot")
from scraper import statRetrieval
from multi import compositePredict, offenseSkillWord, defenseSkillWord, efficiencySkillWord, durabilitySkillWord, sumUp
from sentence import efficiencySent, scoringSent, defenseSent, durableSent, sumUpSent

from flask import Flask, render_template

app = Flask(__name__)

METRIC_SETS = 5
PLAYER_DATA = []

#OLD FORMAT
#TS%/PPG
# scoring_svm = statFit(9,28)
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
		summary += sumUpSent(name, sumUp(compositePredict(PLAYER_DATA)))
	except(TypeError):
		pass

	return summary.lower()

#main sauce
@app.route("/")
@app.route("/<name>")
def predict(name=None):
	if(name!=None):
		try:
			data = statRetrieval(name)
			prediction = compositePredict(data)
			longform = summary(name, data)

			if(prediction == 0):
				return render_template("index.html", prediction="0.0", longform=longform)

			return render_template("index.html", prediction=prediction, longform=longform)

		except(RuntimeError, TypeError, NameError, KeyError, ValueError, IndexError):
			#for this you have to render a different HTML file with the display of this text so it doesn't look whack
			return render_template("noplayer.html")

	else:
		#means no player has been searched! make a different html file with presentation for this so
		#it doesn't say " ________ has a super potential of SEARCH!"
		return render_template("prompt.html", prediction=None)



