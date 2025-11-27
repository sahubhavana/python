A, B = map(int, input().split())
S = input()

# Check the mandatory '-'
if S[A] != '-':
    print("No")
elif not (S[:A] + S[A+1:]).isdigit():   # check digits except position A
    print("No")
else:
    print("Yes")

    
        
    
    