# 4 10 0
# 0 3 4 8
# 5 8 3 6

N, L, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a += [L]
is_exists_taller = True
while is_exists_taller != False and K != 0:
    is_exists_taller = False
    max_val = 0
    max_idx = 0
    for i in range(len(b)):
        if (a[i+1] - a[i])*b[i] >= 0:
            is_exists_taller = True

            if max_val < (a[i+1] - a[i])*b[i] and i != 0:
                max_val = (a[i+1] - a[i])*b[i]
                max_idx = i
    if is_exists_taller:
        a[max_idx:max_idx+2] = [a[max_idx] + a[max_idx+1]]
        b[max_idx:max_idx+2] = [b[max_idx]]
        print(max_idx)
        K -= 1
s = 0
for i in range(len(b)):
    s += (a[i+1] - a[i]) * b[i]
print(s)