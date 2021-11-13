# 3
# 0 0 0
# 0 0 0
# 0 0 0

cache = {}


def dp(xy, state):
    global g
    if cache.get((xy, state)):
        return cache.get((xy, state))

    m = 0
    # 0 가로로 누은 경우
    # 1 대각선의 경우
    # 2 세로의 경우
    x = xy[0]
    y = xy[1]

    ########## base conditions ############
    if x == 3 and y == 1 and state == 0: # 가로 막대 base condition
        if g[y][x] == 0 and g[y][x-1] == 0:
            cache[((3, 1), 0)] = 1
            return 1
    if x == 3 and y == 2 and state == 1: # 대각선 막대 base condition
        if g[y-1][x-1] == 0 and g[y-1][x] == 0 and g[y][x-1] == 0 and g[y][x] == 0:
            cache[((3, 2), 1)] = 1
            return 1

    if state == 0:
        if g[y][x-1] == 0 and g[y][x] == 0: # 가로 막대기 가능?
            m += dp((x-1, y), 0)
        if g[y][x-1] == 0 and g[y-1][x-1] == 0 and g[y-1][x] == 0 and g[y][x] == 0: # 대각선 막대기 가능?
            m += dp((x - 1, y), 1)
    elif state == 1:
        if g[y][x-1] == 0 and g[y][x] == 0: # 가로 막대기 가능?
            m += dp((x-1, y-1), 0)
        if g[y][x-1] == 0 and g[y-1][x-1] == 0 and g[y-1][x] == 0 and g[y][x] == 0: # 대각선 막대기 가능?
            m += dp((x - 1, y-1), 1)
        if g[y-1][x] == 0 and g[y][x]==0:  # 세로 막대기 가능?
            m += dp((x-1, y-1), 2)
    else:
        if g[y][x - 1] == 0 and g[y - 1][x - 1] == 0 and g[y - 1][x] == 0 and g[y][x] == 0:  # 대각선 막대기 가능?
            m += dp((x, y-1), 1)
        if g[y-1][x] == 0 and g[y][x] == 0:  # 가로 막대기 가능?
            m += dp((x, y-1), 2)

    cache[((x, y), state)] = m
    return m


N = int(input())
g = []
g.append([-1]*(N+2))
for _ in range(N):
    g.append([-1] + list(map(int, input().split())) + [-1])
g.append([-1]*(N+2))

ans = dp((N, N), 0) + dp((N, N), 1) + dp((N, N), 2)
print(ans)
