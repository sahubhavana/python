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
        
