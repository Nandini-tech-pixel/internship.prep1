import pandas as pd
df = pd.read_csv("titanic_sample.csv")
# Feature: Title from Name
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
# Feature: Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
# Feature: Age Group
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 50, 100], labels=["Child", "Teen", "Adult", "Senior"])
print(df[['Name', 'Title', 'FamilySize', 'AgeGroup']].head())

#Block 2
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X = df[['Fare', 'Age']].fillna(0)
y = df['Survived']
scaler = StandardScaler()
X_scaled_wrong = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled_wrong, y, test_size=0.3)
# Model trained with leaked data
# ✅ Correct Way
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
