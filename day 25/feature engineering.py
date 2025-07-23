import pandas as pd
df = pd.read_csv("titanic_sample.csv")
# Feature: Title from Name
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
# Feature: Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
# Feature: Age Group
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 50, 100], labels=["Child", "Teen", "Adult", "Senior"])
print(df[['Name', 'Title', 'FamilySize', 'AgeGroup']].head())
