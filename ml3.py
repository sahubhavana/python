sns.scatterplot(x='cgpa',y='package',data=data)
plt.plot(data['cgpa'],y_prd,c='red')
plt.legend(["org_data","predict_line"])
