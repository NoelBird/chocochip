# too slow because it is hard to find prime number
# ============================================================
#      5                                           @profile
#      6                                           def func(N, L, l):
#      7                                               # 1. find prime number at index 0
#      8         2          5.6      2.8      0.0      p1 = 0
#      9         2          1.7      0.9      0.0      p2 = 0
#     10         2          1.6      0.8      0.0      ff = l[0]
#     11   1646574     443127.4      0.3     47.0      for j in range(2, l[0]//2):
#     12   1646572     498289.4      0.3     52.9          if (ff % j) == 0:
#     13         4          1.8      0.5      0.0              p1 = j
#     14         4          2.1      0.5      0.0              p2 = l[0]//j
#     15                                               # 2. try idx 1, idx 2
#     16         2          2.7      1.4      0.0      if l[1] % p1 != 0 or l[2] % (l[1]//p1) != 0:
#     17                                                   p1, p2 = p2, p1
#     18         2         14.8      7.4      0.0      ll = [0]*(len(l)+1)
#     19         2          1.3      0.7      0.0      ll[0] = p2
#     20                                               # 3. propagate
#     21        58         28.1      0.5      0.0      for j in range(1, len(ll)):
#     22        56         35.5      0.6      0.0          ll[j] = l[j-1] // ll[j-1]
#     23
#     24         2         29.2     14.6      0.0      tt = sorted(list(set(ll)))
#     25         2          1.3      0.7      0.0      d = {}
#     26        54         22.4      0.4      0.0      for j in range(len(tt)):
#     27        52         44.1      0.8      0.0          d[tt[j]] = chr(65 + j)
#     28         2         26.7     13.4      0.0      sys.stdout.write("Case {}: ".format(i))
#     29        60         26.4      0.4      0.0      for j in range(len(ll)):
#     30        58         44.0      0.8      0.0          sys.stdout.write(d[ll[j]])
#     31         2        798.9    399.5      0.1      sys.stdout.write("\n")

"""
import sys

T = int(input())

def func(N, L, l):
    # 1. find prime number at index 0
    p1 = 0
    p2 = 0
    ff = l[0]
    for j in range(2, l[0]//2):
        if (l[0] % j) == 0:
            p1 = j
            p2 = l[0]//j
    # 2. try idx 1, idx 2
    if l[1] % p1 != 0 or l[2] % (l[1]//p1) != 0:
        p1, p2 = p2, p1
    ll = [0]*(len(l)+1)
    ll[0] = p2
    # 3. propagate
    for j in range(1, len(ll)):
        ll[j] = l[j-1] // ll[j-1]
    
    tt = sorted(list(set(ll)))
    d = {}
    for j in range(len(tt)):
        d[tt[j]] = chr(65 + j)
    sys.stdout.write("Case {}: ".format(i))
    for j in range(len(ll)):
        sys.stdout.write(d[ll[j]])
    sys.stdout.write("\n")

for i in range(1, T+1):
    N, L = map(int, input().split())
    l = list(map(int, input().split()))
    func(N, L, l)
"""

def gcd(a, b):
    return gcd(b, a%b) if b else a

import sys
sys.setrecursionlimit(10000)


T = int(input())

def func(N, L, l):
    # 1. find prime number at index 0
    g = gcd(l[0], l[1])
    ll = [l[0]//g, g]

    for j in range(1, L):
        g = l[j]//g
        ll.append(g)

    tt = sorted(list(set(ll)))
    d = {}
    for j in range(len(tt)):
        d[tt[j]] = chr(65 + j)
    sys.stdout.write("Case #{}: ".format(i))
    for j in range(len(ll)):
        sys.stdout.write(d[ll[j]])
    sys.stdout.write("\n")

for i in range(1, T+1):
    N, L = map(int, input().split())
    l = list(map(int, input().split()))
    func(N, L, l)
