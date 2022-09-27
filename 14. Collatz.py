def collatz():
    array = dict()
    longest_seq = 0
    for i in range(1000000,2,-1):
        n = i
        j = 0
        while n != 1:
            if n%2 == 0:
                n = n/2
            elif n%2 != 0:
                n = 3*n+1
            j += 1
        else:
            array.update({i:j})   
    print(max(array, key = array.get))
collatz()