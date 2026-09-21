import seaborn as sns
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [35, 45, 55, 65, 80]

sns.scatterplot(x=hours, y=marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
