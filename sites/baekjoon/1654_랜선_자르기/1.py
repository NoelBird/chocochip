M, N = map(int, input().split())
l = []
for _ in range(M):
    l.append(int(input()))

def check(l, length, N):
    return sum(map(lambda x: x//length, l)) >= N

def binary_search(l, N):
    left = 0
    right = 2**32
    mid = 0
    while left < right:
        mid = left + (right - left)//2
        result = check(l, mid, N)
        if result:
            left = mid + 1
        else:
            right = mid
    return left - 1

print(binary_search(l, N))