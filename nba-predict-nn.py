#Author: Sidharth Rajaram
#Version: 7/9/17
#Simple NN

import numpy as np
from termcolor import colored

METRICS = 14
PLAYERS = 32
CSV_START_COLUMN = 29
n_epochs = 750000

# sigmoid activation function
def sigmoid(data,deriv=False):
    if(deriv==True):
        #simple calculation for derivative
        return data*(1-data)
    return 1/(1+np.exp(-data))

    
# input dataset
dataset = np.genfromtxt('statistics.csv', delimiter=',', skip_header=1, 
    usecols=np.arange(CSV_START_COLUMN,CSV_START_COLUMN+METRICS+1), 
    invalid_raise=False)
print(dataset)

X = np.array(dataset[:,:14])

# output dataset
temp_y = np.array(dataset[:,14])
y = temp_y.reshape((PLAYERS,1))

np.random.seed(1)

WEIGHTS = 2 * np.random.random((METRICS,1)) - 1

#TRAINING
for iter in range(n_epochs):

    l0 = X #layer 1 = input values
    weighted_raw = np.dot(l0,WEIGHTS)
    l1 = sigmoid(weighted_raw) 
    error = y - l1 #expected - predicted 
    delta = error * sigmoid(l1,True)
    change  = np.dot(l0.T,delta)
    # update weights
    WEIGHTS += change

#OUTPUT...
print("Rounded Outputs:")
for a in range(l1.size):
    for b in range(l1[a].size):
        if(round(l1[a][b]) == 1.0):
            status = colored("A STAR!", 'green')
        else:
            status = colored("NOT A STAR!",'red')
        print("STAR Result: {0} | {1} ".format(round(l1[a][b]), status))

#for fun prediction
print()
print("PREDICTION")

player_name = colored("Steve Rogers", 'cyan')
player_to_be_predicted = [[0,1,0,1,0,1,0,1,1,1,0,1,0,0]]

prediction_value = sigmoid(np.dot(player_to_be_predicted,WEIGHTS))
if(round(prediction_value[0][0]) == 1.0):
    status = "will be an NBA star!"
else:
    status = "will not be an NBA star!"

print("STAR Result: {0} | {1} {2} ".format(round(prediction_value[0][0]), 
    player_name, status))
print()





