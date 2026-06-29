#55.Write a program which Swap first column of array with second column in the array of 3x3 matrix.
import numpy as np
arr=np.arange(1,10).reshape(3,3)
arr[ :,[0, 1]] = arr[:,[1, 0]]
arr
