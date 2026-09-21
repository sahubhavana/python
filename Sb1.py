import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [35, 45, 55, 65, 80]
}

df = pd.DataFrame(data)

sns.scatterplot(data=df, x="Hours", y="Marks")

plt.show()
