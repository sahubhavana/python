N=int(input())
L=list(map(int, input().split()))
mn=min(L)
print(mn,L.index(mn)+1)
