#normal  function
def double(x):
    return x*2
print(double(5))


#lambda function 
double =lambda x:x*2
print(double(5))

#example using withn filter
lst=[1,2,3,4,5]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

#example using with map()
lst=[1,2,3,4]
new_lst=list(map(lambda x:x**2,lst))
print(new_lst)

#example using with reduce()
from functools import reduce
lst=[1,2,3,4,5]
newlis= reduce(lambda x,y:(x*y),lst)
print(newlis)



##################     MODULE ####################

import math
print(math.pi)

import datetime
print(datetime.datetime.now())