def findprimes():
    n = input()
    try:
        n = int(n)
    except ValueError:
        print('Invalid input')
        findprimes()
    primes =[]
    while len(primes)<=n:
        for j in range(2,(n+1)//2):
            if i%j == 0:
                continue
        else:
            primes.append(i)
    primes.remove(4)
    print(primes)
    findprimes()
findprimes()
