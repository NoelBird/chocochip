# 3 2
# 1 2 3
from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
l = list(map(int, input().split()))

q = l[:K]
heapify(q)
a = heappop(q)
print(a)
heappush(q, a)
for i in range(K, N):
    minVal = heappop(q)
    if l[i] > minVal:
        heappush(q, l[i])
        a = heappop(q)
        print(a)
        heappush(q, a)
    else:
        print(minVal)
        heappush(q, minVal)
