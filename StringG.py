S=input()

s2=""
for i in  S:
    if i.islower():
        s2=s2+i.upper()
    else:
        if i.isupper():
            s2=s2+i.lower()
        else:
           s2=s2+ i.replace(","," ")
print(s2)