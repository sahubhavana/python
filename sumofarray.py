# 10.sum of array using tail recursion 
def arrSum(arr, n, sum=0):
    # Base Case
    if n == 0:
        return sum

    # Recursive call
    return arrSum(arr, n - 1, sum + arr[n - 1])


# Driver code
arr = [2, 55, 1, 7]
n = len(arr)
print(arrSum(arr, n, 0))
