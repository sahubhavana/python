df.loc[(df['SibSp']>1)&(df['Age']<30),['Name','SibSp','Age']]
