from collections import deque
import sys
input = sys.stdin.readline
############
# 전역 변수 #
############
actions = {}
actions[1] = [0, 90, 180, 270]
actions[2] = [0, 90]
actions[3] = [0, 90, 180, 270]
actions[4] = [0, 90, 180, 270]
actions[5] = [0]

############
# 함수 부분 #
############
def find_safe(g, cctv, cctv_states):
    global N
    global M
    def fill_right(g_cpy, cctv, i_cctv):
        i = cctv[i_cctv][1]
        for j in range(cctv[i_cctv][0] + 1, M):
            if g_cpy[i][j] == 6:
                break
            if g_cpy[i][j] == 0:
                g_cpy[i][j] = 7  # 광선의 경우 7로 표시
    def fill_up(g_cpy, cctv, i_cctv):
        j = cctv[i_cctv][0]
        for i in range(cctv[i_cctv][1] - 1, -1, -1):
            if g_cpy[i][j] == 6:
                break
            if g_cpy[i][j] == 0:
                g_cpy[i][j] = 7  # 광선의 경우 7로 표시
    def fill_left(g_cpy, cctv, i_cctv):
        i = cctv[i_cctv][1]
        for j in range(cctv[i_cctv][0] - 1, -1, -1):
            if g_cpy[i][j] == 6:
                break
            if g_cpy[i][j] == 0:
                g_cpy[i][j] = 7  # 광선의 경우 7로 표시
    def fill_down(g_cpy, cctv, i_cctv):
        j = cctv[i_cctv][0]
        for i in range(cctv[i_cctv][1] + 1, N):
            if g_cpy[i][j] == 6:
                break
            if g_cpy[i][j] == 0:
                g_cpy[i][j] = 7  # 광선의 경우 7로 표시
    g_cpy = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            g_cpy[i][j] = g[i][j]

    for i_cctv in range(len(cctv)):
        if cctv[i_cctv][2] == 1 and cctv_states[i_cctv] == 0: # cctv가 1번 종류고 각도가 0도인 경우
            fill_right(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 1 and cctv_states[i_cctv] == 90:  # cctv가 1번 종류고 각도가 90도인 경우
            fill_up(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 1 and cctv_states[i_cctv] == 180:  # cctv가 1번 종류고 각도가 180도인 경우
            fill_left(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 1 and cctv_states[i_cctv] == 270:  # cctv가 1번 종류고 각도가 270도인 경우
            fill_down(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 2 and cctv_states[i_cctv] == 0:  # cctv가 2번 종류고 각도가 0도인 경우
            fill_right(g_cpy, cctv, i_cctv)
            fill_left(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 2 and cctv_states[i_cctv] == 90:  # cctv가 2번 종류고 각도가 90도인 경우
            fill_up(g_cpy, cctv, i_cctv)
            fill_down(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 3 and cctv_states[i_cctv] == 0:  # cctv가 3번 종류고 각도가 0도인 경우
            fill_right(g_cpy, cctv, i_cctv)
            fill_up(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 3 and cctv_states[i_cctv] == 90:  # cctv가 3번 종류고 각도가 90도인 경우
            fill_up(g_cpy, cctv, i_cctv)
            fill_left(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 3 and cctv_states[i_cctv] == 180:  # cctv가 3번 종류고 각도가 180도인 경우
            fill_left(g_cpy, cctv, i_cctv)
            fill_down(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 3 and cctv_states[i_cctv] == 270:  # cctv가 3번 종류고 각도가 270도인 경우
            fill_down(g_cpy, cctv, i_cctv)
            fill_right(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 4 and cctv_states[i_cctv] == 0:  # cctv가 4번 종류고 각도가 0도인 경우
            fill_right(g_cpy, cctv, i_cctv)
            fill_up(g_cpy, cctv, i_cctv)
            fill_left(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 4 and cctv_states[i_cctv] == 90:  # cctv가 4번 종류고 각도가 90도인 경우
            fill_up(g_cpy, cctv, i_cctv)
            fill_left(g_cpy, cctv, i_cctv)
            fill_down(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 4 and cctv_states[i_cctv] == 180:  # cctv가 4번 종류고 각도가 180도인 경우
            fill_left(g_cpy, cctv, i_cctv)
            fill_down(g_cpy, cctv, i_cctv)
            fill_right(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 4 and cctv_states[i_cctv] == 270:  # cctv가 4번 종류고 각도가 270도인 경우
            fill_down(g_cpy, cctv, i_cctv)
            fill_right(g_cpy, cctv, i_cctv)
            fill_up(g_cpy, cctv, i_cctv)
        elif cctv[i_cctv][2] == 5 and cctv_states[i_cctv] == 0:  # cctv가 5번 종류고 각도가 0도인 경우
            fill_right(g_cpy, cctv, i_cctv)
            fill_up(g_cpy, cctv, i_cctv)
            fill_left(g_cpy, cctv, i_cctv)
            fill_down(g_cpy, cctv, i_cctv)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if g_cpy[i][j] == 0:
                cnt += 1
    return cnt


def dfs(g, cctv, states, n): # 그리드 g, cctv의 리스트 cctv, 현재 cctv의 넘버 n
    global LEN_CCTV
    global actions
    if n >= LEN_CCTV:
        return find_safe(g, cctv, states)
    cur_cctv_kind = cctv[n][2]
    cur_actions = actions[cur_cctv_kind]
    min_n = 65
    for cur_action in cur_actions:
        cur_min = dfs(g, cctv, states + [cur_action], n+1)
        if cur_min < min_n:
            min_n = cur_min
    return min_n

############
# 입력 부분 #
############
# 4 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 6 0
# 0 0 0 0 0 0
N, M = map(int, input().split()) # 행의 개수 N, 열의 개수 M
g = []
cctv = []
for i in range(N):
    g.append(list(map(int, input().split())))
    for j in range(M):
        v = g[i][j]
        if 1 <= v < 6:
            cctv.append([j, i, v, 0])

LEN_CCTV = len(cctv)
ans = dfs(g, cctv, [], 0)
print(ans)
