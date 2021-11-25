# (1) 빠른정렬 알고리즘 실습
print("(1)Quicksort Algorithm")
import random
import matplotlib.pyplot as plt
#%matplotlib inline #주피터 노트북에서

global count #데이터 비교 횟수 측정(if(s[i] < pivotItem))
count = 0

def quickSort(s, low, high):
    pivotpoint = 0
    if low < high:
        pivotpoint = partition(s, low, high, pivotpoint)
        quickSort(s, low, pivotpoint-1)
        quickSort(s, pivotpoint+1, high)

def partition(s, low, high, pivotpoint):
    global count
    pivotitem = s[low]
    j = low
    i = low + 1
    while i <= high:
        if s[i] < pivotitem:
            j += 1
            s[i], s[j] = s[j], s[i]
            count += 1
        i += 1
    pivotpoint = j
    s[low], s[pivotpoint] = s[pivotpoint], s[low]
    return pivotpoint

n = [8, 16, 24, 32, 40]
set = []
for k in range(5):
    set.append([[random.randrange(n[k]+1) for i in range(n[k])] for j in range(20)] )
# n=8, 16, .. 40일때의 각각 20개 데이터셋(중복허용) 저장

avg_count_compare = [] # 평균 비교횟수의 리스트 (ex) count_compare[0]은 set[0]의 평균)

for i in range(len(n)):
    sum = 0 # 비교횟수의 합
    for j in range(len(set[i])):
        quickSort(set[i][j], 0, len(set[i][j])-1)
        sum += count
        count = 0 # 비교횟수를 새로 측정하기 위해 글로벌 변수 초기화
    avg_count_compare.append(sum/len(set[i])) # 비교횟수의 평균을 저장해준다

print(f'avg_count_compare: {avg_count_compare}')
print()
print()
plt.figure()
plt.plot(avg_count_compare)
plt.show()
#증가하는 그래프의 곡선이 나타난다. f(n) = n
# 가로축은 n, 세로축은 평균 데이터 비교 횟수



# (2) 쉬트라센 알고리즘 실습
print('(2)Strassen Algorithm')
import numpy as np
def strassen(n, A, B, C):
    threshold = 2
    A11 = np.array([[A[rows][cols] for cols in range(int(n/2))]\
                  for rows in range(int(n/2))])
    A12 = np.array([[A[rows][cols+int(n/2)] for cols in range(int(n/2))]\
                  for rows in range(int(n/2))])
    A21 = np.array([[A[rows+int(n/2)][cols] for cols in range(int(n/2))]\
                  for rows in range(int(n/2))])
    A22 = np.array([[A[rows+int(n/2)][cols+int(n/2)] for cols in range(int(n/2))]\
                  for rows in range(int(n/2))])
    B11 = np.array([[B[rows][cols] for cols in range(int(n/2))]\
                  for rows in range(int(n/2))])
    B12 = np.array([[B[rows][cols+int(n/2)] for cols in range(int(n/2))]\
                    for rows in range(int(n/2))])
    B21 = np.array([[B[rows+int(n/2)][cols] for cols in range(int(n/2))]\
                    for rows in range(int(n/2))])
    B22 = np.array([[B[rows+int(n/2)][cols+int(n/2)] for cols in range(int(n/2))]\
                    for rows in range(int(n/2))])

    # print(A11, A12, A21, A22, B11, B12, B21, B22, sep='\n') 결과 테스트
    if n <= threshold:
        C = np.array(A) @ np.array(B)
    else:
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = np.array([])
        M1 = strassen(int(n/2), (A11+A22), (B11+B22), M1)
        M2 = strassen(int(n/2), (A21+A22), B11, M2)
        M3 = strassen(int(n/2), A11, (B12-B22), M3)
        M4 = strassen(int(n/2), A22, (B21-B11), M4)
        M5 = strassen(int(n/2), (A11+A12), B22, M5)
        M6 = strassen(int(n/2), (A21-A11), (B11+B12), M6)
        M7 = strassen(int(n/2), (A12-A22), (B21+B22), M7)
        #행렬 병합하기
        C = np.vstack([np.hstack([M1+M4-M5+M7, M3+M5]),\
                       np.hstack([M2+M4, M1+M3-M2+M6])])
    return C

n = 4
A = [[1 for cols in range(n)] for rows in range(n)]
B = [[2 for cols in range(n)] for rows in range(n)]
A = [[1, 2, 0, 2], [3, 1, 0, 0], [0, 1, 1, 2], [2, 0, 2, 0]]
B = [[0, 3, 0, 2], [1, 1, 4, 0], [1, 1, 0, 2], [0, 5, 2, 0]]
C = np.array(A)@np.array(B)
D = [[0 for cols in range(n)]for rows in range(n)]
print('단순한 알고리즘:\n', C)
print()
D = strassen(n, A, B, D)
print('쉬트라쎈 알고리즘:\n', D)
