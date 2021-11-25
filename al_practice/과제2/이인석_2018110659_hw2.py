
memory_used = [0]
#합병정렬1
'''
def mergeSort(n, s):
    h = int(n / 2)
    m = n - h
    if n > 1:
        u = s[:h]
        v = s[h:]
        memory_used.append(memory_used[-1] + len(u))
        memory_used.append(memory_used[-1] + len(v))
        mergeSort(h, u)
        memory_used.append(memory_used[-1] - len(u))
        mergeSort(m, v)
        memory_used.append(memory_used[-1] - len(u))
        merge(h, m, u, v, s)

# 리스트에 메모리의 사용량을 저장하면, 리스트의 MAX값이 결국에는
#시스템이 필요로 하는 메모리의 크기가 된다.
# 저장하는 방식 -> 리스트가 생성될 때마다 추가, 반환할 때마다 삭제

def merge(h, m, u, v, s):
    i, j, k = 0, 0, 0

    while i < h and j < m:
        if u[i] < v[j]:
            s[k] = u[i]
            i += 1
        else:
            s[k] = v[j]
            j += 1
        k += 1

    if i >= h:
        while j < m:
            s[k] = v[j]
            j += 1
            k += 1

    else:
        while i < h:
            s[k] = u[i]
            i += 1
            k += 1

s = [11,5,2,16, 12,1,8,15, 6,14,9,3, 10,7,13,4]
mergeSort(8, s)
print('added_storage: ', max(memory_used))
print(s)
'''

#합병정렬2
def mergeSort2(s, low, high):
    if low < high:
        mid = int((low + high)/2)
        mergeSort2(s, low, mid)
        mergeSort2(s, mid + 1, high)
        merge2(s, low, mid, high)
        memory_used.append((high - low + 1))

def merge2(s, low, mid, high):
    i, j, k = low, mid + 1, low
    u = []
    while i <= mid and j <= high:
        if s[i] < s[j]:
            u.append(s[i])
            i += 1
        else:
            u.append(s[j])
            j += 1
        k += 1

    if i > mid:
        while j <= high:
            u.append(s[j])
            j += 1
            k += 1
    else:
        while i <= mid:
            u.append(s[i])
            i += 1
            k += 1

    t = 0
    for i in range(low, high+1):
        s[i] = u[t]
        t += 1

s = [11,5,2,16, 12,1,8,15, 6,14,9,3, 10,7,13,4]
mergeSort2(s, 0, 7)
print('added_storage2: ', max(memory_used))
print(s)
