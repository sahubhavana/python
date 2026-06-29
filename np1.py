#56.Q1. Write a program which Subtract the mean of each row from a 
#matrix. (Create a matrix of random elements)
arr=np.arange(1,10).reshape(3,3)
for i in range(len(arr)):
    x=np.mean(i)
