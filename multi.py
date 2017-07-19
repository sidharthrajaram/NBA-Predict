from sklearn import svm
import numpy as np

np.random.seed(1)

CSV_START_COLUMN = 6
CSV_END_COLUMN = 30

DATASET = np.genfromtxt('training_set.csv', delimiter=',', skip_header=1, 
    usecols=np.arange(CSV_START_COLUMN,CSV_END_COLUMN), invalid_raise=False)

X = DATASET[:,:23]
Y = DATASET[:,23]

def combineData(values1, values2):
    combined_stats = []
    for a in range(values1.size):
        result_component = [values1[a],values2[a]]
        combined_stats.append(result_component)
    combined_stats = np.array(combined_stats)
    return combined_stats

# TS%/PPG
scoring_set = combineData(X[:,3], X[:,22])
# #usage/PER
efficiency_set = combineData(X[:,13], X[:,2])
# #VORP/WS
value_set = combineData(X[:,21], X[:,16])
# #GP/WS48
durability_set = combineData(X[:,0], X[:,17])
# #USG/TOV%
further_set = combineData(X[:,13], X[:,12])

classifier = svm.SVC()

def scoringPredict(data):
	classifier.fit(scoring_set, Y) 
	print("STAR Scoring Rating:",classifier.predict(data)[0])
	return classifier.predict(data)

def efficiencyPredict(data):
	classifier.fit(efficiency_set, Y) 
	print("STAR Efficiency Rating:",classifier.predict(data)[0])
	return classifier.predict(data)

def valuePredict(data):
	classifier.fit(value_set, Y) 
	print("STAR Value Rating:",classifier.predict(data)[0])
	return classifier.predict(data)

def durabilityPredict(data):
	classifier.fit(durability_set, Y) 
	print("STAR Durability Rating:",classifier.predict(data)[0])
	return classifier.predict(data)

def furtherPredict(data):
	classifier.fit(further_set, Y) 
	print("STAR Further Rating:",classifier.predict(data)[0])
	return classifier.predict(data)

def compositePredict(player):
	scoring = scoringPredict([[ player[1][3], player[0][23] ]])
	efficiency = efficiencyPredict([[ player[1][13], player[1][2] ]])
	value = valuePredict([[ player[1][23], player[1][17] ]])
	durability = durabilityPredict([[ player[1][0], player[1][18] ]])
	further = furtherPredict([[ player[1][13], player[1][12] ]])

	prediction = (scoring+efficiency+value+durability+further)/5
	return round(prediction[0],3)


if __name__ == "__main__":
	scoringPredict([[0.55,11.3]])


