s=input().strip()
t=input().strip()
position=0
for i in t:
    if(i==s[position]):
        position=+1
print(position+1)