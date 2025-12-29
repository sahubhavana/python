#l=[10,12,20,22]
##print(sum(l))

###################### print a sum of posititve elemnt  in list #########################
# l=[-10,12,-20,22]
# s=0
# for i in l:
#     if i>0:
#         s=s+i
# print(s)
###################### sum of elemnt except those which is multiple of 3 #########################
# l=[10,12,20,22,9,15,18]
# s=0 
# for i in l:
#     if i%3!=0:
#         s=s+i
# print(s)
###################### product of element in list ########################
# l=[3,1,2,3]
# s=1 
# for i in l:
#     s=s*i
# print(s)

######################### product of element which is odd ########################
# l=[3,1,2,3,4,5,6]
# s=1 
# for i in l:
#     if i%2!=0:
#         s=s*i
# print(s)


##############################Write a Python program to multiply all elements in a list except those that are zero####################

# l=[3,0,2,3,0,5,6]
# s=1 
# for i in l:
#     if i!=0:
#         s=s*i
# print(s)


##########################Write a Python program to find the product of numbers in a list without using a loop.###########
# from functools import reduce
# l=[3,1,2,3,4,5,6]
# product=reduce((lambda x, y: x*y), l)
# print(product)

################################Write a Python program to calculate the cumulative product of elements in a list.##############
# l=[2, 3, 4, 5]
# cumprod=[]
# p=1 
# for i in l:
#     p=p*i
#     cumprod.append(p)
# print(cumprod)