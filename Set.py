s={1,2,3,5,6,8,98}
#print(s)
###set can ignore duplicate
#s={1,2,3,4,1,5,3}
#print(s)
#s=set([1,2,3,1])
#print(s)
#s=set()
#print(type(s))
####set does not support indexing 
##s.add(4)
##print(s)
### to update multiple element
# s.update([5,6,1])
# print(s)
# s.update([8,9],{10,2,3})
# print(s)

####to remove element of set
# s.dicard(3)
# print(s)
#s.discard(4)
#print(s)
#s.remove(4)
#print(s)

#### to remove a random element
#s.pop()
#print(s)

#### to remove all elemnt of set
#s.clear()
#print(s)
### union opreator 
# set1={1,2,3,4,5}
# set2={3,4, 5,6,7}
#print(set1|set2)
#print(set1.union(set2))

#### intersection opreator ###
# print(set1&set2)
# print(set1.intersection(set2))

###3 to print diffrence between opreator 
#print(set1 - set2)
#print(set1.difference(set2))

##print a symmetric diffrence between opreator
#print(set1.symmetric_difference(set2))

# setx={"a","b","c","d","e"}
# sety={"b","c"}
# print("is set x is subset of y",sety.issubset(setx))
# set1=frozenset([1,2,3,4])
# set2=frozenset([3,4,5,6])
# print(set1|set2)
# print(set1.union(set2))

## to print a common  word in set of list
# word=["steal","least","stale","tales"]
# common=set(word[0])
# for i in word[1:]:
#     common&=set(i)
# print("comman word are ",common)
    
    
    

    
    

