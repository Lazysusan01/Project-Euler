import math
def print_factors():
    n = int(input())
    factors = []
    prime_factors = []
    for i in range(1,(n+2)//2):
        if n % i == 0:
            factors.append(i)
    print(factors)
    for i in factors:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            prime_factors.append(i)
    print(prime_factors)
    print_factors()
        
print_factors()
