N = int(input())

a = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    a[0][i] = 1
for i in range(N-1):
    for j in range(1, 10):
        if j > 1:
            a[i+1][j] += a[i][j-1]
        if j < 9:
            a[i+1][j] += a[i][j+1]
        a[i+1][j] += a[i][j]
        a[i+1][j] %= 998244353
print(sum(a[N-1]) % 998244353)