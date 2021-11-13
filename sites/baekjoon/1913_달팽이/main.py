import sys
rdl = sys.stdin.readline

n = int(rdl())
target = int(rdl())

l = [[0]*n for _ in range(n)]

x = n//2
y = n//2

_n = 1
ans = [0, 0]
if _n == target:
    ans[0], ans[1] = x, y
l[y][x] = _n
_n += 1
y -= 1
for i in range(n//2):
    for dx in range(1 + 2*i):
        if _n == target:
            ans[0], ans[1] = x, y
        l[y][x] = _n
        _n += 1
        x += 1
    for dy in range(2 + 2*i):
        if _n == target:
            ans[0], ans[1] = x, y
        l[y][x] = _n
        _n += 1
        y += 1
    for dx in range(2 + 2*i):
        if _n == target:
            ans[0], ans[1] = x, y
        l[y][x] = _n
        _n += 1
        x -= 1
    for dy in range(3 + 2*i):
        if _n == target:
            ans[0], ans[1] = x, y
        l[y][x] = _n
        _n += 1
        y -= 1
for i in range(len(l)):
    print(' '.join(map(str, l[i])))
print('%d %d' % (ans[1]+1, ans[0]+1))
