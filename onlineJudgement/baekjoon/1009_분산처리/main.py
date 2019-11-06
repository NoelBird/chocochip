import sys
rdl = sys.stdin.readline

d = {}
d[0] = [10]
d[1] = [1]
d[2] = [2, 4, 8, 6]
d[3] = [3, 9, 7, 1]
d[4] = [4, 6]
d[5] = [5]
d[6] = [6]
d[7] = [7, 9, 3, 1]
d[8] = [8, 4, 2, 6]
d[9] = [9, 1]

n = int(rdl())
for _ in range(n):
    a, b = map(int, rdl().split(' '))
    a1 = a % 10
    b1 = (b-1) % len(d[a1])
    print(d[a1][b1])