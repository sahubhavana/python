k=int(input())
n=int(input())
w=int(input())
cost=0
for i in range(1,w+1):
    cost=cost+(i*k)
print(cost-n)
