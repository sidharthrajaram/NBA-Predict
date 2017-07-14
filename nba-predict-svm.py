#Author: Sidharth Rajaram
#Version: 7/13/17
#SVM 

import numpy as np 
from sklearn import svm

import matplotlib.pyplot as plt #visualization
from matplotlib import style # ^
style.use("ggplot")

#FULL DATA
DATASET = np.genfromtxt('statistics.csv', delimiter=',', skip_header=1, 
    
    #referring to indices of statsheet
    usecols=np.arange(0,43), invalid_raise=False)
LABELS = DATASET[:,42]
print(LABELS)
print()

SVMS = []

STATS = []

COLORS = ['red','blue','cyan','magenta','black','green']

#METHODS
def combineData(values1, values2):
    combined_stats = []
    for a in range(values1.size):
        result_component = [values1[a],values2[a]]
        combined_stats.append(result_component)
    combined_stats = np.array(combined_stats)
    return combined_stats

def fit(col1, col2):
    stats1 = DATASET[:,col1]
    print(stats1)
    print()
    stats2 = DATASET[:,col2]
    print(stats2)
    print()
    a_stat_set = combineData(stats1, stats2)
    STATS.append(a_stat_set)
    an_svm = svm.SVC(kernel='linear', C = 1.0)
    an_svm.fit(a_stat_set, LABELS)
    SVMS.append(an_svm)
    return an_svm #for use in nba-predict.py

def queueVisual():
    for index in range(len(STATS)):
        the_svm = SVMS[index]
        the_stats = STATS[index]
        line_color = COLORS[index]
        w = the_svm.coef_[0]
        a = -w[0] / w[1]
        xx = np.linspace(-4,35)
        yy = a * xx - the_svm.intercept_[0] / w[1]
        h0 = plt.plot(xx, yy, '-', label=index, color=line_color)
        plt.scatter(the_stats[:, 0], the_stats[:, 1], c = LABELS)

#TS%/PPG
fit(9, 28)

#usage/PER
fit(19, 8)  

#VORP/WS
fit(27, 22)

#visuals
queueVisual()
plt.legend()
plt.show()



