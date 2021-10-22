import utility


print("1. 최적이진검색트리 구축 알고리즘")
class Node:
    def __init__(self, data):
        self.l_child=None
        self.r_child=None
        self.data = data

def tree(key, r, i, j):
    k = r[i][j]
    if k==0:
        return
    else:
        p = Node(key[k])
        p.l_child = tree(key, r, i, k-1)
        p.r_child = tree(key, r, k+1, j)
        return p

#데이터
key = [" ", "A", "B", "C", "D", "E"]
p = [0, 3/15, 1/15, 2/15, 5/15, 4/15]
n = len(p)-1 # n=5

a = [[0 for j in range(0, n+2)] for i in range(0, n+2)]
r = [[0 for j in range(0, n+2)] for i in range(0, n+2)]

for i in range(1, n+1):
    a[i][i-1] = 0
    a[i][i] = p[i]
    r[i][i] = i
    r[i][i-1] = 0
a[n+1][n] = 0
r[n+1][n] = 0

#최적 이진검색트리 구하기
def optsearchtree(n, p, r):
    for i in range(1, n+1):
        a[i][i-1] = 0
        a[i][i] = p[i]
        r[i][i] = i
        r[i][i-1] = 0
    a[n+1][n] = 0
    r[n+1][n] = 0

    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            temp = [a[i][k-1]+a[k+1][j] for k in range(i, j+1)] #list
            a[i][j] = min(temp) + sum([p[m] for m in range(i, j+1)])
            r[i][j] = temp.index(min(temp)) + i
    minavg = a[1][n]

optsearchtree(n, p, r)

utility.printMatrixF(a)
print()
utility.printMatrix(r)

root = tree(key, r, 1, n)
utility.print_inOrder(root)
print()
utility.print_postOrder(root)
print()
print()




print("2. DNA서열 맞춤 알고리즘")
import utility
a = ['C', 'A', 'C', 'A', 'T', 'T', 'A', 'C', 'C'] # 행
b = ['C', 'A', 'C', 'G', 'T', 'C', 'C', 'A'] # 열

m = len(a) # 행 개수 9
n = len(b) # 열 개수 8
table = [[0 for j in range(0, n+1)] for i in range(0, m+1)]
minindex = [[(0, 0) for j in range(0, n+1)] for i in range(0, m+1)]

for j in range(n-1, -1, -1): # 7, 6, 5, 4, 3, 2, 1, 0
    table[m][j] = table[m][j+1]+2

for i in range(m-1, -1, -1): # 8, 7, 6, 5, 4, 3, 2, 1, 0
    table[i][n] = table[i+1][n]+2


# 테이블 생성 구현
#opt(i, j) = min(opt(i+1, j+1)+penalty, opt(i+1, j)+2, opt(i, j+1)+2)
def opt_dsa(): # optimal DNA sequence alignment
    for i in range(m-1, -1, -1): # 8~0
        for j in range(n-1, -1, -1): # 7~0
            if a[i] == b[j]:
                penalty = 0
            else:
                penalty = 1
            temp = [table[i+1][j+1]+penalty, table[i+1][j]+2, table[i][j+1]+2] # 인덱스 0, 1, 2
            table[i][j] = min(temp) # 최소값 찾기
            idx = temp.index(min(temp)) # 최소값 인덱스 찾기
            if idx == 0:
                minindex[i][j] = (i+1, j+1)
            elif idx == 1:
                minindex[i][j] = (i+1, j)
            else:
                minindex[i][j] = (i, j+1)


opt_dsa() # 함수 실행(테이블 채우기)

print("")
utility.printMatrix(table)
print()
x = 0
y = 0

while x < m and y < n:
    tx, ty = x, y
    print(minindex[x][y])
    (x, y) = minindex[x][y]
    if x == tx + 1 and y == ty + 1:
        print(a[tx], " ", b[ty])
    elif x == tx and y == ty + 1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " ", " -")