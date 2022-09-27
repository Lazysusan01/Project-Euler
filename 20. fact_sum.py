def factorial_sum():
    x = 100
    y = x
    for i in range(1,x):
        y=y * (x-i)
    str1 = str(y)
    print(y)
    def split(number):
        return [char for char in number]
    list1 = split(str1)
    x_list = list(map(int,list1))
    print(sum(x_list))
factorial_sum()