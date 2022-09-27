def fibonacci():
    n = input()
    try:
        n = int(n)
    except ValueError:
        print('Invalid')
        fibonacci()
    x = 0
    y = 1
    fib = []
    for i in range(n):
        z = x+y
        x = y
        y = z
        if z<4000000:
            fib.append(z)
        else:
            continue
    even_fib = []
    for i in range(len(fib)):
        if fib[i]%2 == 0:
            even_fib.append(fib[i])
        else:
            continue
    print(even_fib)
    print(sum(even_fib))
    fibonacci()
fibonacci()
