import sys
rdl = sys.stdin.readline
n = int(rdl())
a = list(map(int, rdl().split(' ')))
b = list(map(int, rdl().split(' ')))

a.sort()
b.sort(reverse=True)
ans = 0
for i in range(n):
    ans += a[i]*b[i]
print(ans)