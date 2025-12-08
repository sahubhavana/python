def data(S,i):
    if i==len(S):
        return 0
    if S[i].lower() in "aeiou":
            return 1+data(S,i+1)
    else:
            return data(S,i+1)
   
S=input()
print(data(S,0))