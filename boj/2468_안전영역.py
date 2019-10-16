import sys
from collections import deque

input = sys.stdin.readline

#####################################################
#################### 전역 변수 #######################
#####################################################
vis = []
actions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#####################################################
#################### 함수 부분 #######################
#####################################################
def bfs(g, xy, level):
    global N
    global vis

    x, y = xy
    if vis[y][x] or g[y][x] - level <= 0: # 이미 방문한 경우
        return 0

    q = deque([xy])
    vis[y][x] = True

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for action in actions:
                x_next = x + action[0]
                y_next = y + action[1]
                if 0 <= x_next < N and 0 <= y_next < N and not vis[y_next][x_next]:
                    if g[y_next][x_next] - level <= 0:
                        continue
                    vis[y_next][x_next] = True
                    q.append((x_next, y_next))
    return 1

def find_class(g, level):
    global N
    global vis

    vis = [[False for _ in range(N)] for _ in range(N)] # 변수 초기화
    n_class = 0
    for i in range(N):
        for j in range(N):
            n_class += bfs(g, (j, i), level)
    return n_class


#####################################################
#################### 입력 부분 #######################
#####################################################
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
N = int(input())
g = []
val_min = 100
val_max = 1
ans = 0
for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(N):
        cur_val = g[i][j]
        if cur_val > val_max:
            val_max = cur_val
        if cur_val < val_min:
            val_min = cur_val

is_all_same = True

tmp = g[0][0]
for i in range(N):
    for j in range(N):
        if g[i][j] != tmp:
            is_all_same = False
            break

if is_all_same:
    print(1)
else:
    for i in range(val_min, val_max + 1):
        tmp = find_class(g, i)
        if tmp > ans:
            ans = tmp
    print(ans)
