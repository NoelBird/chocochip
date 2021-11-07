# 3
# 3 0
# 5 1 1
# 7 1 1
# from collections import defaultdict
from collections import deque
T = int(input())

g = {}

for i in range(T):
    tmp = list(map(int, input().split()))
    g[i] = tmp

q = deque()
q.extend(g[len(g)-1][2:])

visited = [0]*(T+1)
cnt = g[len(g)-1][0]

visited[len(g)-1] = True

while q:
    cur = q.popleft() - 1

    if visited[cur]:
        continue
    visited[cur] = True
    cnt += g[cur][0]
    q.extend(g[cur][2:])

print(cnt)