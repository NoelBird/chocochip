from collections import deque
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

############
# 전역 변수 #
############

############
# 함수 부분 #
############
def up(g):
    global N
    _g = [[g[i][j] for j in range(N)] for i in range(N)]

    # 땡기기
    ans_g = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        cnt = 0
        for i in range(N):
            if _g[i][j] != 0:
                ans_g[cnt][j] = _g[i][j]
                cnt += 1
    _g = [[ans_g[i][j] for j in range(N)] for i in range(N)]
    # 합치기
    j = 0
    while j < N:
        i = 0
        while i < N:
            if i + 1 < N and _g[i][j] == _g[i+1][j]:  # found
                _g[i][j] *= 2
                _g[i+1][j] = 0
                i += 2
            else:  # not found
                i += 1
        j += 1
    # 땡기기
    ans_g = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        cnt = 0
        for i in range(N):
            if _g[i][j] != 0:
                ans_g[cnt][j] = _g[i][j]
                cnt += 1
    return ans_g


def down(g):
    global N
    # 합치기
    _g = [[g[i][j] for j in range(N)] for i in range(N)]

    # 땡기기
    ans_g = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        cnt = N - 1
        for i in range(N - 1, -1, -1):
            if _g[i][j] != 0:
                ans_g[cnt][j] = _g[i][j]
                cnt -= 1
    _g = [[ans_g[i][j] for j in range(N)] for i in range(N)]

    j = 0
    while j < N:
        i = N-1
        while i >= 0:
            if i - 1 >= 0 and _g[i][j] == _g[i - 1][j]:  # found
                _g[i][j] *= 2
                _g[i - 1][j] = 0
                i -= 2
            else:  # not found
                i -= 1
        j += 1
    # 땡기기
    ans_g = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        cnt = N-1
        for i in range(N-1, -1, -1):
            if _g[i][j] != 0:
                ans_g[cnt][j] = _g[i][j]
                cnt -= 1
    return ans_g


def right(g):
    global N
    # 합치기
    _g = [[g[i][j] for j in range(N)] for i in range(N)]

    # 땡기기
    ans_g = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        cnt = N - 1
        for j in range(N - 1, -1, -1):
            if _g[i][j] != 0:
                ans_g[i][cnt] = _g[i][j]
                cnt -= 1

    _g = [[ans_g[i][j] for j in range(N)] for i in range(N)]

    i = 0
    while i < N:
        j = N-1
        while j >= 0:
            if j - 1 >= 0 and _g[i][j] == _g[i][j - 1]:  # found
                _g[i][j] *= 2
                _g[i][j - 1] = 0
                j -= 2
            else:  # not found
                j -= 1
        i += 1
    # 땡기기
    ans_g = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        cnt = N-1
        for j in range(N-1, -1, -1):
            if _g[i][j] != 0:
                ans_g[i][cnt] = _g[i][j]
                cnt -= 1
    return ans_g


def left(g):
    global N
    # 합치기
    _g = [[g[i][j] for j in range(N)] for i in range(N)]

    # 땡기기
    ans_g = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        cnt = 0
        for j in range(N):
            if _g[i][j] != 0:
                ans_g[i][cnt] = _g[i][j]
                cnt += 1
    _g = [[ans_g[i][j] for j in range(N)] for i in range(N)]

    i = 0
    while i < N:
        j = 0
        while j < N:
            if j + 1 < N and _g[i][j] == _g[i][j + 1]:  # found
                _g[i][j] *= 2
                _g[i][j + 1] = 0
                j += 2
            else:  # not found
                j += 1
        i += 1
    # 땡기기
    ans_g = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        cnt = 0
        for j in range(N):
            if _g[i][j] != 0:
                ans_g[i][cnt] = _g[i][j]
                cnt += 1
    return ans_g


def get_max(g):
    global N

    max_val = 0
    for i in range(N):
        for j in range(N):
            if g[i][j] > max_val:
                max_val = g[i][j]
    return max_val


def dfs(g, cnt):
    global N
    stack = deque([(g, cnt)])
    results = deque([])

    while stack:
        for _ in range(len(stack)):
            cur_g, cur_cnt = stack.pop()
            if cur_cnt >= 5: # 종료조건 depth를 5번 들어갔을 때
                results.append(get_max(cur_g))
                continue
            stack.append((up(cur_g), cur_cnt + 1))
            stack.append((down(cur_g), cur_cnt + 1))
            stack.append((left(cur_g), cur_cnt + 1))
            stack.append((right(cur_g), cur_cnt + 1))
    return max(results)





############
# 입력 부분 #
############
N = int(input())
g = []
for _ in range(N):
    g.append(list(map(int, input().split())))

ans = dfs(g, 0) # 총 5번이니까, 5보다 작을 때까지 반복
print(ans)