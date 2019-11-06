n, m = map(int, input().split())

l = []
for _ in range(n):
    l = [int(input())] + l

aa = 0
ans = 0
for i in range(len(l)):
    if m == 0:
        break
    if l[i] <= m:
        aa =  m//l[i]
        ans += aa
        m -= aa*l[i]
print(ans)