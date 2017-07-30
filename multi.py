from sklearn import svm
import numpy as np

np.random.seed(1)

CSV_START_COLUMN = 6
CSV_END_COLUMN = 53

DATASET = np.genfromtxt('training.csv', delimiter=',', skip_header=1, 
    usecols=np.arange(CSV_START_COLUMN,CSV_END_COLUMN), invalid_raise=False)

X = DATASET[:,:46]
Y = DATASET[:,46]

def combineData(values1, values2):
    combined_stats = []
    for a in range(values1.size):
        result_component = [values1[a],values2[a]]
        combined_stats.append(result_component)
    combined_stats = np.array(combined_stats)
    return combined_stats

classifier = svm.SVC()

#offense
# #TS% vs PPG
scoring_ability = combineData(X[:,3], X[:,45])
# # #3Pr vs 3P%
# threept = combineData(X[:,4], X[:,29])
# #FTr vs FT%
ft = combineData(X[:,5], X[:,36])
# #ast vs TOV
passing = combineData(X[:,40], X[:,43])
# # #OWS vs WS
# off_presence = combineData(X[:,14], X[:,16])

def offense(player):
	result = 0.0

	# #TS% vs PPG
	classifier.fit(scoring_ability, Y) 
	result += classifier.predict([[ player[1][3], player[0][23] ]])[0]

	# classifier.fit(ft, Y) 
	# result += classifier.predict([[ player[1][4], player[0][14] ]])[0]

	# # #FTr vs FT%
	# classifier.fit(ft, Y) 
	# result += classifier.predict([[ player[1][5], player[0][14] ]])[0]

	# # #AST vs TOV
	# classifier.fit(passing, Y) 
	# result += classifier.predict([[ player[0][18], player[0][21] ]])[0]

	# # #OWS vs WS
	# classifier.fit(off_presence, Y) 
	# result += classifier.predict([[ player[1][15], player[1][17] ]])[0]

	print("STAR Offensive Rating:",result)
	return result


#defense
# #DWS vs WS
# def_presence = combineData(X[:,15], X[:,16])
# #STL vs BLK
stalwart = combineData(X[:,41], X[:,42])
# #DBPM vs DBPM
def_rating = combineData(X[:,19], X[:,19])
# pf vs pf
fouls = combineData(X[:,44], X[:,44])

def defense(player):
	result = 0.0

	# #STL vs BLK
	classifier.fit(stalwart, Y) 
	result += classifier.predict([[ player[0][20], player[0][19] ]])[0]

	# #DBpm vs DBPM
	classifier.fit(def_rating, Y) 
	result += classifier.predict([[ player[1][21], player[1][21] ]])[0]

	# #pf vs pf
	# classifier.fit(fouls, Y) 
	# result += classifier.predict([[ player[0][22], player[0][22] ]])[0]

	print("STAR Defensive Rating:",result)
	return result


#overall efficiency
# #usage/PER
efficiency_set = combineData(X[:,13], X[:,2])
# #USG/TOV%
further_set = combineData(X[:,13], X[:,12])
# #MPG vs TOV
# turnovers = combineData(X[:,23], X[:,43])
# # #FGA vs FGM
# scoring_eff = combineData(X[:,24], X[:,25])
# #PER/PER lol
per = combineData(X[:,2], X[:,2])

def efficiency(player):
	result = 0.0

	# #usage/PER
	classifier.fit(efficiency_set, Y) 
	result += classifier.predict([[ player[1][13], player[1][2] ]])[0]

	# #USG/TOV%
	classifier.fit(further_set, Y) 
	result += classifier.predict([[ player[1][13], player[1][12] ]])[0]

	# # #MPG vs TOV
	# classifier.fit(turnovers, Y) 
	# result += classifier.predict([[ player[0][1], player[0][21] ]])[0]

	# # #FGA vs FGM
	# classifier.fit(scoring_eff, Y) 
	# result += classifier.predict([[ player[0][3], player[0][2] ]])[0]

	# #PER/PER lol
	classifier.fit(per, Y) 
	result += classifier.predict([[ player[1][2], player[1][2] ]])[0]

	print("STAR Efficiency Rating:",result)
	return result


#durability
# # #GP/WS48
# durability_set = combineData(X[:,0], X[:,17])
# #GP/MP
play = combineData(X[:,0], X[:,1])
# # #MP/WS48
# perforty = combineData(X[:,1], X[:,17])

def durability(player):
	result = 0.0

	# #MPG/MP
	classifier.fit(play, Y) 
	result += classifier.predict([[ player[1][0], player[1][1] ]])[0]

	print("STAR Durability Rating:",result)
	return result


#value
# #VORP/WS
value_set = combineData(X[:,21], X[:,21])
# VORP/WS48
# game_forty = combineData(X[:,21], X[:,17])
#BPM / WS
# box = combineData(X[:,20], X[:,16])

def value(player):
	result = 0.0

	# #VORP/VORp
	classifier.fit(value_set, Y) 
	result += classifier.predict([[ player[1][23], player[1][23] ]])[0]

	# #BPM / WS
	# classifier.fit(box, Y) 
	# result += classifier.predict([[ player[1][22], player[1][17] ]])[0]
	print("STAR Value Rating:",result)
	return result


def compositePredict(player):
	result = 0.0
	result += offense(player)
	result += defense(player)
	result += efficiency(player)
	result += 1.5*(durability(player))
	# result += value(player)
	result = 1.25*result
	if(result >= 5):
		result = 5
	return round(result,3)

def offenseSkillWord(player):
	if(offense(player) > 0):
		return True
	else:
		return False

def defenseSkillWord(player):
	if(defense(player) > 0):
		return True
	else:
		return False

def efficiencySkillWord(player):
	if(efficiency(player) > 0):
		return True
	else:
		return False

def durabilitySkillWord(player):
	if(durability(player) > 0):
		return True
	else:
		return False

def sumUp(value):
	if(value):
		return True

# if __name__ == "__main__":
	# scoringPredict([[0.55,11.3]])


