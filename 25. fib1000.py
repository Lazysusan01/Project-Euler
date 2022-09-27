def fibonacci1000():
    x = 0
    y = 1
    z= 1
    index = 1
    while len(str(z))<1000:
        z = x+y
        x = y
        y = z
        index += 1 
    print(index)

fibonacci1000()
