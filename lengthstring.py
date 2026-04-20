 8.To count a length of string
def countlength(s,count,i):
    if i==len(s): return count
    count=count+1
    return countlength(s,count,i+1)
s=input("Enter a string=")
x=countlength(s,count=0,i=0)
print("length of string=",x)
