#Extract passengers whose "Pclass" is either 1 or 3 and store their information in a new DataFrame.

df1['pclass1']=df.loc[(df['pclass']==1 )| (df['pclass']==3)]
