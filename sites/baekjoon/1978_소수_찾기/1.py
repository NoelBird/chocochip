N = int(input())
l = list(map(int, input().split()))
nums = [1]*1001
nums[0] = 0
nums[1] = 0

for i in range(2, 1001):
    for j in range(2, 1000//i+1):
        nums[i*j] = 0

cnt = 0
for i in l:
    if nums[i]:
        cnt += 1
print(cnt)