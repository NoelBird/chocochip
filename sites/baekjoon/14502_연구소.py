from collections import deque
import sys
input = sys.stdin.readline

############
# 전역 변수 #
############
actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

############
# 함수 부분 #
############
def spread_virus(g, NM, l_virus):
    N, M = NM

    vis = [[False for _ in range(M)] for _ in range(N)] # 방문여부 체크

    for virus in l_virus:
        q = deque([virus])
        x, y = virus
        vis[y][x] = True

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for action in actions:
                    x_next = x + action[0]
                    y_next = y + action[1]

                    if 0 <= x_next < M and 0 <= y_next < N and not vis[y_next][x_next] and g[y_next][x_next] == 0:
                        vis[y_next][x_next] = True
                        q.append((x_next, y_next))
    ret_g = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if g[i][j] or vis[i][j]:
                ret_g[i][j] = 1
    return ret_g

def calc_max(g, MN):
    M, N = MN
    vis = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not vis[i][j] and not g[i][j]:
                vis[i][j] = True
                cnt += 1
                q = deque([(j, i)])
                while q:
                    for _ in range(len(q)):
                        x, y = q.popleft()
                        for action in actions:
                            x_next = x + action[0]
                            y_next = y + action[1]

                            if 0 <= x_next < M and 0 <= y_next < N and not vis[y_next][x_next] and g[y_next][x_next] == 0:
                                vis[y_next][x_next] = True
                                cnt += 1
                                q.append((j, i))
    return cnt

############
# 입력 부분 #
############
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

N, M = map(int, input().split())
g = []
l_virus = []
for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(M):
        if g[i][j] == 2:
            l_virus.append((j, i))

max_val = 0
i1 = 0

for n1 in range(M*N):
    i1 = n1 // M
    j1 = n1 % M
    if g[i1][j1] != 0:
        continue
    tmp1 = 1
    g[i1][j1], tmp1 = tmp1, g[i1][j1]
    for n2 in range(n1+1, M*N):
        i2 = n2 // M
        j2 = n2 % M
        if g[i2][j2] != 0:
            continue
        tmp2 = 1
        g[i2][j2], tmp2 = tmp2, g[i2][j2]
        for n3 in range(n2+1, M*N):
            i3 = n3 // M
            j3 = n3 % M
            if g[i3][j3] != 0:
                continue
            tmp3 = 1
            g[i3][j3], tmp3 = tmp3, g[i3][j3]
            virus_map = spread_virus(g, (N, M), l_virus)
            ans = calc_max(virus_map, (M, N))
            if ans > max_val:
                max_val = ans
            g[i3][j3], tmp3 = tmp3, g[i3][j3]
        g[i2][j2], tmp2 = tmp2, g[i2][j2]
    g[i1][j1], tmp1 = tmp1, g[i1][j1]

print(max_val)