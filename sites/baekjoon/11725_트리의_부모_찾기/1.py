from collections import defaultdict
# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
N = int(input())

d = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    d[a] += [b]
    d[b] += [a]

parent = [0]*(N+1)
visited = [0]*(N+1)

q = [1]
parent[1] = 1
while q:
    cur = q.pop(0)
    for item in d[cur]:
        if parent[item]:
            continue
        parent[item] = cur
        q.append(item)

print('\n'.join(map(str, parent[2:])))