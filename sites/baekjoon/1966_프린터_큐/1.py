# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

T = int(input())
for _ in range(T):
    N, A = map(int, input().split())
    l = list(map(int, input().split()))
    
    out_cnt = 0
    while l:
        cur = l.pop(0)
        max_val = 0
        for v in l:
            if v > max_val:
                max_val = v
        if cur >= max_val:
            out_cnt += 1
            if A == 0:
                break
        else:
            l.append(cur)
        A -= 1
        if A < 0:
            A = len(l) - 1
    print(out_cnt)