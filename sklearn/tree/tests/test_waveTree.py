__author__ = 'beau'



import sklearn
print sklearn

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(splitter="wave")
print clf.splitter

import numpy  as np

X = [[-2, -1], [-1, -1], [-1, -2], [1, 1], [1, 2], [2, 1]]
y = [-1, -1, -1, 1, 1, 1]
T = [[-1, -1], [2, 2], [3, 2]]
true_result = [-1, 1, 1]

clf.fit(X,y)


print clf.predict(T)

