from collections import defaultdict
import sys
import numpy as np
rdl = sys.stdin.readline
n = int(rdl())
d = defaultdict(int)

def fib(n):
    global d
    if n==0:
        return [1,0]
    if n==1:
        return [0,1]
    if d[n]:
        return d[n]
    else:
        tmp = [sum(i) for i in zip(fib(n-1), fib(n-2))]
        d[n] = tmp
        return tmp
    
for i in range(n):
    a = int(rdl())
    print(*fib(a))
