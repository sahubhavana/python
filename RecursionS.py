def average(lst,i,s=0):
    if i==len(lst):
        return 0
    else:
        
        s=lst[i]+average(lst,i+1)
        return s
       
       
        
        
n=int(input())
lst=list(map(int,input().split()))
total=average(lst,0,s=0)
print("{:.6f}".format(total/n))