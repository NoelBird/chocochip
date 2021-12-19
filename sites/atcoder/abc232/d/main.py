M, N = map(int, input().split())

MAP = []

# create a MAP
for i in range(M):
    MAP.append(list(input()))

visited = {}

q = [((0, 0), 1)]
rslt = []
while q:
    cur = q.pop()
    pt = cur[0]
    cur_walk = cur[1]

    if pt in visited:
        continue

    visited[pt] = True

    # check below
    if pt[1]+1 < M and MAP[pt[1]+1][pt[0]] != "#":
        q.append([(pt[0], pt[1]+1), cur_walk+1])

    # check right
    if pt[0]+1 < N and MAP[pt[1]][pt[0]+1] != "#":
        q.append([(pt[0]+1, pt[1]), cur_walk+1])
    
    if not(pt[1]+1 < M and MAP[pt[1]+1][pt[0]] != "#") and not(pt[0]+1 < N and MAP[pt[1]][pt[0]+1] != "#"):
        rslt.append(cur_walk)

print(max(rslt))