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

################################# write a python to find maximum elemnt in a list#####################
# l=[10,-9,8,4,5,6,7,8,9,-0,-3]
# max1=0 
# for i in range(len(l)-1):
#     if l[i]>max1:
#         max1=l[i]
# print("MAximum element of list", max1)
# x=max(l)
# print("maximum element of list=",x)

########################## write a program to find second maximum of list ####################
#l=[12,3,4,5,6,7,8,9,49,59,66]
#########1way to find second element #######
# s=max(l)
# l.pop(l.index(s))
# print("second maximum element=",max(l))
############# 2 way to find maximum element #############
# l.sort(reverse=True)
# print("Second maximum element=",l[1])
######### 3 way to find the element of stack############################
# first=0
# for num in l:
#     if(num>first):
#         second=first
#         first=num
#     elif num>second and num!=first:
#         second=num
# print("second largest elemnt=",second)
        
#Write a Python program to find the largest number that is a multiple of 5 in a given list.
# l1=[]
# for i in l:
#     if(i%5==0):
#         l1.append(i)
# print("Maximum element which is mutlitple of 5 is=",max(l1))
# mx=0
# for i in l:
#     if(i%5==0 and i>mx):
#         mx=i 
# print("the maximum element divisible by 5=",mx)
        
        
#print a greater element which is even
# mx=0
# for i in l:
#     if(i%2==0 and i>mx):
#         mx=i 
# print("the maximum element that is even=",mx)
    
#Write a Python program to find the second smallest number in a list.

#l=[12,3,4,5,6,7,8,9,49,59,66]
# x=min(l)
# print("first minimum element of list=",x)
# l.remove(x)
# print("second minimum element of list=",min(l))

# l.sort()
# print("second smallest element of list=",l[1])

# first=max(l)
# second=max(l)
# for i in l:
#     if i<first:
#         second=first 
#         first=i
#     elif first<i<second:
#         second=i
# print(second)


#Write a Python program to find the smallest number that is a prime number in a given list

# l1=[]
# for i in l:
#     if(i<=1):
#         continue
#     else:
#         for a in range(2, int(i**0.5) + 1):
#             if i % a == 0:
#                 l1.append(i)
# print(l1)

# Write a Python program to find the smallest number that is a multiple of 3 in a given list.
# l1=[]
# for i in l:
#     if(i%3==0):
#         l1.append(i)
# print(min(l1))


# Count Strings with Same Start and End
# count=0
# l=['abc', 'xyz', 'aba', '1221']
# for a in l:
#     if(a[0]==a[-1] and len(a)>2):
#             count=count+1
# print(count)


#Write a Python program to get a list, sorted in increasing order
# l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# l.sort()
# print(l)

#write a program to remove a dupliacate
# a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# l1=[]
# l=set(a)
# for i in l:
#     l1.append(i)
# print(l1)

#cloning of list
# l=[10,22,44,23,4]
# l2=list(l)
# print(l2)
# n=int(input("enter a length  of word"))
# l1=[]
# l=['The','quick','lazy','fox','jump','over','the','lazy','dog']
# for i in l:
#     if len(i)>n:
#         l1.append(i)

# print(l1)      


