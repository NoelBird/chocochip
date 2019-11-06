# 다시 풀어보기

import sys
from collections import defaultdict
rdl = sys.stdin.readline

d = defaultdict(list)
N, M, V = map(int, rdl().split(' '))
for _ in range(M):
    a, b = map(int, rdl().split())
    d[a].append(b)
    d[b].append(a)

def dfs(d, V):
    visited = []
    stack = [V]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += sorted(list(set(d[n]) - set(visited)), reverse=True)
    return visited
print(*dfs(d, V))

def bfs(d, V):
    visited = []
    queue = [V]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += sorted(list(set(d[n]) - set(visited)))
    return visited
print(*bfs(d, V))
