# Replace all missing values in the "Embarked" column with the value that 
#occurs most frequently in it. 

df['embark_town'].fillna(df['embark_town'].mode(),inplace=True)
