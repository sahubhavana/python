n=int(input())
for i in range(n):
    l,s=map(int,input().split())
    found=False

    for start in range(1,l+1):
        ls=[]
        sum=0
        for num in range(start,l+1):
            sum=sum+num
            ls.append(num)
            if(sum==s):
                print(ls)
                found=True
                break
            if sum>s:
                break
        if found:
            break
    if not found:
        print(-1)           
            