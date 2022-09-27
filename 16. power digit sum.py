y = 2**1000
y = str(y)
array = []
for i in range(len(y)):
    array.append(int(y[i]))
print(array)
print(sum(array))