from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn import datasets
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn import preprocessing
import numpy as np

np.random.seed(1)

CSV_START_COLUMN = 6
CSV_END_COLUMN = 30

DATASET = np.genfromtxt('training_set.csv', delimiter=',', skip_header=1, 
    usecols=np.arange(CSV_START_COLUMN,CSV_END_COLUMN), invalid_raise=False)

X = DATASET[:,:23]
Y = DATASET[:,23]

distro_scaler = StandardScaler().fit(X)
X = distro_scaler.transform(X)
# print(X)
# print(Y)

le = preprocessing.LabelEncoder()
le.fit(["Generational Talent", "All Star", "Good Player", "Low Ceiling"])
# print(list(le.classes_))
Y_Int = np.array(Y).astype(int)
# print(list(le.inverse_transform(Y_Int)))

classifer = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X, Y)
# print("TRAINING RUn")
# print(classifer.predict(X))
# print()

print("prediction")
predict_data = [[31, 1000, 16.3, 0.5, 0.132, 0.275, 1.8, 12, 6.8, 24.6, 
2.5, 0.5, 21.4, 20.4, 3, 1.6, 4.7, 0.077, 1.1, -0.7, 0.4, 0.7, 8.5]]
predict_data = distro_scaler.transform(predict_data)
print(classifer.predict(predict_data))
