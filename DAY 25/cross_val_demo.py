from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
df = pd.read_csv("titanic_sample.csv")
X = df[['Fare', 'Age']].fillna(0)
y = df['Survived']
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
model = RandomForestClassifier()
scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
print("Cross-validation scores:", scores)
print("Mean CV Score:", scores.mean())
