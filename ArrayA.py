import math
N=int(input())

sum=0
n=list(map(int,input().split()))
for j in n:
    sum=sum+j
print(abs(sum),end='')
    