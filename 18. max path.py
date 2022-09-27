def max_path():
    maxpath = open("maxpathtext.txt")
    maxpath_array = [x.strip('\n') for x in maxpath.readlines()]
    maxpathsplit = []
    global maxpathints
    maxpathints = []
    global paths
    paths = []

    for i in maxpath_array:
        maxpathsplit.append(i.split(' '))
    
    for i in maxpathsplit:
        i = list(map(int,i))
        maxpathints.append(i)
        #print(i)
    return maxpathints

def binary():
    x = 2**14
    print(bin(x))
    y = [] 
    for i in range(x):
        z = bin(x-i)
        y.append(z)

    global new_y
    new_y = []

    for i in range(len(y)):
        j = y[i][2:]
        j = j.zfill(14)
        new_y.append(j)
        
    return new_y

# def adjacent(i,j):
#     # take in coords of maxpathints
#     x = maxpathints[i+1][j], maxpathints[i+1][j+1]
#     if x[0] > x[1]:
#          y = x[0]
#     else:
#          y = x[1]
#          j = j+1
#     i = i+1
#     paths.append(y)
#     print(i,j)
#     try:
#         adjacent(i,j)
#     except:
#         IndexError
    
    #outputs coords of adjacent on next line
    # i-->i+1 
    #j-->j & j+1
#find which is bigger, append to path

max_path()
binary()

print(len(new_y))

def summing(): 
    for i in range(len(new_y)):
        x = 0
        path = []
        for j in range(len(maxpathints)):
            path.append(maxpathints[j][x])
            x = x + int(new_y[i][-j])
        paths.append(sum(path))
summing()

print(new_y[0])

print(max(paths))


    #make some ticker for x coord within loop over binaries
    # add new_y[-i] to ticker
    #append maxpathints