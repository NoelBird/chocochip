# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
# 
# 5 5
# #####
# #..B#
# #.#.#
# #RO.#
# #####

# 시간제한: 2초
# 메모리 제한: 512MB
# 제한: 보드 세로 길이 N, 보드 가로 길이 M (3 ≤ N, M ≤ 10)
# 빨간 구슬의 개수 1, 파란 구슬의 개수 1
# 판을 흔들 수 있는 최대한의 횟수: 10

# 전략 1: 무식하게 풀자 - BFS

# 현재 2020-01-17 기준으로 푸는 시간이 오래 걸립니다. 풀이를 중단합니다.

from collections import deque
MAX_LEN = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split()) # M: 판의 세로 길이, N: 판의 가로 길이

def get_input()
    board = []
    for y in range(M):
        tmp = input()
        if tmp.find('R') != -1:
            x = tmp.find('R')
            red = (x, y)
        if tmp.find('B') != -1:
            x = tmp.find('B')
            blue = (x, y)
        board.append(list(tmp))
    return board, red, blue

def solve(board, red, blue):
    """BFS와 MEMOIZATION.
    상태는 빨간 공과 파란 공의 위치로 결정됩니다.
    
    Arguments:
        board {list} -- board의 2중 리스트
        red {tuple} -- 빨간 공의 x, y 정보를 담고 있는 tuple
        blue {tuple} -- 파란 공의 x, y 정보를 담고 있는 tuple
    """
    q = deque([(red, blue),])
    visited = [(red, blue),]

    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur in visited:
                continue
            visited.append(cur) # 방문여부 체크

            red_cur = cur[0]
            blue_cur = cur[1]

            # 기울이기
            for i in range(4):
                if red_cur[1] != blue_cur[1]: # y값이 다른 값이면 어떤 것을 먼저 굴리든 상관 없음
                    red_x_next, red_y_next = red_cur
                    while True:
                        if not(0 <= red_x_next + dx[i] < M and 0 <= red_y_next + dy[i] < N):
                            break
                        red_x_next += dx[i]
                        red_y_next += dy[i]

                    blue_x, blue_y = blue_cur
                else: # 같은 y 값이면 왼쪽에 있는 것을 먼저 굴려야 함
                    if red_cur[0] < blue_cur[0]:
                        while()
                    else:
                        pass



board, red, blue = get_input()
solve(board, red, blue)