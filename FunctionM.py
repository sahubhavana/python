def count_unique(L):
    print(len(set(L)))

n = int(input())
L = []

while len(L) < n:
    L.extend(map(int, input().split()))

L = L[:n]   
count_unique(L)



