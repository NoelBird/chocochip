# 3
# 4
# 7
# 10
N = int(input())

hist = {}

def solution(n):
    if hist.get(n):
        return hist[n]
    if n < 0:
        return 0
    elif n == 0:
        return 1
    s = 0
    for i in range(1, 4):
        s += solution(n-i)
    hist[n] = s
    return s

for _ in range(N):
    A = int(input())
    hist = {}
    print(solution(A))
