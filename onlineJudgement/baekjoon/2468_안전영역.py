from collections import deque
import sys
input = sys.stdin.readline

#########################전역 변수#################################
grps = 0
actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#########################함수 부분#################################
def bfs(g, cur_level, xy):
    global N
    global vis
    global grps

    x, y = xy
    if vis[y][x]:
        return

    if g[y][x] - cur_level <= 0:
        return

    q = deque([xy])
    vis[y][x] = True
    grps += 1

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for action in actions:
                x_next = x + action[0]
                y_next = y + action[1]

                if 0 <= x_next < N and 0 <= y_next < N:
                    if vis[y_next][x_next]: # 이미 방문한 경우 continue
                        continue
                    if g[y_next][x_next] - cur_level <= 0:
                        continue

                    vis[y][x] = True
                    q.append((x_next, y_next))


def find_grps(g, cur_level):
    global N
    global grps
    global vis
    grps = 0 # 그룹의 개수 초기화
    vis = [[False for _ in range(N)] for _ in range(N)] # 방문여부 초기화
    for i in range(N):
        for j in range(N):
            bfs(g, cur_level, (j, i)) # x, y
    return grps



#########################입력 부분#################################
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
N = int(input())
g = []
vis = []
min_val, max_val = 100, 1 # 초기화
for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(N):
        if g[i][j] < min_val:
            min_val = g[i][j]
        if g[i][j] > max_val:
            max_val = g[i][j]

max_grp = 0
for i in range(min_val, max_val + 1):
    ans = find_grps(g, i)
    if ans > max_grp:
        max_grp = ans
print(max_grp)
