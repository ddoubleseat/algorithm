# 1. Dijkstra 알고리즘
inf = 1000
w = [[0, 7, 4, 6, 1], [inf, 0, inf, inf, inf],
     [inf, 2, 0, 5, inf], [inf, 3, inf, 0, inf], [inf, inf, inf, 1, 0]]
n = 5
f = set()
touch = n * [0]
length = n * [0]
save_length = n * [0]

for i in range(1, n):
    length[i] = w[0][i]

for r in range(n - 1):
    mmin = inf
    for i in range(1, n):
        if 0 <= length[i] and length[i] < mmin:
            mmin = length[i]
            vnear = i
    e = (touch[vnear], vnear)

    f.add(e)
    for i in range(1, n):
        if vnear == i:
            save_length[i] = length[i]
            continue
        if length[vnear] + w[vnear][i] < length[i]:
            length[i] = length[vnear] + w[vnear][i]
            touch[i] = vnear

    length[vnear] = -1

print(f)

print(save_length)

# 2 n-Queens 알고리즘
# import utility
#
# e = {0: [1, 2, 3], 1: [2, 5], 2: [3, 4, 5, 6], 3: [4, 6], 4: [6, 7]}
# n = 8
# a = [[0 for j in range(0, n)] for i in range(0, n)]
# for i in range(0, n - 1):
#     for j in range(i + 1, n):
#         if i in e:
#             if j in e[i]:
#                 a[i][j] = 1
#                 a[j][i] = 1
# utility.printMatrix(a)
#
# visited = n * [0]
#
#
# def DFS(a, v):
#     print(v)
#     visited[v] = 1
#     if v in e:
#         for i in e[v]:
#             if visited[i] != 1:
#                 DFS(a, i)
#
#
# DFS(a, 0)
# print('\n\n ---------------------------\n\n')
#
#
# def promising(i, col):
#     k = 0
#     switch = True
#     while (k < i and switch):
#         if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
#             switch = False
#         k += 1
#
#     return switch
#
#
# def queens(n, i, col):
#     if promising(i, col):
#         if i + 1 == n:
#             print(col)
#         else:
#             for j in range(0, n):
#                 col[i + 1] = j
#                 queens(n, i + 1, col)
#
# n = 7
# col = n * [0]
# queens(n, -1, col)
