7.Revrse of string 
def revstring(s,i,result=""):
    if i==-1: return result
    return revstring(s,i-1,result+s[i])

s=input()
i=len(s)-1
x=revstring(s,i,result="")
print(x)
