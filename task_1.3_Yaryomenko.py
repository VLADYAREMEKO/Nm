import numpy as np
from math import sqrt
def choleskyDecomposition(A):
    L = np.zeros((len(A),len(A)),float)
    L[0, 0] = sqrt(A[0, 0])
    for j in range(1, len(A), 1):
        L[j, 0] = A[j, 0]/L[0, 0]
    for i in range(1, len(A), 1):
        arr = []
        for p in range(0, i, 1):
            arr.append(L[i, p]**2)
        L[i, i] = sqrt(A[i, i] - sum(arr))
    for i in range(1, len(A)-1, 1):
        for j in range(i+1, len(A)):
            arr = []
            for p in range(1, i, 1):
                arr.append(L[i, p]*L[j, p])
            L[j, i] = (A[j, i] - sum(arr))/L[i, i]
    return L
if __name__=="__main__":
    A=np.array([[17,3,10],[3,17,-2],[10,-2,12]],float)
    L = choleskyDecomposition(A)
    print(L)