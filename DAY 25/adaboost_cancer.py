from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)
base = DecisionTreeClassifier(max_depth=1)
model = AdaBoostClassifier(base_estimator=base, n_estimators=100, learning_rate=0.1)
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))
