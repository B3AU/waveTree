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

#clf.fit(X,y)

from sklearn import datasets

iris = datasets.load_iris()
rng = np.random.RandomState(1)
perm = rng.permutation(iris.target.size)
iris.data = np.hstack([iris.data[perm],iris.data[perm],iris.data[perm],iris.data[perm]])
iris.target = iris.target[perm]

print iris.target
clf.fit(iris.data,iris.target)


print clf.predict(iris.data)

