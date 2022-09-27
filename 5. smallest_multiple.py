def smallest_multiple(i):
    x = 1
    for j in range(1,21):
        if i%j == 0:
            continue
        else:
            x = 0
    return x

for i in range(1,1000000000):
    if smallest_multiple(i) == 1:
        print(i)
        break
    else:
        continue
s
