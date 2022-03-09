import heapq
N = int(input())

l = []
for _ in range(N):
    V = int(input())
    if V == 0:
        if len(l) == 0:
            print(0)
        else:
            print(-heapq.heappop(l))
    else:
        heapq.heappush(l, -V)