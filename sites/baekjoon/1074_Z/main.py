N, r, c = map(int, input().split())

ans = 0
max_n = (2**N)**2
l = [[0, 1], [2, 3]]
n = N
for i in range(n):
    max_n = max_n//4
    ans += max_n*l[r>=2**(N-1)][c>=2**(N-1)]
    r = r % 2**(N-1)
    c = c % 2**(N-1)
    N -= 1
print(ans)
