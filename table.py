##print a dictionary in table format
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

l=my_dict.keys()
l1=my_dict.values()
for i in l:
    print(i,end=" ")
print('')
for j in l1:
    for k in j:
        print(k,end=" ")
    print('')
