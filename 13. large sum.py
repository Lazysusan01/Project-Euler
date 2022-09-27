def largesum():
    n = open("Project Euler\longnumber.txt")
    array = []
    results = [int(x) for x in n.readlines()]
    result = sum(results)
    print(result)
largesum()