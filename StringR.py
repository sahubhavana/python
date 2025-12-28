N = int(input())
n = list(input().strip())   # FIX HERE
S = n.copy()

scorep = 0
i = 0

while i < len(S):
    if S[i] == 'V':
        scorep += 5

    elif S[i] == 'W':
        scorep += 2

    elif S[i] == 'X':
        if i + 1 < len(S):
            del S[i + 1]

    elif S[i] == 'Y':
        if i + 1 < len(S):
            S.append(S[i + 1])
            del S[i + 1]
            continue   # reprocess same index

    elif S[i] == 'Z':
        if i + 1 < len(S):
            if S[i + 1] == 'V':
                scorep //= 5
                del S[i + 1]
            elif S[i + 1] == 'W':
                scorep //= 2
                del S[i + 1]

    i += 1

print(scorep)
