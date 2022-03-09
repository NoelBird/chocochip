M, N = map(int, input().split())
nums = [1]*1000001
nums[0] = 0
nums[1] = 0

for i in range(2, 1000001):
    for j in range(2, 1000000//i+1):
        nums[i*j] = 0

for i in range(M, N+1):
    if nums[i]:
        print(i)