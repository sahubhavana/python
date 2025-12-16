n,m=map(int,input().split())
min_move=(n+1)//2
answer=-1
for i in range(min_move,n+1):
    if i%m==0:
        answer=i
        break
print(answer)
