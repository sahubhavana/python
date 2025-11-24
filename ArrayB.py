N=int(input())
for i in range(N):
    n=list(map(int, input().split()))
    x=int(input())
    for i in range(len(n)):
        if(n[i]==x):
            return i
        else:
            print(-1)
            break
            
            
                 
    