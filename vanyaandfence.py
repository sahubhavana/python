n,h=map(int,input().split())
l=list(map(int,input().split()))
width=0 
for height in l:
    if (height>h):
        width=width+2
    else:
        width=width+1
print(width)
