def isapalindrome(n):
    n = str(n)
    x = 1
    for i in range(len(n)):
        if n[i] == n[-i-1]:
            continue
        else:
            x = 0
    return x

N = []
for i in range(999,500,-1):
    for j in range(999,500,-1):
        n = j * i        
        N.append(n)

palindromes = []

for i in range(len(N)):
    if isapalindrome(N[i]) == 1:
        palindromes.append(N[i])
print(max(palindromes))
