def name_score():
    names = open("p022_names.txt")
    x = names.read()
    x = x.replace('"','')
    x = x.split(',')
    x.sort()
    #print(x)
    alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26} 
    #alpha_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    words = []
    for i in range(len(x)):
        word = []
        for j in range(len(x[i])):
            letter = alphabet.get(x[i][j])
            word.append(letter)
        words.append(sum(word)*(i+1))
    print(sum(words))
name_score()