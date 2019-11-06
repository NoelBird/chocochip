import sys
rdl = sys.stdin.readline

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

n = int(rdl())
for _ in range(n):
    a, b = map(int, rdl().split())
    print(a*b//gcd(a,b))