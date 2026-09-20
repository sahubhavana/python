df=pd.DataFrame({'name':['webscue','cow','cat','dog','black']})
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['en_name']=le.fit_transform(df['name'])
df
