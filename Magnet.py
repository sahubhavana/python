n=int(input())
prev=input()
count=1
for i in range(n-1):
    t=input()
    if t!=prev:
        count=count+1
    prev=t    

print(count)