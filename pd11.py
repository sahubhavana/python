# Create a new column named "Above_Avg_Age" that stores True if a 
#passenger's age is greater than the dataset's average age, otherwise 
#False.

df['Above_Avg_Age']=False
df['Above_Avg_Age']=df.loc[df['age']>df['age'].mean(),"Above_Avg_Age"]=True
