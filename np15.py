#42.Create an 8×8 checkerboard pattern using 0s and 1s

arr=np.arange(64).reshape(8,8)
for i in range(8):
    for j in range(8):
        arr[i][j]=(i + j) %2
arr
