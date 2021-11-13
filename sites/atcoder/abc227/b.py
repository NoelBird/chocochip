l = []
for a in range(1, 1000):
    for b in range(1, 1000):
        l.append(4*a*b+3*a+3*b)

N = int(input())
ll = list(map(int, input().split()))
cnt = 0
for i in ll:
    if 1 <= i <= 1000 and i in l:
        cnt += 1

print(len(ll)-cnt)
