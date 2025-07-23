from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv("titanic_sample.csv")
X = df[['Fare', 'Age']].copy()
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y)

pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipe.fit(X_train, y_train)
print("Pipeline accuracy:", pipe.score(X_test, y_test))

#MODEL 
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.base import BaseEstimator, TransformerMixin

df = pd.read_csv("titanic_sample.csv")   
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
def age_group(age):
    if pd.isnull(age):
        return np.nan
    elif age < 13:
        return 'Child'
    elif age < 20:
        return 'Teen'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(age_group)

features = ['Title', 'FamilySize', 'AgeGroup', 'Fare', 'Sex']
target = 'Survived'

X = df[features]
y = df[target]

num_features = ['FamilySize', 'Fare']
num_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy='median')),
    ("scaler", StandardScaler())
])
cat_features = ['Title', 'AgeGroup', 'Sex']
cat_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy='most_frequent')),
    ("encoder", OneHotEncoder(handle_unknown='ignore'))
])
preprocessor = ColumnTransformer([
    ("num", num_transformer, num_features),
    ("cat", cat_transformer, cat_features)
])
clf_pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(clf_pipeline, X, y, cv=skf, scoring='accuracy')
print("Cross-Validation Accuracy Scores:", scores)
print("Average CV Accuracy:", np.mean(scores))
clf_pipeline.fit(X, y)
y_pred = clf_pipeline.predict(X)
print("\nClassification Report on Full Data:")
print(classification_report(y, y_pred))
