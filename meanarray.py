3.Mean of array

def meanarray(arr,i,sum):
    if(i==len(arr)) :return sum
    sum=sum+arr[i]
    return  meanarray(arr,i+1,sum)
    
arr=[]
n=int(input())
for i in range(n):
    x=int(input())
    arr.append(x)
y=meanarray(arr,i=0,sum=0)
print("mean of array=",y/n)
