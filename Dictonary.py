# my_dict={'name':'satish','age':27,'address':'guntur','mob':9897654321}
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.get('age'))
# my_dict.update({'City':'Jabalpur'})
# print(my_dict)



##sort a dictionary with the help of value
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# l=dict(sorted(d.items()))
# print(l)

#update a key with new element 
# d={0: 10, 1: 20}
# d.update(({2:30}))
# print(d)

#concadinate three dictionary
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

#to check the key existince in the dictionary
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# x=int(input("enter a value"))
# l=d.keys()
# for key in l:
#     if key==x:
#         print("element present")
#         break
# else:
#     print("element not present")


#to itreate over dictionary
# d = {'x': 10, 'y': 20, 'z': 30} 
# for key,value in d.items():
#     print(key,'->',value)

#Generate Dictionary of Numbers and Their Squares
# n=int(input("enter a length of dictionary"))
# d={}
# for i in range(n):
#     a=int(input())
#     d[a]=a**2
# print(d)
#Generate Dictionary of Numbers and Their Squares from 1 to 15
# d={}
# for i in range(1,16):
#     d[i]=i**2
# print(d)





#### Merege two python dictonary
# d1 = {'a': 100, 'b': 200}


# d2 = {'x': 300, 'y': 200}
# d1.update(d2)
# print(d1)

# my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
# l=my_dict.values()
# print(sum(l))
# sum=1 
# for i in l:
#     sum=sum*i
# print(sum)



# delete a key from  dictionary
# myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# del myDict['a']
# print(myDict)


# color_dict = {
#     'red': '#FF0000',
#     'green': '#008000',
#     'black': '#000000',
#     'white': '#FFFFFF'
# }
# for key in sorted(color_dict):
#     print(key,color_dict[key])