# TLE
# TODO 1: apply heap
# TODO 2: change language

N = int(input())

l = []
max_date = 0
for _ in range(N):
    p, d = map(int, input().split())
    if d > max_date:
        max_date = d
    l.append((p, d))

l.sort(key=lambda x: -x[1])

date = max_date
result = 0
for i in range(date, 0, -1):
    max_idx = -1
    max_pay = 0
    for j in range(len(l)):
        if l[j][1] >= i and l[j][0] > max_pay:
            max_pay = l[j][0]
            max_idx = j
    result += max_pay
    if max_idx != -1:
        del l[max_idx]

print(result)