q1=dataset['CoapplicantIncome'].quantile(0.25)
q3=dataset['CoapplicantIncome'].quantile(0.75)
IQr=q3-q1
min_range=q1-(1.5*IQr)
max_range=q3+(1.5*IQr)
min_range
max_range
