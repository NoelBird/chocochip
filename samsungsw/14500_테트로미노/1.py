# brute force 버젼 - 시간초과
pats = [
    [[1, 1, 1, 1]], # 1
    [
        [1],
        [1],
        [1],
        [1]
    ], # 2
    [
        [1, 1],
        [1, 1]
    ], # 3
    [
        [1, 0],
        [1, 0],
        [1, 1]
    ], # 4
    [
        [1, 1, 1],
        [1, 0, 0]
    ], # 5
    [
        [1, 1],
        [0, 1],
        [0, 1],
    ], # 6
    [
        [0, 0, 1],
        [1, 1, 1]
    ], # 7
    [
        [1, 1],
        [1, 0],
        [1, 0]
    ], # 8
    [
        [1, 1, 1],
        [0, 0, 1]
    ], # 9
    [
        [0, 1],
        [0, 1],
        [1, 1]
    ], # 10
    [
        [1, 0, 0],
        [1, 1, 1]
    ], # 11
    [
        [1, 0],
        [1, 1],
        [0, 1]
    ], # 12
    [
        [0, 1, 1],
        [1, 1, 0]
    ], # 13
    [
        [0, 1],
        [1, 1],
        [1, 0]
    ], # 14
    [
        [1, 1, 0],
        [0, 1, 1]
    ], # 15
    [
        [0, 1, 0],
        [1, 1, 1]
    ], # 16
    [
        [1, 0],
        [1, 1],
        [1, 0]
    ], # 17
    [
        [1, 1, 1],
        [0, 1, 0]
    ], # 18
    [
        [0, 1],
        [1, 1],
        [0, 1]
    ] # 19
]

N, M = map(int, input().split()) # input
mat = [] # create matrix
for _ in range(N):
    tmp = list(map(int, input().split()))
    mat.append(tmp)

max_v = 0
for pat in pats:
    h = len(pat)
    w = len(pat[0])
    for j in range(N-h+1):
        for k in range(M-w+1):
            cur_v = 0
            for m in range(h):
                for n in range(w):
                    cur_v += mat[j+m][k+n]*pat[m][n]
            if cur_v > max_v:
                max_v = cur_v
print(max_v)

