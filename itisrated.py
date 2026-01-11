t=int(input())
found=0
rating=[]
for i in range(t):
    a,b=map(int,input().split())
    rating.append((a,b))
    if a!=b:
        found=1
if found:
    print("rated")
else:
    
        # Check if pre-round ratings are consistent with standings
    for i in range(t - 1):
        if rating[i][0] < rating[i+1][0]:
            print("unrated")
            break
    else:
        print("maybe") 