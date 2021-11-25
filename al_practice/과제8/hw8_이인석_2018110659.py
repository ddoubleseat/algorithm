# 1. 분기한정 가지치기로 깊이우선검색
def kp(i, profit, weight):
    global bestset
    global maxp

    if (weight <= W and profit > maxp):
        maxp = profit
        bestset = include[:]

    if (promising(i, weight, profit)):
        include[i + 1] = 1
        kp(i + 1, profit + p[i + 1], weight + w[i + 1])
        include[i + 1] = 0
        kp(i + 1, profit, weight)

def promising(i, weight, profit):
    global maxp

    if weight >= W:
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while (j < n and totweight + w[j] <= W):
            totweight = totweight + w[j]
            bound = bound + p[j]
            j += 1

    k = j
    if k < n: bound = bound + (W + totweight) * p[k] / w[k]

    return bound > maxp

n = 4
W = 16
p = [20, 40, 24, 40]
w = [2, 5, 4, 8]
maxp = 0
include = [0, 0, 0, 0]
bestset = [0, 0, 0, 0]
kp(-1, 0, 0)
print(maxp)
print(bestset)


# 2. 분기한정 가지치기로 최고우선검색
# import queue
#
# class Node:
#     def __init__(self, level, weight, profit, bound, include):
#         self.level = level
#         self.weight = weight
#         self.profit = profit
#         self.bound = bound
#         self.include = include
#
#     def __cmp__(self, other):
#         return cmp(self.bound, other.bound)
#
#     def __repr__(self):
#         s = "node : level:{0}, weight:{1}, profit:{2}, bound:{3}".format(self.level, self.weight, self.profit,
#                                                                          self.bound)
#         return s
#
#     def __lt__(self, other):
#         return self.bound < other.bound
#
# def kp_Best_FS():
#     global maxProfit
#     global bestset
#     temp = n * [0]
#     v = Node(-1, 0, 0, 0.0, temp)
#     v.bound = compBound(v)
#
#     PQ = queue.PriorityQueue()
#     PQ.put((v.bound, v))
#
#     while (not PQ.empty()):
#         v = PQ.get()[1]
#         u = Node(-1, 0, 0, 0.0, temp)
#
#         # print("get:",v , "\nmp:",maxProfit)
#         if (v.bound < -maxProfit):
#             u.level = v.level + 1
#             u.weight = v.weight + w[u.level]
#             u.profit = v.profit + p[u.level]
#             u.include = v.include[:]
#             # print(u)
#             if (u.weight <= W and u.profit > maxProfit):
#                 maxProfit = u.profit
#                 # print("update mp:",maxProfit)
#             # print(u.include)
#
#             u = Node(u.level, u.weight, u.profit, 0.0, u.include[:])
#             # print("전",u)
#             u.bound = compBound(u)
#
#             # print("후",u)
#             u.include[u.level] = 1
#             # print("1:",u.include)
#
#             if u.bound < -maxProfit:
#                 # print("insert",u)
#                 PQ.put((u.bound, u))
#                 bestset = u.include[:]
#             # u.weight = v.weight
#             # u.profit = v.profit
#
#             # print("전",u)
#             u = Node(u.level, v.weight, v.profit, 0.0, u.include[:])
#             u.bound = compBound(u)
#             # print("후",u)
#             u.include[u.level] = 0
#             # print("2:",u.include)
#
#             if u.bound < -maxProfit:
#                 # print("insert",u)
#                 PQ.put((u.bound, u))
#                 bestset = u.include[:]
#
# def compBound(u):
#     if u.weight >= W:
#         return 0
#     else:
#         result = u.profit
#         j = u.level + 1
#         totweight = u.weight
#         while (j < n and totweight + w[j] <= W):
#             totweight += w[j]
#             result += p[j]
#             j += 1
#         k = j
#         if k < n:
#             result += (W - totweight) * p[k] / w[k]
#
#         return -result
#
# # heap이 minheap이라 bound를 계산하여 -를 하여 리턴한다. 비교를 < maxProfit으로 수행한다.
# n = 4
# W = 16
# p = [20, 40, 24, 40]
# w = [2, 5, 4, 8]
# include = [0] * n
# maxProfit = 0
# bestset = n * [0]
# kp_Best_FS()
# print(bestset)
# print(maxProfit)