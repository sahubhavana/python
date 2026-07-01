#43.Find the value in an array that is closest to a number 3.

arr = np.array([1.5, 2.8, 3.2, 4.1])
index = np.abs(arr - 3).argmin()
print("value=",arr[index])
