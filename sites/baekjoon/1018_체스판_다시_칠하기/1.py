# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
M, N = map(int, input().split())
l = []
for _ in range(M):
    l.append(list(map(lambda x: 0 if x == 'W' else 1, input())))

min_val = 999999999999999999
for i in range(M-7):
    for j in range(N-7):
        s = 0
        for y in range(8):
            for x in range(8):
                if l[i+y][j+x] != (x+y)%2:
                    s += 1
        if s < min_val:
            min_val = s

for i in range(M-7):
    for j in range(N-7):
        s = 0
        for y in range(8):
            for x in range(8):
                if l[i+y][j+x] != (x+y+1)%2:
                    s += 1
        if s < min_val:
            min_val = s

print(min_val)