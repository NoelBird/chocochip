# final try
# it is important to use fast gcd algorithm
# because it was used a lot

import sys

input = sys.stdin.readline

T = int(input())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(N, L, l):
    ll = [0]*(L+1)
    for j in range(L-1):
        if l[j] != l[j+1]:
            ll[j+1] = gcd(l[j], l[j+1])
            # propagate forward
            for k in range(j+1, L):
                ll[k+1] = l[k]//ll[k]
            
            # propagate backward
            for k in range(j, -1, -1):
                ll[k] = l[k]//ll[k+1]
            break
    tt = sorted(list(set(ll)))
    d = {}
    for j in range(26):
        d[tt[j]] = chr(65+j)
    return ll, d

for i in range(1, T+1):
    N, L = map(int, input().split())
    l = list(map(int, input().split()))
    ll, d = solution(N, L, l)
    print(f"Case #{i}: ", end="")
    for j in range(L+1):
        print(d[ll[j]], end="")
    print()