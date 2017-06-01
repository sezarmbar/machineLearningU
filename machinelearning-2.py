import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()

iris_idx = [0,50,100]


data = np.delete(iris.data, iris_idx, axis= 0)
target =np.delete(iris.target ,iris_idx)

test_data   = iris.data[iris_idx]
test_target = iris.target[iris_idx]


clf = tree.DecisionTreeClassifier()
clf.fit(data,target)

d_pred = clf.predict(test_data)


import os     
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import pydotplus 
from IPython.display import Image  
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydotplus.graph_from_dot_data(dot_data)  
graph.write_pdf("iris.pdf") 