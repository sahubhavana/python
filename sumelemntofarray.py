6.Sum of element of the array

def sumofarr(arr,i,sum):
    if i==len(arr):return sum
    sum=sum+arr[i]
    return sumofarr(arr,i+1,sum)

n=int(input("enter a size of array"))
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
a=sumofarr(arr,i=0,sum=0)
print("sum of element of array=",a)
