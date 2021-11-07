import math

N = int(input())

x = []
y = []
l = []
for _ in range(N):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)

def gcd(a, b):
    return gcd(b, a % b) if b else a

def make_pairs(a, b):
    g = gcd(x[a]-x[b], y[a]-y[b])
    l.append(((x[a] - x[b])//g, (y[a] - y[b])//g))
    l.append((-1*(x[a] - x[b])//g, -1*(y[a] - y[b])//g))

for i in range(N):
    for j in range(i+1, N):
        make_pairs(i, j)

print(len(set(l)))