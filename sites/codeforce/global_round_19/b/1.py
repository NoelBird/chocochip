# 4
# 2
# 1 2
# 3
# 2 0 1
# 4
# 2 0 5 1
# 5
# 0 1 1 0 1

T = int(input())

def solve(l, idx_l, idx_r):
    cnt = 0
    for i in range(idx_l, idx_r):
        if l[i] == 0:
            cnt += 1
    return cnt + len(l[idx_l:idx_r])

for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(i+1, N+1):
            cnt += solve(l, i, j)
    print(cnt)