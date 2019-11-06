from collections import deque
import sys
input = sys.stdin.readline

#############
# 전역 변수 #
#############
actions_air = [(1, 0), (-1, 0), (0, 1), (0, -1)]
actions_upper = [(1, 0), (0, -1), (-1, 0), (0, 1)]
actions_lower = [(1, 0), (0, 1), (-1, 0), (0, -1)]

#############
# 함수 부분 #
#############
def update_air(R, C):
    global g
    g_next = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            # current cell
            x = j
            y = i
            if g[y][x] == -1: # 현재 셀이 청정기면 패스
                continue
            for action_air in actions_air: # 다음 셀들 탐색
                next_x = x + action_air[0]
                next_y = y + action_air[1]

                if 0 <= next_x < C and 0 <= next_y < R and g[next_y][next_x] != -1:
                    g_next[next_y][next_x] += g[y][x]//5
                    g_next[y][x] -= g[y][x]//5
    for i in range(R):
        for j in range(C):
            g[i][j] += g_next[i][j]



def update_fresher(R, C, air_fresher):
    global g
    x_fresher_upper, y_fresher_upper = air_fresher[0]
    x_fresher_lower, y_fresher_lower = air_fresher[1]

    cur_x = 0
    cur_y = 0
    next_x = 0
    next_y = 0
    prev_save = 0
    next_save = 0

    # initialize current point
    cur_x = x_fresher_upper
    cur_y = y_fresher_upper
    next_x = cur_x
    next_y = cur_y

    isEnd = False
    while not isEnd:
        for action_upper in actions_upper:
            while True: # 오른쪽으로
                next_x = cur_x + action_upper[0]
                next_y = cur_y + action_upper[1]
                if next_x >= C or next_x < 0 or next_y > y_fresher_upper or next_y < 0:
                    next_x -= action_upper[0]
                    next_y -= action_upper[1]
                    break
                if (next_x, next_y) == (x_fresher_upper, y_fresher_upper):
                    isEnd = True
                    break
                next_save = g[next_y][next_x] # next to next_save
                if g[cur_y][cur_x] == -1: # current to next
                    g[next_y][next_x] = 0
                else:
                    g[next_y][next_x] = prev_save
                prev_save = next_save
                cur_x = next_x
                cur_y = next_y
            if isEnd:
                break

    cur_x = 0
    cur_y = 0
    next_x = 0
    next_y = 0
    prev_save = 0
    next_save = 0

    # initialize current point
    cur_x = x_fresher_lower
    cur_y = y_fresher_lower
    next_x = cur_x
    next_y = cur_y

    isEnd = False
    while not isEnd:
        for action_lower in actions_lower:
            while True:  # 오른쪽으로
                next_x = cur_x + action_lower[0]
                next_y = cur_y + action_lower[1]
                if next_x >= C or next_x < 0 or next_y >= R or next_y < y_fresher_lower:
                    next_x -= action_lower[0]
                    next_y -= action_lower[1]
                    break
                if (next_x, next_y) == (x_fresher_lower, y_fresher_lower):
                    isEnd = True
                    break
                next_save = g[next_y][next_x]  # next to next_save
                if g[cur_y][cur_x] == -1:  # current to next
                    g[next_y][next_x] = 0
                else:
                    g[next_y][next_x] = prev_save
                prev_save = next_save
                cur_x = next_x
                cur_y = next_y
            if isEnd:
                break



#############
# 입력 부분 #
#############
R, C, T = map(int, input().split())  # 행의 수 R, 열의 수 C, 몇 초 후의 상황인지 T

g = []
air_fresher = []
for i in range(R):
    g.append(list(map(int, input().split())))
    for j in range(C):
        if g[i][j] == -1:
            air_fresher.append((j, i))

for _ in range(T):
    update_air(R, C)
    update_fresher(R, C, air_fresher)

s = 0
for i in range(R):
    for j in range(C):
        s += g[i][j] if g[i][j] != -1 else 0

print(s)