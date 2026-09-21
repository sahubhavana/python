import seaborn as sns
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = [80, 65, 90, 75]

sns.barplot(x=names, y=marks)

plt.show()
