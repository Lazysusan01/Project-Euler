def number_letter():
    array = []
    for i in range (1,100):
        array.append(str(i))
        # print single digits
    try:
        print(array[5][-1])
    except:
        print('Something broke')

number_letter()