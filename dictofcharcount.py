#Create Dictionary from a String (Letter Frequency)
s=input('enetr a string')
l=s.split()
d={}
for i in s:
    d[i]=s.count(i)
    
print(d)
