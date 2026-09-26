import numpy as np

arr = np.array([[1, 2, np.nan, 4],
                [5, 6, 7, np.nan]])

for i in range(arr.shape[0]):

    x = np.nanmean(arr[i])

    for j in range(arr[i].size):

        if np.isnan(arr[i][j]):
            arr[i][j] = x

print(arr)
