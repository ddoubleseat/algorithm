import utility
import numpy as np

#최적의 해를 주는 순서의 출력
def order(p, i, j):
    if i==j:
        print("A{}".format(i), end="")
    else:
        k = p[i][j]
        print("(", end="")
        order(p, i, k)
        order(p, k+1, j)
        print(")", end="")

# A1=5x2, A2=2x3, A3=3x4, A4=4x5, A5=6x7, A6=7x8
d = [5, 2, 3, 4, 6, 7, 8]
n = len(d)-1 #6

m = [[0 for j in range(1, n+2)] for i in range(1, n+2)]
p = [[0 for j in range(1, n+2)] for i in range(1, n+2)]

#minmult함수 구현
def minmult(n, d, p):
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            temp = [m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j] for k in range(i, j)]
            m[i][j] = min(temp)
            p[i][j] = temp.index(min(temp)) + i
    return m[1][n]

print("n개의 행렬 곱셈의 최소 횟수: ", minmult(n, d, p))

print()
print("M matrix")
utility.printMatrix(m)
print()
print("P matrix")
utility.printMatrix(p)
print()
print("최적의 해를 주는 순서의 출력")
order(p, 1, 6)