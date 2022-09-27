import itertools

def permutations():
    y = itertools.permutations([0,1,2,3,4,5,6,7,8,9],10)
    x = list(y)
    print(x[999999])

permutations()