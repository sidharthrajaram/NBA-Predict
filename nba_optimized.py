import numpy as np 
import scipy
import pandas as pd
import matplotlib.pyplot as plt #visualization
from matplotlib import style # ^
style.use("ggplot")

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm

CSV_START_COLUMN = 0
CSV_END_COLUMN = 46

DATASET = np.genfromtxt('statistics.csv', delimiter=',', skip_header=1, 
    usecols=np.arange(CSV_START_COLUMN+6,CSV_END_COLUMN), invalid_raise=False)

LABELS = DATASET[:,CSV_START_COLUMN-1]

#preprocessing
rescaler = MinMaxScaler(feature_range=(0,1))
RESCALED_DATASET = rescaler.fit_transform(DATASET)
np.set_printoptions(precision=3)
