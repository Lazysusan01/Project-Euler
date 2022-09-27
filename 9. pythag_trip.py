import time
def pythag_triplet():
    A = []
    B = []
    C = []
    triplet = []
    for i in range(1,500):
        for j in range(i+1,500):
            A.append(i)
            B.append(j)
            c = 1000-i-j
            C.append(c)
    print(A,B,C)
    for k in range(len(C)):
        if ((A[k]**2) + (B[k]**2))==(C[k]**2):
            print(A[k],B[k],C[k])
            time.sleep(100)
pythag_triplet()