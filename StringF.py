T=int(input())
for i in range(T):
    count=0
    S=input()
    if(len(S)>10):
        print(S[0],end="")
        for i in range(1,len(S)-1):
            count=count+1
        print(count,end="")
        print(S[len(S)-1])
    else:
        print(S)
      
    