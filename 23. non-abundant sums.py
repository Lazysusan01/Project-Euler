def divisors_sum(n):
    divisors = []
    for j in range(1,(n+2)//2):
        if n%j == 0:
            divisors.append(j)
    return sum(divisors)

def abundant_numbers():
    full_list = {}
    sum_list = []
    for i in range(1,28124):
        full_list.update({i:divisors_sum(i)})
    abundant = []
    not_in_sum_list = []
    for j in full_list:
        x = divisors_sum(j)
        if j<full_list.get(j):
        #if divisors_sum(x) == j and divisors_sum(j) == x:
            abundant.append(j)
        # if divisors_sum(j) == j:
        #     abundant.append(j)
    #print(abundant)
    for i in abundant:
        for j in abundant:
            sum_list.append(j+i)
    for i in range(28124):
        if i not in sum_list:
            not_in_sum_list.append(i)    
    print(sum(not_in_sum_list))
abundant_numbers()