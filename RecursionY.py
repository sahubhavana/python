def step(n,E):
    if n==E:
        return 1 
    if n>E:
        return 0
    return (step(n+1,E)+step(n+2,E)+step(n+3,E))

n,E=map(int,input().split())
print(step(n,E))