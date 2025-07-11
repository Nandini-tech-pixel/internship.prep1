from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)
rf = RandomForestClassifier(random_state=42)
params = {
'n_estimators': [100, 200],
'max_depth': [4, 6, None],
'max_features': ['sqrt', 'log2']
}
gs = GridSearchCV(rf, params, cv=5)
gs.fit(X_train, y_train)
print("Best params:", gs.best_params_)

#Mini Project 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

dataset_choice = 'iris'  

if dataset_choice == 'iris':
    data = load_iris()
elif dataset_choice == 'wine':
    data = load_wine()
else:
    raise ValueError("Invalid dataset. Choose 'iris' or 'wine'.")

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=data.target_names))

importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]
feature_names = X.columns

plt.figure(figsize=(8, 6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], color='skyblue', align='center')
plt.xticks(range(X.shape[1]), feature_names[indices], rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("\n🔝 Top 3 Important Features:")
for i in range(3):
    feature = feature_names[indices[i]]
    importance = importances[indices[i]]
    print(f"{i+1}. {feature} (Importance: {importance:.3f})")
