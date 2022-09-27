def largest_product():
    x = input()
    x_list = list(x)
    x_list = list(map(int,x_list))
    answers = []
    for i in range(len(x_list)):
        new_list = x_list[i:i+13]
        print(new_list)
        result = 1
        for i in new_list:
            result = result * i
        answers.append(result)
    print(max(answers))
    
largest_product()
