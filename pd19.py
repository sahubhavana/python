#Assign ranks to passengers based on their "Fare", with higher fares 
#getting higher ranks. Allow ties in the ranking.

df["Rank"] = "Second"         
df.loc[df["fare"]>100, "Rank"] = "First"
