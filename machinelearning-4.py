import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train,X_test, y_train, y_test = train_test_split(X,y, test_size = 0.5)

#clf = tree.DecisionTreeClassifier()
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)  

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)