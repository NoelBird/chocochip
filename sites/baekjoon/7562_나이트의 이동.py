from collections import deque
import sys
input = sys.stdin.readline

actions = ((2, -1), (2, 1), (1, -2), (1, 2), (-2, -1), (-2, 1), (-1, 2), (-1, -2))


def bfs(siz, xy, xxyy):
    global actions
    g = [[0 for _ in range(siz)] for _ in range(siz)]

    q = deque([xy])
    x, y = xy
    cnt = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) == xxyy:
                return cnt
            if not g[y][x]:
                g[y][x] = 1
                for action in actions:
                    x_nxt = x + action[0]
                    y_nxt = y + action[1]
                    if 0 <= x_nxt < siz and 0 <= y_nxt < siz:
                        if not g[y_nxt][x_nxt]:
                            q.append((x_nxt, y_nxt))
        cnt += 1
    return -1


N = int(input())
for _ in range(N):
    siz = int(input())
    x_begin, y_begin = map(int, input().split())
    x_target, y_target = map(int, input().split())
    ans = bfs(siz, (x_begin, y_begin), (x_target, y_target))
    print(ans)