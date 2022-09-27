def divisors_sum(n):
    divisors = []
    for j in range(1,(n+2)//2):
        if n%j == 0:
            divisors.append(j)
    return sum(divisors)

def amicable_numbers():
    full_list = {}
    for i in range(1,10000):
        full_list.update({i:divisors_sum(i)})
    amicable = []
    for j in full_list:
        x = divisors_sum(j)
        if full_list.get(j) == x and full_list.get(x) == j and j!=full_list.get(j):
        #if divisors_sum(x) == j and divisors_sum(j) == x:
            amicable.append(j)
        # if divisors_sum(j) == j:
        #     amicable.append(j)
    print(sum(amicable))

amicable_numbers()