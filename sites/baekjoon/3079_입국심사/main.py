import sys
import math

n, m = map(int, sys.stdin.readline().split(' '))
l = [0]*n
for i in range(n):
    l[i] = int(sys.stdin.readline())

lb = min(l)*m//n     # lower bound
ub = max(l)*math.ceil(m/n) # upper bound
mv = (lb+ub)//2

while lb<ub:
    c = 0           # the number of people
    for i in range(n):
        c += mv//l[i]
    if c < m:
        lb = mv + 1
    elif c > m:
        ub = mv
    else:
        break
    mv = (lb+ub)//2

s = 0
__max = 0
for i in l:
    tmp = i*(mv//i)
    if tmp > __max:
        __max = tmp
print(__max)
