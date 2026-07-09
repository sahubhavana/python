import pandas as pd

df = pd.read_csv("students.csv")

average_marks = df.groupby("Department")["Marks"].mean()

print(average_marks)
