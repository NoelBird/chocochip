# 3
# 1 1 0
# 1 0 1
# 0 1 1

# initialize
N = int(input())
d = []
a = []
b = []

# get inputs(d - diagonal, b - below, a - above)
b.append(0)
for i in range(N):
    cur = list(map(int, input().split()))
    if i != 0:
        b.append(cur[i-1])
    d.append(cur[i])
    if i != N-1:
        a.append(cur[i+1])
a.append(0)

# fill the results
bb = [0]
dd = [d[0]]
for i in range(1, N):
    if dd[i-1] == 0:
        print("-1")
        exit(0)
    bb.append(b[i]/(dd[i-1]))
    dd.append(d[i]-bb[i]*a[i-1])

# print result matrices
for i in range(N):
    # print L
    if i>1:
        print(" ".join(["0.000"]*(i-1)), end=" ") # left filler
    if i!=0:
        print(f"{bb[i]:.3f}", end=" ") # below
    print("1.000", end=" ") # diagonal
    if i<N-1:
        print(" ".join(["0.000"]*(N-1-i)), end="") # right filler
    print()
for i in range(N):
    # print U
    if i>0:
        print(" ".join(["0.000"]*(i)), end=" ") # left filler
    print(f"{dd[i]:.3f}", end=" ") # diagonal
    if i!=N-1:
        print(f"{a[i]:.3f}", end=" ") # above
    if i<N-2:
        print(" ".join(["0.000"]*(N-2-i)), end="") # right filler
    print()
