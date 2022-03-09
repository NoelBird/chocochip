N = int(input())
T = 665
cnt = 0
result = 0
for i in range(T, 1000000000):
    if "666" in str(i):
        cnt += 1
        if cnt == N:
            result = i
            break
print(result)