# TLE
N, K = map(int, input().split()) # N department, K employee
l = list(map(lambda x: -int(x), input().split()))

import heapq

l.sort()
heapq.heapify(l)

cnt = 0
while len(l) >= K:
    idx_last = len(l)-1
    ll = []
    for i in range(K):
        ll.append(heapq.heappop(l))
    subtract_val = ll[K-1] if ll[K-1] > -K else -K
    for k in range(K):
        ll[k] -= subtract_val
        if ll[k] < 0:
            heapq.heappush(l, ll[k])
    cnt -= subtract_val

print(cnt)