#Author: Sidharth Rajaram
#Version: 7/13/17
#SVM 

import numpy as np 
from sklearn import svm

import matplotlib.pyplot as plt #visualization
from matplotlib import style # ^
style.use("ggplot")

#######methods########
def combineData(values1, values2):
    combined_stats = []
    for a in range(values1.size):
        result_component = [values1[a],values2[a]]
        combined_stats.append(result_component)
    combined_stats = np.array(combined_stats)
    return combined_stats

def queueVisualization(the_svm, stats, label, line_color):
    w = the_svm.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(0,65)
    yy = a * xx - the_svm.intercept_[0] / w[1]
    h0 = plt.plot(xx, yy, '-', label=label, color=line_color)
    plt.scatter(stats[:, 0], stats[:, 1], c = labels)

#FULL DATA
dataset = np.genfromtxt('svm-stats.csv', delimiter=',', skip_header=1, 
    usecols=[1,2,3,4,5], invalid_raise=False)
labels = dataset[:,4]

#SCORING 
ts_stats = dataset[:,0]
ppg_stats = dataset[:,1]

scoring_stats = combineData(ts_stats, ppg_stats)
ppg_svm = svm.SVC(kernel='linear', C = 1.0)
ppg_svm.fit(scoring_stats, labels)  

#USAGE AND EFFICIENCY
usage_stats = dataset[:,2]
per_stats = dataset[:,3]

efficiency_stats = combineData(usage_stats, per_stats)
eff_svm = svm.SVC(kernel='linear', C = 1.0)
eff_svm.fit(efficiency_stats, labels)  

#VISUALIZE
queueVisualization(ppg_svm, scoring_stats, "TS% vs PPG","blue")
queueVisualization(eff_svm, efficiency_stats, "Usage% vs PER","red")

plt.legend()
plt.show()



