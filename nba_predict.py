import numpy as np
from termcolor import colored
from sklearn import svm

import matplotlib.pyplot as plt #visualization
from matplotlib import style # ^
style.use("ggplot")
from nba_predict_svm import statFit

#TS%/PPG prediction test
scoring_svm = statFit(9,28)
print("yee")
print(scoring_svm.predict([[0.48, 19.5]])) #1-d passing is deprecated haha