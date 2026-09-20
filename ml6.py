from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy="mean")
ar=si.fit_transform(data(['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Item_Outlet_Sales']))
new_dataset=pd.Dataframe(ar,columns=data.select_dtypes(include='float64').columns)
new_data.isnull().sum()
