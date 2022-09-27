import sys
def triangle():
    seq = []
    for i in range(20000):
        x=0
        for j in range(i):
            x = x + j
        seq.append(x)
    #print(seq)
    dict_triangles = {i:i for i in seq}
    y = 0 
    for i in dict_triangles:
        x = []
        x.append(i)
        for j in range(1,(i+1)//2):
            if i%j == 0:
                x.append(j)
        dict_triangles.update({i:x})
        print(str(y) + " " + str(i))
        if len(dict_triangles[i]) > y:
            y = len(dict_triangles[i])
            print(y)
        if len(dict_triangles[i]) > 500:
            print(dict_triangles[i])
            sys.exit()


triangle()