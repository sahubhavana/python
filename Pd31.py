import pandas as pd

df = pd.read_csv("data.csv")

result = df[df["Age"] > 25]
print(result)
