T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    result = sum(l) % M
    print(f"Case #{i}: {result}")