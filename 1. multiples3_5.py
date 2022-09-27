def multiples(n):
    array = []
    for i in range(n):
        if i%3 ==0:
            array.append(i)
        elif i%5==0:
            array.append(i)
        else:
            continue
    print(array)
    print(sum(array))
    
n = int(input())
multiples(n)
