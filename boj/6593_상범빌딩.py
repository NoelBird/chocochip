# 3 4 5
# S....
# .###.
# .##..
# ###.#
#
# #####
# #####
# ##.##
# ##...
#
# #####
# #####
# #.###
# ####E
#
# 1 3 3
# S##
# #E#
# ###
#
# 0 0 0

from collections import deque

###################변수 부분#####################
actions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0,), (0, -1, 0,), (0, 0, 1,), (0, 0, -1,)]

###################함수 부분#####################
def bfs(g, p_begin):
    # visited graph만들기
    global L
    global R
    global C
    vis = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

    # 변수 초기화
    q = deque([p_begin])
    l, x, y = p_begin
    vis[l][y][x] = True

    cnt = 0

    while q:
        for _ in range(len(q)):
            l, x, y = q.popleft()
            if g[l][y][x] == 'E':
                return cnt
            for action in actions:
                l_next = l + action[0]
                x_next = x + action[1]
                y_next = y + action[2]
                if 0 <= l_next < L and 0 <= x_next < C and 0 <= y_next < R:
                    if vis[l_next][y_next][x_next]:
                        continue
                    if g[l_next][y_next][x_next] == '#':
                        continue
                    vis[l_next][y_next][x_next] = True
                    q.append((l_next, x_next, y_next))
        cnt += 1
    return -1


###################입력 부분#####################
while True:
    L, R, C = map(int, input().split())  # L: 빌딩의 층 수, R, C는 행, 열의 수
    if (L, R, C) == (0, 0, 0):
        break
    g = []
    p_begin = None
    for i in range(L):
        tmp = []
        for j in range(R):
            tmp.append(list(input()))
            for k in range(C):
                if tmp[j][k] == 'S':
                    p_begin = (i, k, j) # 레벨, x, y
        input()
        g.append(tmp)
    # print(g)
    # print(p_begin)
    ans = bfs(g, p_begin)
    if ans == -1:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % ans)
