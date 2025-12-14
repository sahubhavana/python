s=input()
ch=input().strip()
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
result=""
for x in ch:
    idx=keyboard.index(x)
    if(s=='L'):
        result+=keyboard[idx+1]
    else:
        if(s=='R'):
            result+=keyboard[idx-1]
print(result)