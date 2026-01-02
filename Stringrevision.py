#Count character frequency in a string.
# s=input("enter a string")
# d={}
# count=0 
# for i in s:
#     count=s.count(i)
#     d[i]=count
    
# print(d)

#Get string of first and last 2 chars.
# s=input("enetr a string")
# t=""
# t=t+(s[0:2]+s[len(s)-2:])
# print(t)



#Replace first char occurrences with $.
# s=input("enter a string")
# s1=list(s)
# for i in range(len(s1)-1):
#     for j in range(i+1,len(s1)):
#         if(s1[i]==s1[j]):
#             s1[j]='$'
# print("".join(s1))



##Swap first 2 chars of 2 strings.
# a="abc"
# v="xyz"
# l1=list(a)
# l2=list(v)
# temp=l1[0]
# l1[0]=l2[0]
# l2[0]=temp
# print("".join(l1))
# print("".join(l2))

##longest word in list
# length=0
# mx=0
# result =["PHP", "Exercises", "Backend"]
# for i in result:
#     length=len(i)
#     mx=max(length,mx)
# print(mx)

#Write a Python script that takes input from the user and displays that input back in upper and lower cases.
    
# s=input("enter a string")
# if(s.isupper()):
#     print(s.lower())
# else:
#     (s.islower())
#     print(s.upper())
#Sort distinct words in comma-separated input.
# s="red, white, black, red, green, black"
    
# s1=s.split(',')
# for i in range(len(s1)-1):
#     for j in range(i+1,len(s1)):
#         if(s1[i]==s1[j]):
#             s1.pop(j)
        
    
# s1.sort()
# print(s1)


###Repeat last four character of string 4 time
# s="python"
# s1=""
# s1=s1+(s[len(s)-2:])
# print(s1*4)


#sort string leoxigraphicaly

# s='w3resource'
# l=list(s)
# l.sort()
# print(''.join(l))
    
    
    