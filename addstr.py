#Create Combinations of Letters from Dictionary Keys

d={'1':['a','b'], '2':['c','d']}
l=d.get('1')
l1=d.get('2')

print(l)
print(l1)
for i in range(len(l)):
    for j in range(len(l1)):
        print(l[i]+l1[j])
