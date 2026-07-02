#X. Write a program to remove duplicate rows from the DataFrame df permanently. Display the DataFrame after the changes. 

df1.drop_duplicates().inplace=True
df1.count()
