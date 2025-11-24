N=int(input())
for i in range(N):
    sum=0
    n=list(map(int, input().split()))
    for i in n:
        sum=sum+i
    print(abs(sum))
    