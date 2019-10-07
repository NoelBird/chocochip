T = int(input())

l = [0]*(T+1)
l[0] = [0]*(T+1)
for i in range(0, T):
    l[i+1] = [0] + list(map(int, input().split()))

cache = {}
@profile
def dp(direc, x, y):
    global l
    global cache

    if cache.get((direc, x, y)):
        return cache[direc, x, y]

    if not (x and y):
        return 0
    if direc == 0 and x == 2 and y == 1:
        return 1
    
    ret = 0
    if direc == 0:
        if not l[y][x-1]:
            ret = dp(0, x-1, y) + dp(2, x-1, y)
    elif direc == 1:
        if not l[y-1][x]:
            ret = dp(1, x, y-1) + dp(2, x, y-1)
    else:
        if not (l[y-1][x-1] or l[y][x-1] or l[y-1][x]):
            ret = dp(0, x-1, y-1) + dp(1, x-1, y-1) + dp(2, x-1, y-1)
    cache[direc, x, y] = ret
    return ret

print(sum([dp(i, T, T) for i in range(3)]))