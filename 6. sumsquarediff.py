import math
def sumsquaredifference():
    n = []
    n_squared = []
    x = int(input())
    for i in range(1,x+1):
        i2 = i**2
        n_squared.append(i2)
        n.append(i)
    result = (sum(n)**2)- sum(n_squared)
    print(result)
sumsquaredifference()
