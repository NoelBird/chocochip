N = int(input())
l = []
for _ in range(N):
    x, y = map(int, input().split())
    l.append((x, y))

maxVal = 0
for i in range(N):
    for j in range(i, N):
        curVal = (l[i][0] - l[j][0])**2 + (l[i][1] - l[j][1])**2
        if curVal > maxVal:
            maxVal = curVal

print(maxVal**0.5)