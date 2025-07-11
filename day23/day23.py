from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
tree = DecisionTreeClassifier(max_depth=4, min_samples_split=10, random_state=0)
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)
tree = DecisionTreeClassifier(max_depth=4, min_samples_split=10, random_state=0)
tree.fit(X_train, y_train)
scores = cross_val_score(tree, X_train, y_train, cv=5)
print("CV Accuracy:", scores.mean())
tree.fit(X_train, y_train)
scores = cross_val_score(tree, X_train, y_train, cv=5)
print("CV Accuracy:", scores.mean())

#MINI PROJECT

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.dropna(subset=['survived'], inplace=True)

features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
X = titanic[features]
y = titanic['survived']
X['age'].fillna(X['age'].median(), inplace=True)
X['embarked'].fillna(X['embarked'].mode()[0], inplace=True)
X = pd.get_dummies(X, drop_first=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", round(accuracy, 3))
print("Precision:", round(precision, 3))
print("Recall:", round(recall, 3))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=['Not Survived', 'Survived'], filled=True)
plt.show()

