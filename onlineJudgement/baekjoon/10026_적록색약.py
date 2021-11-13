from collections import deque
# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR


def bfs(x, y, color):
    global g
    global actions
    global visited
    global N
    global cnt_normal

    if visited[y][x]:
        return
    q = deque([(x, y)])

    while q:
        for _ in range(len(q)):
            cur_x, cur_y = q.popleft()
            if not visited[cur_y][cur_x]:
                visited[cur_y][cur_x] = True
                for action in actions:
                    next_x = cur_x + action[0]
                    next_y = cur_y + action[1]
                    if 0 <= next_x < N and 0 <= next_y < N:
                        if not visited[next_y][next_x] and color == g[next_y][next_x]:
                            q.append((next_x, next_y))
    cnt_normal += 1


def bfs_weak(x, y, color):
    global g
    global actions
    global visited
    global N
    global cnt_weak

    if visited[y][x]:
        return
    q = deque([(x, y)])

    while q:
        for _ in range(len(q)):
            cur_x, cur_y = q.popleft()
            if not visited[cur_y][cur_x]:
                visited[cur_y][cur_x] = True
                for action in actions:
                    next_x = cur_x + action[0]
                    next_y = cur_y + action[1]
                    if 0 <= next_x < N and 0 <= next_y < N:
                        if not visited[next_y][next_x] and color == g[next_y][next_x]:
                            q.append((next_x, next_y))
    cnt_weak += 1

actions = ((1, 0), (-1, 0), (0, 1), (0, -1))
# initialize
N = int(input())
g = []
cnt_normal = 0
cnt_weak = 0


visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    g.append(list(input()))

for y in range(N):
    for x in range(N):
        bfs(x, y, g[y][x])


visited = [[False for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if g[y][x] == 'G':
            g[y][x] = 'R'

for y in range(N):
    for x in range(N):
        bfs_weak(x, y, g[y][x])

print(cnt_normal, cnt_weak)