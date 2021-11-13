# TLE
N = int(input())

cnt = 0
for a in range(1, 4700):
    for b in range(a, int(N//a**0.5)+1):
        if a*b*b > N:
            break
        dd = max(0, N//(a*b)-(b-1))
        # print(a, b, dd)
        cnt += dd
print(cnt)