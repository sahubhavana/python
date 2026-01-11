s=input().strip()
t=input().strip()
pos=0
for i in t:
    if s[pos]==i:
        pos=pos+1
print(pos+1)